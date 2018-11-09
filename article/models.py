from django.db import models
from ckeditor.fields import RichTextField


# Create your models here.
class Article(models.Model):
    
    author = models.ForeignKey( "auth.User",on_delete= models.CASCADE,verbose_name="Makale" )
    title = models.CharField(max_length = 50,verbose_name="Baslik")
    content = RichTextField()
    created_date = models.DateTimeField(verbose_name="Oluşturulma Tarihi",auto_now_add=True)
    article_image = models.FileField(blank=True,null=True,verbose_name="Resim Ekle")





