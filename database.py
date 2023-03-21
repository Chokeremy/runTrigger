from config import *
import psycopg2


def con_data():
    conn = psycopg2.connect(database=DATABASE, user=USER, password=PASSWORD, host=HOST, port=PORT)
    cursor = conn.cursor()

    cursor.execute(SQL)
    re = cursor.fetchall()
    param = list()

    for i in re:
        parameter = [
            {
                "patientId": i[0],
                "visitId": i[1],
                "tag": "cdss"
            }
        ]
        param.append(parameter)
    return param









