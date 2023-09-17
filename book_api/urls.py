from django.urls import path
# from .views import book_list, book_create, book_detail
from .views import BookList, BookCreate, BookDetail

urlpatterns = [
  path("", BookCreate.as_view(), name="book-create"),
  path("<int:pk>/", BookDetail.as_view(), name="book-detail"),
  # path("list/", book_list, name="book-list"),
  path("list/", BookList.as_view(), name="book-list"),
]