from django.urls import path, include
from . import views
from .views import AuthorEdit, AuthorList, FriendEdit, FriendList

app_name = 'library'
urlpatterns = [
    path('', views.index, name='home'), # путь домашней страницы, использует шаблон index.html
    path('library/', views.library, name='library'), # путь библиотеки, шаблон library.html
    path('book_increment/', views.book_increment),    
    path('book_decrement/', views.book_decrement), # пути форм для добавления/изъятия книг из библиотеки, шаблоны book_increment.html. book_decrement.html соответсвенно
    path('redactions/', views.redactions, name='redactions'), # путь издательств, шаблон redactions.html
    path('authors/create', AuthorEdit.as_view(), name='author_create'), # путь формы создания автора, шаблон author_edit.html
    path('authors', AuthorList.as_view(), name='author_list'), # путь списка авторов, шаблон authors_list.html
    path('authors/create_many', views.author_create_many, name='author_create_many'),
    path('authors/books_authors_create_many', views.books_authors_create_many, name='books_authors_create_many'), # два пути из модуля, могут быть игнорированы
    path('friends', FriendList.as_view(), name='friends'), # путь списка друзей, шаблон friends.html
    path('friends/create', FriendEdit.as_view(), name='friend_create'), # путь формы создания друзей, шаблон friends_create.html
    path('lend/<int:book_id>', views.lend_book, name='lend'), # путь формы одалживания книги, шаблон lend.html
    path('borrowers', views.borrowers, name='borrowers'), # путь списка должников, путь borrowers.html
]