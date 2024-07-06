# imports ________________________________________________________
# psycopg2
import psycopg2
# Error
from psycopg2 import Error

# connection settings ____________________________________________

# CREATE TABLE movies (id BIGINT PRIMARY KEY, name TEXT, quality BIGINT, size BIGINT, views BIGINT, mes
# sage_id TEXT);

# values
# database name
database = 'postgres'
# username
user = 'postgres'
# password
password = 'postgres'
# host
host = 'localhost'
# port
port = '5432'


# functions ______________________________________________________

# function for getting movie
def get_movie(movie_id: int) -> dict[int, str, int, int, int, str]:
    try:
        # connection
        conn = psycopg2.connect(
            host=host,
            database=database,
            port=port,
            user=user,
            password=password,
        )

        # cursor
        cur = conn.cursor()

        # query
        query = f"SELECT id, name, quality, size, views, message_id FROM movies WHERE id = %s;"
        # executing query
        cur.execute(query, (movie_id,))
        # fetching data
        data = cur.fetchall()[0]

        movie = {'id': data[0], 'name': data[1], 'quality': data[2], 'size': data[3], 'views': data[4],
                 'message_id': data[5]}

        # committing connection
        conn.commit()
        # closing cursor
        cur.close()
        # closing connection
        conn.close()

        # returning data
        return movie

    # handling error
    except Error as error:
        print('Error:', error)


# function for checking movie
def check_movie(movie_id: int):
    try:
        # connection
        conn = psycopg2.connect(
            host=host,
            database=database,
            port=port,
            user=user,
            password=password,
        )

        # cursor
        cur = conn.cursor()

        # query
        query = f"SELECT id FROM movies WHERE id = %s;"
        # executing query
        cur.execute(query, (movie_id,))
        # fetching data
        data = cur.fetchone()

        # committing connection
        conn.commit()
        # closing cursor
        cur.close()
        # closing connection
        conn.close()

        # returning boolean
        if type(data) is tuple:
            return bool(data[0])
        return bool(data)

    # handling error
    except Error as error:
        print('Error:', error)


# function for adding movie
def add_movie_db(id: int, name: str, quality: int, size: int, message_id: str, views: int = 0) -> None:
    try:
        # connection
        conn = psycopg2.connect(
            host=host,
            database=database,
            port=port,
            user=user,
            password=password,
        )

        # cursor
        cur = conn.cursor()

        # query
        query = f"INSERT INTO movies (id, name, quality, size, views, message_id) VALUES (%s, %s, %s, %s, %s, %s);"
        # executing query
        cur.execute(query, (id, name, quality, size, views, message_id))

        # committing connection
        conn.commit()
        # closing cursor
        cur.close()
        # closing connection
        conn.close()

    # handling error
    except Error as error:
        print('Error:', error)


# function for getting movie id
def get_movie_id(movie_name: str) -> int:
    try:
        # connection
        conn = psycopg2.connect(
            host=host,
            database=database,
            port=port,
            user=user,
            password=password,
        )

        # cursor
        cur = conn.cursor()

        # query
        query = f"SELECT id FROM movies WHERE name = %s;"
        # executing query
        cur.execute(query, (movie_name,))
        # fetching data
        data = cur.fetchone()[0]

        # committing connection
        conn.commit()
        # closing cursor
        cur.close()
        # closing connection
        conn.close()

        # returning data
        return data

    # handling error
    except Error as error:
        print('Error:', error)


# function for checking movies
def check_movies() -> bool:
    try:
        # connection
        conn = psycopg2.connect(
            host=host,
            database=database,
            port=port,
            user=user,
            password=password,
        )

        # cursor
        cur = conn.cursor()

        # query
        query = f"SELECT id FROM movies;"
        # executing query
        cur.execute(query)
        # fetching data
        data = cur.fetchall()

        # committing connection
        conn.commit()
        # closing cursor
        cur.close()
        # closing connection
        conn.close()
        # returning boolean
        return bool(data)

    # handling error
    except Error as error:
        print('Error:', error)


# function for getting movies' list
def get_movies() -> list[tuple[int, str]]:
    try:
        # connection
        conn = psycopg2.connect(
            host=host,
            database=database,
            port=port,
            user=user,
            password=password,
        )

        # cursor
        cur = conn.cursor()

        # query
        query = f"SELECT id, name FROM movies;"
        # executing query
        cur.execute(query)
        # fetching data
        data = cur.fetchall()

        # committing connection
        conn.commit()
        # closing cursor
        cur.close()
        # closing connection
        conn.close()

        # returning data
        return data

    # handling error
    except Error as error:
        print('Error:', error)
