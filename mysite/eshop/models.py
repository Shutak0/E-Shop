from django.db import models
from django.urls import reverse
class Group(models.Model): 
    '''
    Group - образец, по которому существуют все группы; служит для разделения всех товаров на группы
    '''
    name = models.TextField(max_length=30) #Name - название конкретной группы
    image = models.ImageField() #Image - картинка конкретной группы
    def get_absolute_url(self): #Функция, которая должна бы возвращать ссылку на этот конкретный товар, но с ней косяки *
        return reverse("eshop:group", args=[self.name])
class Product(models.Model): 
    '''
    Product - образец, по которому существуют все товары в магазине
    '''
    name = models.TextField(max_length=12) #Name - название конкретного товара
    author = models.CharField(max_length=16) #Author - имя пользователя, разместившего конкретный товар
    group = models.ForeignKey(Group, on_delete=models.SET_NULL, null=True) #Group - принадлежность конкретного товара к конкретной группе 
    created = models.DateField(auto_now_add=True) #Created - дата создания конкретного товара
    text = models.TextField(max_length=500) #Text - Описание конкретного товара
    specification = models.CharField(max_length=50) #Specification - принадлежность конкретного товара к той или иной спецификации; для упрощения поиска
    image = models.ImageField(upload_to='products/%Y/%m/%d', blank=True) #Image - картинка конкретного товара
    cost = models.TextField(max_length=20) #Cost - цена конкретного товара
    amount = models.TextField(max_length=10) #Amount - количество конкертного товара
    slug = models.SlugField(max_length=200, db_index=True) #Slug - уникальный код, предназначенный для отличимости каждого конкретного товара, и для создания ссылок
    def get_absolute_url(self): #Функция, возвращающая ссылку на этот конкретный товар
        return reverse("eshop:productpage", args=[self.id, self.slug])
    