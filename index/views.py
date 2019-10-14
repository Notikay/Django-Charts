from django.http import JsonResponse
from django.shortcuts import render
from .models import DataChart

db_chart = DataChart.objects.all()

def index(request):
	db_labels = []
	db_data = []
	for i in db_chart:
		db_labels.append(i.col1)
		db_data.append(i.col2)
	return render(request, 'index/index.html', {"db_chart": db_chart, "db_labels": db_labels, "db_data": db_data})