from django.contrib.auth import views as auth_views
from user import views 
from django.conf import settings
from django.contrib.staticfiles.urls import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('atendimento/', include('atendimento.urls')),
    path('produto/', include('produto.urls')),
    path('sacola/', include('sacola.urls')),
    path('relatorio/', include('relatorio.urls')),
    path('user/', include('django.contrib.auth.urls')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
