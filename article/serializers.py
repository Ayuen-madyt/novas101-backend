from rest_framework import serializers
from .models import Article, Views, Comment  #i need to import category here
# from django.utils.html import strip_tags

class ViewsSerializer(serializers.ModelSerializer):
    class Meta:
        model =  Views
        fields = ['views', 'article']

# class ArticleDetailSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Article
#         fields = '_all_'


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model =  Comment
        fields = '__all__'

# class CategorySerializer(serializers.ModelSerializer):
#     class Meta:
#         model =  Category
#         fields = ['categoryName']

class ArticleSerializer(serializers.ModelSerializer):
    views = ViewsSerializer(many=True, read_only=True)
    comments = CommentSerializer(many=True, read_only=True)
    # category = serializers.SlugRelatedField(read_only=True, slug_field='categoryName')
    author = serializers.SlugRelatedField(read_only=True, slug_field='username')
    class Meta:
        model = Article
        fields = ['id', 'author', 'title', 'category', 'image','trending', 'featured', 'body', 'time_added', 'views', 'comments']
    
  