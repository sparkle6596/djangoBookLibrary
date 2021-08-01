from django.urls import path
from .views import book_add,get_books,book_details,remove_book,update_book,create_account,singn_in,signout
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

urlpatterns=[
    path("bookadd",book_add,name="adds"),
    path('books/accounts',create_account,name="regester"),
    path('books/account/singnin',singn_in,name="singnin"),
    path('books/account/singnout',signout,name="singnout"),
    path("index",login_required(lambda request:render(request,"index.html"),login_url="singnin"),name="index"),
    path('books',get_books,name="books"),
    path('books/<int:id>',book_details,name="details"),
    path('books/remove/<int:id>',remove_book,name="remove"),
    path('books/change/<int:id>',update_book,name="update")


]