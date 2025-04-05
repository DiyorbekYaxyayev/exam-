from django.contrib import admin

# Register your models here.


from .models import Category, SubCategory, Product

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'slug', 'created_at')
    search_fields = ('name', 'slug', 'created_at')
    

class SubcategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'category', 'name', 'slug')
    search_fields = ('category__name', 'name', 'slug')
    list_filter = ('category',)

admin.site.register(Category, CategoryAdmin)
admin.site.register(SubCategory, SubcategoryAdmin)