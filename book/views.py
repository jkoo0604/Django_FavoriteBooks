from django.shortcuts import render, redirect
from .models import *
from datetime import datetime, timedelta
import pytz
from django.contrib import messages
from django.http import JsonResponse

# Create your views here.
def index(request):
    # Render welcome.html
    if 'userid' in request.session:
        user = User.objects.filter(id=request.session['userid'])
        if user:
            context = {
                'current_user': User.objects.get(id=request.session['userid']),
                'all_books': Book.objects.all(),
            }
            return render(request,'welcome.html',context)
    return redirect('/')

def bookInfo(request, bookid):
    # Render bookdetail.html
    if 'userid' in request.session and request.method == 'GET':
        user = User.objects.filter(id=request.session['userid'])
        book = Book.objects.filter(id=bookid)
        if user and book:
            context = {
                'current_user': User.objects.get(id=request.session['userid']),
                'one_book': Book.objects.get(id=bookid),
                'all_books': Book.objects.all(),
            }
            return render(request,'bookdetail.html',context)
    return redirect('/book')

def userInfo(request):
    # Render userdetail.html
    if 'userid' in request.session:
        user = User.objects.filter(id=request.session['userid'])
        if user:
            context = {
                'current_user': User.objects.get(id=request.session['userid']),
                'liked_by_user': Book.objects.filter(liked_by__id=request.session['userid']).exclude(uploaded_by__id=request.session['userid']).all()
            }
            return render(request,'userdetail.html',context)
    return redirect('/book')

def addBook(request):
    #Process POST request for new book
    #   Redirect to index
    if request.method == 'POST' and 'userid' in request.session:
        user = User.objects.filter(id=request.session['userid'])
        if user:
            errors = Book.objects.basic_validator(request.POST)
            if len(errors) > 0:
                for key, value in errors.items():
                    messages.error(request, value, extra_tags=key)
                return redirect('/book')
            newbook = Book.objects.create(title=request.POST['title'],desc=request.POST['desc'],uploaded_by_id=request.session['userid'])
            # currentuser = User.objects.get(id=request.session['userid'])
            # currentuser.books_liked.add(newbook)
            user[0].books_liked.add(newbook)
            return redirect(f'/book/{newbook.id}')
            # if request.is_ajax():
            #     return render(request,'posts-index.html',context)
    return redirect('/book')

def updateBook(request, bookid):
    #Process POST request for update
    #   Redirect to index
    if request.method == 'POST' and 'userid' in request.session:
        user = User.objects.filter(id=request.session['userid'])
        book = Book.objects.filter(id=bookid)
        if user and book:
            errors = Book.objects.edit_validator(request.POST,bookid)
            if len(errors) > 0:
                for key, value in errors.items():
                    messages.error(request, value, extra_tags=key)
                return redirect(f'/book/{bookid}')

            # updatebook = Book.objects.get(id=bookid)
            # if updatebook.uploaded_by_id == request.session['userid']:
            #     updatebook.title = request.POST['title']
            #     updatebook.desc = request.POST['desc']
            #     updatebook.save()
            if book[0].uploaded_by_id == request.session['userid']:
                book[0].title = request.POST['title']
                book[0].desc = request.POST['desc']
                book[0].save()
            return redirect(f'/book/{bookid}')
            # if request.is_ajax():
            #     return render(request,'posts-index.html',context)
    return redirect('/book')

def deleteBook(request, bookid):
    #Process request to delete book made by user who uploaded it
    #   Redirect to index
    if 'userid' in request.session:
        user = User.objects.filter(id=request.session['userid'])
        book = Book.objects.filter(id=bookid)
        if user and book:
            # deletebook = Book.objects.get(id=bookid)
            # if deletebook.uploaded_by_id == request.session['userid']:
            #     deletebook.delete()
            if book[0].uploaded_by_id == request.session['userid']:
                book[0].delete()
                return redirect('/book')
            else:
                return redirect(f'/book/{bookid}')
            # if request.is_ajax():
            #     return render(request,'posts-index.html',context)
    return redirect('/book')

def addFavorite(request,bookid):
    if 'userid' in request.session:
        user = User.objects.filter(id=request.session['userid'])
        book = Book.objects.filter(id=bookid)
        if user and book:
            user = User.objects.get(id=request.session['userid'])
            book = Book.objects.get(id=bookid)
            if not user in book.liked_by.all():
                user.books_liked.add(book)
            return redirect(f'/book/{bookid}')
            # if request.is_ajax():
            #     return render(request,'posts-index.html',context)
    return redirect('/book')

def removeFavorite(request,bookid):
    if 'userid' in request.session:
        user = User.objects.filter(id=request.session['userid'])
        book = Book.objects.filter(id=bookid)
        if user and book:
            user = User.objects.get(id=request.session['userid'])
            book = Book.objects.get(id=bookid)
            if user in book.liked_by.all():
                user.books_liked.remove(book)
            return redirect(f'/book/{bookid}')
            # if request.is_ajax():
            #     return render(request,'posts-index.html',context)
    return redirect('/book')

# index
#   render welcome.html
#   session userid
#   context: books.all
#   display all books in div (scrollbar auto)
#   for each book, if book is liked by session userid, then display 'liked' otherwise display like button


# create
#   process POST request to create book
#   create and use validator
#   create many to many relationship between user and book also


# update
#   process POST request to update book
#   session userid must match book created by
#   use validator


# bookinfo
#   render book detail page


# userinfo
#   render user detail page


# addfavorite
#   like a book
#   create a many to many relationship
#   reload current page (or jquery)
#   use hidden input (or custom attribute) to go back to previous page?


# removefavorite
#   unlike a book
#   remove many to many relationship
#   reload current page (or jquery)