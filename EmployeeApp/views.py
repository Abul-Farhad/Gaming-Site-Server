# from django.shortcuts import render
# from django.views.decorators.csrf import csrf_exempt
# from rest_framework.parsers import JSONParser
# from django.http.response import JsonResponse
# from EmployeeApp.models import Departments, Employees
# from EmployeeApp.serializers import DepartmentSerializer, EmployeeSerializer

# # Create your views here.
# @csrf_exempt
# def departmentApi(request, id = 0):
#     if request.method == 'GET':
#         departments = Departments.objects.all()
#         departments_serializer = DepartmentSerializer(departments, many = True)  
#         return JsonResponse(departments_serializer.data, safe=False)
#     elif request.method == 'POST':
#         department_data = JSONParser().parse(request)
#         departments_serializer = DepartmentSerializer(data=department_data)
#         if departments_serializer.is_valid():
#             departments_serializer.save()
#             return JsonResponse('Added Successfully', safe=False)
#         return JsonResponse('Failed to Add', safe=False) 
#     elif request.method == 'PUT':
#         department_data = JSONParser().parse(request)
#         department = Departments.objects.get(DepartmentId = department_data['DepartmentId']) 
#         departments_serializer = DepartmentSerializer(department, data=department_data) 
#         if departments_serializer.is_valid():
#             departments_serializer.save()      
#             return JsonResponse('Updated Successfully', safe=False)
#         return JsonResponse('Failed to Update', safe=False) 
    
#     elif request.method == 'DELETE':
#         department = Departments.objects.get(DepartmentId = id)
#         department.delete()
#         return JsonResponse('Deleted Successfully', safe = False)
    
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse, HttpResponse

from EmployeeApp.models import Departments,Employees
from EmployeeApp.serializers import DepartmentSerializer,EmployeeSerializer

from django.core.files.storage import default_storage

# Create your views here.

@csrf_exempt
def departmentApi(request,id=0):
    if request.method=='GET':
        departments = Departments.objects.all()
        departments_serializer=DepartmentSerializer(departments,many=True)
        return JsonResponse(departments_serializer.data,safe=False)
    
    elif request.method=='POST':
        print("Post method called")
        department_data=JSONParser().parse(request)
        departments_serializer=DepartmentSerializer(data=department_data)
        if departments_serializer.is_valid():
            departments_serializer.save()
            return JsonResponse("Added Successfully",safe=False)
        return JsonResponse("Failed to Add",safe=False)
    
    elif request.method=='PUT':
        department_data=JSONParser().parse(request)
        department=Departments.objects.get(DepartmentId=department_data['DepartmentId'])
        departments_serializer=DepartmentSerializer(department,data=department_data)
        if departments_serializer.is_valid():
            departments_serializer.save()
            return JsonResponse("Updated Successfully",safe=False)
        return JsonResponse("Failed to Update")
    
    elif request.method=='DELETE':
        department=Departments.objects.get(DepartmentId=id)
        department.delete()
        return JsonResponse("Deleted Successfully",safe=False)
    
def Home(request):
    return HttpResponse("Server is running at port 8000")