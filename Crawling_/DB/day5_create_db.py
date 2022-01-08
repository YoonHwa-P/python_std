# /c/Users/brill/Desktop/python_std/venv/Scripts/python

from psycopg2 import connect, extensions

def main():
    # step 01 연결
    conn = connecting()
    print(conn)

    createDB(conn)

def connecting():
    # DB Connect
    conn = connect(
        host = "localhost", # SQL 서버 주소
        dbname = "postgres",
        user = "postgres",
        password = "1234",
        port = "5432"
    )

    # print(conn)
    return conn

def createDB(conn):
    print("createDB function.. in... ")
    DB_NAME = "GREEN"

    # AutoCommit
    autocommit = extensions.ISOLATION_LEVEL_AUTOCOMMIT
    print("ISOLATION_LEVEL_AUTOCOMMIT:", extensions.ISOLATION_LEVEL_AUTOCOMMIT)
    conn.set_isolation_level(autocommit)

    # 쿼리 작성
    '''
    SQL_QUERY = """
        SELECT 'CREATE DATABASE GREEN' 
        WHERE NOT EXISTS (SELECT FROM pg_database WHERE datname = 'GREEN')
    """
    '''
    QUERY = '''CREATE DATABASE GREEN''';

    cursor = conn.cursor()
    cursor.execute(QUERY)
    print("Database created...")

    cursor.close()

    conn.close()

if __name__ == "__main__":
    main()