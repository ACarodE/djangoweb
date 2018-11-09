from django.db import models
from ckeditor.fields import RichTextField
# Create your models here.
class Contact(models.Model):
    content = models.CharField(max_length = 50,verbose_name="adsoyad")
    content2 = models.CharField(max_length = 50,verbose_name="mail")
    content3 = models.CharField(max_length = 20,verbose_name="tel")
    content4 = models.TextField(verbose_name="mesaj")
    created_date = models.DateField(auto_now_add=True,verbose_name="oluşturulma Tarihi")
 

