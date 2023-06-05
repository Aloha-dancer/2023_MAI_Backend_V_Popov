from django.contrib import admin
from .models import Game, Company, Category

@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
    pass

@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    pass

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass