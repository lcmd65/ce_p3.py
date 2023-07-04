import pymssql
import pandas as pd
import backend.const
<<<<<<< HEAD
import meta.external_var
=======
>>>>>>> 1e443b0b670d391e81d7c91f7afb8cbef4ef8273

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
<<<<<<< HEAD
            meta.external_var.roll = df.loc[index,4]
=======
>>>>>>> 1e443b0b670d391e81d7c91f7afb8cbef4ef8273
            break
    cnxn.close()
    return bool_var

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
