import pymssql
import pandas as pd
import backend.const

# dataframe of user information include ID, username, pass and email
def dataframeUSER():
    cnxn = pymssql.connect(server= backend.const.jsonConst()["HOST"], port= backend.const.jsonConst()["PORT"]\
                        , database= backend.const.jsonConst()["DB_USER"]\
                        , user= backend.const.jsonConst()["USER"]\
                        , password= backend.const.jsonConst()["PASSWORD"])
    if cnxn != None: print("PROCESS DATABASE: CONNECT SUCCESS", cnxn)
    cur = cnxn.cursor()
    cur.execute("SELECT * FROM " + backend.const.jsonConst()["TABLE_USER"])
    data = cur.fetchall()
    df = pd.DataFrame(data)
    return df

def authenticantionUser(username, password):
    bool_var = False
    cnxn = pymssql.connect(server= backend.const.jsonConst()["HOST"], port= backend.const.jsonConst()["PORT"]\
                        , database= backend.const.jsonConst()["DB_USER"]\
                        , user= backend.const.jsonConst()["USER"]\
                        , password= backend.const.jsonConst()["PASSWORD"])
    if cnxn != None: print("PROCESS DATABASE: CONNECT SUCCESS", cnxn)
    cur = cnxn.cursor()
    cur.execute("SELECT * FROM " + backend.const.jsonConst()["TABLE_USER"])
    data = cur.fetchall()
    df = pd.DataFrame(data)
    for index in range(df.shape[0]):
        if df.loc[index, 1] == username and df.loc[index, 3] == password:
            bool_var = True
            break
    return bool_var

def changePass(username, email, password):
    cnxn = pymssql.connect(server= backend.const.jsonConst()["HOST"], port= backend.const.jsonConst()["PORT"]\
                        , database= backend.const.jsonConst()["DB_USER"]\
                        , user= backend.const.jsonConst()["USER"]\
                        , password= backend.const.jsonConst()["PASSWORD"])
    print("PROCESS DATABASE: CONNECT SUCCESS", cnxn)
    cur = cnxn.cursor()
    temp = backend.const.jsonConst()['TABLE_USER']
    cur.execute(f"UPDATE {temp} SET PASS_WORD = '{password}' WHERE USER_NAME = '{username}' AND EMAIL = '{email}';")
    cnxn.commit()
