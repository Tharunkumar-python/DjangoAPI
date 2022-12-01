from django.http import QueryDict
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from api.models import Employee
from rest_framework import mixins
from api.serailizers import EmployeeSerializer
from rest_framework import generics
# Create your views here.

class EmployeeViewSet(viewsets.ModelViewSet):
    serializer_class = EmployeeSerializer
    queryset = Employee.objects.all()
    
    def create(self, request, *args, **kwargs):
        data = request.data
        if isinstance(request.data, QueryDict): # optional
            request.data._mutable = True
        data["total_salary"]  = int(data['salary_hr'])*int(data["working_hrs"])
        ser = EmployeeSerializer(data=data)
        if ser.is_valid(raise_exception=True):
            ser.save()
            return Response(ser.data, status=status.HTTP_201_CREATED)
        return Response(ser.errors, status=status.HTTP_422_UNPROCESSABLE_ENTITY)
    
class EmployeeUpdateDestroyViewSet(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = EmployeeSerializer
    queryset = Employee.objects.all()
