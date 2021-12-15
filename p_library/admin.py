from django.contrib import admin
from p_library.models import Author, Book, Publisher, Friend, Reader

# Register your models here.

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
	list_display = ('title', 'author')

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
	pass

@admin.register(Publisher)
class PublisherAdmin(admin.ModelAdmin):
	pass

@admin.register(Friend)
class FriendAdmin(admin.ModelAdmin):
	pass

@admin.register(Reader)
class ReaderAdmin(admin.ModelAdmin):
	pass