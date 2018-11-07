
import pymysql.cursors
import os


class DbConnection():
  to_conn = None

  def get_connect(self):
    con = pymysql.connect(
        host=os.environ['DB_HOST'],
        user=os.environ['DB_USER'],
        password=os.environ['DB_PASSWORD'],
        db=os.environ['DB_DATABASE'],
        charset='utf8',
        cursorclass=pymysql.cursors.DictCursor
    )
    return con
