from django.db import models

class Category(models.Model):
    title =models.CharField(max_length=150)
    icon = models.ImageField(upload_to='category_icons')

    def __str__(self) -> str:
        return self.title

class Product(models.Model):
    title =models.CharField(max_length=150)
    description = models.TextField()
    price = models.FloatField()
    image = models.ImageField(upload_to='images')
    category = models.ForeignKey(Category, default=None, on_delete=models.CASCADE)


    def __str__(self) -> str:
        return self.title