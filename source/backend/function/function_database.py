from backend.database.control_plan_processing import *
from backend.function.function_xml import *
from backend.database.parameter_processing import *
from backend.function.constrain import *

def control_plan_maker():
    list_run = {"A", "B", "C"}
    df = fc_ce.read_excel(excel_file)
    data = fc_ce.read_sheet(df)
    for i in list_run:
        push_db_controlplan(data,size, i)

def processing():
    list_run = {"A", "B", "C"}
    for i in list_run:
        try:
            df = control_plan_server_get(i)
            parse_para_xml_db(xml_globals, df)
            parse_para_xml_db(xml_recipe, df)
            push_db_actual(df, i)
        except:
            print(f"{i} error")
    print ("DATABASE PROCESSING: SUCCESS")

def processingConsistOfType(type):
    if type =="A":
        df = control_plan_server_get("A")
        parse_para_xml_db(xml_globals, df)
        parse_para_xml_db(xml_recipe, df)
        push_db_actual(df, "A")
    elif type =="B":
        df = control_plan_server_get("B")
        parse_para_xml_db(xml_globals, df)
        parse_para_xml_db(xml_recipe, df)
        push_db_actual(df, "B")
    elif type =="C":
        df = control_plan_server_get("C")
        parse_para_xml_db(xml_globals, df)
        parse_para_xml_db(xml_recipe, df)
        push_db_actual(df, "C")
    print ("DATABASE PROCESSING: SUCCESS")
##________________________________________________________________________________________________

def processingUnpush(type):
    if type =="A":
        df = control_plan_server_get("A")
        parse_para_xml_db(xml_globals, df)
        parse_para_xml_db(xml_recipe, df)
    elif type =="B":
        df = control_plan_server_get("B")
        parse_para_xml_db(xml_globals, df)
        parse_para_xml_db(xml_recipe, df)
    elif type =="C":
        df = control_plan_server_get("C")
        parse_para_xml_db(xml_globals, df)
        parse_para_xml_db(xml_recipe, df)
    return df

## python3 function/function_database.py