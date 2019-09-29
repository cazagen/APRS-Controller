from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView

from apps.frontend.views import Dashboard

from .models import Device

class CreateDevice(LoginRequiredMixin, CreateView):
    model = Device
    fields = [
        'name',
        'owner',
    ]
    
    def get_success_url(self):
        return reverse('dashboard')


class ListDevices(LoginRequiredMixin, ListView):
    model = Device


class AllDeviceStatus(LoginRequiredMixin, ListView):
    model = Device
    template_name = 'devices/devices_online.html'

    def get_context_data(self):
        context = super(AllDeviceStatus, self).get_context_data()

        context['active_objects'] = context['object_list'].filter(status='active')
        return context