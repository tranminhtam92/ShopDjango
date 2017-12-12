from django.shortcuts import render
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from src.models import Comment,Shop
from .serializers import commentSerializer
from django.core import serializers
from django.db import connection
import json, ast
from collections import OrderedDict
# Create your views here.
class CommentList(APIView):
    def get(self, request):
        comment = Comment.objects.all()
        serializer = commentSerializer(comment, many = True)
        return HttpResponse(serializer.data)

    def post(self, request):

        serializer = commentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



# class ShopDetail(APIView):
#     """
#     Retrieve, update or delete a snippet instance.
#     """
#     def get_object(self, pk):
#         try:
#             return Shop.objects.get(pk=pk)
#         except Shop.DoesNotExist:
#             raise Http404
#
#     def get(self, request, pk, format=None):
#         shop = self.get_object(pk)
#         serializer = shopSerializer(shop)
#         return Response(serializer.data)
#
#     def put(self, request, pk, format=None):
#         shop = self.get_object(pk)
#         serializer = shopSerializer(shop, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     def delete(self, request, pk, format=None):
#         shop = self.get_object(pk)
#         shop.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
#
# def ShopUsingSQL (request):
#
#     cursor = connection.cursor()
#     cursor.execute("SELECT * FROM src_shop inner join src_comment on src_shop.id = src_comment.id_shop")
#     rows = dictfetchall(cursor)
#     # result = ast.literal_eval(json.dumps(rows))
#     return HttpResponse(rows);
#
# def dictfetchall(cursor):
#     columns = [col[0] for col in cursor.description]
#     return [
#         dict(zip(columns, row))
#         for row in cursor.fetchall()
#     ]
