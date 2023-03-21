from django.contrib import admin

from .models import Product, Group

class ProductAdmin(admin.ModelAdmin): #Передаёт в Админку информацию от models; Product
    list_display =  ['author', 'text', 'name', 'group', 'created', 'specification', 'image', 'cost', 'amount', 'id'] 
    list_filter = ['author', 'text', 'name', 'group', 'created', 'specification', 'image', 'cost', 'amount', 'id']
    prepopulated_fields = {'slug': ('name',)}
class GroupAdmin(admin.ModelAdmin): #Передаёт в Админку информацию от models; Group
    list_display =  ['name', 'image']
    list_filter = ['name', 'image']
admin.site.register(Product, ProductAdmin)
admin.site.register(Group, GroupAdmin)