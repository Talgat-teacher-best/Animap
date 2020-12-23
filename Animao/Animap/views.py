from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView
from .models import Anime, Manga
from django.views import generic
import random
igre = {
	'Code Geass' : 'Lelouch',
	'Berserk' : 'Gats',
	'Steins Gate' : 'Okabe',
	'91 days' : 'Avilio'
}
# Create your views here.
def SearchAnime(request):
	try:
		q = request.GET.get('q')
	except:
		q = None
	if q:
		result = Anime.objects.filter(title__icontains=q)
		context = {'query': q, 'result': result}
		template = 'result.html'
	else:
		template = 'search_anime.html'
		context = {}
	return render(request, template, context)
def SearchManga(request):
	try:
		q = request.GET.get('q')
	except:
		q = None
	if q:
		result = Manga.objects.filter(title__icontains=q)
		context = {'query': q, 'result': result}
		template = 'result2.html'
	else:
		template = 'search_manga.html'
		context = {}
	return render(request, template, context)

def login(request):
	return render(
        request,
        'registration/login.html')
	
def index2(request):
	return render(
        request,
        'index2.html')
	
def Instruction(request):
	return render(
		request, 
		'Instruction.html')
def Menu(request):
	return render(
		request, 
		'Menu.html')

def Anime_Detail(request):
	information = Anime.objects.all()
	return render(
        request,
        'Anime_Detail.html',
        context={'information': information,}
        )

def Manga_Detail(request):
	information = Manga.objects.all()
	return render(
        request,
        'Manga_Detail.html',
        context={'information': information,}
        )
def Game(request):
	score = 0
	title = ('Код Гиас', 'Берсерк', 'Тетрадь Смерти', 'Евангелион', 'Дневник Будущего', 'Стальной Алхимик')
	character = ('Лелуш Британский', 'Гатс', 'Ягами Лайт', 'Синдзи Икари', 'Юкитэру Амано', 'Эдвард Элрик')
	d = dict(zip(title, character))
	title, character = random.choice(list(d.items()))
	answer = request.POST.get('answer')
	if answer == character:
		msg = "Правильно ответил"
		score = score + 1
	elif answer != character:
		msg = "Adlet"
		score = 0
	return render(request, 'Game.html', {'msg' : msg, 'title' : title, 'score' : score})

