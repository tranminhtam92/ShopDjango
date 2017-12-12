from django.conf.urls import include, url
from . import views
urlpatterns = [
     url(r'^list/',views.CommentList.as_view()),
    #  url(r'^comment/',views.CommentList.as_view()),
    #  url(r'^detail/(?P<pk>[0-9]+)/$', views.ShopDetail.as_view()),
    #  url(r'^sql/', views.ShopUsingSQL),
]
