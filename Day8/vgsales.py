# data = {
#     'name': 'Wii Sports',
#     'year': 2006,
#     'platform': {
#         'id': 1,
#         'name': 'Wii'
#     },
#     'publisher': {
#         'id': 1,
#         'name': 'Nintendo'
#     },
#     'genre': {
#         'id': 1,
#         'name': 'Sports'
#     }
# }

# from file import function
from connect import init_connection

connection = init_connection()

vg_data = connection[0]
board = connection[1]
# E T L: Extract Transform Load
# Platform
for i in range(len(vg_data)):
    # extract data
    platform_name = vg_data[i]['Platform']

    # verify to add data
    board.execute(f'''
        SELECT name FROM vgsales.platform
        WHERE name = "{platform_name}"
    ''')

    # transform type of data
    # code here
    
    platform_found = board.fetchone()
    if platform_found == None:
        # load data
        board.execute(f'''
            INSERT INTO vgsales.platform(
                id,
                name
            ) VALUE (
                {i},
                '{platform_name}'
            )
        ''')

# Genre
for i in range(len(vg_data)):
    genre_name = vg_data[i]['Genre']
    board.execute(f'''
        SELECT name FROM vgsales.genre
        WHERE name = "{genre_name}"
    ''')

    genre_found = board.fetchone()
    if genre_found == None:
        board.execute(f'''
            INSERT INTO vgsales.genre(
                id,
                name
            ) VALUE (
                {i},
                '{genre_name}'
            )
        ''')

# Publisher
for i in range(len(vg_data)):
    publisher_name = vg_data[i]['Publisher']
    board.execute(f'''
        SELECT name FROM vgsales.publisher
        WHERE name = "{publisher_name}"
    ''')

    publisher_found = board.fetchone()
    if publisher_found == None:
        board.execute(f'''
            INSERT INTO vgsales.publisher(
                id,
                name
            ) VALUE (
                {i},
                "{publisher_name}"
            )
        ''')
        
client.commit()
# board.execute('CREATE DATABASE vgsales')

# board.execute('''
#     CREATE TABLE vgsales.platform(
#         id INT(11) PRIMARY KEY,
#         name VARCHAR(255)
#     )
# ''')

# board.execute('''
#     CREATE TABLE vgsales.video_game(
#         id iNT(11) PRIMARY KEY,
#         name VARCHAR(255),
#         year INT(11),
#         platform_id INT(11) REFERENCES vgsales.platform(id),
#         genre_id INT(11) REFERENCES vgsales.genre(id),
#         publisher_id INT(11) REFERENCES vgsales.publisher(id)
#     )
# ''')

# board.execute('''
#     CREATE TABLE vgsales.genre(
#         id INT(11) PRIMARY KEY,
#         name VARCHAR(255)
#     )
# ''')

# board.execute('''
#     CREATE TABLE vgsales.publisher(
#         id INT(11) PRIMARY KEY,
#         name VARCHAR(255)
#     )
# ''')

