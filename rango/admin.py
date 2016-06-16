#coding:utf-8
from django.contrib import admin
from models import Category,Page,UserProfile
# Register your models here.


admin.site.register(UserProfile)
@admin.register(Page)
class PageAdmin(admin.ModelAdmin):
    list_display = ['title','url','views']
@admin.register(Category)
class CategroyAdmin(admin.ModelAdmin):
    prepopulated_fields =  {'slug':('name',)}#预处理，表框联动效果