from rest_framework import serializers, parsers, renderers
from .models import Game, Category, Company, Sales


class GameSerializer(serializers.ModelSerializer):

    def create(self, validated_data):
        return Game.objects.create(**validated_data)

    class Meta:
        model = Game
        fields = ('uuid', 'title', 'description', 'sysreq', 'price',
                  'company', 'category')


class CategorySerializer(serializers.ModelSerializer):

    def create(self, validated_data):
        return Category.objects.create(**validated_data)

    class Meta:
        model = Category
        fields = ('uuid', 'title', 'description', 'age_bot_lim')

class CompanySerializer(serializers.ModelSerializer):

    def create(self, validated_data):
        return Company.objects.create(**validated_data)

    class Meta:
        model = Company
        fields = ['uuid', 'name', 'country', 'cash_per_cent', 'contract_info']

class SalesSerializer(serializers.ModelSerializer):

    def create(self, validated_data):
        return Sales.objects.create(**validated_data)

    class Meta:
        model = Sales
        fields = ['company', 'category', 'product', 'date', 'total']
