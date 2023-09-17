from django.urls import path
from . import views


app_name = "blog"
urlpatterns = [
    path('detail/<slug:slug>' , views.post_detail , name="article_detail"),
    path('list' , views.article_list , name="articles_list"),
    path('category/<int:pk>' , views.category_detail , name="category_detail"),
    path('search/' , views.search , name="search_articles"),
    path('contactus' , views.contactus , name="contact_us"),
    # path('testbase' , views.TestBaseView.as_view() , name="test_base"),
    path('users' , views.UserList.as_view() , name="user_list"),
    path('red' , views.HomePageRedirect.as_view() , name="redirect"),
]