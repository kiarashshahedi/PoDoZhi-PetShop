from django.contrib import admin
from .models import Product, ProductImage, Tag, SubCategory, AnimalType, MainCategory

class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 1

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'name_in_list', 'sub_category', 'price', 'stock', 'available', 'is_featured', 'created_at', 'updated_at']
    list_filter = ['available', 'sub_category', 'is_featured', 'created_at', 'updated_at']
    search_fields = ['name', 'sub_category__name', 'manufacturer', ]
    inlines = [ProductImageInline]

@admin.register(ProductImage)
class ProductImageAdmin(admin.ModelAdmin):
    list_display = ['product', 'image']

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']

class SubCategoryInline(admin.TabularInline):
    model = SubCategory
    extra = 1

class MainCategoryInline(admin.TabularInline):
    model = MainCategory
    extra = 1

class AnimalTypeAdmin(admin.ModelAdmin):
    list_display = ('name',)
    inlines = [MainCategoryInline]

class MainCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'animal_type')
    list_filter = ('animal_type',)
    inlines = [SubCategoryInline]

class SubCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'main_category')
    list_filter = ('main_category',)

admin.site.register(AnimalType, AnimalTypeAdmin)
admin.site.register(MainCategory, MainCategoryAdmin)
admin.site.register(SubCategory, SubCategoryAdmin)
