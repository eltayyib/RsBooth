from django.shortcuts import render, redirect, get_object_or_404
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
from jobApp.models import CustomUser, Employer, Employee, CreateJob, Application
from jobApp.forms import (
    EmployeeRegistrationForm,
    EmployerRegistrationForm,
    EmployeeUpdateForm,
    ApplicationForm,
)
from django.contrib import messages


class EmployeeSignupView(CreateView):
    model = Employee
    form_class = EmployeeRegistrationForm
    template_name = "jobApp/employee_signup.html"

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect("employee_profile", pk=user.id)


class EmployeeListView(TemplateView):
    model = Employee
    template_name = "jobApp/employee/employee_dashboard.html"
    context_object_name = "posts"


def emp_profile(request, pk):
    current_rec = Employee.objects.get(user_id=pk)

    u_form = EmployeeUpdateForm()
    if request.method == "POST":
        u_form = EmployeeUpdateForm(
            request.POST, request.FILES, instance=request.user.employee
        )
        if u_form.is_valid():
            # print(request.POST,request.FILES)
            u_form.save()
            # print('im valid')
            messages.success(request, f"Your account has been updated succesfully!")
            return redirect("home")
        else:
            u_form = EmployeeUpdateForm(
            
            )
    # else:
    #     u_form = EmployeeUpdateForm(instance=request.user.employee)

    context = {"current_rec": current_rec, "u_form": u_form}
    return render(request, "jobApp/employee/employee_profile.html", context)


# def apply_job(request, pk):
#     job = CreateJob.objects.get(pk=pk)
#     print(job)
#     job_detail = ""
#     employee_job_applied = get_object_or_404(Application, pk=user_id)
#     candidate_id = employee_job_applied

#     if request.method == "POST":
#         form = ApplicationForm(request.POST, request.FILES)

#         if form.is_valid():
#             form.save()
#             messages.success(request, f"You have successfully applied for the job!")

#             return redirect("home")
#     else:
#         form = ApplicationForm()

#     return render(
#         request, "jobApp/employee/apply_for_job.html", {"form": form, "job": job}
#     )

def apply_job(request, pk):
    job =  get_object_or_404(CreateJob,pk=pk)
    employee_id = request.user
    employer_id = job.company_name
    openings_postition =job.openings_postition
    applyjob_obj = Application.objects.get_or_create(job_id = job,employee_id=employee_id,employer_id=employer_id, openings_postition=openings_postition)
    messages.success(request, f'You are successfully applied')
    return redirect( "detail", pk=pk,)

def  Applied_Jobs_by_Jobseeker(request):
    user = request.user
    Applied_Jobs = Application.objects.filter(employee_id=request.user)
    template = 'jobApp/Applied_Jobs_by_employee.html'
    return render(request, template,{'Applied_Jobs':Applied_Jobs, 'user':user})

# class Candidates(ListView):
#     model = Employee
#     template_name = "jobApp/employee/browse_candidate.html"
#     context_object_name = "can"





# def candidates(request,pk):
#     can = Employee.objects.get(user_id=pk)
#     print(can)

#     return render(request, 'jobApp/employee/browse_candidate.html')
