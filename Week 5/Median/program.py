import numpy as np
import psycopg2

def column_stats(table, col):
  conn = psycopg2.connect(dbname='db', user='grok')
  cursor = conn.cursor()

  query = 'SELECT ' + col + ' FROM ' + table + ';'
  cursor.execute(query)
  column = np.array(cursor.fetchall())
  return np.mean(column), np.median(column)