import pymssql
import pandas as pd
import backend.const
import meta.external_var
from tkinter import messagebox

# dataframe of user information include ID, username, pass and email
def dataframeUSER():
    cnxn = pymssql.connect(server= backend.const.jsonConst()["HOST"], port= backend.const.jsonConst()["PORT"]\
                        , database= backend.const.jsonConst()["DB_USER"]\
                        , user= backend.const.jsonConst()["USER"]\
                        , password= backend.const.jsonConst()["PASSWORD"])
    cur = cnxn.cursor()
    cur.execute("SELECT * FROM " + backend.const.jsonConst()["TABLE_USER"])
    data = cur.fetchall()
    df = pd.DataFrame(data)
    cnxn.close()
    return df

def authenticantionUser(username, password):
    try: 
        bool_var = False
        cnxn = pymssql.connect(server= backend.const.jsonConst()["HOST"], port= backend.const.jsonConst()["PORT"]\
                            , database= backend.const.jsonConst()["DB_USER"]\
                            , user= backend.const.jsonConst()["USER"]\
                            , password= backend.const.jsonConst()["PASSWORD"])
        cur = cnxn.cursor()
        cur.execute("SELECT * FROM " + backend.const.jsonConst()["TABLE_USER"])
        data = cur.fetchall()
        df = pd.DataFrame(data)
        for index in range(df.shape[0]):
            if df.loc[index, 1] == username and df.loc[index, 3] == password:
                bool_var = True
                meta.external_var.roll = df.loc[index,4]
                meta.external_var.email = df.loc[index,2]
                break
        cnxn.close()
        return bool_var
    except Exception as e:
        messagebox.show 

def changePass(username, email, password):
    cnxn = pymssql.connect(server= backend.const.jsonConst()["HOST"], port= backend.const.jsonConst()["PORT"]\
                        , database= backend.const.jsonConst()["DB_USER"]\
                        , user= backend.const.jsonConst()["USER"]\
                        , password= backend.const.jsonConst()["PASSWORD"])
    cur = cnxn.cursor()
    temp = backend.const.jsonConst()['TABLE_USER']
    cur.execute(f"UPDATE {temp} SET PASS_WORD = '{password}' WHERE USER_NAME = '{username}' AND EMAIL = '{email}';")
    cnxn.commit()
    cnxn.close()
