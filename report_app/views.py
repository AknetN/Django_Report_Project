from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view 
from .models import Report
from .serializers import ReportSerializer


# Create your views here.
class ReportView(APIView):
    def get(self, request):
        reports = Report.objects.all()
        serializer = ReportSerializer(reports, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = ReportSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


@api_view(['GET', 'PUT', 'DELETE'])
def report_detail(request, pk):
    try:
        report = Report.objects.get(id=pk)
    except Report.DoesNotExist:
        return Response(status=400)
    
    if request.method == 'GET':
        serializer = ReportSerializer(report)
        return Response(serializer.data, status=200)
    
    elif request.method == 'PUT':
        serializer = ReportSerializer(report, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)
    
    elif request.method == 'DELETE':
        report.delete()
        return Response(status=204)