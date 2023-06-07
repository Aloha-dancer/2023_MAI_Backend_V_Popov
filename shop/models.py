from django.db import models
from djmoney.models.fields import MoneyField
import uuid
import json

class Game(models.Model):

    uuid = models.BigAutoField(primary_key = True, editable = False)

    title = models.CharField(unique = True,
                              blank = False,
                              null = False,
                              max_length = 256
    )

    description = models.TextField(blank = True, null = False)

    sysreq = models.TextField(blank = True, null = False)   

    category = models.ForeignKey(to = "Category",
                                 to_field = "uuid",
                                 default = 0,
                                 on_delete = models.CASCADE
    )

    price = MoneyField(max_digits=14, decimal_places=2, blank = True, null=True,  default_currency='USD')

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
    
    def to_json_view(self) -> dict[str, str]:
        return 
        {
            'id': str(self.uuid),
            'game_title': str(self.title),
            'category': str(self.category),
            'company': str(self.company),
            'description': str(self.description),
            'sysreq': str(self.sysreq),
            'release': str(self.date_release),
            'price': str(self.price)
        }
    
    def __ent_view__(self) -> str:
        return self.__name__
        
    
class Category(models.Model):
        
    uuid = models.BigAutoField(primary_key = True, editable = False)

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
    
    def __str__(self) -> str:
        return str(self.title)
    
    def to_json_view(self) -> dict[str, str]:
        return 
        {
            'id': str(self.uuid),
            'Category_title': str(self.title),
            'Category_description': str(self.description),
            'Age_restrictions': str(self.age_bot_lim)
        }

class Company(models.Model):

    uuid = models.BigAutoField(primary_key = True,  editable = False)

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
    
    def to_json_view(self) -> dict[str, str]:
        return 
        {
            'id': str(self.uuid),
            'name': str(self.name),
            'contract_info': str(self.contract_info0),
            'tax': str(self.cash_per_cent)
        }
        

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

    def __str__(self) -> str:
        return str(self.company) + "\\" + str(self.category) + " :" + str(self.total)

    def to_json_view(self) -> dict[str, str]:
        return 
        {
            'company_sale': str(self.company),
            'category_sale': str(self.category),
            'product_sale': str(self.product),
            'date_sale': str(self.date),
            'total': str(self.total)
        }