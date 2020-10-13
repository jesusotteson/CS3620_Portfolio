from django.db import models


# Create your models here.
class Hobby(models.Model):

    def __str__(self):
        return self.hobby_name + " " + self.hobby_description

    hobby_name = models.CharField(max_length=200)
    hobby_description = models.CharField(max_length=200)
    hobby_image = models.CharField(max_length=500,
                                   default="https://upload.wikimedia.org/wikipedia/commons/8/88"
                                           "/Danny_DeVito_cropped_and_edited_for_brightness.jpg")


class Portfolio(models.Model):

    def __str__(self):
        return self.portfolio_name + " " + self.portfolio_description

    portfolio_name = models.CharField(max_length=200)
    portfolio_description = models.CharField(max_length=200)
    portfolio_image = models.CharField(max_length=500,
                                       default="https://upload.wikimedia.org/wikipedia/commons/8/88"
                                               "/Danny_DeVito_cropped_and_edited_for_brightness.jpg")


class Contact(models.Model):

    def __str__(self):
        return self.contact_name + " " + self.contact_email + " " + self.contact_message

    contact_name = models.CharField(max_length=200)
    contact_email = models.CharField(max_length=200)
    contact_message = models.CharField(max_length=500)
