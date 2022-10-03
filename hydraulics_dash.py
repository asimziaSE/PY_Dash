import PySimpleGUI as sg
import pandas as pd
import pyodbc 
# Some other example server values are
# server = 'localhost\sqlexpress' # for a named instance
# server = 'myserver,port' # to specify an alternate port

#QUERIES-------------------------------------

server = 'hydrovoltasql.database.windows.net' 
database = 'hydraulicssql' 
username = 'hydrosql' 
password = 'Tar95889' 
# ENCRYPT defaults to yes starting in ODBC Driver 18. It's good to always specify ENCRYPT=yes on the client side to avoid MITM attacks.
cnxn = pyodbc.connect('DRIVER={ODBC Driver 18 for SQL Server};SERVER='+server+';DATABASE='+database+';ENCRYPT=yes;UID='+username+';PWD='+ password)
cursor = cnxn.cursor()


#cursor.execute("select M901_TSA_pH from [dbo].[demoTable] ORDER BY ts DESC")

cursor.execute("""Select DeviceId, ts, [ADAM-4017+_1:AI0_100mV],[ADAM-4017+_1:AI1_100mV],[ADAM-4017+_1:AI2_100mV],[ADAM-4017+_1:AI3_100mV],
[ADAM-4017+_1:AI4_100mV],[ADAM-4017+_1:AI5_100mV],[ADAM-4017+_1:AI6_100mV],
M901_TSA_pH, M902_TSA_pressure, M903_TSA_Flow, M904_TSA_Cond, M905_TSA_Level, M908_TE_LEVEL,
M910_TD_Temperature, M911_TSA_Temperature, M912_TB_Temperature, M913_E_G1_Pressure, M914_E_G2_Pressure, M915_TF_Cond,
M916_TF_pressure, M917_TD_Level, M918_TC_Level, M919_E_Conducitivity, M920_Drain_pressure, M921_TD_pH, M922_TD_pressure, M923_TD_Flow,
M926_TC_pressure_231, M927_TC_Flow, M928_TC_Cond, M930_Drain_Flow, M932_C1Loop_Flow, M933_D2In_pressure,
M934_D2In_Flow, M936_C1In_Pressure, M937_C2Out_Conductivity, M938_C2Loop_Flow, M939_D3In_pressure, M942_C2In_pressure from [dbo].[demoTable] ORDER BY ts DESC""")

hyd_vals = cursor.fetchone()
values = list(hyd_vals)
values_df = pd.DataFrame(values)
#DASHBOARD----------------------------------

M901_col = sg.Column([
    [sg.Frame('M901_TSA_pH', [[sg.Text(hyd_vals[10], font=["Helvetica", 10], text_color="#000000", justification="left")]])]])
TS_col = sg.Column([
    [sg.Frame('TimeStamp', [[sg.Text(hyd_vals[1], font=["Helvetica", 10], text_color="#000000", justification="left")]])]])

bg_layout = [sg.theme_text_color(), sg.theme_background_color(), [sg.Image(r'hyd3.png')]]

layout = [[M901_col], [TS_col],
    [sg.Push(),sg.Text('Hydrovolta Hydraulics Subsystem',size=(40, 1), font=('Any 15')),sg.Push()],
    [sg.Image(size=(800,500),filename="hyd3.png")],
    [sg.Button('Exit')]
]

window = sg.Window("Hydraulics Dash", layout).Finalize()
window.Maximize()

while True:
    event, values = window.read()
    if event == "Exit" or event == sg.WIN_CLOSED:
        break


window.close()
