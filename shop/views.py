import json

from django.core.handlers.asgi import HttpRequest, HttpResponse, HttpResponseBadRequest
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt



@csrf_exempt
@require_http_methods("POST")
def add_new_game(request: HttpRequest) -> HttpResponse:
    return JsonResponse({"Good" : "Yep"})

@csrf_exempt
@require_http_methods("POST")
def add_new_category(request: HttpRequest) -> HttpResponse:
    return JsonResponse({"Good": "Semy"})

@csrf_exempt
@require_http_methods("POST")
def add_new_company(request: HttpRequest) -> HttpResponse:
    return JsonResponse({"New": "Response"})

@csrf_exempt
@require_http_methods("GET")
def get_game(request: HttpRequest) -> HttpResponse:
    return JsonResponse("1")

@csrf_exempt
@require_http_methods("GET")
def get_category(request: HttpRequest) -> HttpResponse:
    return JsonResponse("2")

@csrf_exempt
@require_http_methods("GET")
def get_company(request: HttpRequest) -> HttpResponse:
    return JsonResponse("3")