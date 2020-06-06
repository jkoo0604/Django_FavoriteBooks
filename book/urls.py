from django.urls import path
from . import views

urlpatterns = [ 
    path('', views.index),
    path('<int:bookid>', views.bookInfo),
    path('user', views.userInfo),
    path('addnew', views.addBook),
    path('update/<int:bookid>', views.updateBook),
    path('delete/<int:bookid>', views.deleteBook),
    path('addtofavorite/<int:bookid>', views.addFavorite),
    path('removefavorite/<int:bookid>', views.removeFavorite),
]