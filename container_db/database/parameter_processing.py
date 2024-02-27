
import pymssql
import backend.function.database as db
import backend.constrain 

## Push actual value to DB after get data from XML SChema
def pushDatabaseActual(df,type):
    cnxn = pymssql.connect(server= backend.constrain.HOST, port= backend.constrain.PORT\
                        , database= backend.constrain.DB_PUSH\
                        , user= backend.constrain.USER\
                        , password= backend.constrain.PASSWORD)
    cursor = cnxn.cursor()
    cursor.execute("SELECT * FROM " + backend.constrain.TABLE_ACTUAL_A)
    if type == "A":
        for index in range (backend.constrain.size_df):
            cursor.execute("""INSERT INTO """ + backend.constrain.TABLE_ACTUAL_A + """ (ITEM, CATALOG_NAME, PARA_NAME, POR_VALUE, PRIORITY_VALUE, TOOL_VALUE) VALUES (%s, %s, %s, %s, %s, %s)""",\
                (str(df.iloc[index, 0]),\
                str(df.iloc[index, 1]), \
                str(df.iloc[index, 2]), \
                str(df.iloc[index, 3]), \
                str(df.iloc[index, 4]), \
                str(df.iloc[index, 7])))
            cnxn.commit()
    elif type == "B":
        for index in range (backend.constrain.size_df):
            cursor.execute("""INSERT INTO """ + backend.constrain.TABLE_ACTUAL_B + """ (ITEM, CATALOG_NAME, PARA_NAME, POR_VALUE, PRIORITY_VALUE, TOOL_VALUE) VALUES (%s, %s, %s, %s, %s, %s)""",\
                (str(df.iloc[index, 0]),\
                str(df.iloc[index, 1]), \
                str(df.iloc[index, 2]), \
                str(df.iloc[index, 3]), \
                str(df.iloc[index, 4]), \
                str(df.iloc[index, 7])))
            cnxn.commit()
    elif type == "C":
        for index in range (backend.constrain.size_df):
            cursor.execute("""INSERT INTO """ + backend.constrain.TABLE_ACTUAL_C + """ (ITEM, CATALOG_NAME, PARA_NAME, POR_VALUE, PRIORITY_VALUE, TOOL_VALUE) VALUES (%s, %s, %s, %s, %s, %s)""",\
                (str(df.iloc[index, 0]),\
                str(df.iloc[index, 1]), \
                str(df.iloc[index, 2]), \
                str(df.iloc[index, 3]), \
                str(df.iloc[index, 4]), \
                str(df.iloc[index, 7])))
            cnxn.commit()
    cnxn.close()