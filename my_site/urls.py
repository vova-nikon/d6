"""my_site URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from p_library import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    # Book Views
    path('book_list/', views.BookList.as_view()),
    path('book/<pk>/', views.BookDetail.as_view()),
    path('book/<pk>/update/', views.BookUpdate.as_view()),
    path('book/<pk>/delete/', views.BookDelete.as_view()),
    path('add/book/', views.AddBook.as_view()),
    # Author Views
    path('author_list/', views.AuthorList.as_view()),
    path('author/<pk>/', views.AuthorDetail.as_view()),
    path('author/<pk>/update/', views.AuthorUpdate.as_view()),
    path('author/<pk>/delete/', views.AuthorDelete.as_view()),
    path('add/author/', views.AddAuthor.as_view()),
    # Publisher Views
    path('publisher_list/', views.PublisherList.as_view()), 
    path('publisher/<pk>/', views.PublisherDetail.as_view()),
    path('publisher/<pk>/update/', views.PublisherUpdate.as_view()),
    path('publisher/<pk>/delete/', views.PublisherDelete.as_view()),
    path('add/publisher/', views.AddPublisher.as_view()),
    # Other Views
    path('', views.home_view),
    path('add/', views.add_view),
    path('', include('p_library.urls', namespace='p_library')),
    path('accounts/', include('allauth.urls')),


]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)