from django.contrib import admin
from .models import Category, Tag, Post, About, Link

# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    list_display = ('name', 'active', 'created')

admin.site.register(Category, CategoryAdmin)

class TagAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    list_display = ('name', 'active', 'created')

admin.site.register(Tag, TagAdmin)

class PostAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    list_display = ('title', 'category', 'published', 'author', 'created','post_tags')
    ordering = ('author', '-created')
    search_fields = ('title', 'content', 'author__username','category__name')
    list_filter = ('author', 'category', 'tags')

    def post_tags(self,obj):
        return ' - '.join([t.name for t in obj.tags.all().order_by('name')])

    post_tags.short_description = 'etiquetas'

admin.site.register(Post,PostAdmin)

class AboutAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    list_display = ('description', 'created')

admin.site.register(About, AboutAdmin)

class LinkAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    list_display = ('name', 'key', 'url', 'icon')

admin.site.register(Link, LinkAdmin)