from django.db import models


class Brand(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Beverage(models.Model):
    name = models.CharField(max_length=100)
    temp_f = models.IntegerField()
    iced = models.BooleanField()
    size_in_ounces = models.FloatField()
    caffeine_in_mg = models.IntegerField()

    # associations
    # the related_name allows brands to see their beverages with a back reference (brand_one.beverages)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, blank=True, null=True, related_name="beverages")

    categories = models.ManyToManyField(Category, blank=True, null=True)

    def __str__(self):
        return self.name