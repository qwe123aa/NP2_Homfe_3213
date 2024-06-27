from django.conf.urls.static import static
from django.urls import path

from HomFe import settings
from 홈피 import views

app_name='홈피'

urlpatterns=[
    path('', views.recipeListView.as_view(),name='recipe_list'),
    path('create/', views.recipeCreateView.as_view(), name='recipe_create'),
    path('detail/<int:pk>/', views.recipeDetailView.as_view(), name='recipe_detail'),
    path('delete/<int:pk>/', views.recipeDeleteView.as_view(), name='recipe_delete'),
    path('update/<int:pk>/', views.recipeUpdateView.as_view(), name='recipe_update'),

    path('signIn/', views.signInView, name='sign_in'),
    path('signUp/', views.signUpView, name='sign_up'),
    path('logOut/', views.logOutView, name='log_out'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)