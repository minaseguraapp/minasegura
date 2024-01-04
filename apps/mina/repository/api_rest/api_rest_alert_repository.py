from django.conf import settings

from apps.mina.repository.alert_repository import IAlertRepository


class ApiRestAlertRepository(IAlertRepository):
    _api_gateway = settings.API_GATEWAY_URL
    _api_token = settings.API_GATEWAY_TOKEN

    def __init__(self):
        self._alerts = []

    def save(self, alert):
        self._alerts.append(alert)

    def find_all(self):
        return self._alerts
