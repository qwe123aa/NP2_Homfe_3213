from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, DeleteView, UpdateView

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