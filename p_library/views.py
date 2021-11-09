from django.utils import timezone
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, View, DetailView, UpdateView, DeleteView
from django.template import loader
from django.shortcuts import HttpResponse, redirect, render
from django.forms import formset_factory
from django.http.response import HttpResponseRedirect
from p_library.models import Author, Book, Publisher
from p_library.forms import AuthorForm, BookForm
import json

# Create your views here.

def book_list(request):
	books = Book.objects.all()
	return HttpResponse(books)

def index(request):
	template = loader.get_template('index.html')
	books = Book.objects.all()
	biblio_data = {
		'title': 'My Library',
		'books': books,
	}
	return HttpResponse(template.render(biblio_data, request))

# def publishers(request):
# 	template = loader.get_template('publishers.html')
# 	publisher_list = Publisher.objects.all()
# 	data = {
# 		'publisher_list': publisher_list,
# 	}
# 	return HttpResponse(template.render(data, request))

def book_increment(request):
	if request.method == 'POST':
		book_id = request.POST['id']
		if not book_id:
			return redirect('/index/')
		else:
			book = Book.objects.filter(id=book_id).first()
			if not book:
				return redirect('/index/')
			book.copy_count += 1
			book.save()
		return redirect('/index/')
	else:
		return redirect('/index/')

def book_decrement(request):
	if request.method == 'POST':
		book_id = request.POST['id']
		if not book_id:
			return redirect('/index/')
		else:
			book = Book.objects.filter(id=book_id).first()
			if not book:
				return redirect('/index/')
			if book.copy_count < 1:
				book.copy_count = 0
				return redirect('/index/')
			else:
				book.copy_count -= 1
			book.save()
		return redirect('/index/')
	else:
		return redirect('/index/')	


class AuthorEdit(CreateView):
	model = Author
	form_class = AuthorForm
	success_url = reverse_lazy('authors_list')
	template_name = 'author_edit.html'

def author_create_many(request):
	AuthorFormSet = formset_factory(AuthorForm, extra=2)
	if request.method == 'POST':
		author_formset = AuthorFormSet(request.POST, request.FILES, prefix='authors')
		if author_formset.is_valid():
			for author_form in author_formset:
				author_form.save()
			return HttpResponseRedirect(reverse_lazy('p_library:author_list'))
	else:
		author_formset = AuthorFormSet(prefix='authors')
	return render(request, 'manage_authors.html', {'author_formset': author_formset})

def books_authors_create_many(request):
	AuthorFormSet = formset_factory(AuthorForm, extra=2)
	BookFormSet = formset_factory(BookForm, extra=2)
	if request.method == 'POST':
		author_formset = AuthorFormSet(request.POST, request.FILES, prefix='authors')
		book_formset = BookFormSet(request.POST, request.FILES, prefix='books')
		if author_formset.is_valid() and book_formset.is_valid():
			for author_form in author_formset:
				author_form.save()
			for book_form in book_formset:
				book_form.save()
			return HttpResponseRedirect(reverse_lazy('p_library.author_list'))
	else:
		author_formset = AuthorFormSet(prefix='authors')
		book_formset = BookFormSet(prefix='books')
	
	return render(
		request,
		'manage_books_authors.html',
		{
			'author_formset': author_formset,
			'book_formset': book_formset,
		}
	)



class AuthorCreate(CreateView):
	model = Author
	fields = '__all__'
	template_name = 'author_edit.html'
	success_url = reverse_lazy('authors_list')

class AuthorUpdate(UpdateView):
	model = Author
	fields = '__all__'
	template_name = 'author_edit.html'
	success_url = reverse_lazy('authors_list')

class AuthorDelete(DeleteView):
	model = Author
	fields = '__all__'
	template_name = 'author_delete.html'
	success_url = reverse_lazy('authors_list')





# H/W Views

def home_view(request, *args, **kwargs):
	return render(request, 'pages/home.html', {})


# Book Views

class BookList(ListView):
	model = Book
	context_object_name = 'books'
	template_name = 'pages/books/book_list.html'


class BookDetail(DetailView):
	model = Book
	template_name = 'pages/books/book_detail.html'

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		return context

class BookUpdate(UpdateView):
	model = Book
	fields = '__all__'
	context_object_name = 'book'
	template_name = 'pages/books/book_update.html'
	success_url = '../'

class BookDelete(DeleteView):
	model = Book 
	context_object_name = 'book'
	template_name = 'pages/books/book_delete.html'
	success_url = '/book_list/'

class AddBook(CreateView):
	model = Book
	fields = '__all__'
	template_name = 'pages/books/add_book.html'
	success_url = '/book_list/'


# Author Views

class AuthorList(ListView):
	model = Author
	context_object_name = 'authors'
	template_name = 'pages/authors/author_list.html'

class AuthorDetail(DetailView):
	model = Author
	template_name = 'pages/authors/author_detail.html'

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		return context

class AuthorUpdate(UpdateView):
	model = Author
	fields = '__all__'
	context_object_name = 'author'
	template_name = 'pages/authors/author_update.html'
	success_url = '../'

class AuthorDelete(DeleteView):
	model = Author 
	context_object_name = 'author'
	template_name = 'pages/authors/author_delete.html'
	success_url = '/author_list/'

class AddAuthor(CreateView):
	model = Author
	fields = '__all__'
	template_name = 'pages/authors/add_author.html'
	success_url = '/author_list/'


# Publisher Views

class PublisherList(ListView):
	model = Publisher
	context_object_name = 'publishers'
	template_name = 'pages/publishers/publisher_list.html'


class PublisherDetail(DetailView):
	model = Publisher
	template_name = 'pages/publishers/publisher_detail.html'

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		return context

class PublisherUpdate(UpdateView):
	model = Publisher
	fields = '__all__'
	context_object_name = 'publisher'
	template_name = 'pages/publishers/publisher_update.html'
	success_url = '../'

class PublisherDelete(DeleteView):
	model = Publisher 
	context_object_name = 'publisher'
	template_name = 'pages/publishers/publisher_delete.html'
	success_url = '/publisher_list/'

class AddPublisher(CreateView):
	model = Publisher
	fields = '__all__'
	template_name = 'pages/publishers/add_publisher.html'
	success_url = '/publisher_list/'


# Other Views

def add_view(request, *args, **kwargs):
	return render(request, 'pages/add.html', {})