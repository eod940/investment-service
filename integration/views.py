from django.http import HttpResponse
from django.shortcuts import render
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView

from integration.models import Transfer
from integration.serializers import TransferSerializer





class TransferView(APIView):
    queryset = Transfer.objects.all()
    serializer_class = TransferSerializer
    permission_classes = [AllowAny]
