from django.forms import ModelForm
from .models import Rectangle


class RectangleForm(ModelForm):
    class Meta:
        model = Rectangle
        fields = ['X', 'Y', 'width', 'height', 'color']

