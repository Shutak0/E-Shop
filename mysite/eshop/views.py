from django.shortcuts import render
from .models import Product, Group
from django.shortcuts import get_object_or_404
def index(request): 
    '''
    Для index.html, возвращает список всех существующих товаров, пока без сортировки, + прогружает страницу.
    '''
    products = Product.objects.all()
    return render(request, 'html/index.html', {'products':products})
def productpage(request, id, slug): 
    '''
    Для productpage.html, генерирует страницу с конкретным товаром по id и slug, ссылка на который доступна из index.html/search.html. Прогружает страницу.
    '''
    id = int(id)
    product = get_object_or_404(Product, id=id, slug=slug)
    return render(request, 'html/productpage.html', {'product':product})
def search(request):
    '''
    Для search.html, в случае поиска по какому-то слову - ищет по тому слову во всех товарах, и выдаёт искомое; прогружает страницу.
    '''
    needed = None
    text_search = None
    if request.method == 'POST':
        text_search = request.POST.get('text', False)
        needed = Product.objects.filter(name__icontains=text_search)
    return render(request, 'html/search.html', {'products':needed})
def categories(request):
    '''
    Формирует страницу со списком всех существующих групп товаров.
    '''
    categories = Group.objects.all()
    return render(request, 'html/categories.html', {'categories': categories})
def group(request, name):
    '''
    Должно бы действовать по аналогии с productpage, ища нужный список продуктов, относящихся к одной группе товаров.
    Получает имя и запрос из models.py Group get_absolute_url().
    Любит вредничать.
    '''
    needed = Product.objects.filter(group__name=name)
    return render(request, 'html/group.html', {'products': needed})