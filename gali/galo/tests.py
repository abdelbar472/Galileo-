from django.test import TestCase
from .models import BlogPost
from .serializers import BlogPostSerializer

# Create a sample blog post
post = BlogPost(title='Test Post', content='Test content')
post.save()

# Serialize the blog post
serializer = BlogPostSerializer(post)
print(serializer.data)
