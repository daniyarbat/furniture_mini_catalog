from django.shortcuts import render

from catalog.models import Category, Product, Contact


def index(request):
    context = {
        'object_list': Product.objects.all(),
        'title': 'Мягкая мебель для уютного дома'
    }
    return render(request, 'catalog/index.html', context)


def categories(request):
    context = {
        'object_list': Category.objects.all(),
        'title': 'Мягкая мебель: категории'
    }
    return render(request, 'catalog/categories.html', context)


def category_items(request, pk):
    category_item = Category.objects.get(pk=pk)
    context = {
        'object_list': Product.objects.filter(category_id=pk),
        'title': f'Мягкая мебель: {category_item.name}'
    }
    return render(request, 'catalog/products.html', context)


def contacts(request):
    context = {
        'object_list': Contact.objects.all(),
        'title': 'Контакты'
    }
    return render(request, 'catalog/contacts.html', context)


# def contacts(request):
#     if request.method == 'POST':
#         name = request.POST.get('name')
#         email = request.POST.get('email')
#         message = request.POST.get('message')
#         print(f'{name} ({email}): {message}')
#     return render(request, "catalog/contacts.html")
