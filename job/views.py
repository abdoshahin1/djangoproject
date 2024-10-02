from django.shortcuts import render
from .models import job
# Create your views here.
def jobs(request):
    jobs = job.objects.all()
    context = {"jobs" : jobs}
    return render(request,'job/jobs.html',context)

def job_details(request, id):
    job_details = job.objects.get(id=id)
    context = {'job_details':job_details}
    return render(request,'job/job_details.html',context)