# Now write out to postgres
import psycopg2
from secrets import username, password, host, dbname


con_string = "host='{}' dbname='{}' user='{}' password='{}'".format(host, dbname, username,password)

def get_conn():
    return psycopg2.connect(con_string)

def get_cur():
    conn =  psycopg2.connect(con_string)
    return conn.cursor()

def runsql(sql):
    conn = get_conn()
    with conn:
        cur = conn.cursor()
        with cur:
            cur.execute(sql)


def get_freq_conn():

    connected = False
    for i in range(10):
        try:
            con_string_freq = "host='{}' dbname='{}' user='{}' password='{}' options='-c statement_timeout=600'"
            con_string_freq = con_string_freq.format(host, dbname, username, password)
            freq_con = psycopg2.connect(con_string_freq)
            connected = True
        except psycopg2.OperationalError:
            pass
        if connected:
            break
        if i == 1:
            print("Some connections are being rejected by database")

    return freq_con

def get_data_conn():

    connected = False

    for i in range(10):

        try:
            con_string_data = "host='{}' dbname='{}' user='{}' password='{}' options='-c statement_timeout=600'"
            con_string_data = con_string_data.format(host, dbname, username, password)
            data_conn = psycopg2.connect(con_string_data)
            connected = True
        except psycopg2.OperationalError:
            pass
        
        if connected:
            break
        if i == 1:
            print("Some connections are being rejected by database")
    return data_conn
            

from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, MetaData

from sqlalchemy import create_engine

def get_engine():
    con_string = 'postgresql://{}:{}@{}:5432/{}'.format(username, password, host, dbname)
    engine = create_engine(con_string) 
    return engine


