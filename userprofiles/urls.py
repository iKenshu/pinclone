from django.conf.urls import url

from .views import SignUpView, LogInView, LogOutView

app_name = 'Profile'
urlpatterns = [
    url(r'^signup/$', SignUpView.as_view(), name='sign_up'),
    url(r'^login/$', LogInView.as_view(), name='login'),
    url(r'^logout/$', LogOutView.as_view(), name='logout'),
]