from django.shortcuts import redirect, render, get_object_or_404
from django.urls import reverse, reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView, UpdateView, DeleteView
from allauth.account.views import SignupView, LoginView
from django.contrib.auth.views import PasswordResetConfirmView
from .forms import CustomSignupForm, CustomLoginForm, CustomSetPasswordForm, GPXFileForm
from .models import GPXFile
from django.http import FileResponse

class MyMembersView(LoginRequiredMixin, TemplateView):
    template_name = 'members/members.html'
    login_url = '/account/login/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = GPXFileForm()
        context['files'] = GPXFile.objects.all()
        return context

    def post(self, request, *args, **kwargs):
        form = GPXFileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('my_members')
        return self.get(request, *args, **kwargs)

class GPXFileEditView(LoginRequiredMixin, UpdateView):
    model = GPXFile
    form_class = GPXFileForm
    template_name = 'members/gpxfile_edit.html'
    success_url = reverse_lazy('my_members')

class GPXFileDeleteView(LoginRequiredMixin, DeleteView):
    model = GPXFile
    template_name = 'members/gpxfile_confirm_delete.html'
    success_url = reverse_lazy('my_members')

def download_gpxfile(request, pk):
    gpxfile = get_object_or_404(GPXFile, pk=pk)
    response = FileResponse(gpxfile.file.open('rb'), as_attachment=True)
    return response

class CustomSignupView(SignupView):
    form_class = CustomSignupForm

    def form_valid(self, form):
        response = super().form_valid(form)
        user = self.user
        user.is_active = True
        user.save()
        return redirect(self.get_success_url())

    def get_success_url(self):
        return reverse('my_members')

class CustomLoginView(LoginView):
    form_class = CustomLoginForm

    def get_success_url(self):
        return reverse('my_members')

def custom_logout_view(request):
    from django.contrib.auth import logout
    logout(request)
    return redirect('home')

class CustomPasswordResetConfirmView(PasswordResetConfirmView):
    form_class = CustomSetPasswordForm
    template_name = 'account/password_reset_confirm.html'
    success_url = reverse_lazy('password_reset_complete')

    def form_valid(self, form):
        return super().form_valid(form)

def custom_404_view(request, exception):
    return render(request, '404.html', status=404)

def custom_500_view(request):
    return render(request, '500.html', status=500)

def custom_403_view(request, exception):
    return render(request, '403.html', status=403)
