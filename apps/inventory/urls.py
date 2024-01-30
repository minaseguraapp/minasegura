from django.urls import path

from .views import MaintenanceListView

app_name = "inventory"

urlpatterns = [
    path("maintenance/list", MaintenanceListView.as_view(), name="maintenance_list"),
]
