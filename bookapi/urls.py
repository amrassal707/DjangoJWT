from django.urls import path
from . import views
from rest_framework.authtoken.views import obtain_auth_token 
urlpatterns = [
    path('books/',views.readBooks),
    path('secret/', views.secret),
    path('tokengenerate/', obtain_auth_token),
    path('manager/', views.manager_view),
    path('throttle/', views.throttle),
    path('throttleauth/' , views.throttleAuth),
    path('customthrottle/', views.throttlesfortenminutes),
]
