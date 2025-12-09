from rest_framework import serializers
from .models import Beverage, Category, Brand

# ModelSerializer is great for models
class BeverageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Beverage
        fields = ["id", "name", "temp_f", "iced", "size_in_ounces", "caffeine_in_mg"]
# the serializer the decides what data we send


class SimpleBeverageSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField()
# using this serializer means we would only send the name and none of the other attributes

# red_bull = Beverage(name="Red Bull" ...)
# serialized_data = BeverageSerializer(red_bull)
# serialized_data.data <-- this would now be red_bull in JSON format

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ["id", "name"]

class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = ["id", "name"]

class BrandWithBevsSerializer(serializers.ModelSerializer):
    # we can get beverages because the Beverage class has a related_name for brand
    beverages = BeverageSerializer(read_only=True, many=True)

    class Meta:
        model = Brand
        fields = ["id", "name", "beverages"]

class BeverageWithRelationshipsSerializer(serializers.ModelSerializer):
    brand = BrandSerializer(read_only=True)
    categories = CategorySerializer(read_only=True, many=True)
    # we need many=True because we can have many categories

    class Meta:
        model = Beverage
        fields = ["id", "name", "temp_f", "iced", "size_in_ounces", "caffeine_in_mg", "categories", "brand"]