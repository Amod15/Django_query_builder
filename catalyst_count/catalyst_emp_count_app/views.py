from django.contrib.auth.decorators import login_required
from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import CompanyInfo
from django.http import JsonResponse
import regex as re
from .forms import CSVUploadForm
from .models import CSVUpload
from django.core.files.storage import default_storage
import os

from django.conf import settings


@login_required
def index(request):
    return render(request, "querybuilder.html")

def query_data(request):
    name = request.POST.get('keyword', '')  # Default to an empty string if 'keyword' is not provided
    industry = request.POST.get('industry', '')
    employees_from = request.POST.get('employees-from-textbox', '')
    employees_to = request.POST.get('employees-to-textbox', '')
    country = request.POST.get('country', '')
    year_founded=request.POST.get('year_founded', '')
    queryset = CompanyInfo.objects.all()

    if employees_from:
        employees_from = int(employees_from)
    if employees_to:
        employees_to = int(employees_to)

    # Applying the filters based on the input
    if name:
        queryset = queryset.filter(name__icontains=name)
    if industry:
        industry=re.sub('_',' ',industry)
        queryset = queryset.filter(industry__icontains=industry)
    if country:
        queryset = queryset.filter(country__icontains=country)
    if year_founded:
        queryset = queryset.filter(year_founded=year_founded)
    if employees_from and employees_to:
        queryset = queryset.filter(
            current_employee_estimate=employees_from,
            total_employee_estimate=employees_to
        )
    elif employees_from:
        queryset = queryset.filter(current_employee_estimate=employees_from)
    elif employees_to:
        queryset = queryset.filter(total_employee_estimate=employees_to)

    # Getting the count of the filtered records
    count = queryset.count()
    return JsonResponse({'count': count})

def upload_file_template(request):
    return render(request, 'uploadfile.html')


def upload_csv(request):
    if request.method == 'POST':
        BASE_DIR= settings.BASE_DIR
        form = CSVUploadForm(request.POST, request.FILES)
        if form.is_valid():
            csv_upload = form.save()

            file = request.FILES['file']
            main_path=os.path.join(BASE_DIR, 'media')
            full_file_path=os.path.join(main_path , file.name)

            csv_upload.file.name = full_file_path

            csv_upload.status = 'Completed'
            csv_upload.user = request.user.username

            csv_upload.save()
            return JsonResponse({'status': 'success', 'csv_upload_id': csv_upload.id})
    return JsonResponse({'status': 'error', 'message': 'Form is not valid'}, status=400)

