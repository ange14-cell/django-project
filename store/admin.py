from django.contrib import admin
from store.models import Product, Cart, Order


class ProductAdmin(admin.ModelAdmin):
    list_display = ("name", "price", "stock", "slug",)
    search_fields = ["name"]
    list_editable = ("price", "stock", "slug",)
    list_display_links = ("name",)


admin.site.register(Product, ProductAdmin)
admin.site.register(Order)
admin.site.register(Cart)