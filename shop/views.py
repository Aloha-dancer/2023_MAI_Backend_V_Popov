import json

from django.core.handlers.asgi import HttpRequest, HttpResponse, HttpResponseBadRequest
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
from .service import *


@csrf_exempt
@require_http_methods("POST")
def add_new_game(request: HttpRequest) -> HttpResponse:
    if(request.body):
        logging.debug(request)
        return HttpResponse(game_handler(request.method, 2, body= request.body), content_type = "application/json")
    else:
        title = request.GET.get('title')
        req = request.GET.get('req')
        company = request.GET.get('company')
        category = request.GET.get('category')
        descr = request.GET.get('description')
        rel = request.GET.get('release')
        price = request.GET.get('price')
        return HttpResponse(game_handler(request.method, 1, title = title,
                                         description = descr, release = rel, price = price,
                                         req = req, company = company, category = category), content_type="application/json")

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
    id = request.GET.get('id')
    title = request.GET.get('title')
    req = request.GET.get('req')
    company = request.GET.get('company')
    category = request.GET.get('category')
    return HttpResponse(game_handler(request.method, id = id, title = title,
                                     req = req, company = company, category = category), content_type="application/json")

@csrf_exempt
@require_http_methods("GET")
def get_category(request: HttpRequest) -> HttpResponse:
    return JsonResponse({1: "2"})

@csrf_exempt
@require_http_methods("GET")
def get_company(request: HttpRequest) -> HttpResponse:
    return JsonResponse({3: "3"})

@csrf_exempt
@require_http_methods("GET")
def get_sales_statiscs(reques: HttpRequest) -> HttpResponse:
    return JsonResponse({1: "4"})

@csrf_exempt
@require_http_methods("GET")
def get_all_content(reques: HttpRequest) -> HttpResponse:
    return JsonResponse({2: "5"})
