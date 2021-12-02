from django.urls import path, include
from rest_framework import routers
from .views import ArticleViewSet, ViewSerializerViewSet, CommentViewSet, ArticleDetailSerializerView
from django.views.decorators.csrf import csrf_exempt

router = routers.DefaultRouter()


router.register('views', ViewSerializerViewSet)
router.register('comments', CommentViewSet)
router.register('', ArticleViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('article_detail/<uuid:pk>', csrf_exempt(ArticleDetailSerializerView.as_view())), #removing csrf cookie error
]