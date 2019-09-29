from django.urls import path, include

urlpatterns = [
    path('accounts/', include('django.contrib.auth.urls')),
    path('', include('apps.frontend.urls')),
    path('devices/', include('apps.devices.urls')),
]
