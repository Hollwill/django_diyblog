from django.contrib import admin
from .views import Blog, Blogger, Comment


class CommentInline(admin.TabularInline):
    model = Comment


class BlogAdmin(admin.ModelAdmin):
    inlines = [
        CommentInline,
    ]


admin.site.register(Blog, BlogAdmin)
admin.site.register(Blogger)
