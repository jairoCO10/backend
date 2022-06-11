
# backend/urls.py

from django.contrib import admin
from django.conf import settings
from django.urls import path, include                 # add this
from rest_framework import routers                    # add this
from empresa import views        
from django.conf.urls.static import static                    # add this
        
router = routers.DefaultRouter()                      # add this
router.register(r'datos-empresas', views.empresaView, 'datos-empresas')     # add this
        
urlpatterns = [
    path('admin/', admin.site.urls),           
    path('api/', include(router.urls))                # add this
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)