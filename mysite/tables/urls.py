from django.urls import path, include
from . import views


urlpatterns = [
    path('dashboard/<str:pk_task>', views.Dashboard, name='dashboard'),

    path('cooperator/<str:pk_test>', views.CooperatorView, name='cooperator'),
    path('specialist_list', views.SpecialistListView, name='specialist_view'),
    path('specialist_delete/<str:pk>', views.DeleteSpecialist, name="delete_specialist"),
    path('specialist_update/<str:pk>', views.UpdateSpecialist, name='update_specialist'),

    path('create_task/<str:pk>', views.CreateTaskTable, name='create_task'),
    path('update_task/<str:pk>', views.UpdateTableTask, name="update_task"),
    path('delete_task/<str:pk>', views.DeleteTableTask, name='delete_task'),

    path("create_project", views.CreateProjects, name='create_project'),
    path("update_project/<str:pk>", views.UpdateProjects, name="update_project"),
    path("delete_project/<str:pk>", views.DeleteProject, name="delete_project"),

    path('user/', views.userPage, name='user-page'),
    path('account/', views.accountSettings, name='account'),

]
