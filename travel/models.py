from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.


class Destination(models.Model):
    country = models.CharField(max_length=50)
    desc = models.TextField()
    img1 = models.ImageField(upload_to='pics')
    rating = models.FloatField(
        validators=[MinValueValidator(1), MaxValueValidator(5)]
    )

    # rating = models.IntegerField(default=5)
    def __str__(self):
        return self.country


class Package(models.Model):
    destination = models.ForeignKey(Destination, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    img1 = models.ImageField(upload_to='pics')
    days = models.IntegerField(default=5)
    person = models.IntegerField(default=1)
    description = models.CharField(max_length=500)
    price = models.CharField(max_length=50)
    rating = models.FloatField(
        validators=[MinValueValidator(1), MaxValueValidator(5)]
    )
    # summary = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.title
