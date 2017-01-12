from .views import View
from django.http import HttpResponse, HttpResponseRedirect
from .models import *

class AbstractController:

	table = ''
	model = ''

	def get(self, request):
		return View(self.table + '.html', request, self.model().get()).renderPage()

	def add(self, request):
		if self.model(self.table).add(request.GET.copy()):
			return HttpResponse(1)
		return HttpResponse(0)

	def update(self, request):
		self.model.objects.filter(id = request.GET['id']).update(name = request.GET['name'],
																country = request.GET['country'],
																ganre = request.GET['ganre'])
		return HttpResponseRedirect('/' + self.table + '/get')

	def delete(self, request):
		self.model.objects.get(id = request.GET['id']).delete()
		return HttpResponseRedirect('/' + self.table + '/get')

class IndexController (AbstractController):

	def get(self, request):
		return View('index.html', request, []).renderPage()

class ActorsController (AbstractController):

	def __init__(self):
		self.table = 'actors'
		self.model = Actors

class DirectorsController (AbstractController):

	def __init__(self):
		self.table = 'directors'
		self.model = Directors

class StudiosController (AbstractController):

	def __init__(self):
		self.table = 'studios'
		self.model = Studios

	def update(self, request):
		return HttpResponseRedirect('/' + self.table + '/get')

	def update(self, request):
		self.model.objects.filter(id = request.GET['id']).update(name = request.GET['name'],
																country = request.GET['country'])
		return HttpResponseRedirect('/' + self.table + '/get')

class FilmsController (AbstractController):

	def __init__(self):
		self.table = 'films'
		self.model = Films

class ProductionController (AbstractController):

	def __init__(self):
		self.table = 'production'
		self.model = Production