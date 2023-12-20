from django.core.management import BaseCommand
from django.db import connection
from catalog.models import Product, Category


class Command(BaseCommand):

    def handle(self, *args, **options):
        categories_list = [
            {'name': 'Футболка', 'description': 'Какая-то Футболка'},
            {'name': 'Свитшот', 'description': 'Какой-то Свитшот'},
            {'name': 'Худи', 'description': 'Какое-то Худи'},
            {'name': 'Кроссовки', 'description': 'Какие-то Кроссовки'},
        ]

        product_list = [
            {'name': 'Nike', 'description': 'Фирма Nike', 'category_id': 1, 'price': '10000'},
            {'name': 'Adidas', 'description': 'Фирма Adidas', 'category_id': 2, 'price': '11000'},
            {'name': 'Puma', 'description': 'Фирма Puma', 'category_id': 3, 'price': '12000'},
            {'name': 'New balance', 'description': 'Фирма New balance', 'category_id': 2, 'price': '13000'},
            {'name': 'Reebok', 'description': 'Фирма Reebok', 'category_id': 4, 'price': '9000'},
        ]

        for model in (Product, Category):
            model.objects.all().delete()
            table_name = model._meta.db_table

            # сбрасываем счетчик
            with connection.cursor() as cursor:
                query = f"SELECT setval(pg_get_serial_sequence('{table_name}', 'id'), 1, false);"
                cursor.execute(query)

        category_for_create = []
        for category_item in categories_list:
            category_for_create.append(Category(**category_item))

        Category.objects.bulk_create(category_for_create)

        products_for_create = []
        for product_item in product_list:
            products_for_create.append(Product(**product_item))

        Product.objects.bulk_create(products_for_create)
