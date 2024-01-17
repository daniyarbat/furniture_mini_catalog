from django.contrib import admin

from catalog.models import Product, Category, Contact, Version


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
	list_display = ('pk', 'name',)


class VersionInline(admin.StackedInline):
	model = Version
	extra = 1
	can_delete = False
	verbose_name = 'версия'
	verbose_name_plural = 'версии'


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
	list_display = ('pk', 'name', 'price', 'category',)
	list_filter = ('category',)
	search_fields = ('name', 'description')
	inlines = [
		VersionInline,
	]


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
	list_display = ('name', 'email',)
	search_fields = ('name', 'email',)
