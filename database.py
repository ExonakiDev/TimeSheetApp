import pymysql

class Database:
    def __init__(self):
        host = "127.0.0.1"
        user = "root"
        password = "toor"
        db = "timesheet"
        self.con = pymysql.connect(host=host, user=user, password=password, db=db,
                                   cursorclass=pymysql.cursors.DictCursor)
        self.cur = self.con.cursor()

    # def list_products(self):
    #     self.cur.execute("SELECT PID, Name, Price FROM products WHERE PID='1'")
    #     result = self.cur.fetchall()
    #     return result

    def check_credentials(self, username):
        sql = "SELECT * from Login WHERE employee_id = %s"
        self.cur.execute(sql, username)
        rows = self.cur.fetchall()
        return rows

    # def close_cursor(self):
    #     self.con.close()
