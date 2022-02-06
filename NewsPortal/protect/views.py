from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from news.views import Category


class IndexView(LoginRequiredMixin, TemplateView):
    template_name = 'protect/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['is_not_authors'] = not self.request.user.groups.filter(name='authors').exists()
        context['category'] = Category.objects.all()
        context['user'] = self.request.user
        context['user_id'] = self.request.user.id
        # sub_category - это все категории подписчика!!
        context['sub_category'] = Category.objects.all().filter(subscribers=self.request.user.id)

        # print(f'''USER:  "{context['user']}", user_id: "{user_id}"''')
        #
        # qs = Category.subscribers
        # print('QS= ', qs)
        # print('ПОДПИСАН НА КАТЕГОРИЮ ? ', qs.filter(username=context['user']).exists())
        print(context)
        return context

