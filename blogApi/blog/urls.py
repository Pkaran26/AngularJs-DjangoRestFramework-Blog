from django.urls import path
from .import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('post/', views.BlogPostList.as_view()),
    path('post/<int:pk>/', views.BlogDetail.as_view()),
    path('post/createpost', views.CreatePost.as_view()),
    path('post/managepost/<int:pk>/', views.ManagePost.as_view()),
    path('post/search/<int:id>/', views.SearchByCategory.as_view()),
    path('post/search/<str:search>/', views.SearchByAll.as_view()),

    path('category/', views.CategoryList.as_view()),
    path('category/<int:pk>', views.GetCategory.as_view()),
    path('category/createcategory', views.CreateCategory.as_view()),
    path('category/managecategory/<int:pk>/', views.ManageCategory.as_view()),

    path('comment/<int:pk>', views.GetComment.as_view()),
    path('comment/createcomment', views.CreateComment.as_view()),
    path('comment/managecomment/<int:pk>', views.ManageComment.as_view()),

    path('post/user/', views.GetUser.as_view()),
]