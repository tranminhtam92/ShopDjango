from django.conf.urls import include, url
from . import views
urlpatterns = [
     url(r'^list/',views.ShopList.as_view()),
     url(r'^detail/(?P<pk>[0-9]+)/$', views.ShopDetail.as_view()),
]
