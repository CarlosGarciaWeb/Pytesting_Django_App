from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .serializers import CompanySerializer
from rest_framework.pagination import PageNumberPagination
from .models import Company

# Create your views here.


class CompanyViewSet(ModelViewSet):
    serializer_class = CompanySerializer
    queryset = Company.objects.all().order_by("-last_update")
    pagination_class = PageNumberPagination
