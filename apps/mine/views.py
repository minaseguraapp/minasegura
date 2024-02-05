import datetime

from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.views import View

from apps.mine.choices import MeasurementSiteChoice
from apps.mine.models import Zone
from apps.mine.repository.api_rest.api_rest_measurement_repository import ApiRestMeasurementRepository

MEASUREMENT_TYPE = {
    "gas": "METHANE",
    "coal": "COAL_DUST"
}


def parse_data_methane(post_data):
    zone = Zone.objects.get(id=post_data.get("zone"))
    present_date = datetime.datetime.now()
    timestamp = datetime.datetime.timestamp(present_date)
    data = {
        "timestamp": timestamp,
        "measurementType": "METHANE",
        "zone": {
            "id": zone.id,
            "type": zone.zone_type.name,
            "mine": {
                "id": post_data.get("mine"),
            }
        },
        "measurementInfo": {
            "measurementSite": post_data.get("measurement_site"),
            "methaneLevel": post_data.get("methane_level"),
        }
    }
    return data


def parse_data_coal_dust(request):
    data = {}
    return data


class Measurement(LoginRequiredMixin, View):
    repository = ApiRestMeasurementRepository()
    measurement_site_choice = MeasurementSiteChoice.choices

    def get(self, request, mine: int, type_name: str, *args, **kwargs):
        measurement_list = self.repository.find_by_mine(mine,
                                                        MEASUREMENT_TYPE.get(type_name), **kwargs)
        return render(
            request,
            self.get_template(type_name),
            {
                "type_name": type_name,
                "measurement_site_choice": self.measurement_site_choice,
                "measurement_list": measurement_list,
            },
        )

    def post(self, request, mine: int, type_name: str, *args, **kwargs):
        data = request.POST.copy()
        data["mine"] = mine
        save_result = False
        if type_name == "gas":
            measurement_data = parse_data_methane(data)
            save_result = self.repository.save(measurement_data)
        if type_name == "coal":
            measurement_data = parse_data_coal_dust(data)
            save_result = self.repository.save(measurement_data)

        if save_result:
            messages.success(request, "Medición guardada correctamente")
        else:
            messages.error(request, "Error al guardar la medición")
        return redirect('mine:measurement', mine=mine, type_name=type_name)

    @staticmethod
    def get_template(type_name: str):
        return f"mine/{type_name}/measurement.html"


class Alerts(LoginRequiredMixin, View):

    def get(self, request, mine: int, type_name: str):
        template_name = self.get_template(type_name)
        return render(
            request,
            template_name,
            {
                "type_name": type_name,
            },
        )

    @staticmethod
    def get_template(type_name: str):
        return f"mine/{type_name}/alerts.html"


class Settings(LoginRequiredMixin, View):

    def get(self, mine: int, request, type_name: str):
        template_name = self.get_template(type_name)
        return render(
            request,
            template_name,
            {
                "type_name": type_name,
            },
        )

    @staticmethod
    def get_template(type_name: str):
        return f"mine/{type_name}/settings.html"


def zone_select(request, mine: int):
    if request.method == 'GET':
        query = request.GET.get('q')
        if query:
            list_zone = Zone.objects.filter(Q(name__icontains=query) | Q(code__icontains=query)).values('id',
                                                                                                        'name')
            return JsonResponse({"zones": list(list_zone)})
    return JsonResponse({"zones": []})
