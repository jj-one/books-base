# from django.shortcuts import render
# from django.http import JsonResponse
from rest_framework.response import Response
# from rest_framework.decorators import api_view
# from rest_framework.parsers import JSONParser
from rest_framework import status
from .serializers import BookSerializer
from .models import Book
from django.http import Http404

# # Create your views here.

# @api_view(["GET"])
# def book_list(request):
#   books = Book.objects.all()
#   serializer = BookSerializer(books, many=True)
#   return Response(serializer.data)

#   """python_books = list(books.values())
#   return JsonResponse({
#     "count": len(python_books),

#     "result": python_books
#   })"""

# @api_view(["GET", "PUT", "DELETE"])
# def book_detail(request, pk):
#   try:
#     book = Book.objects.get(id=pk)
#   except Book.DoesNotExist as _:
#     Response(status=status.HTTP_404_NOT_FOUND)

#   if request.method == "GET":
#     serializer = BookSerializer(book)
#     return Response(serializer.data)
#   elif request.method == "PUT":
#     serializer = BookSerializer(book, data=request.data)
#     if serializer.is_valid():
#       serializer.save()
#       return Response(serializer.data, status=status.HTTP_200_OK)
#     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#   else:
#     book.delete()
#     return Response(status=status.HTTP_204_NO_CONTENT)

# @api_view(["POST"])
# def book_create(request):
#   # data = JSONParser().parse(request.data)
#   serializer = BookSerializer(data=request.data)
#   if serializer.is_valid():
#     serializer.save()
#     return Response(serializer.data, status=status.HTTP_201_CREATED)
#   return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


from rest_framework.views import APIView
class BookList(APIView):
  def get(self, request):
    books = Book.objects.all()
    serializer = BookSerializer(books, many=True)
    return Response(serializer.data)
  
class BookCreate(APIView):
  def post(self, request):
    serializer = BookSerializer(data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
  
class BookDetail(APIView):
  def get_book(self, pk):
    try:
       return Book.objects.get(id=pk)
    except Book.DoesNotExist as _:
      raise Http404
    
  def get(self, request, pk):
    book = self.get_book(pk)
    serializer = BookSerializer(book)
    return Response(serializer.data)
  
  def put(self, request, pk):
    book = self.get_book(pk)
    serializer = BookSerializer(book, data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
  
  def delete(self, request, pk):
    book = self.get_book(pk)
    book.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)
  