from django.shortcuts import render
from .models import Product, Group
from django.shortcuts import get_object_or_404
def index(request): 
    '''
    For index.html, returns a list of all existing products, not sorted yet, + loads the page.
    '''
    products = Product.objects.all()
    return render(request, 'html/index.html', {'products':products})
def productpage(request, id, slug): 
    '''
    For productpage.html, generates a page with a specific product by id and slug, the link to which is available from index.html/search.html. Loads the page.
    '''
    id = int(id)
    product = get_object_or_404(Product, id=id, slug=slug)
    return render(request, 'html/productpage.html', {'product':product})
def search(request):
    '''
    For search.html, in case of searching for a certain word, it searches for that word in all products, and returns the search result; loads the page.
    '''
    needed = None
    text_search = None
    if request.method == 'POST':
        text_search = request.POST.get('text', False)
        needed = Product.objects.filter(name__icontains=text_search)
    return render(request, 'html/search.html', {'products':needed})
def categories(request):
    '''
    Generates a page with a list of all existing product groups.
    '''
    categories = Group.objects.all()
    return render(request, 'html/categories.html', {'categories': categories})
def group(request, name):
    '''
    It should act like a productpage, looking for the desired list of products that belong to the same product group.
    Gets name and query from models.py Group get_absolute_url().
    '''
    needed = Product.objects.filter(group__name=name)
    return render(request, 'html/group.html', {'products': needed})
def login(request):
    return render(request, 'html/login.html')
def profile(request):
    return render(request, 'html/profile.html')