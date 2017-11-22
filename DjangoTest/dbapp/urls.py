from django.conf.urls import url
from dbapp import views
urlpatterns = [
    url(r'^login/',views.login)
]