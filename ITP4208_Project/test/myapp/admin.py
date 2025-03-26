from django.contrib import admin
from .models import ModelAuthor, ModelPost
# Register your models here.
admin.site.register(ModelAuthor)
admin.site.register(ModelPost)
