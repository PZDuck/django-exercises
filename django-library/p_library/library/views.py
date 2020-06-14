from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.template import loader
from library.models import Book, Author, Redaction, Friend
from library.forms import AuthorForm, BookForm, FriendForm
from django.views.generic import CreateView, ListView
from django.urls import reverse_lazy
from django.forms import formset_factory
from django.http.response import HttpResponseRedirect
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages

import json


# Отображение стартовой страницы, нулевой функционал
def index(request):
    return render(request, 'index.html')

# Отображение списка книг из библиотеки
def library(request):
    template = loader.get_template('library.html')
    books = Book.objects.all()
    biblio_data = {
        "title": "my personal library",
        "books": books,
    }
    return HttpResponse(template.render(biblio_data, request))

# Увеличение количества определенной книги
def book_increment(request):
    if request.method == 'POST':
        book_id = request.POST['id']
        if not book_id:
            return redirect('/library/')
        else:
            book = Book.objects.filter(id=book_id).first()
            if not book:
                return redirect('/library/')
            book.copy_count += 1
            book.save()
        return redirect('/library/')
    else:
        return redirect('/library/')

# Уменьшение количества определенной книги
def book_decrement(request):
    if request.method == 'POST':
        book_id = request.POST['id']
        if not book_id:
            return redirect('/library/')
        else:
            book = Book.objects.filter(id=book_id).first()
            if not book:
                return redirect('/library/')
            if book.copy_count < 1:
                book.copy_count = 0
            else:
                book.copy_count -= 1
            book.save()
        return redirect('/library/')
    else:
        return redirect('/library/')

# Отображение списка издательств
def redactions(request):
    template = loader.get_template('redactions.html')
    books = Book.objects.all()
    redactions = Redaction.objects.all()
    data = {
        "redactions": redactions,
        "books": books,
    }

    return HttpResponse(template.render(data, request))

# Отображение списка авторов
class AuthorList(ListView):
    model = Author
    template_name = "authors_list.html"

# Создание нового автора с помощью формы
class AuthorEdit(SuccessMessageMixin, CreateView):
    model = Author
    form_class = AuthorForm
    success_url = reverse_lazy("author_list")
    success_message = "Author was created successfully"
    template_name = "authors_edit.html"

# Отображение списка друзей
class FriendList(ListView):
    model = Friend
    template_name = "friends.html"

# Создание нового друга с помощью формы
class FriendEdit(CreateView):
    model = Friend
    form_class = FriendForm
    success_url = reverse_lazy("friends")
    template_name = "friends_create.html"

# Создание нескольких авторов с помощью formset
def author_create_many(request):
    AuthorFormSet = formset_factory(AuthorForm, extra=2)
    if request.method == 'POST':

        author_formset = AuthorFormSet(request.POST, request.FILES, prefix='authors')

        if author_formset.is_valid():
            for author_form in author_formset:
                author_form.save()
            return HttpResponseRedirect(reverse_lazy('author_list'))
    else:
        author_formset = AuthorFormSet(prefix='authors')
    
    return render(request, 'manage_authors.html', {'author_formset': author_formset})

# Создание нескольких книг и авторов с помощью formset
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
            return HttpResponseRedirect(reverse_lazy('author_list'))
    else:
        author_formset = AuthorFormSet(prefix='authors')
        book_formset = BookFormSet(prefix='books')
    return render(request, 'manage_books_authors.html', {'author_formset': author_formset, 'book_formset': book_formset})

# Выдача книги в долг
def lend_book(request, book_id):
    # Находим нужную книгу и достаем список друзей
    book = Book.objects.get(id__exact=book_id)
    friends = Friend.objects.all()

    if request.method == 'POST':
        friend_id = request.POST.get('id')  # Получаем id нужного друга
        friend = friends.get(id=friend_id)  # и находим его в списке всех друзей

        # Проверка на наличие запрашиваемой книги у друга
        if book in friend.borrowed_books.all():
            messages.error(request, 'This friend already has this book.')
            return HttpResponseRedirect(reverse_lazy('borrowers'))

        friend.borrowed_books.add(book)
        book.copy_count -= 1
        book.save()
        return HttpResponseRedirect(reverse_lazy('borrowers'))

    return render(request, 'lend.html', {'book': book, 'friends': friends})

# Отображение списка должников
def borrowers(request):
    borrowers = Friend.objects.exclude(borrowed_books__isnull=True).all() # Фильтруем запрос, исключая друзей, которые не брали книг вовсе
    return render(request, 'borrowers.html', {'borrowers': borrowers} )