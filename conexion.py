import sqlite3 
import json

class conex:
    def __init__(self):
        self.conn= sqlite3.connect('appdatabase.sqlite')
    
    def db_conexion(self):    
        try:
            self.conn = sqlite3.connect('appdatabase.sqlite')
            self.cursor= self.conn.cursor()
        except sqlite3.Error as e:
            print(e)
        return self.conn 
    """"busqueda url"""
    def get_news(self):
        dbase = self.conn.execute("SELECT * FROM busquedaNew")
        busquedasNews = [
            dict(id=row[0], url=row[1])
            for row in dbase.fetchall()
        ]
        if busquedasNews is not None:        
            return busquedasNews
    def get_new(self, id):
        self.id=id
        new= None
        cursor=self.conn.cursor() 
        cursor.execute('SELECT * FROM busquedaNew WHERE id=? ', (self.id,))        
        rows = cursor.fetchall()
        for r in rows:
            new = r 
        if new is not None:
            return new, 200
        else: 
            return "error", 404
    def delete_new(self, id):
        self.id= id
        cursor=self.conn.cursor() 
        cursor.execute('DELETE FROM busquedaNew WHERE id=? ', (self.id,))        
        self.conn.commit()
        return "new deleted"
    def post_news(self, new_url):
        self.new_url = new_url
        cursor = self.conn.cursor()
        print(self.new_url)
        cursor.execute('INSERT INTO busquedaNew (url) VALUES("'+self.new_url+'")')
        self.conn.commit()
    def put_url(self, id, url):
        self.id= id 
        self.url = url 
        cursor = self.conn.cursor()                
        print(self.url, self.id)              
        cursor.execute('UPDATE busquedaNew SET url=? WHERE id=?', (self.url, self.id) )
        self.conn.commit()
    """usuario"""
    def get_users(self):
        dbase = self.conn.execute("SELECT * FROM usuario")
        busquedasUsers = [
            dict(id=row[0], name=row[1], email=row[2], password=row[3])
            for row in dbase.fetchall()
        ]
        if busquedasUsers is not None:        
            return busquedasUsers
    def get_user(self,id):
        self.id=id
        user=None
        cursor=self.conn.cursor()
        cursor.execute('SELECT * FROM usuario WHERE id=? ', (self.id,))
        rows = cursor.fetchall() 
        for r in rows:
            user = r 
        if user is not None:
            return user, 200
        else: 
            return "error: no encontrado", 404
    def delete_user(self,id):
        self.id= id
        cursor=self.conn.cursor() 
        cursor.execute('DELETE FROM usuario WHERE id=? ', (self.id,))        
        self.conn.commit()
        return "usuario deleted"
    def post_user(self, name, email, password):
        self.name = name
        self.email = email
        self.password =password
        cursor = self.conn.cursor() 
        cursor.execute('INSERT INTO usuario (name, email, password) VALUES("'+self.name+'", "'+self.email+'","'+self.password+'")')
        self.conn.commit()
        return f"usuario con id: {cursor.lastrowid} creado", 201





