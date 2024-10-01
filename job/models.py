from django.db import models

# Create your models here.
jobType = (
    ('full time','full time'),
    ('part time','part time'),
)
class job(models.Model):
    title = models.CharField(max_length =20)
    #location
    job_type = models.CharField(max_length =20, choices = jobType)
    description = models.TextField(max_length=1000)
    published = models.DateTimeField(auto_now=True)
    Vacancy = models.IntegerField(default=1)
    salary = models.IntegerField(default=0)
    experience = models.IntegerField(default=1)
    def __str__(self) -> str:
        return self.title