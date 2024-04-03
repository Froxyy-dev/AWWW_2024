from django.contrib import admin

from .models import Image, Rectangle, UserToImage

# Register your models here.

admin.site.register(Image)
admin.site.register(Rectangle)
admin.site.register(UserToImage)
