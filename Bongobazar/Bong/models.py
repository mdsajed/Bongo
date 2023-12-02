from django.db import models
from django.contrib.auth.models import User


# Create your models here.
STATE_CHOICES = (
('Dhaka','Dhaka'),
('Noakhali','Noakhali'),
('Cumilla','Cumilla'),
('Rajshahi','Rajshahi'),
('Jessore','Jessore'),
('Barishal','Barishal'),
('Khulna','Khulna'),
('Chittagong','Chittagong'),
('Madaripur','Madaripur'),
('Faridpur','Faridpur'),
('Narayangonj','Narayangonj'),
)

CATEGORY_CHOICES=(
    ('GR','Groceries'),
    ('MW','Mens&Women'),
    ('DY','Dairy'),
    ('SH','Shoes'),
    ('HD','Home-Decor'),
    ('CS','Cosmetics'),
)



class Product(models.Model):
    title = models.CharField(max_length=100)
    selling_price = models.FloatField()
    discounted_price = models.FloatField()
    description = models.TextField()
    composition = models.TextField(default='')
    prodBong = models.TextField(default='')
    category = models.CharField(choices=CATEGORY_CHOICES, max_length=2)
    product_image = models.ImageField(upload_to='product')
    def __str__(self):
        return self.title
class Customer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name  = models.CharField(max_length=200)
    locality = models.CharField(max_length=200)
    city = models.CharField(max_length=50)
    mobile = models.IntegerField(default=0)
    zipcode = models.IntegerField()
    state = models.CharField(choices=STATE_CHOICES, max_length=100)
    def __str__(self):
        return self.name
    
    


