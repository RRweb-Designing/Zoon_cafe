
from django.contrib import admin
from django.urls import path
from myapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index,name="index"),
    path('contact_us/',views.contact_us,name="contact_us"),
    path('feature/',views.feature,name="feature"),
    path('blog/',views.blog,name="blog"),
    path('booking/',views.booking,name="booking"),
    path('about/',views.about,name="about"),
    path('team/',views.team,name="team"),
    path('base/',views.base,name="base"),
    path('register/',views.register,name="register"),
    path('check_user_exists/',views.check_user_exists,name="check_user_exist"),
]
