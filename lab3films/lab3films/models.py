from django.db import models, IntegrityError
from django.core.exceptions import ObjectDoesNotExist

class Actors (models.Model):
	
	id = models.IntegerField(primary_key = True)
	name = models.CharField(max_length = 100)
	country = models.CharField(max_length = 100)
	birth_year = models.IntegerField()
	ganre = models.CharField(max_length = 100)
	language = models.CharField(max_length = 100)

	class Meta:
		db_table = 'actors'

	def get(self):
		return Actors.objects.all()

	def add(self, data):
		Actors(name = data['name'],
				country = data['country'],
				birth_year = data['birth_year'],
				ganre = data['ganre'],
				language = data['language']).save()
		return Actors.objects.latest('id')

#
class Directors (models.Model):
	
	id = models.IntegerField(primary_key = True)
	name = models.CharField(max_length = 100)
	country = models.CharField(max_length = 100)
	birth_year = models.IntegerField()
	ganre = models.CharField(max_length = 100)

	class Meta:
		db_table = 'directors'

	def get(self):
		return Directors.objects.all()

	def add(self, data):
		Directors(name = data['name'],
					country = data['country'],
					birth_year = data['birth_year'],
					ganre = data['ganre']).save()
		return Directors.objects.latest('id')
#
class Studios (models.Model):
	
	id = models.IntegerField(primary_key = True)
	name = models.CharField(max_length = 100)
	country = models.CharField(max_length = 100)
	creation_year = models.IntegerField()

	class Meta:
		db_table = 'studios'

	def get(self):
		return Studios.objects.all()

	def add(self, data):
		Studios(name = data['name'],
				country = data['country'],
				creation_year = data['creation_year']).save()
		return Studios.objects.latest('id')

class Films (models.Model):
	
	id = models.IntegerField(primary_key = True)
	name = models.CharField(max_length = 100)
	country = models.CharField(max_length = 100)
	filmed_year = models.IntegerField()
	ganre = models.CharField(max_length = 100)
	duration = models.CharField(max_length = 100)
	budget = models.CharField(max_length = 100)
	director = models.ForeignKey(Directors, on_delete = models.CASCADE)
	studio = models.ForeignKey(Studios, on_delete = models.CASCADE)

	class Meta:
		db_table = 'films'

	def get(self):
		res = []
		films = Films.objects.all()
		actors = Production.objects.all()
		for film in films:
			res.append({'film': film,
						'actors': [actor.actor for actor in actors if film.id == actor.film.id]})
		return res

	def add(self, data):
		try:
			Films(name = data['name'],
				country = data['country'],
				filmed_year = data['filmed_year'],
				ganre = data['ganre'],
				duration = data['duration'],
				budget = data['budget'],
				director = Directors.objects.get(name = data['director']),
				studio = Studios.objects.get(name = data['studio'])).save()
			return Films.objects.latest('id')
		except ObjectDoesNotExist:
			return False	
# 
class Production (models.Model):
	
	id = models.IntegerField(primary_key = True)
	film = models.ForeignKey(Films, on_delete = models.CASCADE)
	actor = models.ForeignKey(Actors, on_delete = models.CASCADE)

	class Meta:
		db_table = 'production'

	def add(self, data):
		try:
			Production(film_id = data['film_id'],
						actor = Actors.objects.get(name = data['actor'])).save()
			return Production.objects.latest('id')
		except ObjectDoesNotExist:
			return False
		except IntegrityError:
			return False