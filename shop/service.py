from .models import *
from .serializer import GameSerializer, CompanySerializer, CategorySerializer, SalesSerializer, renderers, parsers

import logging
import io
import json
from typing import Any


from django.core.handlers.asgi import HttpRequest, HttpResponse, HttpResponseBadRequest
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
from django.core.exceptions import FieldError, FieldDoesNotExist, ObjectDoesNotExist

def game_handler(method: str, way: int = 1,
                 **kwargs: dict[Any, Any]):
    query_result = Game.objects.all()
    if method == "GET":
        if not len(kwargs):
            return query_result
        else:
            try:
                for (i, j) in kwargs.items():
                    if j is not None:
                        if i == 'title':
                            query_result = query_result.filter(title__contains = j)
                            continue
                        if i == 'req':
                            query_result = query_result.filter(sysreq__contains = j)
                            continue
                        if i == 'category':
                            query_result = query_result.filter(category__extract = j)
                            continue
                        if i == 'company':
                            query_result = query_result.filter(company__extract = j)
                            continue
            except (FieldError, FieldDoesNotExist, 
                    ValueError, ObjectDoesNotExist ) as err:
                raise err
        json = renderers.JSONRenderer().render(GameSerializer(query_result, many = True).data)
        return json
    elif method == "POST":
        logging.debug('I am here')
        if way == 1:
            try:
#                logging.debug(f'way=={way}')
#                logging.debug(f'descr == {kwargs.keys()}')
                obj = Game(title = kwargs['title'],
                           sysreq = kwargs['req'], description = kwargs['description'],
                           price = kwargs['price'], date_release = kwargs['release'])
                obj.category = Category.objects.get(uuid = kwargs['category'])
                obj.company = Company.objects.get(uuid = kwargs['company'])
            except (FieldError, FieldDoesNotExist, 
                    ValueError, ObjectDoesNotExist ) as err:
                raise err
            obj.save()
            return
        elif way == 2:
            logging.debug(f'way=={way}')
            stream = io.BytesIO(kwargs['body'])
            data = parsers.JSONParser().parse(stream)
            serializer = GameSerializer(data = data)
            if not serializer.is_valid():
                logging.debug(serializer.errors)
            if serializer.is_valid():
                logging.debug(serializer.validated_data)
                serializer.save()
            return



# to_do: replace relevant fields
def company_handler(method: str, way: int = 1,
                 **kwargs: dict[Any, Any]):
    query_result = Company.objects.all()
    if method == "GET":
        if not len(kwargs):
            return query_result
        else:
            try:
                for (i, j) in kwargs.items():
                    if j is not None:
                        if i == 'title':
                            query_result = query_result.filter(title__contains = j)
                            continue
                        if i == 'req':
                            query_result = query_result.filter(sysreq__contains = j)
                            continue
                        if i == 'category':
                            query_result = query_result.filter(category__extract = j)
                            continue
                        if i == 'company':
                            query_result = query_result.filter(company__extract = j)
                            continue
            except (FieldError, FieldDoesNotExist, 
                    ValueError, ObjectDoesNotExist ) as err:
                raise err
        json = renderers.JSONRenderer().render(GameSerializer(query_result, many = True).data)
        return json
    elif method == "POST":
        logging.debug('I am here')
        if way == 1:
            try:
#                logging.debug(f'way=={way}')
#                logging.debug(f'descr == {kwargs.keys()}')
                obj = Game(title = kwargs['title'],
                           sysreq = kwargs['req'], description = kwargs['description'],
                           price = kwargs['price'], date_release = kwargs['release'])
                obj.category = Category.objects.get(uuid = kwargs['category'])
                obj.company = Company.objects.get(uuid = kwargs['company'])
            except (FieldError, FieldDoesNotExist, 
                    ValueError, ObjectDoesNotExist ) as err:
                raise err
            obj.save()
            return
        elif way == 2:
            logging.debug(f'way=={way}')
            stream = io.BytesIO(kwargs['body'])
            data = parsers.JSONParser().parse(stream)
            serializer = GameSerializer(data = data)
            if not serializer.is_valid():
                logging.debug(serializer.errors)
            if serializer.is_valid():
                logging.debug(serializer.validated_data)
                serializer.save()
            return

# to_do: replace relevant fields
def category_handler(method: str, way: int = 1,
                 **kwargs: dict[Any, Any]):
    query_result = Category.objects.all()
    if method == "GET":
        if not len(kwargs):
            return query_result
        else:
            try:
                for (i, j) in kwargs.items():
                    if j is not None:
                        if i == 'title':
                            query_result = query_result.filter(title__contains = j)
                            continue
                        if i == 'req':
                            query_result = query_result.filter(sysreq__contains = j)
                            continue
                        if i == 'category':
                            query_result = query_result.filter(category__extract = j)
                            continue
                        if i == 'company':
                            query_result = query_result.filter(company__extract = j)
                            continue
            except (FieldError, FieldDoesNotExist, 
                    ValueError, ObjectDoesNotExist ) as err:
                raise err
        json = renderers.JSONRenderer().render(GameSerializer(query_result, many = True).data)
        return json
    elif method == "POST":
        logging.debug('I am here')
        if way == 1:
            try:
#                logging.debug(f'way=={way}')
#                logging.debug(f'descr == {kwargs.keys()}')
                obj = Game(title = kwargs['title'],
                           sysreq = kwargs['req'], description = kwargs['description'],
                           price = kwargs['price'], date_release = kwargs['release'])
                obj.category = Category.objects.get(uuid = kwargs['category'])
                obj.company = Company.objects.get(uuid = kwargs['company'])
            except (FieldError, FieldDoesNotExist, 
                    ValueError, ObjectDoesNotExist ) as err:
                raise err
            obj.save()
            return
        elif way == 2:
            logging.debug(f'way=={way}')
            stream = io.BytesIO(kwargs['body'])
            data = parsers.JSONParser().parse(stream)
            serializer = GameSerializer(data = data)
            if not serializer.is_valid():
                logging.debug(serializer.errors)
            if serializer.is_valid():
                logging.debug(serializer.validated_data)
                serializer.save()
            return

# to_do: create_sales_handler
def sales_handle():
    pass

def util_handler():
    pass