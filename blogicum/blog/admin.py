# ice_cream/admin.py
from django.contrib import admin

# Из модуля models импортируем модель Category...
from .models import User, Post, Category, Location


class PostAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'text',
        'pub_date',
        'author',
        'location',
        'is_published',
        'category'
    )
    list_editable = (
        'title',
        'pub_date',
        'is_published'
    )
    search_fields = ('title',)
    list_filter = ('category',)
    list_display_links = ('text', 'author', 'location', 'category')
    #filter_horizontal = ('toppings',)


# ...и регистрируем её в админке:
admin.site.register(Post, PostAdmin)
admin.site.register(Category)
admin.site.register(Location)

admin.site.empty_value_display = 'Не задано'
