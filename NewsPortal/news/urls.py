from django.urls import path
from .views import NewsList, NewsDetail, Search, NewsAdd, NewsEdit, NewsDelete
from .views import CategoryView, add_subscribe #del_subscribe


urlpatterns = [
    # path('newsLLL/', index, name='index'),
    # path('new/<str:slug>', detail, name='detail'),
    path('', NewsList.as_view()),
    path('<int:pk>', NewsDetail.as_view(), name='news_detail'),
    # path('<int:pk>', NewsDetailView.as_view()),
    path('search/', Search.as_view(), name='search'),
    path('add/', NewsAdd.as_view(), name='news_create'),
    path('edit/<int:pk>', NewsEdit.as_view(), name='news_edit'),
    path('delete/<int:pk>', NewsDelete.as_view(), name='news_delete'),

    path('category/', CategoryView.as_view(), name='category'),
    # path('category/<int:pk>', subscribe_category, name='subscribe_category'),
    path('category/<int:pk>', add_subscribe, name='add_subscribe'),
    # path('<int:pk>/del_subscribe/', del_subscribe, name='del_subscribe'),

]




