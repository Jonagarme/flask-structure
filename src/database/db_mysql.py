from decouple import config
import pymysql

def get_connection():
    try:
        return pymysql.connect(
            host=config('MSQL_HOST'),
            user=config('MSQL_USER'),
            password=config('MSQL_PASSWORD'),
            db=config('MSQL_DB')
        )
    except Exception as ex:
        print(ex)
