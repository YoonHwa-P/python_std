# /c/Users/brill/Desktop/python_std/venv/Scripts/python

from psycopg2 import connect, extensions

def main():
    # step 01 연결
    conn = connecting()
    print(conn)
    createTB(conn)

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

def createTB(conn):
    print("createTable function.. in... ")
    TB_NAME = "Subway"

    # AutoCommit
    autocommit = extensions.ISOLATION_LEVEL_AUTOCOMMIT
    print("ISOLATION_LEVEL_AUTOCOMMIT:", extensions.ISOLATION_LEVEL_AUTOCOMMIT)
    conn.set_isolation_level(autocommit)
    cursor = conn.cursor()
    #기존 table이 있으면 삭제
    cursor.execute("DROP TABLE IF EXISTS TEMP")
    print("Table is deleted!")

    # 테이븦 생성
    QUERY = '''
        CREATE TABLE {NAME}(
        STATION CHAR(50) NOT NULL,
        GETON_PPL CHAR(50),
        GETON_OFF CHAR(50),
        
        '''.format(NAME = TB_NAME)

    cursor.execute(QUERY)
    print("Database created...")

    cursor.close()

    conn.close()

if __name__ == "__main__":
    main()