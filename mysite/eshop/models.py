from django.db import models
from django.urls import reverse
class Group(models.Model): 
    '''
    Group - the pattern by which all groups exist; serves to divide all goods into groups
    '''
    name = models.TextField(max_length=30) #Name - the name of a specific group
    image = models.ImageField() #Image - a picture of a specific group
    def get_absolute_url(self): #A function that should return a link to this particular product
        return reverse("eshop:group", args=[self.name])
class Product(models.Model): 
    '''
    Product - a sample by which all goods in the store exist
    '''
    name = models.TextField(max_length=12) #Name - the name of a specific product
    author = models.CharField(max_length=16) #Author - the name of the user who posted the specific product
    group = models.ForeignKey(Group, on_delete=models.SET_NULL, null=True) #Group - принадлежность конкретного товара к конкретной группе 
    created = models.DateField(auto_now_add=True) #Group - belonging of a particular product to a particular group
    text = models.TextField(max_length=500) #Text - Description of a specific product
    specification = models.CharField(max_length=50) #Specification - belonging of a particular product to a particular specification; to simplify the search
    image = models.ImageField(upload_to='products/%Y/%m/%d', blank=True) #Image - a picture of a specific product
    cost = models.TextField(max_length=20) #Cost - the price of a specific product
    amount = models.TextField(max_length=10) #Amount - amount of specific item
    slug = models.SlugField(max_length=200, db_index=True) #Slug - a unique code designed to distinguish each particular product and to create links
    def get_absolute_url(self): #A function that returns a link to this particular product
        return reverse("eshop:productpage", args=[self.id, self.slug])
    