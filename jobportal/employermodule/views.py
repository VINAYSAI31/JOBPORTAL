from django.shortcuts import render
from .models import * #Import only the necessary class

def jobpost(request):
    return render(request, 'employermodule/jobpost.html')

def add_job_details(request):
    if request.method == 'POST':
        work_title = request.POST.get('work_title')
        salary_offered = request.POST.get('salary_offered')
        job_type = request.POST.get('job_type')
        benefits = request.POST.get('benefits')
        education = request.POST.get('education')
        work_location = request.POST.get('work_location')
        required_skills = request.POST.get('required_skills')

        job_details = JobDetails(
            work_title=work_title,
            salary_offered=salary_offered,
            job_type=job_type,
            benefits=benefits,
            education=education,
            work_location=work_location,
            required_skills=required_skills,
        )
        job_details.save()
        return render(request, 'employermodule/datainserted.html')

    return render(request, 'employeerhomepage.html')

def view_job_details(request):
    job_details_list = JobDetails.objects.all()
    return render(request, 'employermodule/view_job_details.html',{'job_details_list':job_details_list})
