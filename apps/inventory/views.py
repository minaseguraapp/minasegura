from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView

from apps.inventory.forms import MaintenanceForm
from apps.inventory.models import Maintenance


class MaintenanceListView(LoginRequiredMixin, ListView):
    template_name = "maintenance/list.html"
    model = Maintenance
    form = MaintenanceForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = self.form
        return context

    def post(self, request, *args, **kwargs):
        form = self.form(request.POST)
        if form.is_valid():
            form.save()
        return super().get(request, *args, **kwargs)
