
from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from employee_register import views 
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('service.urls')),
    path('employee/', include('employee_register.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)