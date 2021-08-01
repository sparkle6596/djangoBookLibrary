from django import forms
from book.models import Books
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class AddBookForm(forms.Form):
    book_name=forms.CharField(widget=forms.TextInput(attrs={'class':"form-control"}))
    author=forms.CharField(widget=forms.TextInput(attrs={'class':"form-control"}))
    category=forms.CharField(widget=forms.TextInput(attrs={'class':"form-control"}))
    price=forms.CharField(widget=forms.TextInput(attrs={'class':"form-control"}))
    number_copies=forms.CharField(widget=forms.TextInput(attrs={'class':"form-control"}))
    def clean(self):
        cleaned_data=super().clean()
        book_name=cleaned_data["book_name"]
        price=cleaned_data["price"]
        books=Books.objects.filter(book_name__iexact=book_name)
        if books:
            msg="book already exist"
            self.add_error("book_name",msg)
        try:
            price=int(price)
            if price<0:
                msg="invalid price"
                self.add_error("price",msg)
        except :
            msg="invalid price"
            self.add_error("price", msg)


class UpdateBookForm(forms.Form):
    book_name=forms.CharField(widget=forms.TextInput(attrs={'class':"form-control"}))
    author=forms.CharField(widget=forms.TextInput(attrs={'class':"form-control"}))
    category=forms.CharField(widget=forms.TextInput(attrs={'class':"form-control"}))
    price=forms.CharField(widget=forms.TextInput(attrs={'class':"form-control"}))
    number_copies=forms.CharField(widget=forms.TextInput(attrs={'class':"form-control"}))

    def clean(self):
        cleaned_data = super().clean()

        price = cleaned_data["price"]


        try:
            price = int(price)
            if price < 0:
                msg = "invalid price"
                self.add_error("price", msg)
        except:
            msg = "invalid price"
            self.add_error("price", msg)



class BookCreateModelForm(ModelForm):
    class Meta:
        model=Books
        fields='__all__'
        widgets={
            "book_name":forms.TextInput(attrs={'class':"form-control"}),
            "author":forms.TextInput(attrs={'class':"form-control"}),
            "category":forms.TextInput(attrs={'class':"form-control"}),
            "price":forms.NumberInput(attrs={'class':"form-control"}),
            "copies":forms.NumberInput(attrs={'class':"form-control"})
        }

class SearchForm(forms.Form):
    book_name=forms.CharField(max_length=50,widget=(forms.TextInput(attrs={'class':"form-control"})))



class RegistrationForm(UserCreationForm):
    password1 =forms.CharField(max_length=15,widget=(forms.PasswordInput(attrs={'class':"form-control"})))
    password2 =forms.CharField(max_length=15,widget=(forms.PasswordInput(attrs={'class':"form-control"})))
    class Meta:
        model=User
        fields=["first_name","email","username","password1","password2"]
        widgets={
            "first_name":forms.TextInput(attrs={'class':"form-control"}),
            "username":forms.TextInput(attrs={'class':"form-control"}),
            "email":forms.TextInput(attrs={'class':"form-control"}),

        }
class SignInForm(forms.Form):
    username=forms.CharField(max_length=15,widget=(forms.TextInput(attrs={'class':"form-control"})))
    password = forms.CharField(max_length=15, widget=(forms.PasswordInput(attrs={'class': "form-control"})))



