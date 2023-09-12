# from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from LLC_AI_VA_core.models import Book

def book_list(request):
    books = Book.objects.all()
    return render(request, 'book_list.html', {'books': books})
