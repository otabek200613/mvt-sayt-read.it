from django.contrib import admin

from .models import Home, Article, About, ContactUs,Contact,SiteSettings,SocialLink,Comment


@admin.register(Home)
class HomeAdmin(admin.ModelAdmin):
    list_display = ['title','is_active']
    list_editable = ['is_active']
@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['title','is_active']
    list_editable = ['is_active']

@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    list_display = ['title','is_active']
    list_editable = ['is_active']

admin.site.register(ContactUs)
@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['name','is_read']
    list_editable = ['is_read']


class SocialLinkInline(admin.StackedInline):
    model = SocialLink
    extra = 0
    max_num = 1

@admin.register(SiteSettings)
class SiteSettingsAdmin(admin.ModelAdmin):
    inlines = [SocialLinkInline]
@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['full_name','article','is_published']
    list_editable = ['is_published']