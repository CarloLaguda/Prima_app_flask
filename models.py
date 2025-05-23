import pymysql

class DatabaseWrapper: #utiliziamo il db come database
    def __init__(self, host, port, password, user, database):
        self.db_config = {
            "host": host, 
            "port": port,
            "password": password,
            "user": user,
            "database": database,
            "cursorclass": pymysql.cursors.DictCursor
        }
        self.create_table()
    def connect(self):
        return pymysql.connect(**self.db_config)
    def execute_query(self, query, params=()): #Operazioni, insert, delete, create
        conn = self.connect()
        with conn.cursor() as cursor:
            cursor.execute(query, params)
            conn.commit() #Non ottengo nulla indietro
        conn.close()
    def fetch_query(self, query, params=()):
        conn = self.connect()
        with conn.cursor() as cursor:
            cursor.execute(query, params)
            result = cursor.fetchall()
        conn.close()
        return result #ritorna qualcola, select
    
    def create_table(self):
        self.execute_query(
            '''
            CREATE TABLE IF NOT EXISTS studenti(
                id  INT AUTO_INCREMENT PRIMARY KEY,
                nome VARCHAR(100) NOT NULL
            )
            '''
        )
    
    def aggiungi_studente(self, nome):
        self.execute_query('INSERT INTO studenti (nome) VALUES (%s)', (nome,))
    
    def get_studenti(self):
        return self.fetch_query('SELECT * FROM studenti')