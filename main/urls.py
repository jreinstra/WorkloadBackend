from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^$', views.index, name="index"),
    
    # API Methods
    url(r'^api/blocks', views.BlockList.as_view(), name="block_list"),
    url(r'^api/block', views.BlockDetail.as_view(), name="block_detail"),
]