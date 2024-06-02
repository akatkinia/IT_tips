from django.http import HttpResponse, HttpResponseNotFound, Http404, HttpResponseRedirect, HttpResponsePermanentRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from django.template.loader import render_to_string


menu = ["О сайте!!", "Добавить статью", "Обратная связь", "Войти"]

menu2 = [
    {"title": "О сайте", "url_name": "about"},
    {"title": "Добавить статью", "url_name": "add_page"},
    {"title": "Обратная связь", "url_name": "contact"},
    {"title": "Войти", "url_name": "login"},
]


data_db = [
    # {'id': 1, 'title': 'Анджелина Джоли', 'content': 'Биография Анджелины Джоли', 'is_published': True},
    {'id': 1, 'title': 'Анджелина Джоли', 'content': '''<h1>Анджелина Джоли</h1> (англ. Angelina Jolie[7], при рождении Войт (англ. Voight), ранее Джоли Питт (англ. Jolie Pitt); род. 4 июня 1975, Лос-Анджелес, Калифорния, США) — американская актриса кино, телевидения и озвучивания, кинорежиссёр, сценаристка, продюсер, фотомодель, посол доброй воли ООН.
Обладательница премии «Оскар», трёх премий «Золотой глобус» (первая актриса в истории, три года подряд выигравшая премию) и двух «Премий Гильдии киноактёров США».''',
     'is_published': True},
    {'id': 2, 'title': 'Марго Робби', 'content': 'Биография Марго Робби', 'is_published': False},
    {'id': 3, 'title': 'Джулия Робертс', 'content': 'Биография Джулия Робертс', 'is_published': True},
]

cats_db = [
    {'id': 1, 'name': 'Актрисы'},
    {'id': 2, 'name': 'Певицы'},
    {'id': 3, 'name': 'Спортсменки'},
]

class MyClass:
    def __init__(self, a, b):
        self.a = a
        self.b = b

# Create your views here.

def index(request): # request - ссы лка на специальный класс HttpRequest и содержит информацию о запросе - сессии, куках и тд
    data = {'title': 'главная страница',
            'menu': menu2,

            'posts': data_db,
            'cat_selected': 0,
            }
    # return HttpResponse('Страница приложения women') # возвращает экземпляр класса HttpResponse, который автоматически формирует заголовок ответа

    # t = render_to_string('women/index.html') # рендер из нашего темплейта index.html
    # return HttpResponse(t) # возвращает отрендеренную html страницу
    # либо можно воспользоваться одной функцией render вместо двух строк выше:
    return render(request=request, template_name='women/index.html', context=data)

def about(request):
    return render(request, 'women/about.html', context={'title': 'О сайте (template)', 'menu2': menu2, })

def categories(request, cat_id):
    return HttpResponse(f'<h1>Статьи по категориям</h1><p>id: {cat_id}</p>')

def categories_by_slug(request, cat_slug):
    if request.GET:
        print(request.GET)
    return HttpResponse(f'<h1>Статьи по категориям</h1><p>slug: {cat_slug}</p>')

def archive(request, year):
    if year > 2024:
        # raise Http404()
        # return redirect('/', permanent=True) # можно передать часть url
        # return redirect(index, permanent=True) # можно передать часть функцию представления
        # return redirect('home', permanent=True) # можно передать именование url (задаётся в urls.py)
        # return redirect('cats', 'music', permanent=True) # можно передать именование url и параметр который передаём в запросе - получится так http://127.0.0.1:8000/cats/music/
        # либо это можно сделать через функцию reverse:
        uri = reverse('cats', args=['sport',]) # функция reverse используется для вычисления url адресов (должна передаваться коллекция)
        # return redirect(uri)
        # return HttpResponsePermanentRedirect(uri) # для 301 (эти классы можно использовать вместо функции redirect)
        return HttpResponseRedirect(uri) # для 302 (эти классы можно использовать вместо функции redirect)


    return HttpResponse(f'<h1>Архив по годам</h1><p>{year}</p>')

def show_post(request, post_id):
    return HttpResponse(f'Отображение статьи с id = {post_id}')

def addpage(request):
    return HttpResponse(f'Добавление статьи')

def contact(request):
    return HttpResponse(f'Обратная связь')

def login(request):
    return HttpResponse(f'Авторизация')

def show_category(request, cat_id):
    # return index(request)
    data = {'title': 'Отображение по рубрикам',
            'menu': menu2,

            'posts': data_db,
            'cat_selected': cat_id,
            }
    return render(request=request, template_name='women/index.html', context=data)
def page_not_found(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')
