from django.urls import path
from . import views
urlpatterns = [
    path('' , views.home , name="home"),
    path('contact/' , views.contact , name="contact"),
    path('signup/' , views.signup , name="signup"),
    path('login/' , views.log_it_in , name="login"),
    path('logout/' , views.log_Out , name="logout"),
    path('CreatePost' , views.CreatePost , name="CreatePost"),
    path('dashboard/' , views.dashboard , name="dashboard"),
    path('CreatePost/' , views.CreatePost , name="CreatePost"),
    path('update/<str:pk>' , views.Update , name="update"),
    path('post/<str:pk>' , views.SeePost , name="SeePost"),
    #path('Privatepost/<str:pk>' , views.SeePrivatePost , name="SeePrivatePost")
]