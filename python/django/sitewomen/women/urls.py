from django.urls import path, re_path, register_converter
from . import views
from . import converters

register_converter(converters.FourDigitYearConverter, "year4")

urlpatterns = [
    path('', views.index, name='home'), # суффикс и функция представления (в нашем случае index, которую описали в women/views.py)
    path('about/', views.about, name='about'),
    # path('cats/', views.categories),
    path('cats/<int:cat_id>/', views.categories, name='cats_id'),
    path('cats/<slug:cat_slug>/', views.categories_by_slug, name='cats'),
    # re_path(r"^archive/(?P<year>[0-9]{4})/", views.archive), # тоже что и path, но с возможностью использования regex
    path('archive/<year4:year>/', views.archive, name='archive'),  # тоже что и path, но с возможностью использования regex

    path('post/<int:post_id>>', views.show_post, name='post'),
    path('addpage/', views.addpage, name='add_page'),
    path('contact/', views.contact, name='contact'),
    path('login/', views.login, name='login'),
    path('category/<int:cat_id>', views.show_category, name='category')
]
