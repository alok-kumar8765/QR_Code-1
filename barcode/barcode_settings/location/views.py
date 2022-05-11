import imp
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import GenericAPIView, ListCreateAPIView
from .serializers import locationserializer
# import requests
import json
# Create your views here.
class locations(APIView):
    def get(self,request,pk):
        loca=request.data['pk']
        ENDPoints = 'https://api.postalpincode.in/loca/'

        # pincode = input('Enter Your Pin Code :')
        response = request.get(ENDPoints+loca)

        # pincode_info = json.loads(response.text)
        # print(pincode_info)
        return Response(response,status=200)