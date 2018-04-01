from django.urls import path
from . import views

app_name = 'app'

urlpatterns = [
    path('', views.PostArchive.as_view(), name='post_archive'),
    path('<int:year>/', views.PostYearArchive.as_view(), name='post_year_archive'),
    path('<int:year>/<int:month>/',views.PostMonthArchive.as_view(), name='post_month_archive'),
    path('<int:year>/<int:month>/<int:day>/',views.PostDayArchive.as_view(), name='post_day_archive'),
    path('<int:year>/<int:month>/<int:day>/<int:pk>/',views.PostDayDetail.as_view(), name='post_day_detail'),
    path('today/',views.PostTodayArchive.as_view(), name='post_today_archive'),
    path('<int:year>/week/<int:week>/',views.PostWeekArchive.as_view(), name='post_week_archive'),
]
