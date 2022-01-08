import psycopg2

def main():
    # step 01 연결
    connecting()

def connecting():
    # DB Connect
    conn = psycopg2.connect(
        host = "localhost", # SQL 서버 주소
        dbname = "postgres",
        user = "postgres",
        password = "1234",
        port = "5432"
    )

    print(conn)

if __name__ == "__main__":
    main()