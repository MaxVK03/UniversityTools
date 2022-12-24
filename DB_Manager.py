import sqlite3 as sqll

connection = sqll.connect("DBHolder/Code_Funcs")
def chk_conn(conn):
        try:
            conn.cursor()
            return True
        except Exception as ex:
            print("There was a error connecting to the code DB, try again")
            return False



def connImprog_C_Funcs(connection):

    cur = connection.cursor()
    cur.execute("select * from C_Funcs_Improg")
    data = cur.fetchall()
    return data


def connCompArch_C_Funcs(connection):
    cur = connection.cursor()
    cur.execute("select * from ASM_Funcs_LC3")
    data = cur.fetchall()
    return data

def getCompArch():
    ret = connCompArch_C_Funcs(connection)
    return ret

def getCImprog():
    ret = connImprog_C_Funcs(connection)
    return ret