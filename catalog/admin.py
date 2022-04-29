from django.contrib import admin
from .models import Author, Genre, Book, BookInstance
# Register your models here

"""admin.site.register(Author)
admin.site.register(Genre)
admin.site.register(Book)
admin.site.register(BookInstance)"""

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'date_of_birth', 'date_of_death')
    #fields = ['last_name', 'first_name', ('date_of_birth', 'date_of_death')] # Если поля в кортеже то будут отобр горизонтально

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'display_genre')
    list_filter = ('author', 'title')

@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
    list_display = ('book', 'status', 'due_back', 'id')
    list_filter = ('status', 'due_back')

