from django.views import generic
from .models import Post


class PostArchive(generic.ArchiveIndexView):
    """全ての記事と、記事が所属する年を返すビュー"""
    model = Post
    date_field = 'pub_date'


class PostYearArchive(generic.YearArchiveView):
    """ある年の全ての記事と、記事が所属する月を返すビュー"""
    model = Post
    date_field = 'pub_date'
    make_object_list = True


class PostMonthArchive(generic.MonthArchiveView):
    """ある月の全ての記事と、記事が所属する日を返すビュー"""
    model = Post
    date_field = 'pub_date'
    make_object_list = True
    month_format = '%m'


class PostDayArchive(generic.DayArchiveView):
    """ある日の全ての記事を返すビュー"""
    model = Post
    date_field = 'pub_date'
    month_format = '%m'


class PostDayDetail(generic.DateDetailView):
    """詳細ページに、日付情報でアクセスさせる

    デフォルトでは、未来の記事にはアクセスできない
    """
    model = Post
    date_field = 'pub_date'
    month_format = '%m'


class PostTodayArchive(generic.TodayArchiveView):
    """今日の全ての記事を返すビュー"""
    model = Post
    date_field = 'pub_date'


class PostWeekArchive(generic.WeekArchiveView):
    """ある週の全ての記事を返すビュー"""
    model = Post
    date_field = 'pub_date'
    make_object_list = True
    week_format = '%W'
