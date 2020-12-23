from django.urls import path, include
from . import views
from django.conf.urls import url

urlpatterns = [
    path('registration/', views.login, name='login'),
    url(r'^$', views.index2, name = 'index2'),
    url(r'^Instruction/$', views.Instruction, name='Instruction'),
    url(r'^Menu/$', views.Menu, name="Menu"),
    url(r'SearchAnime/$', views.SearchAnime.as_view(), name="SearchAnime"),
    path('SearchManga/', views.SearchManga, name="SearchManga"),
    path('Anime_Detail/', views.Anime_Detail, name='Anime_Detail'),
    path('Manga_Detail/', views.Manga_Detail, name='Manga_Detail'),
    path('Game/', views.Game, name='Game'),
]

urlpatterns += [
    path('accounts/', include('django.contrib.auth.urls')),
]
