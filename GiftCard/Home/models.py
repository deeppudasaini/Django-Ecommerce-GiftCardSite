from django.db import models

# Create your models here.
class GiftImages(models.Model):
    name=models.CharField(max_length=100)
    path=models.CharField(max_length=254)

    def __str__(self):
        return self.path
class GiftCard(models.Model):
    name=models.CharField(max_length=100)
    price=models.IntegerField()
    date=models.DateTimeField()
    image=models.ForeignKey(GiftImages,on_delete=models.CASCADE,null=True)
    def __str__(self):
        return self.name
