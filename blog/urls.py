from . import views
from django.urls import path

urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    path('add_post.html/',views.AddPost.as_view(), name='add_post'),
    path('post/edit/<int:pk>/',views.UpdatePost.as_view(), name='edit_post'),
    path('post/<int:pk>/remove',views.DeletePost.as_view(), name='delete_post'),

]