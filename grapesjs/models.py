from django.db import models
from django.urls import reverse
#from django_grapesjs.models import GrapesJsHtmlField
from django.utils.html import format_html
from django.contrib import admin

# Create your models here.
class Pages(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=200, unique=True, blank=True)
    # html = GrapesJsHtmlField(apply_django_tag=True)
    html = models.TextField()
    css = models.TextField()
    # Link xem trước bài đăng
    preview_link = models.TextField(default='')
    # Bật kích hoạt đăng bài
    is_active = models.BooleanField(default=True)
    is_home = models.BooleanField(default=False)
    
    def get_url(self):
        return reverse(args=[self.name])
    
    def __str__(self):
        return self.slug