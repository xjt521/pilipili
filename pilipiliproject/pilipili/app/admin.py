from django.contrib import admin
from app.models import User,Post
# Register your models here.

class Administrator(admin.ModelAdmin):
    list_display = ('user_password','id')


admin.site.register(User,Administrator)