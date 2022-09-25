from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls import reverse
from django.utils import timezone



class CustomUser(AbstractUser):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    is_employer = models.BooleanField(default=False)

    def __str__(self):
        return self.username


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("super_list", kwargs={"pk": self.pk})


class Employer(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, default="")
    company_name = models.CharField(max_length=100)
    phone_no = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    goal = models.TextField(max_length=200)
    vision = models.TextField(max_length=200)
    about_us = models.TextField(max_length=200)
    logo = models.ImageField(upload_to="featured_image", blank=True)

    def __str__(self):
        return self.company_name




class CreateJob(models.Model):

    user = models.ForeignKey(
        CustomUser, on_delete=models.CASCADE, default="", related_name="createjob"
    )
    post_title = models.CharField(max_length=100)
    company_name = models.CharField(max_length=100)
    price = models.CharField(max_length=100)
    company_logo = models.ImageField(upload_to="featured_image", blank=True)
    category = models.CharField(max_length=100, default="")
    location = models.CharField(max_length=100, default="")
    post_type = models.CharField(max_length=100)
    created_date = models.DateTimeField(default=timezone.now)
    description = models.CharField(max_length=500, default="")
    address = models.CharField(max_length=100)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def get_absolute_url(self):
        return reverse("home")


class Application(models.Model):
    job_id = models.ForeignKey(
        CreateJob, related_name="application", on_delete=models.CASCADE
    )
    employer_id = models.CharField(
        max_length=100
    )
    employee_id = models.ForeignKey(
        CustomUser, related_name="application", on_delete=models.CASCADE
    )
    date_applied = models.DateTimeField(default=timezone.now)
    openings_position = models.DateTimeField

    def __str__(self):
        return self.job_title


class Location(models.Model):
    job_by_location    = models.CharField(max_length=200)

    def __str__(self):
        return self.job_by_location 
   
    def get_absolute_url(self):
        return reverse("super_list", kwargs={"pk": self.pk})


class Contact(models.Model):
    name = models.CharField(max_length = 128)
    email = models.CharField(max_length = 200, unique = True)
    phone_number = models.CharField(max_length = 128)
    message = models.TextField()


    def __str__(self):
        return self.name 

    
    def get_absolute_url(self):

        return reverse('contact',)