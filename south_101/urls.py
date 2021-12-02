from django.conf import settings
from django.conf.urls.static import static 
from django.contrib import admin
from dj_rest_auth.views import PasswordResetView, PasswordResetConfirmView
from django.urls import path, include, re_path
from django.views.generic import TemplateView

urlpatterns = [
    path('novas101-admin/', admin.site.urls),
    path('articles/', include('article.urls')),
    path('api-auth/', include('rest_framework.urls')),
    path('users/', include('user.urls')),
    re_path(r'^password/reset/confirm/<uidb64>/<token>/',PasswordResetConfirmView.as_view(), name='password_reset_confirm'),  
    path('accounts/', include('allauth.urls')),
    path('user/accounts/', include('email_signup.urls')),
      # path('user/accounts/registration/', include('dj_rest_auth.registration.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 

# where i include templates from  react build folder
urlpatterns += [
    re_path(r'^.*', TemplateView.as_view(template_name='index.html')),
    
    # password reset confirm url
    #  re_path(r'^password/reset/confirm/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
    #     PasswordResetConfirmView.as_view(),
    #     name='password_reset_confirm'),
    ]