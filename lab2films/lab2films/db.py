import MySQLdb as mdb
import MySQLdb.cursors

def getConnect():
	return mdb.connect(host = '127.0.0.1',
						user = 'vv',
						passwd = '149713vv',
						db = 'lab2films',
						cursorclass = MySQLdb.cursors.DictCursor)

def insert(table, fieldsValues):
	colnames = ''; colValues = ''
	for key in fieldsValues:
		colnames += '`' + key + '`, '
		colValues += "'" + str(fieldsValues[key]) + "', "
	connect = getConnect()
	cursor = connect.cursor()
	cursor.execute('SET NAMES `utf8`')
	cursor.execute('INSERT INTO `' + table + '` (' + colnames[:-2] + ') VALUES (' + colValues[:-2] + ')')
	cursor.close()
	closeConnection(connect)
	return cursor.lastrowid

def select(table, fields = '*', where = '', group = ''):
	connect = getConnect()
	cursor = connect.cursor()
	cursor.execute('SET NAMES `utf8`')
	# print('SELECT ' + fields + ' FROM ' + table + where)
	cursor.execute('SELECT ' + fields + ' FROM ' + table + where + group)
	res = cursor.fetchall()
	cursor.close()
	closeConnection(connect)
	return res

def getWhere(whereParams):
	whereStr = ' WHERE '
	for key in whereParams:
		whereStr += '`' + str(key) + '`' + " = '" + str(whereParams[key]) + "' AND "
	return whereStr[:-4]

def update(table, fieldsValues, where = ''):
	newValues = ''
	for key in fieldsValues:
		newValues += '`' + key + '`' + " = '" + str(fieldsValues[key]) + "', "
	connect = getConnect()
	cursor = connect.cursor()
	cursor.execute('SET NAMES `utf8`')
	cursor.execute('UPDATE ' + table + ' SET ' + newValues[:-2] + where)
	cursor.close()
	closeConnection(connect)
	return cursor.rowcount

def delete(table, where = ''):
	connect = getConnect()
	cursor = connect.cursor()
	cursor.execute('SET NAMES `utf8`')
	cursor.execute('DELETE FROM `' + table + '`' + where)
	cursor.close()
	closeConnection(connect)

def closeConnection(connection):
	connection.commit()
	connection.close()