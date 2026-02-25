# from django.shortcuts import render
# from rest_framework.decorators import api_view
# from rest_framework.response import Response

# # @api_view(['GET'])
# # def hello_world(request):
# #     return Response({'msg':'Hello World'})

# @api_view(['POST','GET'])
# def hello_world(request):
#     if request.method == 'GET':
#      return Response({'msg':'This is post method '})

#     if request.method =='POST':
#        print(request.data)
#        return Response({'msg': 'This is POST Request'})


from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Student
from .serializers import StudentSerializer


@api_view(["GET", "POST", "PUT", "DELETE"])
def student_api(request):
    if request.method == "GET":
        id = request.data.get("id")
        if id is not None:
            stu = Student.objects.get(id=id)
            serializer = StudentSerializer(stu)
            return Response(serializer.data)

        stu = Student.objects.all()
        serializer = StudentSerializer(stu, many=True)
        return Response(serializer.data)

    if request.method == "POST":
        roll = request.data.get("roll")
        if Student.objects.filter(roll=roll).exists():
            return Response({"error": "Data already exists"})
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"msg": "Data Created Successfully"})
        return Response(serializer.errors)

    if request.method == "PUT":
        id = request.data.get("id")
        stu = Student.objects.get(pk=id)
        serializer = StudentSerializer(stu, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"msg": "Data update successfully"})
        return Response(serializer.errors)

    if request.method == "DELETE":
        id = request.data.get('id')
        stu = Student.objects.get(pk=id)
        stu.delete()
        return Response({"msg": "Data Deleted"})
