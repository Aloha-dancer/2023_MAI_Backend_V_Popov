from django.db import models
from djmoney.models.fields import MoneyField
import uuid

class Game(models.Model):

    uuid = models.UUIDField(primary_key = True, editable = False)

    title = models.CharField(unique = True,
                              blank = False,
                              null = False,
                              max_length = 256
    )

    description = models.TextField(blank = False, null = False)

    sysreq = models.TextField(blank = False, null = False)   

    category = models.ForeignKey(to = "Category",
                                 to_field = "uuid",
                                 default = 0,
                                 on_delete = models.CASCADE
    )

    price = MoneyField(max_digits=14, decimal_places=2, null=True, default_currency='USD')

    date_release = models.DateField(auto_now = True)

    company = models.ForeignKey(to = "Company",
                                to_field = "uuid",
                                default = 0,
                                on_delete = models.CASCADE
    )
    
    class Meta:
        db_table = 'shop"."game'
        ordering = ["title"]
        verbose_name = "Game"
        app_label = "shop"
    

    def __str__(self) -> str:
        return str(self.title) + ' ' + str(self.company)
        
    
class Category(models.Model):
        
    uuid = models.UUIDField(primary_key = True, editable = False)

    title = models.CharField(max_length = 256,
                                 blank = False,
                                 null = True,
                                 unique = True)

    description = models.TextField()

    age_bot_lim = models.IntegerField()

    class Meta:
        db_table = 'shop"."category'
        ordering = ['title']
        verbose_name = 'Games category' 
        app_label = "shop"

class Company(models.Model):

    uuid = models.UUIDField(primary_key = True, editable = False)

    name = models.CharField(max_length = 256,
                            null = False,
                            blank = False,
                            unique = True)
        
    contract_info = models.TextField()

    cash_per_cent = models.IntegerField(default = 15,
                                        null = False
    )
        
    country = models.CharField(max_length = 256,
                               null = False,
                               blank = False)
    
    category = models.ManyToManyField(Category,
                                      through = "Sales",
                                      through_fields = ("company", "category"))

    class Meta:
        db_table = 'shop"."comapany'
        ordering = ['name']
        verbose_name = 'Company creator'
        app_label = "shop"


        def __str__(self) -> str:
            return str(self.name)

    class Sales(models.Model):

        company = models.ForeignKey(to = "Company",
                                    to_field = "uuid",
                                    on_delete = models.CASCADE)
        
        category = models.ForeignKey(to = "Category",
                                     to_field = "uuid",
                                     on_delete = models.CASCADE)
        
        product = models.ForeignKey(to = "Game",
                                    to_field = "uuid",
                                    on_delete = models.CASCADE)
        
        date_sale = models.DateField(auto_created = True)

        total = MoneyField(max_digits=14, decimal_places=2, null=True, default_currency='USD')

        class Meta:
            db_table = 'shop"."sale'
            ordering = ['company', 'category', 'product']
            verbose_name = 'Games sales' 
            app_label = "shop"
    