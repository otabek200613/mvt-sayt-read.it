from django.db import models

class Home(models.Model):
    bg_photo = models.ImageField(upload_to='images/')
    title = models.CharField(max_length=100)
    body = models.TextField()
    twitter = models.URLField()
    facebook = models.URLField()
    instagram = models.URLField()
    address = models.TextField()
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    is_active = models.BooleanField()
    def __str__(self):
        return self.title






class Article(models.Model):

    photo = models.ImageField(upload_to='articles/')
    category = models.CharField(max_length=20)
    title = models.CharField(max_length=100)
    body = models.TextField()
    twitter = models.URLField()
    facebook = models.URLField()
    instagram = models.URLField()
    created_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField()
    def __str__(self):
        return self.title

class About(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField()
    photo = models.ImageField(upload_to='about/')
    video = models.URLField(null=True, blank=True)
    mission = models.TextField(null=True,blank=True)
    vision = models.TextField(null=True,blank=True)
    value = models.TextField(null=True,blank=True)
    is_active = models.BooleanField()
    def __str__(self):
        return self.title

class ContactUs(models.Model):
    address = models.TextField()
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    website = models.URLField()
    is_active = models.BooleanField(default=True)



class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=100)
    message = models.TextField()
    is_read = models.BooleanField(default=False)
    def __str__(self):
        return self.name



# home/models.py
from django.db import models

class SiteSettings(models.Model):
    site_name = models.CharField(max_length=120, default="Readit.")
    logo_text = models.CharField(max_length=120, default="Readit.")

    footer_about = models.TextField(blank=True, default="")

    address = models.CharField(max_length=255, blank=True, default="")
    phone = models.CharField(max_length=50, blank=True, default="")
    email = models.EmailField(blank=True, default="")

    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.site_name


class SocialLink(models.Model):
    settings = models.OneToOneField(
        SiteSettings,
        on_delete=models.CASCADE,
        related_name="social"
    )
    twitter = models.URLField(blank=True, default="")
    facebook = models.URLField(blank=True, default="")
    instagram = models.URLField(blank=True, default="")

    def __str__(self):
        return f"Social links for {self.settings.site_name}"
class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='comments')
    full_name = models.CharField(max_length=50, verbose_name="Full name")
    email = models.EmailField(verbose_name="Email")
    message = models.TextField(verbose_name="Message")
    created = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(verbose_name="Is published?", default=False)

    def __str__(self):
        return f"{self.full_name} - {self.article}"






















































