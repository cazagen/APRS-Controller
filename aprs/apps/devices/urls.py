from django.urls import path

from . import views

urlpatterns = [
    path('create/', views.CreateDevice.as_view(), name='create_device'),
    path('list/', views.ListDevices.as_view(), name='list_devices'),
    path('all-device-statuses/', views.AllDeviceStatus.as_view(), name='all_device_statuses'),
]
