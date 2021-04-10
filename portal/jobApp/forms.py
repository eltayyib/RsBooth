from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.db import transaction
from .models import *

# from ckeditor.widgets import CKEditorWidget
#  (CustomUser, Employer, Employee,CreateJob)

choices = Category.objects.all().values_list("name", "name")

choice_list = []

for item in choices:
    choice_list.append(item)
    # print(choice_list)

choices = Location.objects.all().values_list('job_by_location', 'job_by_location') 
choice_location = []
for location in choices:
    choice_location.append(location)


class EmployerRegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    phone_no = forms.CharField(required=True)
    company_name = forms.CharField(required=True)
    address = forms.CharField(required=True)

    class Meta(UserCreationForm.Meta):
        model = CustomUser

        fields = [
            "username",
            "email",
            "phone_no",
            "company_name",
            "address",
            "password1",
            "password2",
        ]

        widgets = {
            "email": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Email"}
            ),
            "company_name": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Company Name"}
            ),
            "address": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Address"}
            ),
        }

    @transaction.atomic
    def save(self, commit=False):
        user = super().save(commit=False)
        user.is_employer = True
        user.is_employee = False
        user.email = self.cleaned_data.get("email")
        user.save()
        employer = Employer.objects.create(user=user)
        employer.phone_no = self.cleaned_data.get("phone_no")
        employer.company_name = self.cleaned_data.get("company_name")
        employer.address = self.cleaned_data.get("address")
        employer.save()
        return user


class EmployerUpdateForm(UserChangeForm):
    goal = forms.Textarea()
    vision = forms.Textarea()
    about_us = forms.Textarea()

    class Meta:
        model = Employer
        fields = ["goal", "vision", "about_us", "logo"]


class EmployeeUpdateForm(UserChangeForm):
    gender = forms.Select()
    status = forms.Select()
    nationality = forms.Select()
    # EDUCATIONAL BACKGROUND
    highest_qualifications = forms.CharField(required=True)
    institute_Names = forms.CharField(required=True)
    graduted_years = forms.CharField(required=True)
    grades = forms.CharField(required=True)
    # WORK EXPERIENCE
    job_title = forms.CharField(required=True)
    compnay_name = forms.CharField(required=True)
    monthly_salary = forms.CharField(required=True)
    work_type = forms.Select()
    country = forms.Select()
    start_date = forms.CharField(required=True)
    end_date = forms.CharField(required=True)
    job_responsibility = forms.Textarea()
    career_objective = forms.Textarea()
    cv = forms.FileField()
    picture = forms.ImageField()

    class Meta:
        model = Employee
        exclude = [
            "user",
            "username",
            "firstname",
            "lastname",
            "email",
            "age",
            "phone_no",
            "address",
        ]

        widgets = {
            "gender": forms.Select(choices=choices, attrs={"class": "form-control"}),
            "status": forms.Select(choices=choices, attrs={"class": "form-control"}),
            "work_type": forms.Select(choices=choices, attrs={"class": "form-control"}),
            "nationality": forms.Select(
                choices=choices, attrs={"class": "form-control"}
            ),
            "highest_qualifications": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "highest_qualifications"}
            ),
            "institute_Names": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "institute_Names"}
            ),
            "graduted_years": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "graduted_years"}
            ),
            "grades": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "grades"}
            ),
            "job_title": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "job_title"}
            ),
            "compnay_name": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "compnay_name"}
            ),
            "start_date": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "month/year"}
            ),
            "end_date": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "month/year"}
            ),
            "job_responsibility": forms.Textarea(
                attrs={"class": "form-control", "placeholder": "job_responsibility"}
            ),
            "career_objective": forms.Textarea(
                attrs={"class": "form-control", "placeholder": "career_objective"}
            ),
        }





class EmployeeRegistrationForm(UserCreationForm):
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    email = forms.EmailField(required=True)
    phone_no = forms.CharField(required=True)
    age = forms.CharField(required=True)
    address = forms.CharField(required=True)

    class Meta(UserCreationForm.Meta):
        model = CustomUser

        fields = [
            "username",
            "first_name",
            "last_name",
            "email",
            "phone_no",
            "age",
            "address",
            "password1",
            "password2",
        ]

        widgets = {
            "first_name": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "First Name"}
            ),
            "last_name": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Last Name"}
            ),
            "email": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Email"}
            ),
            "age": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Age"}
            ),
            "address": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Address"}
            ),
        }

    @transaction.atomic
    def save(self, commit=False):
        user = super().save(commit=False)
        user.is_employee = False
        user.is_employee = True
        user.first_name = self.cleaned_data.get("first_name")
        user.last_name = self.cleaned_data.get("last_name")
        user.email = self.cleaned_data.get("email")
        user.save()
        employee = Employee.objects.create(user=user)
        employee.phone_no = self.cleaned_data.get("phone_no")
        employee.age = self.cleaned_data.get("age")
        employee.address = self.cleaned_data.get("address")
        employee.save()
        return user


class JobCreationForm(forms.ModelForm):
    class Meta:

        model = CreateJob
        exclude = ["published_date", "created_date"]

        j_choices = [
            ("full time", "FULL TIME"),
            ("part time", "PART TIME"),
            ("freelancer", "FREELANCER"),
        ]

        s_choices = [
            ("$30,000", "$30,000"),
            ("$60,000", "$60,000"),
            ("$100,000", "$100,000"),
        ]

        E_CHOICES = [
            ("0 to 6 months", "0 to 6 months"),
            ("1 year", "1 YEAR"),
            ("2 years", "2 YEARS"),
        ]

        widgets = {
            "user": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "value": "",
                    "id": "user",
                    "type": "hidden",
                }
            ),
            "salary": forms.Select(choices=s_choices, attrs={"class": "form-control"}),
            "experience": forms.Select(
                choices=E_CHOICES, attrs={"class": "form-control"}
            ),
            "job_type": forms.Select(
                choices=j_choices, attrs={"class": "form-control"}
            ),
            "category": forms.Select(
                choices=choice_list, attrs={"class": "form-control"}
            ),
             "location": forms.Select(
                choices=choice_location, attrs={"class": "form-control"}
            ),
            "description": forms.Textarea(
                attrs={"class": "form-control", "placeholder": "Description"}
            ),
        }


class ApplicationForm(forms.ModelForm):
    class Meta:
        model = Application
        exclude = ["job", "company", "candidate"]

class ContactForm(forms.ModelForm):
    class Meta:
        model  = Contact
        fields = "__all__"
        labels = {
            
            'name': ("Fullname"),
            'email': ("Email"),
            'phone_number': ("Phone Number"),
            'message': ("Your Message"),
        }
        widgets = {

            'your_message':forms.Textarea(attrs={'class':'form-control', 'placeholder':'Enter your message'}),
        }