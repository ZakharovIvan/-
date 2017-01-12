from . import db
import json

class BaseModel:

	table = ''

	def __init__(self, table):
		self.table = table

	def add(self, data, whereKey = 'name'):
		if db.select(self.table, 'count(*) as `count`', db.getWhere({whereKey: data[whereKey]})) [0]['count'] > 0:
			return False
		return db.insert(self.table, data)

	def get(self):
		return db.select(self.table)

	def update(self, data):
		id = data['id']; del data['id']
		return db.update(self.table, data, db.getWhere({'id': id}))

	def delByID(self, id):
		db.delete(self.table, where = "WHERE `id` = '" + str(id) + "'")
		return self
# 
class IndexModel (BaseModel):

	def get(self):
		return []
	
	def add(self, emptyData):
		with open('lab2films/static/db.json') as dataFile:
			data = json.load(dataFile)
			for self.table in data:
				for row in data[self.table]:
					super().add(row)
		return True
#
class ActorsModel (BaseModel):
	pass
#
class DirectorsModel (BaseModel):
	pass
#
class StudiosModel (BaseModel):
	pass

class FilmsModel (BaseModel):
	
	def get(self):
		fields = 'films.id as id, films.ganre as ganre, films.filmed_year as year, duration, \
				films.name as film, directors.name as director, films.country as country, \
				budget, studios.name as studio'
		tables = 'directors, studios, films'
		where = ' WHERE films.studio_id = studios.id and films.director_id = directors.id'
		films = db.select(tables, fields, where)

		fields = 'actors.name as actor, films.name as film'
		tables = 'production, films, actors'
		where = ' WHERE production.film_id = films.id and production.actor_id = actors.id'
		actors = db.select(tables, fields, where)

		for film in films:
			film['actors'] = [actor for actor in actors if film['film'] == actor['film']]
		return films

	def add(self, data):
		studio = db.select('studios', 'id', db.getWhere({'name': data['studio']}))
		director = db.select('directors', 'id', db.getWhere({'name': data['director']}))
		if len(studio) == 0 or len(director) == 0:
			return False
		del data['studio']; del data['director']
		data['studio_id'] = studio[0]['id']; data['director_id'] = director[0]['id']
		return super().add(data)
# 
class ProductionModel (BaseModel):
	
	def add(self, data):
		actor = db.select('actors', 'id', db.getWhere({'name': data['actor']}))
		if len(actor) == 0:
			return False
		del data['actor']; data['actor_id'] = actor[0]['id']
		if db.select(self.table, 'count(*) as `count`', db.getWhere(data)) [0]['count'] > 0:
			return False
		return db.insert(self.table, data)