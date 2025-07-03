
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
urlpatterns = [

    path("",views.Books,name="books_list"),
    path("authors",views.getAllAuthors,name="author_list"),
    path("publishers",views.getAllPublishers,name="publisher_list"),
    path('signup/', views.signup_view, name='signup'),
    path('login/', auth_views.LoginView.as_view(template_name='bookstoreApp/login.html',redirect_authenticated_user=True), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]