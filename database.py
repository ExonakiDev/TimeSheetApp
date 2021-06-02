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

    def check_credentials_from_email(self, email):
        sql = "SELECT * from Login WHERE email_id = %s"
        self.cur.execute(sql, email)
        rows = self.cur.fetchall()
        return rows

    def check_exist(self, email):
        sql = "SELECT * from Login WHERE email_id = %s"
        self.cur.execute(sql, email.lower())
        rows = self.cur.fetchall()
        return rows

    def insert_user(self, email, password):
        sql = "INSERT INTO Login (email_id, user_password) VALUES (%s, %s)"
        self.cur.execute(sql, (email.lower(), password))
        self.con.commit()

    def close_cursor(self):
        self.con.close()