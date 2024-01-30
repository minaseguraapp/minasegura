from django.urls import path

from apps.mine.views import Measurement, Alerts, Settings

app_name = "mine"

urlpatterns = [
    path("measurement/<str:type_name>", Measurement.as_view(), name="measurement"),
    path("alerts/<str:type_name>", Alerts.as_view(), name="alerts"),
    path("settings/<str:type_name>", Settings.as_view(), name="settings"),
]
