import pymssql
import pandas as pd
import backend.constrain

def authenticantionUser(username, password):
    bool_var = False
    cnxn = pymssql.connect(server= backend.constrain.HOST, port= backend.constrain.PORT\
                        , database= backend.constrain.DB_USER\
                        , user= backend.constrain.USER\
                        , password= backend.constrain.PASSWORD)
    if cnxn != None: print("PROCESS DATABASE: CONNECT SUCCESS", cnxn)
    cur = cnxn.cursor()
    cur.execute("SELECT * FROM " + backend.constrain.TABLE_USER)
    data = cur.fetchall()
    df = pd.DataFrame(data)
    for index in range(df.shape[0]):
        if df.loc[index, 1] == username and df.loc[index, 3] == password:
            bool_var = True
            break
    return bool_var