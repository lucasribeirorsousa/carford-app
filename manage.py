import psycopg2,os,shutil,subprocess
DIR_MIGRATIONS  = './migrations'

def run():
    USER = os.getenv('DB_USER')
    POSTGRES = {
            'user': os.environ['POSTGRES_USER'],
            'password': os.environ['POSTGRES_PASSWORD'],
            'database': os.environ['POSTGRES_DATABASE'],
            'host': os.environ['POSTGRES_HOST'],
            'port': os.environ['POSTGRES_PORT'],
    }
    try:
        conn = psycopg2.connect(**POSTGRES)
        conn.autocommit = True
        cur = conn.cursor()
        cur.execute('delete from alembic_version')
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
        if os.path.exists(DIR_MIGRATIONS):
            shutil.rmtree(DIR_MIGRATIONS, ignore_errors=True)

run()
