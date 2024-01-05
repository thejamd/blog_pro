from django.urls import path
from blog_app.views import HomeView,ArticleView,AddpostView,updatepostview,deletepostview,AddCategoryView,Categoryview,CategoryListView

urlpatterns = [
    
    # path('',views.home,name='home')
    path('',HomeView.as_view(),name='home'),
    path('article_detail/<int:pk>', ArticleView.as_view(), name='article_detail'),
    path('add_post', AddpostView.as_view(), name='add_post'),
    path('add_category', AddCategoryView.as_view(), name='add_category'),
    path('article_detail/edit/<int:pk>',updatepostview.as_view(), name='update_post'),
    path('article_detail/delete/<int:pk>',deletepostview.as_view(), name='delete_post'),
    path('category/<str:cats>',Categoryview.as_view(), name='category'),
    path('category_list/',CategoryListView, name='category_list')
]