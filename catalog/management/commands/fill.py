from django.core.management import BaseCommand
from django.db import connection
from catalog.models import Product, Category


class Command(BaseCommand):

    def handle(self, *args, **options):
        categories_list = [
            {'name': 'Стул', 'description': 'Стулья для гостиной и кухни'},
            {'name': 'Кресло', 'description': 'Кресла для дома, офиса и кафе'},
            {'name': 'Софа', 'description': 'Диваны для жилых и офисных помещений'},
            {'name': 'Диван', 'description': 'Диваны для гостиных и спален'},
        ]

        product_list = [
            {'name': 'Torino', 'description': 'Функциональная модель для разнообразных интерьерных решений', 'category_id': 1, 'price': '440.00'},
            {'name': 'Napoli', 'description': 'Функциональная и лаконичная модель для кофеен и ресторанов', 'category_id': 2, 'price': '590.00'},
            {'name': 'Milano', 'description': 'Роскошная модель для изысканных гостиных и офисных помещений', 'category_id': 3, 'price': '890.00'},
            {'name': 'Firenze', 'description': 'Функциональная модель для разнообразных интерьерных решений', 'category_id': 2, 'price': '690.00'},
            {'name': 'Venezia', 'description': 'Изысканная модель для уютных гостиных и гостевых комнат', 'category_id': 4, 'price': '1190.00'},
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
