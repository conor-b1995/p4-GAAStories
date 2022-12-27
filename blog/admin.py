from django.contrib import admin
from .models import Post, Comment, ContactUs
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):

    prepopulated_fields = {'slug': ('title',)}
    list_filter = ('status', 'created_date')
    list_display = ('title', 'author', 'slug', 'status', 'created_date')
    search_fields = ['title', 'content']
    summernote_fields = ('content')


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):

    list_display = ('name', 'body', 'post', 'created_date', 'approved')
    list_filter = ('approved', 'created_date')
    search_fields = ['name', 'email', 'body']
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(approved=True)


@admin.register(ContactUs)
class ContactAdmin(admin.ModelAdmin):

    list_display = ('name', 'email', 'subject')
    list_filter = ('name', 'subject')
    search_fields = ['name', 'email', 'subject', 'body']
