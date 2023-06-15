import json

from django.core.handlers.asgi import HttpRequest, HttpResponse, HttpResponseBadRequest
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
from .service import *
from .serializer import *
from rest_framework import generics
from rest_framework.response import Response

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
    if(request.body):
        logging.debug(request)
        return HttpResponse(category_handler(request.method, 2, body= request.body), content_type = "application/json")
    else:
        title = request.GET.get('title')
        descr = request.GET.get('description')
        age = request.GET.get('age')
        return HttpResponse(category_handler(request.method, 1, title = title,
                                         description = descr, age = age), content_type="application/json")

@csrf_exempt
@require_http_methods("POST")
def add_new_company(request: HttpRequest) -> HttpResponse:
    if(request.body):
        logging.debug(request)
        return HttpResponse(company_handler(request.method, 2, body= request.body), content_type = "application/json")
    else:
        name = request.GET.get('name')
        contract = request.GET.get('contract')
        country = request.GET.get('country')
        percent = request.GET.get('percent')
        return HttpResponse(company_handler(request.method, 1, name = name,
                                        contract = contract, percent = percent,
                                        country = country), content_type="application/json")

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
    id = request.GET.get('id')
    title = request.GET.get('title')
    age = request.GET.get('age')
    return HttpResponse(category_handler(request.method, id = id, title = title,
                                         age = age), content_type = 'application/json')

@csrf_exempt
@require_http_methods("GET")
def get_company(request: HttpRequest) -> HttpResponse:
    id = request.GET.get('id')
    name = request.GET.get('name')
    contr = request.GET.get('contract')
    country = request.GET.get('country')
    (permin, permax) = (request.GET.get('min'), request.GET.get('max'))
    return HttpResponse(company_handler(request.method, id = id, name = name,
                                         contract = contr, country = country,
                                         min = permin, max = permax), content_type = 'application/json')


class GameList(generics.ListCreateAPIView):
    queryset = Game.objects.all()
    serializer_class = GameSerializer

class CategoryList(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class CompanyList(generics.ListCreateAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer

class GameDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Game.objects.all()
    serializer_class = GameSerializer

class CategoryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class CompanyDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer





@csrf_exempt
@require_http_methods("GET")
def get_sales_statiscs(reques: HttpRequest) -> HttpResponse:
    return JsonResponse({1: "4"})
