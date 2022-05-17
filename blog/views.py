from django.http import Http404

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .serializers import PostSerializer
from .models import Post

# Create your views here.


class PostList(APIView):
    def get(self, request, format=None):
        """
        Return a list of all posts
        """
        posts = Post.objects.all()
        serializer = PostSerializer(posts, many=True, context={'request': request})
        return Response(serializer.data, status=status.HTTP_200_OK)


class PostDetail(APIView):
    def get_object(self, pk):
        # Returns an object instance that should 
        # be used for detail views.
        try:
            return Post.objects.get(pk=pk)
        except Post.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        """
        Retrieve a post instance
        """
        post = self.get_object(pk)
        serializer = PostSerializer(post, context={'request': request})
        return Response(serializer.data, status=status.HTTP_200_OK)
