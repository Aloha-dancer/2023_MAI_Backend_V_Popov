from rest_framework import serializers
from .models import Game, Category, Company


class GameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Game
        fields = ('id', 'title', 'description', 'sys_req', 'price',
                  'company', 'category')


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'title', 'description', 'age_bot_lim')

class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ['name', 'country', 'cash_per_cent', 'contract_info']
