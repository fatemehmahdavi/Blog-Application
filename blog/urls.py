from django.urls import path
from . import views

urlpatterns = [
    path('',views.starrting_page, name = "starting-page"),
    path('posts/', views.posts, name="posts-page"),
    path('posts/<slug:slug>/', views.post_detail, name = "post-detail-page"),
    #path('post/<str:name>/', views.post_detail_by_name, name = "single-post-str"),
    
]