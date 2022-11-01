from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CompanyViewSet

companies_router = DefaultRouter()
companies_router.register("companies", viewset=CompanyViewSet, basename="companies")
