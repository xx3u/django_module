from django.contrib import admin

from .models import Product, Store, StoreItem, Order, OrderItem


class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price')


class StoreItemInLine(admin.TabularInline):
    model = StoreItem
    extra = 0


class StoreAdmin(admin.ModelAdmin):
    list_display = ('id', 'location')
    inlines = (StoreItemInLine,)


class OrderItemInLine(admin.StackedInline):
    model = OrderItem
    extra = 0


class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'city')
    inlines = (OrderItemInLine,)


admin.site.register(Product, ProductAdmin)
admin.site.register(Store, StoreAdmin)
admin.site.register(Order, OrderAdmin)
