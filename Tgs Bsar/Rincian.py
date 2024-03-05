# Nama File: Matakuliah.py
from db import DBConnection as mydb

class Rincian:

    def __init__(self):
        self.__id = None
        self.__noparkir = None
        self.__jeniskendaraan = None
        self.__jammasuk = None
        self.__jamkeluar = None
        self.__totalbiaya = None
        self.conn = None
        self.affected = None
        self.result = None

    @property
    def id(self):
        return self.__id

    @property
    def noparkir(self):
        return self.__noparkir

    @noparkir.setter
    def noparkir(self, value):
        self.__noparkir = value

    @property
    def jeniskendaraan(self):
        return self.__jeniskendaraan

    @jeniskendaraan.setter
    def jeniskendaraan(self, value):
        self.__jeniskendaraan = value

    @property
    def jammasuk(self):
        return self.__jammasuk

    @jammasuk.setter
    def jammasuk(self, value):
        self.__jammasuk = value
    
    @property
    def jamkeluar(self):
        return self.__jamkeluar
    
    @jamkeluar.setter
    def jamkeluar(self, value):
        self.__jamkeluar = value
    
    @property
    def totalbiaya(self):
        return self.__totalbiaya
    
    @totalbiaya.setter
    def totalbiaya(self, value):
        self.__totalbiaya = value
        

    def simpan(self):
        self.conn = mydb()
        val = (self.__noparkir, self.__jeniskendaraan, self.__jammasuk, self.__jamkeluar, self.__totalbiaya)
        sql = "INSERT INTO Rincian (noparkir, jeniskendaraan, jammasuk, jamkeluar, totalbiaya) VALUES (%s, %s, %s)"
        self.affected = self.conn.insert(sql, val)
        self.conn.disconnect()
        return self.affected

    def update(self, id):
        self.conn = mydb()
        val = (self.__noparkir, self.__jeniskendaraan, self.__jammasuk, self.__jamkeluar, self.__totalbiaya, id)
        sql = "UPDATE rincian SET noparkir = %s, jeniskendaraan = %s, jammasuk = %s, jamkeluar = %s, totalbiaya = %s WHERE id = %s"
        self.affected = self.conn.update(sql, val)
        self.conn.disconnect()
        return self.affected

    def updateBy(self, ):
        self.conn = mydb()
        val = (self.__noparkir, self.__jeniskendaraan, self.__jammasuk, self.__jamkeluar, self.__totalbiaya)
        sql = "UPDATE rincian SET noparkir = %s, jeniskendaraan = %s, jammasuk = %s, jamkeluar = %s, totalbiaya = %s WHERE nip = %s"
        self.affected = self.conn.update(sql, val)
        self.conn.disconnect()
        return self.affected

    def delete(self, id):
        self.conn = mydb()
        sql = "DELETE FROM rincian WHERE id = %s"
        self.affected = self.conn.delete(sql, (id,))
        self.conn.disconnect()
        return self.affected

    def delete(self, ):
        self.conn = mydb()
        sql = "DELETE FROM rincian WHERE = %s"
        self.affected = self.conn.delete(sql)
        self.conn.disconnect()
        return self.affected

    def getById(self, id):
        self.conn = mydb()
        sql = "SELECT * FROM rincian WHERE id = %s"
        self.result = self.conn.findOne(sql, (id,))
        self.__noparkir = self.result[1]
        self.__jeniskendaraan = self.result[2]
        self.__jammasuk = self.result[3]
        self.__jamkeluar = self.result[4]
        self.__totalbiaya = self.result[5]
        self.conn.disconnect()
        return self.result

    def getBy(self):
        a = str()
        b = a.strip()
        self.conn = mydb()
        sql = "SELECT * FROM rincian WHERE = %s"
        self.result = self.conn.findOne(sql, (b,))
        if self.result is not None:
            self.__noparkir = self.result[1]
            self.__jeniskendaraan = self.result[2]
            self.__jammasuk = self.result[3]
            self.__jamkeluar = self.result[4]
            self.__totalbiaya = self.result[5]
            self.affected = self.conn.cursor.rowcount
        else:
            self.__noparkir = ''
            self.__jeniskendaraan = ''
            self.__jammasuk = ''
            self.__jamkeluar = ''
            self.__totalbiaya = ''
            self.affected = 0
        self.conn.disconnect()
        return self.result
    
    def getAllData(self):
        self.conn = mydb()
        sql = "SELECT * FROM rincian"
        self.result = self.conn.findAll(sql)
        return self.result