from rest_framework import serializers
from .models import *
class BlogPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogPost
        fields = '__all__'
        def create(self):
            return BlogPost.title