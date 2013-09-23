#coding:utf8
from django.shortcuts import render
from blog.models import BookCategory, Book

def index(req):
    book_list = Book.objects.all()
    book_category_list = BookCategory.objects.all()
    first_book_category_list = [b for b in book_category_list if b.p_category is None]
    print first_book_category_list
    return render(req, u'index.html', {u'first_book_category_list':first_book_category_list, u'book_list':book_list})

