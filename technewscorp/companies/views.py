from django.core.mail import send_mail
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination
from rest_framework.decorators import api_view
from .serializers import CompanySerializer
from .models import Company

# Create your views here.


class CompanyViewSet(ModelViewSet):
    serializer_class = CompanySerializer
    queryset = Company.objects.all().order_by("-last_update")
    pagination_class = PageNumberPagination


@api_view(http_method_names=['POST'])
def send_company_email(request):
    """
    
        sends email with request payload
        sender: someone@email.com
        receiver: othersomeone@email.com


    """

    send_mail (
        'Subject here', 'Here is the message.',
        'carlos.grh@outlook.com', ['carlos.grh@outlook.com'],
        fail_silently=False
    )    

    return Response({"status": "success", "info": "email sent successfully"}, status=200)