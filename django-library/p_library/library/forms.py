from django import forms
from library.models import Author, Book, Friend


# Модель создания нового автора
class AuthorForm(forms.ModelForm):
    full_name = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',            # Добавляем бутстраповский класс для стайлинга формы
            'placeholder': 'e.g. John Doe',     # Добавляем placeholder для конкретики
        }
    ))
    birth_year = forms.IntegerField(widget=forms.NumberInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'e.g. 1954',
        }
    ))
    country = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'e.g. EN',
        }
    ))

    class Meta:
        model = Author
        fields = '__all__'

# Форма создания новой книги
class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = '__all__'

# Форма создания нового друга. Работала бы в реальной жизни, эхх...
class FriendForm(forms.ModelForm):
    class Meta:
        model = Friend
        fields = '__all__'
