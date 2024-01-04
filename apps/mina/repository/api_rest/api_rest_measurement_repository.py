from django.conf import settings

from apps.mina.repository.measurement_repository import IMeasurementRepository


class ApiRestMeasurementRepository(IMeasurementRepository):
    _api_gateway = settings.API_GATEWAY_URL
    _api_token = settings.API_GATEWAY_TOKEN

    def __init__(self):
        self._measurements = []

    def save(self, measurement):
        self._measurements.append(measurement)

    def find_all(self):
        return self._measurements
