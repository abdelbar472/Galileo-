from rest_framework import serializers
from .models import *
class BlogPostSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(format='hex_verbose', read_only=True)
    class Meta:
        model = BlogPost
        fields = '__all__'
        def create(self):
            return BlogPost.title