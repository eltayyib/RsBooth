from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.views.generic import (
    TemplateView,
    CreateView,
    UpdateView,
    DeleteView,
)
from jobApp.models import  Employer, CreateJob, Category
from jobApp.forms import (
    EmployerRegistrationForm,
    JobCreationForm,
    EmployerUpdateForm,
)
from django.urls import reverse_lazy
from django.contrib import messages


class EmployerSignupView(CreateView):
    model = Employer
    form_class = EmployerRegistrationForm
    template_name = "jobApp/employer_signup.html"

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect("emp_detail", pk=user.id)


class EmployerListView(TemplateView):
    model = Employer
    template_name = "jobApp/employer/employer_dashboard.html"
    context_object_name = "post"





def CreateJobView(request):
    c_form = JobCreationForm()
    if request.method == "POST":
        c_form = JobCreationForm(request.POST, request.FILES)
        if c_form.is_valid():
            c_form.save()
            messages.success(
                request,
                f"Your job has been posted and waiting for approval from the Admin!",
            )
            return redirect("home")
        else:
            c_form = JobCreationForm(request.POST, request.FILES)

    return render(request, "jobApp/employer/create_job.html", {"c_form": c_form})

    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()
        context = super(CreateJobView, self).get_context_data(*args, **kwargs)
        context["cat_menu"] = cat_menu
        return context


class JobUpdate(UpdateView):
    login_url = "login"
    redirect_field_name = "jobApp/home.html"
    template_name = "jobApp/employer/job_post_form.html"
    fields = (
        "company_name",
        "qualification",
        "salary",
        "company_logo",
        "experience",
        "no_of_vacancy",
        "job_title",
    )
    model = CreateJob

    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()
        context = super(JobUpdate, self).get_context_data(*args, **kwargs)
        context["cat_menu"] = cat_menu
        return context


class JobDelete(DeleteView):
    template_name = "blogApp/employer/job_delete.html"
    success_url = reverse_lazy("home")
    model = CreateJob

    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()
        context = super(JobDelete, self).get_context_data(*args, **kwargs)
        context["cat_menu"] = cat_menu
        return context


def get_profile(request, pk):
    current_user_rec = Employer.objects.get(user_id=pk)

    u_form = EmployerUpdateForm()
    if request.method == "POST":
        u_form = EmployerUpdateForm(
            request.POST, request.FILES, instance=request.user.employer
        )
        if u_form.is_valid():
           
            u_form.save()
            
            messages.success(request, f"Your account has been updated!")
        
        else:
            u_form = EmployerUpdateForm()
   
    context = {"current_user_rec": current_user_rec, "u_form": u_form}

    return render(request, "jobApp/employer/employer_profile.html", context)




