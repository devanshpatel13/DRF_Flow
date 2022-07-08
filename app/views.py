from django.shortcuts import render
from rest_framework.response import Response

from .models import *
from .serializers import *
from rest_framework.generics import ListCreateAPIView, RetrieveAPIView

# Create your views here.


class HomeView(ListCreateAPIView):
    queryset = Home.objects.all()
    serializer_class = HomeSerizers

    def list(self, request , *args,**kwargs):
        # Note the use of `get_queryset()` instead of `self.queryset`
        queryset = self.get_queryset()
        serializer = HomeSerizers(queryset, many=True)
        return Response(serializer.data)
    #
    def post(self, request, *args, **kwargs):
        # print(request,"ddddddddddddddddd")
        serializer = self.serializer_class(data=request.data)
        # print(serializer,"lllllllllllllllll/////////////////////////////")
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.data)

    # def create(self, request, *args, **kwargs):
    #     serializer = self.get_serializer(data=request.data)
    #     serializer.is_valid(raise_exception=True)
    #     self.perform_create(serializer)
    #     headers = self.get_success_headers(serializer.data)
    #     return Response(serializer.data)
