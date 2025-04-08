from django.contrib import admin
from .models import Category, SubCategory, Product, Cart, Comment

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'slug', 'created_at')
    search_fields = ('name', 'slug', 'created_at')

class SubcategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'category', 'name', 'slug')
    search_fields = ('category__name', 'name', 'slug')
    list_filter = ('category',)

class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'subcategory', 'name', 'price', 'stock', 'slug', 'created_at')
    search_fields = ('name', 'slug')
    list_filter = ('subcategory',)

class CartAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'product', 'quantity', 'added_at')
    search_fields = ('user__username', 'product__name')

class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'product', 'text', 'created_at')
    search_fields = ('user__username', 'product__name', 'text')
    list_filter = ('rating', 'created_at')

admin.site.register(Category, CategoryAdmin)
admin.site.register(SubCategory, SubcategoryAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Cart, CartAdmin)
admin.site.register(Comment, CommentAdmin)
