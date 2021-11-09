from django.db import models
from django.urls import reverse

# Create your models here.

class Author(models.Model):
	full_name = models.CharField(max_length=100)
	birth_year = models.SmallIntegerField()
	country = models.CharField(max_length=2)
	image = models.ImageField(null=True, blank=True)
	def __str__(self):
		return self.full_name

class Publisher(models.Model):
	name = models.CharField(max_length=100)
	def __str__(self):
		return self.name

class Friend(models.Model):
	name = models.CharField(max_length=100)
	def __str__(self):
		return self.name

class Book(models.Model):
	ISBN = models.CharField(max_length=13)
	image = models.ImageField(null=True, blank=True)
	title = models.CharField(max_length=999)
	description = models.TextField()
	year_release = models.SmallIntegerField()
	author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books')
	publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE, null=True, blank=True, related_name='books')
	copy_count = models.IntegerField(default=1)
	price = models.DecimalField(default=0.00, max_digits=10, decimal_places=2)
	friend = models.ForeignKey(Friend, on_delete=models.SET_NULL, null=True, blank=True)
	def __str__(self):
		return self.title

