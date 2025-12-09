from django.shortcuts import render
from .models import Beverage, Brand
from .serializers import BeverageSerializer, SimpleBeverageSerializer, BeverageWithRelationshipsSerializer, BrandSerializer, BrandWithBevsSerializer
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework.pagination import LimitOffsetPagination

# BEVERAGE VIEWS

@csrf_exempt
def beverages_list(request):
    # GET /beverages
    if request.method == "GET":
        # request.GET.get is how we get a specific query parameter (in this case /beverages?name=whatever)
        query_name = request.GET.get('name')
        query_order_by = request.GET.get('order_by')
        # all_bevs is technically a thing called a QuerySet
        all_bevs = Beverage.objects.all()
        # if we have a query_name then filter with it
        if query_name:
            all_bevs = all_bevs.filter(name__icontains=query_name)
        if query_order_by:
            all_bevs = all_bevs.order_by(query_order_by)
        # serializer will convert the objects into JSON data
        serialized_bevs = BeverageSerializer(all_bevs, many=True)
        return JsonResponse(serialized_bevs.data, status=200, safe=False)
    
        # ------- PAGINATION -------- #
        # If you want to instead apply pagination
        # paginator = LimitOffsetPagination()
        # # By default show 3 items per page
        # paginator.default_limit = 3  
        # # Don't let users request more than 10
        # paginator.max_limit = 10     

        # # use the paginator with the queryset (all_bevs)
        # paginated_bevs = paginator.paginate_queryset(all_bevs, request)
        
        # serialized_bevs = SimpleBeverageSerializer(paginated_bevs, many=True)
        # return paginator.get_paginated_response(serialized_bevs.data)
    
    # POST /beverages
    elif request.method == "POST":
        # parse the json into python
        bev_data = JSONParser().parse(request)
        # feed data into serializer
        serializer = BeverageSerializer(data=bev_data)
        # check if its valid
        if serializer.is_valid():
            # commit to db and return the new object
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        else:
            # return the errors from the validations
            return JsonResponse(serializer.errors, status=400)
    
@csrf_exempt
def beverage_detail(request, pk):
    # always try to find the beverage with the proper primary key
    try:
        found_bev = Beverage.objects.get(pk=pk)
    except Beverage.DoesNotExist:
        return JsonResponse( {"error_message": f"Could not find a beverage with id of {pk}"}, status=404 )

    # GET /beverages/<int:pk>
    if request.method == "GET":
        serialized_bev = BeverageWithRelationshipsSerializer(found_bev)
        return JsonResponse(serialized_bev.data, status=200)
    
    # PATCH / PUT /beverages/<int:pk>
    elif request.method == "PATCH" or request.method == "PUT":
        bev_data = JSONParser().parse(request)
        serializer = BeverageSerializer(found_bev, data=bev_data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=202)
        else:
            return JsonResponse(serializer.errors, status=400)
        
    # DELETE /beverages/<int:pk>
    elif request.method == "DELETE":
        # delete the found beverage
        found_bev.delete()
        # return an empty response
        return JsonResponse({}, status=204)
    

# BRAND VIEWS

@csrf_exempt
def brand_list(request):
    # GET
    if request.method == "GET":
        all_brands = Brand.objects.all()
        serialized_brands = BrandSerializer(all_brands, many=True)
        return JsonResponse(serialized_brands.data, status=200, safe=False)
    

@csrf_exempt
def brand_detail(request, pk):
    try:
        found_brand = Brand.objects.get(pk=pk)
    except Brand.DoesNotExist:
        return JsonResponse({ "error_message": "That's not a brand" })
    
    if request.method == "GET":
        # found_brand --> this is a model instance aka an object
        # we have not turned found_brand into a dictionary that we can send as json yet...
        serializer = BrandWithBevsSerializer(found_brand)
        # BrandSerializer helps transform this into a dictionary which is easy to convert into JSON
        return JsonResponse(serializer.data, status=200)