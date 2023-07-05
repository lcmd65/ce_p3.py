import pymssql
import pandas as pd
import backend.function.xml as xml
import backend.const

def cursorFromDatabase(_server , _port, _database, _user, _password):
    cnxn = pymssql.connect(server = backend.const.jsonConst()[_server]\
                        , port = backend.const.jsonConst()[_port]\
                        , database = backend.const.jsonConst()[_database]\
                        , user = backend.const.jsonConst()[_user]\
                        , password = backend.const.jsonConst()[_password])
    if cnxn != None: print("PROCESS DATABASE: CONNECT SUCCESS", cnxn)
    return cnxn
    
## Get data from control plan to trackback
## GET TO DATAFRAME
def controlPlanGet(type):
    cnxn = cursorFromDatabase("HOST", "PORT", "DB_GET", "USER", "PASSWORD")
    cur = cnxn.cursor()
    cur.execute("SELECT * FROM " +backend.const.jsonConst()["".join(["TABLE_CONTROL_PLAN_", type])])
    data = cur.fetchall()
    df = pd.DataFrame(data)
    df['TOOL_VALUE'] = None
    cnxn.close()
    return df

def processing():
    list_run = {"A", "B", "C"}
    for i in list_run:
        try:
            df = controlPlanGet(i)
            xml.parseParaXMLDB(backend.const.jsonConst()["xml_globals"], df)
            xml.parseParaXMLDB(backend.const.jsonConst()["xml_recipe"], df)
            pushDatabaseActual(df, i)
        except:
            print(f"{i} error")
    print ("DATABASE PROCESSING: SUCCESS")

def processingConsistOfType(type):
    df = controlPlanGet(type)
    xml.parseParaXMLDB(backend.const.jsonConst()["xml_globals"], df)
    xml.parseParaXMLDB(backend.const.jsonConst()["xml_recipe"], df)
    pushDatabaseActual(df, type)
    print ("DATABASE PROCESSING: SUCCESS")
##________________________________________________________________________________________________

def processingUnpush(type):
    df = controlPlanGet(type)
    xml.parseParaXMLDB(backend.const.jsonConst()["xml_globals"], df)
    xml.parseParaXMLDB(backend.const.jsonConst()["xml_recipe"], df)
    return df

def pushDatabaseActual(df,type):
    cnxn = pymssql.connect(server=backend.const.jsonConst()["HOST"]\
                        , port=backend.const.jsonConst()["PORT"]\
                        , database=backend.const.jsonConst()["DB_PUSH"]\
                        , user=backend.const.jsonConst()["USER"]\
                        , password=backend.const.jsonConst()["PASSWORD"])
    cursor = cnxn.cursor()
    cursor.execute("SELECT * FROM " +backend.const.jsonConst()["TABLE_ACTUAL_A"])
    if type == "A":
        for index in range (backend.const.jsonConst()["size_df"]):
            cursor.execute("""INSERT INTO """ +backend.const.jsonConst()["TABLE_ACTUAL_A"]+ """ (ITEM, CATALOG_NAME, PARA_NAME, POR_VALUE, PRIORITY_VALUE, TOOL_VALUE) VALUES (%s, %s, %s, %s, %s, %s)""",\
                (str(df.iloc[index, 0]),\
                str(df.iloc[index, 1]), \
                str(df.iloc[index, 2]), \
                str(df.iloc[index, 3]), \
                str(df.iloc[index, 4]), \
                str(df.iloc[index, 7])))
            cnxn.commit()
    elif type == "B":
        for index in range (backend.const.jsonConst()["size_df"]):
            cursor.execute("""INSERT INTO """ +backend.const.jsonConst()["TABLE_ACTUAL_B"] + """ (ITEM, CATALOG_NAME, PARA_NAME, POR_VALUE, PRIORITY_VALUE, TOOL_VALUE) VALUES (%s, %s, %s, %s, %s, %s)""",\
                (str(df.iloc[index, 0]),\
                str(df.iloc[index, 1]), \
                str(df.iloc[index, 2]), \
                str(df.iloc[index, 3]), \
                str(df.iloc[index, 4]), \
                str(df.iloc[index, 7])))
            cnxn.commit()
    elif type == "C":
        for index in range (backend.const.jsonConst()["size_df"]):
            cursor.execute("""INSERT INTO """ +backend.const.jsonConst()["TABLE_ACTUAL_C"] + """ (ITEM, CATALOG_NAME, PARA_NAME, POR_VALUE, PRIORITY_VALUE, TOOL_VALUE) VALUES (%s, %s, %s, %s, %s, %s)""",\
                (str(df.iloc[index, 0]),\
                str(df.iloc[index, 1]), \
                str(df.iloc[index, 2]), \
                str(df.iloc[index, 3]), \
                str(df.iloc[index, 4]), \
                str(df.iloc[index, 7])))
            cnxn.commit()
    cnxn.close()
## python3 function/function_database.py