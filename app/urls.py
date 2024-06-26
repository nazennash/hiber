from django.urls import path
from . import views

urlpatterns = [
    # path('', views.index),
    path('index/', views.index, name="index"),

    #authentications
    path('login/', views.login_view, name="login"),
    path('register/', views.registration_view, name="register"),
    path('logout/', views.logout_view, name="logout"),

    path('administrator/', views.administrator_index, name="administrator"),
    path('add_agent/', views.add_agent, name="add_agent"),
    path('agent/', views.agent_index, name="agent"),
    path('lead/', views.lead_index, name="lead"),
]