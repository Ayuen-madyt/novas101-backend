from django.contrib import admin
from .models import Article ,Comment, Views

class ArticleAdmin(admin.ModelAdmin):
    list_display = ("title","category", "author", "date_added")
    search_fields = ('title',)
    list_filter = ('date_added','category',)
    exclude = ('author',)

    #automatically saves the author to currently logged in user
    def save_model(self, request, obj, form, change):
        obj.author = request.user
        super().save_model(request, obj, form, change)
    
    #where a specific user should only view his/own article
    def get_queryset(self, request):
        qs = super(ArticleAdmin, self).get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(author=request.user)

class ViewsAdmin(admin.ModelAdmin):
    list_display=("article","views",)

class CommentAdmin(admin.ModelAdmin):
    list_display=("article","comment","name",)


admin.site.register(Article, ArticleAdmin)
admin.site.register(Comment, CommentAdmin) 
# admin.site.register(Category)
# admin.site.register(SubCategory)
admin.site.register(Views, ViewsAdmin)

admin.site.site_header = "NOVAS 101"
admin.site.site_title = "Admin Panel"
admin.site.index_title = "NOVAS 101"
admin.site.site_url = "/"