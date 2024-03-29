from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.decorators import api_view

from.models import Post
from .serializers import PostSerializer

User = get_user_model()

@api_view(['GET'])
def post_list(request):
    queryset = Post.objects.all()
    serializer = PostSerializer(queryset, many = True)
    return Response(serializer.data, status=200)
    
@api_view(['POST'])
def create_post(request):
    serializer = PostSerializer(data = request.data)
    if serializer.is_valid(raise_exception = True):
        serializer.save()
        return Response('Пост успешно Сасуке', status = 201)
@api_view(['DELETE'])
def delete_post(request, id):
    post = get_object_or_404(Post, id = id)
    post.delete()
    return Response('Пост успешно не Сасуке', status=204)
    