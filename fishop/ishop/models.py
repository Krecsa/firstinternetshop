from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=128)
    description = models.TextField()
    price = models.IntegerField()
    image_url = models.CharField(max_length=1024)


    dpi = models.IntegerField(null=True, blank=True)
    type_k = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.name