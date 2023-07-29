<<<<<<< HEAD
import psycopg2

#   id_guild numeric not null,
# 	id_spouse1	NUMERIC not null,
# 	id_spouse2	NUMERIC not null,
# 	day_married	date NOT NULL,
# 	PRIMARY KEY(id_guild, id_spouse1,id_spouse2)


def createConnection():
    con = None
    try:
        con = psycopg2.connect(dbname="Discord_bot", host="localhost",
                               user="postgres", password="admin", port="5432")
        print('Connection to PostgreSQL DB successful')
        con.autocommit = True
    except psycopg2.OperationalError as e:
        print(f'The error {e} occurred')
    return con


def insertData(x):
    con = createConnection()
    try:
        cursor = con.cursor()
        cursor.execute('insert into marriages values(%s, %s, %s, %s)', x)
    except psycopg2.OperationalError as e:
        if e.pgcode == 23505:
            return False
        print(f'The error {e} occurred')
        cursor.close()
        con.close()


def getAllData(guild_id):
    con = createConnection()
    try:
        cursor = con.cursor()
        cursor.execute(f'select * from marriages where id_guild={guild_id}')
        out_data = cursor.fetchall()
        cursor.close()
        con.close()
        return out_data
    except psycopg2.OperationalError as e:
        print(f'The error {e} occurred')
        cursor.close()
        con.close()


def getOneData(guild_id, spouse_id):
    con = createConnection()
    try:
        cursor = con.cursor()
        cursor.execute(
            f'select * from marriages where id_guild={guild_id} and (id_spouse1={spouse_id} or id_spouse2={spouse_id})')
        out_data = cursor.fetchone()
        cursor.close()
        con.close()
        return out_data
    except psycopg2.OperationalError as e:
        print(f'The error {e} occurred')


def deleteData(guild_id, spouse1_id):
    con = createConnection()
    try:
        cursor = con.cursor()
        cursor.execute(
            f'delete from marriages where id_guild={guild_id} and (id_spouse1={spouse1_id} or id_spouse2={spouse1_id})')
        cursor.close()
        con.close()
        return True
    except psycopg2.OperationalError as e:
        print(f'The error {e} occurred')
        return False
=======
import psycopg2

#   id_guild numeric not null,
# 	id_spouse1	NUMERIC not null,
# 	id_spouse2	NUMERIC not null,
# 	day_married	date NOT NULL,
# 	PRIMARY KEY(id_guild, id_spouse1,id_spouse2)


def createConnection():
    con = None
    try:
        con = psycopg2.connect(dbname="Discord_bot", host="localhost",
                               user="postgres", password="admin", port="5432")
        print('Connection to PostgreSQL DB successful')
        con.autocommit = True
    except psycopg2.OperationalError as e:
        print(f'The error {e} occurred')
    return con


def insertData(x):
    con = createConnection()
    try:
        cursor = con.cursor()
        cursor.execute('insert into marriages values(%s, %s, %s, %s)', x)
    except psycopg2.OperationalError as e:
        if e.pgcode == 23505:
            return False
        print(f'The error {e} occurred')
        cursor.close()
        con.close()


def getAllData(guild_id):
    con = createConnection()
    try:
        cursor = con.cursor()
        cursor.execute(f'select * from marriages where id_guild={guild_id}')
        out_data = cursor.fetchall()
        cursor.close()
        con.close()
        return out_data
    except psycopg2.OperationalError as e:
        print(f'The error {e} occurred')
        cursor.close()
        con.close()


def getOneData(guild_id, spouse_id):
    con = createConnection()
    try:
        cursor = con.cursor()
        cursor.execute(
            f'select * from marriages where id_guild={guild_id} and (id_spouse1={spouse_id} or id_spouse2={spouse_id})')
        out_data = cursor.fetchone()
        cursor.close()
        con.close()
        return out_data
    except psycopg2.OperationalError as e:
        print(f'The error {e} occurred')


def deleteData(guild_id, spouse1_id):
    con = createConnection()
    try:
        cursor = con.cursor()
        cursor.execute(
            f'delete from marriages where id_guild={guild_id} and (id_spouse1={spouse1_id} or id_spouse2={spouse1_id})')
        cursor.close()
        con.close()
        return True
    except psycopg2.OperationalError as e:
        print(f'The error {e} occurred')
        return False
>>>>>>> master
