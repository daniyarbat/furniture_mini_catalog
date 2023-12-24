from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from catalog.models import Category, Product, Contact


def index(request):
    product_list = Product.objects.all().order_by('pk')
    paginator = Paginator(product_list, 5)
    page_number = request.GET.get("page")
    page_object = paginator.get_page(page_number)
    context = {
        "page_object": page_object,
        'title': 'Мягкая мебель'
    }
    return render(request, 'catalog/index.html', context)


def show_item(request, product_pk):
    item = get_object_or_404(Product, pk=product_pk)
    context = {
        'item': item,
        'title': item
    }
    return render(request, 'catalog/item.html', context)


def contacts(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        print(f'{name} ({email}): {message}')

    contact_list = [{
        'name': contact.name,
        'phone': contact.phone,
        'email': contact.email
    } for contact in Contact.objects.all()]

    context = {
        'title': 'Контакты',
        'contacts': contact_list
    }

    return render(request, "catalog/contacts.html", context)


# def categories(request):
#     context = {
#         'object_list': Category.objects.all(),
#         'title': 'Мягкая мебель: категории'
#     }
#     return render(request, 'catalog/categories.html', context)
#
#
# def category_items(request, pk):
#     category_item = Category.objects.get(pk=pk)
#     context = {
#         'object_list': Product.objects.filter(category_id=pk),
#         'title': f'Мягкая мебель: {category_item.name}'
#     }
#     return render(request, 'catalog/products.html', context)
