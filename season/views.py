from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import *
from .utils import *




#def base_page(request):
#    drivers = Drivers.objects.all()
#    context = {
#        'drivers': drivers,
#        'menu': menu,
#        'title': 'Main Page',
#        'team_selected': 0
#    }
#    return render(request, 'season/base_page.html', context=context)


class DriverHome(DataMixin, ListView):
    model = Drivers
    template_name = 'season/base_page.html'
    context_object_name = 'drivers'
    #extra_context = {'title': 'Main Page'}

    # Создаёт динамический контекст
    def get_context_data(self, *, object_list=None, **kwargs):
        # Получаем контекст который у нас уже существует (drivers)
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Главная страница")
        context = dict(list(context.items()) + list(c_def.items()))
        return context

    # Возвращает то, что должна быть прочитано из Drivers
    def get_queryset(self):
        return Drivers.objects.filter(is_published=True)


class ShowPost(DetailView):
    model = Drivers
    template_name = "season/driver.html"
    slug_url_kwarg = 'driver_slug'   # чтобы из urls брать slug
    #pk_url_kwarg =
    context_object_name = 'drivers'

    def get_context_data(self, *, object_list=None, **kwargs):
        # Получаем контекст который у нас уже существует (drivers)
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title=context['drivers'])
        return dict(list(context.items()) + list(c_def.items()))

#def show_post(request, driver_slug):
#    drivers = get_object_or_404(Drivers, slug=driver_slug)
#    context = {
#        'drivers': drivers,
#        'menu': menu,
#        'title': drivers.name,
#        'team_selected': drivers.teams_id,
#    }
#    print(context)
#    return render(request, 'season/driver.html', context=context)


#def show_team(request, tm_slug):
#    team = Teams.objects.get(slug=tm_slug)
#    drivers = Drivers.objects.filter(teams_id=team.pk)
#    context = {
#        'drivers': drivers,
#        'menu': menu,
#        'title': team.name,
#        'team_selected': team.pk
#    }
#    return render(request, 'season/base_page.html', context=context)


class DriversTeams(DataMixin, ListView):
    model = Drivers
    template_name = 'season/base_page.html'
    context_object_name = 'drivers'
    allow_empty = False # Если страница не найдена то 404

    def get_queryset(self):
        return Drivers.objects.filter(teams__slug=self.kwargs['tm_slug'], is_published=True)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Команда - ' + str(context['drivers'][0].teams),
                                      team_selected=context['drivers'][0].teams_id)
        return dict(list(context.items()) + list(c_def.items()))


def about(request):
    return HttpResponse("About")


class AddPage(LoginRequiredMixin, DataMixin, CreateView):
    form_class = AddPostForm
    template_name = 'season/addpage.html'
    # Если в модели нет get_url
    success_url = reverse_lazy('home') # указываем адрес маршрута, куда нужно перенаправится, когда добавляем статью
    #login_url = '/admin/'  # указывает адрес для неавторизованных (так делать в джанго некрасиво - открыто писать url)
    login_url = reverse_lazy('home')
    raise_exception = True # Генерирует страницу 403 "Доступ запрещён"

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Добавить гонщика")
        return dict(list(context.items()) + list(c_def.items()))

#def addpage(request):
#    if request.method == 'POST':
#        form = AddPostForm(request.POST, request.FILES)
#        if form.is_valid():
#            form.save()
#            return redirect('home')
#    else:
#        form = AddPostForm()
#    return render(request, 'season/addpage.html', {'form': form, 'menu': menu, 'title': 'Add new page'})


def contact(request):
    return HttpResponse("Обратная связь")


def login(request):
    return HttpResponse("Авторизация")


def pageNotFound(request, exception):
    return HttpResponse("Стараца не найдена")
