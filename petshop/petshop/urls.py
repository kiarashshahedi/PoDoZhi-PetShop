from django.contrib import admin
from django.urls import path, include
#importing for media
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    
    path('admin/', admin.site.urls),
    # products app
    path('', include('products.urls')),
    # users app
    path('users/', include('users.urls')),

    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
