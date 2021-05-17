from django.urls import path
from ..views import views
urlpatterns = [
    path('', views.index, name='index'),
    path('all_university/', views.all_university, name='all_university'),
    path('dangnhap/',views.dangnhap, name="dangnhap"),
    path('dangki/',views.dangki, name="dangki"),
    path('dangxuat/',views.dangxuat, name="dangxuat"),
    path('detail_university/<int:truongID>', views.detail_university, name='detail_university'),
    # 
    path('vote', views.user_vote, name='user_vote'),
    path('love', views.user_love, name='user_love'),
    path('my_favorite', views.my_favorite, name='my_favorite'),
    path('test', views.test, name='test'),
]