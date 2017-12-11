from django.contrib import admin
from .models import *

# Register your models here.

# admin.site.register(Book)
# admin.site.register(Author)
admin.site.register(Genre)
# admin.site.register(BookInstance)
admin.site.register(Language)

class Bookinline(admin.StackedInline):
    model = Book

# Define the admin class to customize how the author model shows in the admin site
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'date_of_birth', 'date_of_death')
    fields = ['first_name', 'last_name', ('date_of_birth', 'date_of_death')]
    inlines = [Bookinline]
#Register the admin class with the associated model
admin.site.register(Author, AuthorAdmin)

#Register the admin classes for book using the decorator

class BooksInstanceInline(admin.TabularInline):
    model = BookInstance

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'display_genre')
    inlines = [BooksInstanceInline]

#Register the Admin Classses for BookInstance using the decorator

@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
    list_display = ('id', 'book', 'borrower','status', 'due_back')
    list_filter = ('status', 'due_back')
    fieldsets = (
        (None,{
            'fields': ('book', 'imprint', 'id')
        }),
        ('Availability',{
            'fields': ('status', 'due_back', 'borrower')
        }),
    )