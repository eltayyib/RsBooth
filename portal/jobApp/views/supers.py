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
from jobApp.models import CustomUser, Employer, Employee, Category, CreateJob, Location
from django.contrib import messages


class AdminListView(TemplateView):
    model = CustomUser
    template_name = "jobApp/admin/admin_dashboard.html"
    context_object_name = "super"


def AdminProfile(request,pk):
    current_user_rec = CustomUser.objects.filter(pk=1)
       

    return render(request, "jobApp/admin/admin_profile.html", {"current_user_rec":current_user_rec})

def displaydata(request):
    results = CustomUser.objects.all()
    # context_object_name = 'display'
    # print(results)
    return render(request, "jobApp/admin/data_list.html", {"results": results})


def activate_user(request, user_id):
    user = get_object_or_404(CustomUser, pk=user_id)
    # print(user)
    user.is_staff = True
    user.save()
    return redirect("data_list")


def deactivate_user(request, user_id):
    user = get_object_or_404(CustomUser, pk=user_id)
    # print(user)
    user.is_staff = False
    user.save()
    return redirect("data_list")


class AddCategoryView(CreateView):
    model = Category
    template_name = "jobApp/admin/add_category.html"
    fields = "__all__"

    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()
        context = super(AddCategoryView, self).get_context_data(*args, **kwargs)
        context["cat_menu"] = cat_menu
        return context


def CategoryView(request, cats):
    cat_menu = Category.objects.all()
    template_name = "jobApp/admin/categories.html"
    category_post = CreateJob.objects.filter(category=cats.replace("-", " "))
    return render(
        request,
        template_name,
        {
            "cats": cats.title().replace("-", " "),
            "category_post": category_post,
            "cat_menu": cat_menu,
        },
    )


class DraftListView(ListView):

    template_name = "jobApp/admin/draft_job.html"
    context_object_name = "drafts"
    model = CreateJob

    def get_queryset(self):
        return CreateJob.objects.filter(published_date__isnull=True).order_by(
            "created_date"
        )




class AddLocationView(CreateView):
    model = Location
    template_name = "jobApp/admin/add_location.html"
    fields = "__all__"

    def get_context_data(self, *args, **kwargs):
        loc_menu = Location.objects.all()
        context = super(AddLocationView, self).get_context_data(*args, **kwargs)
        context["loc_menu"] = loc_menu
        return context


def EmployerList(request):
    can = CustomUser.objects.all()
    # context_object_name = 'display'
    # print(results)
    return render(request, "jobApp/admin/employer_list.html", {"can": can})


def Candidates(request):
    can = CustomUser.objects.all()
    # context_object_name = 'display'
    # print(results)
    return render(request, "jobApp/admin/employee_list.html", {"can": can})