from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.utils import timezone
from django.views.generic import ListView, CreateView, DetailView, DeleteView, UpdateView
from .models import recipe, CustomUser

from 홈피.form import RegisterForm, SignInForm
from 홈피.models import recipe

class recipeListView(ListView):
    model = recipe

class recipeDetailView(DetailView):
    model = recipe

class recipeCreateView(CreateView):
    model = recipe
    fields = ['name', 'pic', 'material', 'process']
    template_name_suffix = '_create'
    success_url = reverse_lazy('홈피:recipe_list')

    def form_valid(self, form):
        form.instance.author = self.request.user  # 현재 로그인된 사용자를 author로 설정
        return super().form_valid(form)

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
    if request.method == 'POST':
        form = SignInForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('홈피:recipe_list')  # 로그인 후 리다이렉트할 URL을 설정합니다.
            else:
                error_message = "Invalid username or password."
        else:
            error_message = "Invalid username or password."
    else:
        form = SignInForm()
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

def myPageView(request):
    recipe_list = recipe.objects.filter(author=request.user)
    return render(request, '홈피/my_page.html', {'recipe_list': recipe_list, 'user': request.user})