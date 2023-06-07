from django.urls import path
from .views import *

urlpatterns = [
    path("api/get/", get_all_content, name = "get_all_chosen_content"),
    path("api/add/game", add_new_game, name = "add_game_to_shop"),
    path("api/add/company", add_new_company, name = "add_new_companies_products"),
    path("api/add/category", add_new_category, name = "add_category_for_games"),
    path("api/get/game", get_game, name = "get_game_from_shop"),
    path("api/get/company", get_company, name = "get_companies_all_games"),
    path("api/get/category", get_category, name = "get_categories_all_games"),
    path("api/get/sales", get_sales_statiscs, name = "get_sale_statisctics"),
]
