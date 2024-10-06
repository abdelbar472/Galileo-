from django.shortcuts import render
from django.http import JsonResponse
from rest_framework import status, generics,request
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import BlogPost
from .serializers import  *
# Create your views here.

class BlogPostListCreate(generics.ListCreateAPIView):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer

