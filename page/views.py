import requests

from django.shortcuts import render


def get_lists(request, **kwargs):
    api = "https://onboarding.art-code.team/"
    services = requests.get(api + "api/test/v1/search/terms")
    brands = requests.get(api + "api/test/v1/search/brands_terms")
    styles = requests.get(api + "api/test/v1/search/styles")
    context = {
        "lists": [
            {"name": "Послуги", "content": services.json()["data"]},
            {"name": "Бренди", "content": brands.json()["data"]},
            {"name": "Стилі", "content": styles.json()["data"]},
        ]
    }
    return render(request, "page/main.html", context)
