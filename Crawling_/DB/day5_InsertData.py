import pandas as pd
from psycopg2 import connect, extensions
import psycopg2.extras as extras
import psycopg2
from sqlalchemy import create_engine

# https://docs.sqlalchemy.org/en/14/core/engines.html
# pip install sqlalchemy

def main():
    # Step 01
    conn = connecting()
    print(conn)
    # createDB(conn)
    # createTable(conn)
    data = pd.DataFrame({
        "STATION": ["합계", "서울역"],
        "GETON_PPL": ["271,214,262", "4,465,118"],
        "GETOFF_PPL": ["52,767,099", "4,205,563"]
    })

    # dataInsertPsycopg2(conn, data)
    dataInsertAlchemy(data)



def connecting():

    # DB connect
    conn = connect(
        host = "localhost",
        dbname = "postgres",
        user = "postgres",
        password = "1234",
        port = "5432"
    )

    # print(conn)
    return conn

def createDB(conn):
    DB_NAME = "testDB"

    # AutoCommit
    autocommit = extensions.ISOLATION_LEVEL_AUTOCOMMIT
    print("ISOLATION_LEVEL_AUTOCOMMIT:", extensions.ISOLATION_LEVEL_AUTOCOMMIT)
    conn.set_isolation_level(autocommit)

    # 새로운 데이터베이스 생성
    SQL_QUERY = """
        SELECT 'CREATE DATABASE {DB_NAME}'
        WHERE NOT EXISTS (SELECT FROM pg_database WHERE datname = 'testDB')
    """.format(DB_NAME = DB_NAME)

    cursor = conn.cursor()
    cursor.execute(SQL_QUERY)
    print("Database created successfully...!")

    # close the cursor to avoid memory leaks
    cursor.close()

    # Connection Closed to avoid memory leaks
    conn.close()

def createTable(conn):

    TABLE_NAME = "TEMP"

    # AutoCommit
    autocommit = extensions.ISOLATION_LEVEL_AUTOCOMMIT
    print("ISOLATION_LEVEL_AUTOCOMMIT:", extensions.ISOLATION_LEVEL_AUTOCOMMIT)
    conn.set_isolation_level(autocommit)

    cursor = conn.cursor()

    # 테이블 삭제
    cursor.execute("DROP TABLE IF EXISTS TEMP")
    print("TABLE Deleted successfully...!")

    # 테이블 생성
    SQL_QUERY = '''
        CREATE TABLE {NAME}(
            STATION CHAR(50) NOT NULL, 
            GETON_PPL CHAR(50), 
            GETOFF_PPL CHAR(50)
        )
    '''.format(NAME = TABLE_NAME)
    cursor.execute(SQL_QUERY)
    print("TABLE created successfully........")

    # close the cursor to avoid memory leaks
    cursor.close()

    # Connection Closed to avoid memory leaks
    conn.close()

def dataInsertPsycopg2(conn, data):
    # Single Insert
    TABLE_NAME = "TEMP"

    # AutoCommit
    autocommit = extensions.ISOLATION_LEVEL_AUTOCOMMIT
    print("ISOLATION_LEVEL_AUTOCOMMIT:", extensions.ISOLATION_LEVEL_AUTOCOMMIT)
    conn.set_isolation_level(autocommit)

    tuples = [tuple(x) for x in data.to_numpy()]
    # print(tuples)
    '''
    [('합계', '271,214,262', '52,767,099'), ('서울역', '4,465,118', '4,205,563')]
    '''

    cols = ','.join(list(data.columns))
    print(cols) # STATION,GETON_PPL,GETOFF_PPL


    # SQL query to execute
    query = "INSERT INTO %s(%s) VALUES %%s" % (TABLE_NAME, cols)
    print(query)


    cursor = conn.cursor()
    # https://www.psycopg.org/docs/extras.html
    try:
        extras.execute_values(cursor, query, argslist = tuples)
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print("Error: %s" % error)
        conn.rollback()
        cursor.close()
        return 1
    print("the dataframe is inserted")
    cursor.close()
    conn.close()

def dataInsertAlchemy(data):
    conn_string = "postgresql://postgres:temp@localhost:5432/testdb"
    engine = create_engine(conn_string)
    conn = engine.connect()
    data.to_sql("temp123", con = conn, if_exists="replace", index=False)
    print("DataFrame is inserted")
    conn = psycopg2.connect(conn_string)
    conn.autocommit = True

    conn.close()

if __name__ == "__main__":
    main()