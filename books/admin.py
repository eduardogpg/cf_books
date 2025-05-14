from django.contrib import admin
from .models import Book

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'isbn', 'publication_date')
    search_fields = ('title', 'author', 'isbn')
    list_filter = ('publication_date',)
