from django.contrib import admin
from django.urls import path, include

# media
from django.conf import settings
from django.conf.urls.static import static

import page.views
import lost_property.views
import board.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', page.views.home, name="home"),
    path('', include('page.urls')),
    path('lost', include('lost_property.urls')),
    path('board', include('board.urls')),

]  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)