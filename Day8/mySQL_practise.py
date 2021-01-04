import pymysql

client = pymysql.connect(
    host = 'localhost',
    port = 3306,
    user = 'root',
    password = 'laingocdiep2002',
    cursorclass = pymysql.cursors.DictCursor    # turn data type into dictionary/ list of dictionaries
)

board = client.cursor()

board.execute('SELECT * FROM dan_tri.headline')

# get all/one data from the lastest code 
data = board.fetchall()
# data = board.fetchone()

# for i in range(len(data)):
#     print(f"{i + 1}. {data[i]['title']}")

