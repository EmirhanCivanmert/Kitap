from django.contrib import admin
from .models import Kitap, Category, Slider

@admin.register(Kitap)
class KitapAdmin(admin.ModelAdmin):
    list_display = ("title","isActive","isHome","slug","category_list")
    list_display_links = ("title","slug",)
    prepopulated_fields = {"slug":("title",),}
    list_filter = ("isActive","isHome",)
    list_editable = ("isActive","isHome",)
    search_fields = ("title","description")

    def category_list(self, obj):
        html = ""
        for category in obj.categories.all():
            html += category.name + " "
        return html

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name","slug","book_count")
    prepopulated_fields = {"slug":("name",),}

    def book_count(self, obj):
        return obj.books.count()
    
admin.site.register(Slider)