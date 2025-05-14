from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Book
from .forms import BookForm

# Create your views here.

class BookListView(ListView):
    model = Book
    context_object_name = 'books'
    template_name = 'books/book_list.html'
    ordering = ['-created_at']

class BookDetailView(DetailView):
    model = Book
    context_object_name = 'book'
    template_name = 'books/book_detail.html'

class BookCreateView(CreateView):
    model = Book
    form_class = BookForm
    template_name = 'books/book_form.html'
    success_url = reverse_lazy('books:book_list')

class BookUpdateView(UpdateView):
    model = Book
    form_class = BookForm
    template_name = 'books/book_form.html'
    
    def get_success_url(self):
        return reverse_lazy('books:book_detail', kwargs={'pk': self.object.pk})

class BookDeleteView(DeleteView):
    model = Book
    context_object_name = 'book'
    template_name = 'books/book_confirm_delete.html'
    success_url = reverse_lazy('books:book_list')
