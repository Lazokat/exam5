from django.forms import ModelForm
from .models import *
class PostForm(ModelForm):
    class Meta:
        model=Products
        fields=('__all__')

