from django.core.paginator import Paginator
from django.shortcuts import render
from .models import job
from .form import apply_form

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
    if request.method == 'POST':
        form = apply_form(request.POST, request.FILES)
        if form.is_valid:
            form = form.save(commit=False)
            form.job = job_details
            form.save()
    else:
        form = apply_form()
    context = {'job_details':job_details, 'form1':form}
    return render(request,'job/job_details.html',context)