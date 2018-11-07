from db_connection import DbConnection
from datetime import date, datetime, timedelta
import pandas as pd
import pdb


class DbTest(DbConnection):
  def test(self):
    pdb.set_trace()
