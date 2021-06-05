import pymysql
from helpers import parse_sql

class MakeDB:
    def __init__(self):
        host = "127.0.0.1"
        user = "root"
        password = "toor"

        stmts = parse_sql('final.sql')
        self.con = pymysql.connect(host=host, user=user, password=password,
                                   cursorclass=pymysql.cursors.DictCursor)
        self.cur = self.con.cursor()
        for stmt in stmts:
            self.cur.execute(stmt)
        self.con.commit()
