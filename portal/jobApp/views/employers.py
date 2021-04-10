from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from django.views.generic import (
    TemplateView,
    ListView,
    CreateView,
    DetailView,
    UpdateView,
    DeleteView,
)
from jobApp.models import CustomUser, Employer, Employee, CreateJob, Category
from jobApp.forms import (
    EmployeeRegistrationForm,
    EmployerRegistrationForm,
    JobCreationForm,
    EmployerUpdateForm,
)
from django.urls import reverse_lazy
from jobApp import forms
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


# class CreateJobView(CreateView):
#     model = CreateJob
#     template_name = "jobApp/employer/create_job.html"
#     form_class = JobCreationForm

#     # for lists in context_object_name:
#     #     print(lists)

#     def form_valid(self, form):
#         user = form.save()
#         return super(CreateJobView, self).form_valid(form)

#     def get_context_data(self, *args, **kwargs):
#         cat_menu = Category.objects.all()
#         context = super(CreateJobView, self).get_context_data(*args, **kwargs)
#         context["cat_menu"] = cat_menu
#         return context


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

    # u_form = EmployerUpdateForm()
    if request.method == "POST":
        u_form = EmployerUpdateForm(
            request.POST, request.FILES, instance=request.user.employer
        )
        if u_form.is_valid():
            # print(request.POST,request.FILES)
            u_form.save()
            # print('im valid')
            messages.success(request, f"Your account has been updated!")
            # return redirect('employer_list',pk=pk)
        else:
            u_form = EmployerUpdateForm()
    else:
        # e_form = EmployerUpdateForm(instance=request.user.companyprofile)
        u_form = EmployerUpdateForm(instance=request.user.employer)
        # return HttpResponse(crequest.user)
    context = {"current_user_rec": current_user_rec, "u_form": u_form}

    return render(request, "jobApp/employer/employer_profile.html", context)


# class ProfileUpdate(UpdateView):
#     model = Employer
#     form_class = EmployerUpdateForm
#     template_name = "jobApp/employer/employer_profile.html"
#     redirect_field_name = "jobApp/employer/employer_profile.html"
#     fields = ('goal','vision','about_us','logo')


# class EmployerDetailView(DetailView):
#     model = Employer
#     all_customers = Employer.objects.all()

#     context_object_name = 'employer_detail'
#     template_name = "jobApp/employer/employer_profile.html"

#     def get_queryset(self):
#         current_user = self.request.user
#         # current_user_rec = Employer.objects.filter(user_id__exact=self.request.user.pk)
#         current_user_rec = self.all_customers.filter(user_id__exact=self.request.user.pk)
#         print(self.all_customers)
#         return current_user_rec
#     context_object_name = 'employer_detail'
# return Employer.objects.raw("SELECT * FROM jobapp_employer WHERE user_id = %s",[self.request.user.pk])


# def employer_profile(request,pk):
#     # template_name = 'jobApp/employer/employer_update.html'
#     # profil_obj =""
#     # if pk != '':
#     #     profil_obj = CompanyProfile.objects.raw("SELECT * FROM jobapp_companyprofile WHERE user_id = %s",[pk])
#     if request.method == 'POST':
#         if len(profil_obj) > 0:
#             e_form = EmployerProfileForm(request.POST,request.FILES,instance=request.user.companyprofile)
#             u_form = UpdateForm(request.POST,instance=request.user)
#         else:
#             e_form = EmployerProfileForm(request.POST,request.FILES)
#             u_form = UpdateForm(request.POST,instance=request.user)


#     #     if e_form.is_valid() and u_form.is_valid():
#     #         e_form.save()
#     #         u_form.save()
#     #         return redirect('emp_detail',pk=pk)
#     # else:
#     #     if len(profil_obj) > 0:
#     #         e_form = EmployerProfileForm(instance=request.user.companyprofile)
#     #         u_form = UpdateForm(instance=request.user)
#     #     else:
#     #         e_form = EmployerProfileForm()
#     #         u_form = UpdateForm(instance=request.user)

#     context = {'e_form':e_form,'u_form':u_form}
#     return render(request,"jobApp/employer/employer_profile.html",context)

