from django.contrib import admin
from .models import *

admin.site.register(Category)
class PostA(admin.ModelAdmin):
    list_display = ('user','quantity')
    list_filter = ("user",)

admin.site.register(Cart,PostA)
class PostAdmin(admin.ModelAdmin):
    list_display = ('category','title','price','data',)
    list_filter = ("category",)


admin.site.register(Products,PostAdmin)