from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views import View


class Measurement(LoginRequiredMixin, View):

    def get(self, request, type_name: str):
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
        return f"mina/{type_name}/measurement.html"


class Alerts(LoginRequiredMixin, View):

    def get(self, request, type_name: str):
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
        return f"mina/{type_name}/alerts.html"


class Settings(LoginRequiredMixin, View):

    def get(self, request, type_name: str):
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
        return f"mina/{type_name}/settings.html"
