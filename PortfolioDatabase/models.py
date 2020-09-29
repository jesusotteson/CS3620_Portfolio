from django.db import models


# Create your models here.
class Hobby(models.Model):

    def __str__(self):
        return self.hobby_name
        return self.hobby_description

    hobby_name = models.CharField(max_length=200)
    hobby_description = models.CharField(max_length=200)


class Portfolio(models.Model):

    def __str__(self):
        return self.portfolio_name
        return self.portfolio_description

    portfolio_name = models.CharField(max_length=200)
    portfolio_description = models.CharField(max_length=200)
