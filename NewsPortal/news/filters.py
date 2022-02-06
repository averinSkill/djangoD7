from django_filters import FilterSet, DateFromToRangeFilter
from .models import Post


# import datetime
# start_date = datetime.date(2005, 1, 1)
# end_date = datetime.date(2005, 3, 31)
# Entry.objects.filter(pub_date__range=(start_date, end_date))

# создаём фильтр
class PostFilter(FilterSet):
    d_time = DateFromToRangeFilter()

    class Meta:
        model = Post
        fields = ('author', 'd_time', 'type_post')  # поля, которые мы будем фильтровать (т. е. отбирать по каким-то критериям, имена берутся из моделей)
        # fields = {
        #     'author': [],
        #     'd_time': ['exact', 'year__lt'],
        # }  , 'category'

 # title = CharFilter('title',
 #                               label='Заголовок содержит:',
 #                               lookup_expr='icontains',
 #                               )
 #
 #    author = ModelMultipleChoiceFilter('author',
 #                               label='Автор:',
 #                               lookup_expr='exact',
 #                               queryset=Author.objects.all()
 #                               )
# PostFilter:
#     title = CharFilter(‘title’,
#                                label=‘Заголовок содержит:’,
#                                lookup_expr=‘icontains’,
#                                )
#     author = ModelMultipleChoiceFilter(‘author’,
#                                label=‘Автор:’,
#                                lookup_expr=‘exact’,
#                                queryset=Author.objects.all()
#                                )