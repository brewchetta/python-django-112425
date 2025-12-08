from django.db import models
from django.urls import reverse


class Winner(models.Model):
    first_name = models.CharField()
    last_name = models.CharField()
    age = models.IntegerField()
    address = models.CharField()
    # add the ability to take in images
    profile_pic = models.ImageField(upload_to='profile_pictures/', blank=True, null=True)
    # can add things like max_upload_size which I believe defaults to number of bytes

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class LottoNumber(models.Model):
    winning_numbers = models.IntegerField()
    date = models.DateField()
    location = models.CharField(max_length=200)
    dollar_amount = models.FloatField()
    rounds_not_won = models.IntegerField()
    winner = models.ForeignKey(Winner, on_delete=models.CASCADE, blank=True, null=True)
    # the LottoNumber model does not need a winner aka I can make a lotto number without a winner attached to it

    def __str__(self):
        return f"{self.winning_numbers} - {self.date}"
    
    # if we want to go to this item's detail page, what is the url
    # so here we've set it up so lotto numbers will try to go to 'lotto-number/2' if it has a pk of 2
    def get_absolute_url(self):
        return reverse('lotto-number', kwargs={ "pk": self.pk })
    # we include pk because the url path needs a pk in it