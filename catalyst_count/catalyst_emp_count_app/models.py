from django.db import models

# Create your models here.
class CompanyInfo(models.Model):
    name = models.CharField(max_length=500, blank=True, null=True)
    domain = models.CharField(max_length=255, blank=True, null=True)
    year_founded = models.CharField(max_length=10, blank=True, null=True)  # Adjusted length for year
    industry = models.CharField(max_length=255, blank=True, null=True)
    size_range = models.CharField(max_length=100, blank=True, null=True)
    locality = models.CharField(max_length=255, blank=True, null=True)
    country = models.CharField(max_length=255, blank=True, null=True)
    linkedin_url = models.CharField(max_length=200, blank=True, null=True)
    current_employee_estimate = models.IntegerField(blank=True, null=True)
    total_employee_estimate = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.name

class CSVUpload(models.Model):
    file = models.FileField(upload_to='uploads/')
    upload_time = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, default='Pending')  # e.g., Pending, Processing, Completed
    result = models.TextField(blank=True, null=True)
    user = models.CharField(max_length=255, blank=True, null=True)