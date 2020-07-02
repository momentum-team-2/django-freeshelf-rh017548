from django import forms
from .models import Books


class BookForm(forms.ModelForm):
    class Meta:
        model = Books
        fields = [
            'coverpicture',
            'title',
            'author',
            'url',
            'description',
            
        ]