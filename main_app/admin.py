from main_app.models import Category, Hairpun, Visit
from django.contrib import admin

# Register your models here.
admin.site.register(Hairpun)
admin.site.register(Visit)
admin.site.register(Category)