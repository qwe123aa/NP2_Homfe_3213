from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, DeleteView, UpdateView
from .models import recipe

from 홈피.form import RegisterForm
from 홈피.models import recipe

class recipeListView(ListView):
    model = recipe

class recipeDetailView(DetailView):
    model = recipe

class recipeCreateView(CreateView):
    model = recipe
    fields = '__all__'
    template_name_suffix = '_create'
    success_url = reverse_lazy('홈피:recipe_list')

class recipeDeleteView(DeleteView):
    model = recipe
    success_url = reverse_lazy('홈피:recipe_list')

class recipeUpdateView(UpdateView):
    model = recipe
    fields = '__all__'
    template_name_suffix = '_update'

    def get_success_url(self):
        return reverse_lazy('홈피:recipe_detail', kwargs={'pk': self.object.pk })

def signInView(request):
    if request.method =='POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('홈피:recipe_list')
        else:
            messages.error(request, '아이디 혹은 비밀번호가 틀렸습니다')

    return render(request, '홈피/sign_in.html')

def signUpView(request):
    if request.method =='POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'가입 완료되었습니다')
            return redirect('홈피:sign_in')
    else:
        form = RegisterForm()

    return render(request, '홈피/sign_up.html', {'form' : form})

def logOutView(request):
    logout(request)
    return redirect('홈피:recipe_list')