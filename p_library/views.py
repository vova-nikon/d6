from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib import auth
from django.contrib.auth import login, authenticate
from django.utils import timezone
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, View, DetailView, UpdateView, DeleteView, FormView
from django.template import loader
from django.shortcuts import HttpResponse, redirect, render
from django.forms import formset_factory
from django.http.response import HttpResponseRedirect
from p_library.models import Author, Book, Publisher, Reader
from p_library.forms import AuthorForm, BookForm, ReaderCreationForm
import json

# Create your views here.

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


class RegisterView(FormView):
	form_class = UserCreationForm
	def form_valid(self, form):
		form.save()
		username = form.cleaned_data.get('username')
		raw_password = form.cleaned_data.get('password1')
		login(self.request, authenticate(username=username, password=raw_password))
		return super(RegisterView, self).form_valid(form)

class CreateReaderProfile(FormView):
	form_class = ReaderCreationForm
	template_name = 'reader-create.html'
	success_url = '/../'

	def dispatch(self, request, *args, **kwargs):
		if self.request.user.is_anonymous:
			return HttpResponseRedirect('/login')
		return super(CreateReaderProfile, self).dispatch(request, *args, **kwargs)

	def form_valid(self, form):
		instance = form.save(commit=False)
		instance.user = self.request.user
		instance.save()
		return super(CreateReaderProfile, self).form_valid(form)