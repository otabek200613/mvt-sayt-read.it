from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import home, about, blog, blogsingle, contact

urlpatterns = [
    path('', home, name='home'),
    path('about/', about, name='about'),
    path('blog/', blog, name='blog'),
    path('blogsingle/<int:pk>', blogsingle, name='blogsingle'),
    path('contact/', contact, name='contact'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
