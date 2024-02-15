from rest_framework import serializers
from decimal import Decimal
from store.models import Product, Collection

class CollectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Collection
        fields = ["id", "title"]
        # fields = "__all__"
    # id = serializers.IntegerField()
    # title = serializers.CharField()

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'title', 'unit_price', 'price_with_tax', 'collection']
    price_with_tax = serializers.SerializerMethodField(method_name="calculate_tax")
   
    def calculate_tax(self, product:Product):
        return product.unit_price * Decimal(1.1)
    
    def create(self, validated_data):
        pass        
    # id = serializers.IntegerField()
    # title = serializers.CharField()
    # price = serializers.DecimalField(max_digits=6, decimal_places=2, source = "unit_price")    
    # price_with_tax = serializers.SerializerMethodField(method_name="calculate_tax")
    # collection = serializers.HyperlinkedRelatedField(
    #     queryset = Collection.objects.all(),
    #     view_name = "collection-detail"
    # )
    # collection = CollectionSerializer() #Nested Object Method
    # collection = serializers.StringRelatedField() #String Method
    # #PrimaryKey Method
    # collection = serializers.PrimaryKeyRelatedField( 
    #     queryset = Collection.objects.all()
    # )

    #Below is just for learning Purpose
    # def validate(self, data:dict):
    #     if data['password'] != data['confirm_password']:
    #         return serializers.ValidationError("Passwords do not match")
    #     return data