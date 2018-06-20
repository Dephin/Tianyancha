# coding:utf-8

import pymysql


class Mysql(object):
    def __init__(
        self,
        host="",
        user="",
        passwd="",
        db="",
        charset="utf8"
    ):
        self.host = host
        self.user = user
        self.passwd = passwd
        self.db = db
        self.charset = charset
        self.conn = pymysql.connect(
            host=host, user=user, passwd=passwd, db=db, charset=charset)
        self.cur = self.conn.cursor()

    def __del__(self):
        self.conn.close()

    def _reconnect(self):
        self.conn = MySQLdb.connect(\
            host=self.host, user=self.user, passwd=self.passwd, db=self.db, charset=self.charset)
        self.cur = self.conn.cursor()

    def _rebuild_cur(self):
        self.cur.close()
        self.cur = self.conn.cursor()

    def select(self, sql):
        self.cur.execute(sql)
        result = self.cur.fetchall()

        fields = self.cur.description
        field_info = []
        for field in fields:
            field_info.append(field[0])

        data = []
        data.append(field_info)
        for row in result:
            data.append(row)

        self._rebuild_cur()
        return data

    def insert(self, table, data):
        if len(data) > 1:
            nrows = len(data) - 1
            cols = ','.join(data[0])
            insert_sql = u"INSERT INTO %s(%s) VALUES" % (table, cols)

            try:
                for i in range(1, nrows+1):
                    vals = "('"
                    for j in range(0, len(data[i])):
                        if not isinstance(data[i][j], str):
                            vals += str(data[i][j]) + "','"
                        else:
                            vals += data[i][j] + "','"

                    vals = vals[:-2] + "),"
                    insert_sql += vals
                    # print("(%d/%d) data prepared" % (i, nrows))
                insert_sql = insert_sql[:-1] + ";"

                print("Inserting data...")
                self.cur.execute(insert_sql)
                self.conn.commit()
                self._rebuild_cur()
                print('Compeleted.')

            except Exception as e:
                self.conn.rollback()
                print("[ERROR] %s" % e)
                raise e
    def insert_ignore(self, table, data):
        if len(data) > 1:
            nrows = len(data) - 1
            cols = ','.join(data[0])
            insert_sql = u"INSERT IGNORE INTO %s(%s) VALUES" % (table, cols)

            try:
                for i in range(1, nrows+1):
                    vals = "('"
                    for j in range(0, len(data[i])):
                        if not isinstance(data[i][j], str):
                            vals += str(data[i][j]) + "','"
                        else:
                            vals += data[i][j] + "','"

                    vals = vals[:-2] + "),"
                    insert_sql += vals
                    # print("(%d/%d) data prepared" % (i, nrows))
                insert_sql = insert_sql[:-1] + ";"

                print("Inserting data...")
                self.cur.execute(insert_sql)
                self.conn.commit()
                self._rebuild_cur()
                print('Compeleted.')

            except Exception as e:
                self.conn.rollback()
                print("[ERROR] %s" % e)
                raise e


    def update(self, sql):
        try:
            print("Updating data...")
            self.cur.execute(sql)
            self.conn.commit()
            self._rebuild_cur()
            print('Compeleted.')
        except Exception as e:
            self.conn.rollback()
            print("[ERROR] %s" % e)
            raise e
