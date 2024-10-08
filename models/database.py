import mysql.connector

database = mysql.connector.connect(
        host = 'localhost',
        username = 'root',
        password = '',
        database = 'portfolio'
    )

def login(username, password):
    cursor = database.cursor()
    cursor.execute(f'SELECT * FROM login WHERE username = "{username}" AND password = "{password}"')
    user = cursor.fetchone()

    cursor.close()
    return user

user = login('dianAulia', 'Auliaku1')
if user : 
    return ... 
else :
    return



