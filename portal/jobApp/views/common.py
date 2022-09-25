from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from django.views.generic import (
    ListView,
    DetailView,
   
)
from jobApp.models import  Employer, CreateJob, Category,Location, Application, Contact
from django.contrib import messages  # import messages
from django.utils import timezone

from jobApp.forms import ContactForm


def JobListView(request):
    qs              = CreateJob.objects.filter(published_date__lte=timezone.now()).order_by(
        "-published_date"
    ).count()

    company_name    = Employer.objects.all().count()
    cat_menu        = Category.objects.all()
    appliedjob_count= Application.objects.count()
    joblocation     = Location.objects.all()


    job = CreateJob.objects.filter(published_date__lte=timezone.now()).order_by(
        "-published_date"
    )

    context = {
        "job": job,
        "jobs_qs": qs,
        "company_name": company_name,
        # "candidates": user,
        "cat_menu": cat_menu,
    }

    return render(request, "jobApp/home.html", context)


def publish_drafts_post(request, pk):
    job = get_object_or_404(CreateJob, pk=pk)
    job.publish()
    return redirect("home")



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