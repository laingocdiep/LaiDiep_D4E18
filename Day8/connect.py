import pymysql
import pyexcel

def init_connection():
    vg_data = pyexcel.get_records(file_name = 'vgsales.csv')

    client = pymysql.connect(
        host = 'localhost',
        port = 3306,
        user = 'root',
        password = 'laingocdiep2002',
        cursorclass = pymysql.cursors.DictCursor    # turn data type into dictionary/ list of dictionaries
    )

    board = client.cursor()

    return [vg_data, board]
