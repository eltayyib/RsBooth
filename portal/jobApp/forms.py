from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.db import transaction
from .models import *



choices = Category.objects.all().values_list("name", "name")

choice_list = []

for item in choices:
    choice_list.append(item)

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




class JobCreationForm(forms.ModelForm):
    class Meta:

        model = CreateJob
        exclude = ["published_date", "created_date"]

        p_choices = [
            ("apartment", "APARTMENT"),
            ("land", "LAND"),
            ("let", "LET"),
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
            # "price": forms.Textarea (attrs={"class": "form-control", "placeholder": "Price"}),
            "post_type": forms.Select(
                choices=p_choices, attrs={"class": "form-control"}
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