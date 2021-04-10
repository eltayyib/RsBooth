from django.test import TestCase

# Create your tests here.
def get_profile(request, pk):
    current_user_rec = Employer.objects.get(user_id=pk)

    u_form = forms.EmployerUpdateForm()
    if request.method == 'POST':
        u_form = EmployerUpdateForm(request.POST,request.FILES, instance=request.user)
        if u_form.is_valid():
           # print(request.POST,request.FILES)
            u_form.save()
            print('im valid')
            messages.success(request, f'Your account has been updated!')
    else:
        u_form = EmployerUpdateForm()
            # return redirect('emp_detail',pk=pk)
    context = {'current_user_rec':current_user_rec,'u_form':u_form}
    return render(request,"jobApp/employer/employer_profile.html", context )