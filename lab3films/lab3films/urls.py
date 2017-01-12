from django.conf.urls import url
from .controllers import *

urlpatterns = [

	url(r'^$', IndexController().get),

	url(r'actors/get', ActorsController().get),
	url(r'actors/add', ActorsController().add),
	url(r'actors/upd', ActorsController().update),
	url(r'actors/delete', ActorsController().delete),

	url(r'studios/get', StudiosController().get),
	url(r'studios/add', StudiosController().add),
	url(r'studios/upd', StudiosController().update),
	url(r'studios/delete', StudiosController().delete),

	url(r'directors/get', DirectorsController().get),
	url(r'directors/add', DirectorsController().add),
	url(r'directors/upd', DirectorsController().update),
	url(r'directors/delete', DirectorsController().delete),

	url(r'films/get', FilmsController().get),
	url(r'films/add', FilmsController().add),
	url(r'films/delete', FilmsController().delete),

	url(r'film/add/actor', ProductionController().add),

]
