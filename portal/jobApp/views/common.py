from django.shortcuts import render, redirect
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
from jobApp.models import CustomUser, Employer, Employee, CreateJob, Category,Location, Application, Contact
from django.contrib import messages  # import messages
from django.utils import timezone
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q
from jobApp.forms import ContactForm


def JobListView(request):
    jobs            = CreateJob.objects.all()
    qs              = CreateJob.objects.all().count()
    user            = Employee.objects.all().count()
    company_name    = Employer.objects.all().count()
    cat_menu        = Category.objects.all()
    appliedjob_count= Application.objects.count()
    joblocation     = Location.objects.all()


    job = CreateJob.objects.filter(published_date__lte=timezone.now()).order_by(
        "-published_date"
    )

    # paginator = Paginator(qs, 5)  # Show 5 jobs per page
    # page = request.GET.get("page")
    # try:
    #     jobs = paginator.page(page)
    # except PageNotAnInteger:
    #     jobs = paginator.page(1)
    # except EmptyPage:
    #     jobs = paginator.page(paginator.num_pages)

    context = {
        "jobs": jobs,
        "jobs_qs": qs,
        "company_name": company_name,
        "candidates": user,
        "cat_menu": cat_menu,
    }

    return render(request, "jobApp/home.html", context)


class JobDetail(DetailView):
    template_name = "jobApp/job_detail.html"
    context_object_name = "job_detail"
    model = CreateJob
    paginate_by = 1

    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()
        context = super(JobDetail, self).get_context_data(*args, **kwargs)
        context["cat_menu"] = cat_menu
        return context


def signup(request):
    return render(request, "jobApp/signup.html")


def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_superuser:
                    login(request, user)
                    return redirect("super_list", pk=user.id)
                if user.is_employee:
                    login(request, user)
                    return redirect("employee_list", pk=user.id)
                if user.is_employer:
                    login(request, user)
                    return redirect("employer_list", pk=user.id)

            else:
                messages.error(request, "Invalid username or password")
        else:
            messages.error(request, "Invalid username or password")
    return render(request, "jobApp/login.html", context={"form": AuthenticationForm})


def logout_view(request):
    logout(request)
    return redirect("/")


class SearchView(ListView):
    model = CreateJob
    template_name = "jobApp/search.html"
    context_object_name = "jobs"

    def get_queryset(self):
        return self.model.objects.filter(
            job_title__contains=self.request.GET["job_title"],
            address__contains=self.request.GET["address"],
        )

def contact(request):

        saveFlag = False
        newform = ContactForm()
        if request.method == "POST":

            newform = ContactForm(request.POST)
            names = mail = mess = phone = ""

            if newform.is_valid():        
                names      = request.POST['name']
                mail      = request.POST.get("email")
                mess      = request.POST['message']
                phone = request.POST['phone_number']

                newform  = Contact(name = names, email=mail,  message = mess, phone_number = phone,)
                saveFlag  = newform.save()
                saveFlag = True
                
            if saveFlag:
                message = {
                            "response":"Thank you for contacting us, We will revert back shortly",
                            "name": names
                        }
            else:
                message = {
                            "form":newform
                        }
        else:
            message = { "form":newform}

        return render(request,'JobApp/contact.html', context = message)