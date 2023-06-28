import pymssql
import pandas as pd
import backend.function.xml as xml
import backend.constrain


## Get data from control plan to trackback
## GET TO DATAFRAME
def controlPlanGet(type):
    cnxn = pymssql.connect(server=backend.constrain.HOST, port=backend.constrain.PORT\
                        , database=backend.constrain.DB_GET\
                        , user=backend.constrain.USER\
                        , password=backend.constrain.PASSWORD)
    if cnxn != None: print("PROCESS DATABASE: CONNECT SUCCESS", cnxn)
    if type =="A":
        cur = cnxn.cursor()
        cur.execute("SELECT * FROM " +backend.constrain.TABLE_CONTROL_PLAN_A)
        data = cur.fetchall()
        df = pd.DataFrame(data)
        df['TOOL_VALUE']= None
    elif type =="B":
        cur = cnxn.cursor()
        cur.execute("SELECT * FROM " +backend.constrain.TABLE_CONTROL_PLAN_B)
        data = cur.fetchall()
        df = pd.DataFrame(data)
        df['TOOL_VALUE']= None
    elif type =="C":
        cur = cnxn.cursor()
        cur.execute("SELECT * FROM " +backend.constrain.TABLE_CONTROL_PLAN_C)
        data = cur.fetchall()
        df = pd.DataFrame(data)
        df['TOOL_VALUE']= None
    cnxn.close()
    return df

def processing():
    list_run = {"A", "B", "C"}
    for i in list_run:
        try:
            df = controlPlanGet(i)
            xml.parseParaXMLDB(backend.constrain.xml_globals, df)
            xml.parseParaXMLDB(backend.constrain.xml_recipe, df)
            pushDatabaseActual(df, i)
        except:
            print(f"{i} error")
    print ("DATABASE PROCESSING: SUCCESS")

def processingConsistOfType(type):
    if type =="A":
        df = controlPlanGet("A")
        xml.parseParaXMLDB(backend.constrain.xml_globals, df)
        xml.parseParaXMLDB(backend.constrain.xml_recipe, df)
        pushDatabaseActual(df, "A")
    elif type =="B":
        df = controlPlanGet("B")
        xml.parseParaXMLDB(backend.constrain.xml_globals, df)
        xml.parseParaXMLDB(backend.constrain.xml_recipe, df)
        pushDatabaseActual(df, "B")
    elif type =="C":
        df = controlPlanGet("C")
        xml.parseParaXMLDB(backend.constrain.xml_globals, df)
        xml.parseParaXMLDB(backend.constrain.xml_recipe, df)
        pushDatabaseActual(df, "C")
    print ("DATABASE PROCESSING: SUCCESS")
##________________________________________________________________________________________________

def processingUnpush(type):
    if type =="A":
        df = controlPlanGet("A")
        xml.parseParaXMLDB(backend.constrain.xml_globals, df)
        xml.parseParaXMLDB(backend.constrain.xml_recipe, df)
    elif type =="B":
        df = controlPlanGet("B")
        xml.parseParaXMLDB(backend.constrain.xml_globals, df)
        xml.parseParaXMLDB(backend.constrain.xml_recipe, df)
    elif type =="C":
        df = controlPlanGet("C")
        xml.parseParaXMLDB(backend.constrain.xml_globals, df)
        xml.parseParaXMLDB(backend.constrain.xml_recipe, df)
    return df

def pushDatabaseActual(df,type):
    cnxn = pymssql.connect(server=backend.constrain.HOST, port=backend.constrain.PORT\
                        , database=backend.constrain.DB_PUSH\
                        , user=backend.constrain.USER\
                        , password=backend.constrain.PASSWORD)
    cursor = cnxn.cursor()
    cursor.execute("SELECT * FROM " +backend.constrain.TABLE_ACTUAL_A)
    if type == "A":
        for index in range (backend.constrain.size_df):
            cursor.execute("""INSERT INTO """ +backend.constrain.TABLE_ACTUAL_A + """ (ITEM, CATALOG_NAME, PARA_NAME, POR_VALUE, PRIORITY_VALUE, TOOL_VALUE) VALUES (%s, %s, %s, %s, %s, %s)""",\
                (str(df.iloc[index, 0]),\
                str(df.iloc[index, 1]), \
                str(df.iloc[index, 2]), \
                str(df.iloc[index, 3]), \
                str(df.iloc[index, 4]), \
                str(df.iloc[index, 7])))
            cnxn.commit()
    elif type == "B":
        for index in range (backend.constrain.size_df):
            cursor.execute("""INSERT INTO """ +backend.constrain.TABLE_ACTUAL_B + """ (ITEM, CATALOG_NAME, PARA_NAME, POR_VALUE, PRIORITY_VALUE, TOOL_VALUE) VALUES (%s, %s, %s, %s, %s, %s)""",\
                (str(df.iloc[index, 0]),\
                str(df.iloc[index, 1]), \
                str(df.iloc[index, 2]), \
                str(df.iloc[index, 3]), \
                str(df.iloc[index, 4]), \
                str(df.iloc[index, 7])))
            cnxn.commit()
    elif type == "C":
        for index in range (backend.constrain.size_df):
            cursor.execute("""INSERT INTO """ +backend.constrain.TABLE_ACTUAL_C + """ (ITEM, CATALOG_NAME, PARA_NAME, POR_VALUE, PRIORITY_VALUE, TOOL_VALUE) VALUES (%s, %s, %s, %s, %s, %s)""",\
                (str(df.iloc[index, 0]),\
                str(df.iloc[index, 1]), \
                str(df.iloc[index, 2]), \
                str(df.iloc[index, 3]), \
                str(df.iloc[index, 4]), \
                str(df.iloc[index, 7])))
            cnxn.commit()
    cnxn.close()
## python3 function/function_database.py