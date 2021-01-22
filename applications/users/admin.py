from django.contrib import admin
from .models import User, Doctor
admin.site.register(User)

# Register your models here.
# @admin.register(User)
# class UserAdmin(admin.ModelAdmin):
#     class Media:
#         js = [
#             'js/mask-plugin/jquery.mask.js', 
#             'js/mask-plugin/jquery.mask.min.js',
#             'js/app.js',
#         ]