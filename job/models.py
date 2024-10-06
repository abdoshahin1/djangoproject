from django.db import models
from django.utils.text import slugify
# Create your models here.
jobType = (
    ('full time','full time'),
    ('part time','part time'),
)

def upload_image(job,filename):
    imagename, extention = filename.split(".")
    return f"jobs/{job.id}.{extention}"
class job(models.Model):
    title = models.CharField(max_length =20)
    #location
    job_type = models.CharField(max_length =20, choices = jobType)
    description = models.TextField(max_length=1000)
    published = models.DateTimeField(auto_now=True)
    Vacancy = models.IntegerField(default=1)
    salary = models.IntegerField(default=0)
    experience = models.IntegerField(default=1)
    category = models.ForeignKey('category', on_delete=models.CASCADE)
    image = models.ImageField(upload_to=upload_image)
    slug = models.SlugField(blank=True, null=True)

    def save(self,*args, **kwargs):
        self.slug = slugify(self.title)
        super(job,self).save(*args, **kwargs)
    def __str__(self) -> str:
        return self.title

class category(models.Model):
    name = models.CharField(max_length=20)
    def __str__(self):
        return self.name