import pymysql

client = pymysql.connect(
    host = 'localhost',
    port = 3306,     # so mac dinh tu server
    user = 'root',
    password = 'laingocdiep2002'
)

# create a board to run code in mysql
board = client.cursor()

# send and run code inside execute() in mysql
# as we run these code only once, we turn them into a function, call it once to run, then delete it
def create_db():
    board.execute('CREATE DATABASE `from_python`')

def create_table():
    board.execute('''
        CREATE TABLE `from_python`.`table1`(
            customer varchar(255),
            phone varchar(255),
            product varchar(255),
            quantity int(11),
            price decimal(19,2)
        )
    ''')

def insert_row():
    board.execute('''
        INSERT INTO `from_python`.`table1`(
            customer,
            phone,
            product,
            quantity,
            price
        ) VALUE (
            'Doris',
            '0358606213',
            'evermore merch',
            1,
            45.00
        )
    ''')

insert_row()







# commit all code of insert to add data to table
client.commit()