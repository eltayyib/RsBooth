from django.urls import path
from . import views
from jobApp.views import common, employees, employers, supers

urlpatterns = [
    # registration urls
    path("employee_reg", employees.EmployeeSignupView.as_view(), name="employee_reg"),
    path("employer_reg", employers.EmployerSignupView.as_view(), name="employer_reg"),
    # list views urls
    path(
        "employee_list/<int:pk>",
        employees.EmployeeListView.as_view(),
        name="employee_list",
    ),
    path(
        "employer_list/<int:pk>",
        employers.EmployerListView.as_view(),
        name="employer_list",
    ),
    path("super_list/<int:pk>", supers.AdminListView.as_view(), name="super_list"),
    path("data_list", supers.displaydata, name="data_list"),
    path("draft_list", supers.DraftListView.as_view(), name="draft_list"),
    path("activate/<int:user_id>", supers.activate_user, name="activate_data"),
    path("deactivate/<int:user_id>", supers.deactivate_user, name="deactivate_data"),
    path("publish/<int:pk>", supers.publish_drafts_post, name="publish"),
    path("detail/<int:pk>", common.JobDetail.as_view(), name="detail"),
    path('contact', common.contact, name='contact'),
    # create views urls
    path("create_job", employers.CreateJobView, name="create_job"),
    path("category/<str:cats>", supers.CategoryView, name="category"),
    path("add_category", supers.AddCategoryView.as_view(), name="add_category"),
    path("add_location", supers.AddLocationView.as_view(), name="add_location"),
    path("update/<int:pk>", employers.JobUpdate.as_view(), name="update"),
    path("delete/<int:pk>", employers.JobDelete.as_view(), name="delete"),
    path("emp_detail/<int:pk>", employers.get_profile, name="emp_detail"),
    path("employee_profile/<int:pk>", employees.emp_profile, name="employee_profile"),
    path("apply_for_job/<int:pk>", employees.apply_job, name="apply_for_job"),
    path("candidate", employees.Candidates, name="candidate"),
    path("search/", common.SearchView.as_view(), name="search"),
]

