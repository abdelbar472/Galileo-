from django.shortcuts import render
from django.http import JsonResponse
from rest_framework import status, generics,request
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import BlogPost
from .serializers import  *
# Create your views here.

class BlogPostListCreate(generics.ListCreateAPIView):
    serializer_class = BlogPostSerializer

    def get_queryset(self):
        # Fetch all blog posts using Cassandra's querying system
        # Cassandra may not support .all() in the same way as Django ORM.
        return BlogPost.objects.all()

    def get(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


