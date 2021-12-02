from rest_framework import viewsets
from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .serializers import ArticleSerializer, ViewsSerializer, CommentSerializer
from .models import Article, Comment, Views
from django.db.models import F

# Create your views here.
class ArticleViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticatedOrReadOnly,)
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    
    # automatically saves the author to currently logged in user
    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

# article detail
class ArticleDetailSerializerView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

class ViewSerializerViewSet(viewsets.ModelViewSet):
    queryset = Views.objects.all()
    serializer_class = ViewsSerializer

    def perform_create(self, serializer):
        id = self.request.data['article']
        view = self.request.data['views']
        article = Views.objects.filter(article=id)
        if article.exists():
            article = Views.objects.filter(article=id).update(views= F('views') + view)
        else:
            serializer.save()
        print(id)
        print(article)

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer