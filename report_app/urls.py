from django.urls import path
from .views import ReportView, report_detail


app_name = 'report-app'
urlpatterns = [
    path('reports/', ReportView.as_view(), name='report-detail'),
    path('reports/<int:pk>/', report_detail, name='report-detail'),
]