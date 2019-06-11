import mysql.connector as connector
import config as cfg
from ApplicationModel import Application

class Repository(object):
    def connect(self):
        return connector.connect(host = cfg.mysql['host'], user = cfg.mysql['user'], 
                                       passwd = cfg.mysql['password'], database = cfg.mysql['db'], 
                                       auth_plugin='mysql_native_password')
    def get(self, query, params):
        try:
            result = []

            mySQLConnection = self.connect()
            cursor = mySQLConnection.cursor(prepared=True)
            cursor.execute(query, params)

            records = cursor.fetchall()
            for row in records:
                result.append(Application(row[0], row[1], row[2], row[3], row[4]))

            return result

        except connector.Error as error:
            print("Failed to get record from database: {}".format(error))

        finally:
            if (mySQLConnection.is_connected()):
                cursor.close()
                mySQLConnection.close()

    def update(self, spName, params):
        try:
            mySQLConnection = self.connect()
            cursor = mySQLConnection.cursor()

            cursor.callproc(spName, params)
            mySQLConnection.commit()

        except connector.Error as error:
            print("Failed to update record in database: {}".format(error))

        finally:
            if (mySQLConnection.is_connected()):
                cursor.close()
                mySQLConnection.close()

    def getApplicationById(self, id):
        sql_select_query = "SELECT Id, Name, Description, IsAdvertiserFriendly, StemmedDescription from Application WHERE Id = %s"
        result = self.get(sql_select_query, (id,))
        return next((a for a in result), None)

    def getApplicationByName(self, name):
        sql_select_query = "SELECT Id, Name, Description, IsAdvertiserFriendly, StemmedDescription from Application WHERE Name = %s"
        result = self.get(sql_select_query, (name,))
        return next((a for a in result), None)

    def search(self, name, unclassifiedOnly):
        if unclassifiedOnly:
            sql_select_query = "SELECT Id, Name, Description, NULL, StemmedDescription from Application WHERE Name LIKE %s AND IsAdvertiserFriendly IS NULL"
        else:
            sql_select_query = "SELECT Id, Name, Description, IsAdvertiserFriendly, StemmedDescription from Application WHERE Name LIKE %s"
        
        return self.get(sql_select_query, ("%" + name + "%",))

    def updateOrInsert(self, application):
        spName = "update_or_insert"
        return self.update(spName, (application.name, application.description, application.isAdvertizerFriendly,))