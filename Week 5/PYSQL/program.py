import psycopg2

def select_all(table):

  conn = psycopg2.connect('dbname=db user=grok')
  cursor = conn.cursor()

  query = 'SELECT * FROM ' + table + ';'
  
  cursor.execute(query)
  records = cursor.fetchall()

  return records
