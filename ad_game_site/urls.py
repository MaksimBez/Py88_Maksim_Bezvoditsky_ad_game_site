from django.contrib import admin
from django.urls import include, path
from django.conf.urls.static import static
from django.conf import settings
from django.views.generic import TemplateView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
    path('registration/', include('registration.urls')),
    path('', include('authentication.urls')),
] + static(settings.STATIC_URL)

urlpatterns.extend(
    static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
)
