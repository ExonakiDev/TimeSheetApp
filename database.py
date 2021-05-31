import pymysql

class Database:
    def _init_(self):
        host = "127.0.0.1"
        user = "root"
        password = "Minusb@12"
        db = "demo"
        self.con = pymysql.connect(host=host, user=user, password=password, db=db,
                                   cursorclass=pymysql.cursors.DictCursor)
        self.cur = self.con.cursor()

    def list_products(self):
        self.cur.execute("SELECT PID, Name, Price FROM products WHERE PID='1'")
        result = self.cur.fetchall()
        return result
