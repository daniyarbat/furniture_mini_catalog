from django.contrib import admin

from catalog.models import Product, Category, Contact, Version


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
	list_display = ('pk', 'name',)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
	list_display = ('pk', 'name', 'price', 'category',)
	list_filter = ('category',)
	search_fields = ('name', 'description')


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
	list_display = ('name', 'email',)
	search_fields = ('name', 'email',)


@admin.register(Version)
class VersionAdmin(admin.ModelAdmin):
	list_display = ('pk', 'product', 'version_number', 'name', 'is_version_active',)
	list_filter = ('product', 'version_number', 'name', 'is_version_active',)
	search_fields = ('product', 'version_number', 'name',)
