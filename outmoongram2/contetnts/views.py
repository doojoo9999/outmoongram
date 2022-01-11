from django.views.generic.base import TemplateView

@method_decorator(login_required, name='dispatch')
class HomeView(TemplateView):
    template_name = 'home.html'
