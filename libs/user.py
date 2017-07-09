class User:
    def __init__(self,):
        self.__id = -1
        self.email = ""
        self.username = ""
        self.__hashed_password = ""

    @property
    def id(self):
        return self.__id

    @property
    def hashed_password(self):
        return self.__hashed_password

    def set_password(self, password, salt ):
        self.__hashed_password = password + salt

    def save_to_db(self, cursor):
        if self.__id == -1:
            sql='INSERT INTO User(email, username, hashed_password) VALUES (%s, %s, %s);'
            params = (self.email, self.username,self.__hashed_password)
            cursor.execute(sql, params)
            self.__id = cursor.lastrowid
            return True
        return False