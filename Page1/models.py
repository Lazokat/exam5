from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
# Create your models here.
class Category(models.Model):
    name=models.CharField(max_length=250)
    def __str__(self):
        return self.name

class Products(models.Model):
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    title=models.CharField(max_length=100)
    price=models.DecimalField(max_digits=10,decimal_places=2)
    description=models.TextField()
    data=models.DateField(auto_now_add=True)
    image=models.ImageField(upload_to='images/',blank=True)


    def __str__(self):
        return str(self.title)
class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Products, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return f" {Products.title}=>{self.quantity} x {(Products.objects.get(id=self.product.id)).price}"

    def get_absolute_url(self):
        return reverse("home")
