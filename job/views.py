from django.core.paginator import Paginator
from django.shortcuts import render
from .models import job
# Create your views here.

def jobs(request):
    jobs = job.objects.all()
    paginator = Paginator(jobs, 1)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    context = {"jobs" : page_obj}
    return render(request,'job/jobs.html',context)

def job_details(request, slug):
    job_details = job.objects.get(slug=slug)
    context = {'job_details':job_details}
    return render(request,'job/job_details.html',context)