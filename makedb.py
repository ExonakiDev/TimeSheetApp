import pymysql
from helpers import parse_sql
from boto.s3.connection import S3Connection

class MakeDB:
    def __init__(self):
        host = S3Connection(os.environ['server'])
        user = S3Connection(os.environ['SQLusername'])
        password = S3Connection(os.environ['SQLpassword'])

        stmts = parse_sql('final.sql')
        self.con = pymysql.connect(host=host, user=user, password=password,
                                   cursorclass=pymysql.cursors.DictCursor)
        self.cur = self.con.cursor()
        for stmt in stmts:
            self.cur.execute(stmt)
        self.con.commit()
