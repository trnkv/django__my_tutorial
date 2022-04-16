from django.db import models
from django.contrib.auth.models import  User


class Category(models.Model):  # категория товара
    id = models.AutoField(primary_key=True, help_text="Unique ID for this Category")
    name = models.CharField(max_length=200)
    
    def __str__(self):
        """
        String for representing the Model object.
        """
        return self.name
    
    
class Product(models.Model):  # товар
    id = models.AutoField(primary_key=True, help_text="Unique ID for this Product")
    name = models.CharField(max_length=200)
    price = models.PositiveIntegerField(default=100)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    
    def __str__(self):
        """
        String for representing the Model object.
        """
        return f"{self.name}, {self.price}, {self.category}"
    
    
class Cart(models.Model):  # корзина пользователя
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    product = models.ManyToManyField(Product, blank=True)
    
    def __str__(self):
        return f"{self.user.get_full_name()} (@{self.user.get_username()}), {', '.join(self.product.all().values_list('name', flat=True))}"

