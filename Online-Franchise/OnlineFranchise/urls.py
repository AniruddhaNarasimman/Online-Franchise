
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from voting import views as voting_views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('homepage.urls')),
    path('register/', include('candidatereg.urls')),
    path('vote/',voting_views.scan,name='voting')
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)