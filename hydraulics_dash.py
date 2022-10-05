import PySimpleGUI as sg
import pandas as pd
import pyodbc 

deviceId = ""
ts = ""
AI0 = ""
AI1 = ""
AI2 = ""
AI3 = ""
AI4 = ""
AI5 = ""
AI6 = ""
M901 = ""
M902 = ""
M903 = ""
M904 = ""
M905 = ""
M908 = ""
M910 = ""
M911 = ""
M912 = ""
M913 = ""
M914 = ""
M915 = ""
M916 = ""
M917 = ""
M918 = ""
M919 = ""
M920 = ""
M921 = ""
M922 = ""
M923 = ""
M926 = ""
M927 = ""
M928 = ""
M930 = ""
M932 = ""
M933 = ""
M934 = ""
M936 = ""
M937 = ""
M938 = ""
M939 = ""
M942 = ""


#QUERIES-------------------------------------

server = 'hydrovoltasql.database.windows.net' 
database = 'hydraulicssql' 
username = 'hydrosql' 
password = 'Tar95889' 
# ENCRYPT defaults to yes starting in ODBC Driver 18. It's good to always specify ENCRYPT=yes on the client side to avoid MITM attacks.

cnxn = pyodbc.connect('DRIVER={ODBC Driver 18 for SQL Server};SERVER='+server+';DATABASE='+database+';ENCRYPT=yes;UID='+username+';PWD='+ password)
cursor = cnxn.cursor()

#DASHBOARD----------------------------------

#FRAMES

M901_col = sg.Column([
    [sg.Frame('M901_TSA_pH',[[sg.Text(M901, font=["Helvetica", 10], text_color="#00FF00", justification="left",key="-M901-")]])]])
M901_btn = sg.Column([
    [sg.Frame("M901 Graph", [[sg.Button('Graph')]], key="-M901_btn-", element_justification="center", size=(100, 100))]])

M902_col = sg.Column([
    [sg.Frame('M902_TSA_pressure', [[sg.Text(M902, font=["Helvetica", 10], text_color="#00FF00", justification="left",key="-M902-")]])]])

M903_col = sg.Column([
    [sg.Frame('M903_TSA_Flow', [[sg.Text(M903, font=["Helvetica", 10], text_color="#00FF00", justification="left",key="-M903-")]])]])

M904_col = sg.Column([
    [sg.Frame('M904_TSA_Cond', [[sg.Text(M904, font=["Helvetica", 10], text_color="#00FF00", justification="left",key="-M904-")]])]])

M905_col = sg.Column([
    [sg.Frame('M905_TSA_Level', [[sg.Text(M905, font=["Helvetica", 10], text_color="#00FF00", justification="left",key="-M905-")]])]])

M908_col = sg.Column([
    [sg.Frame('M908_TE_LEVEL', [[sg.Text(M908, font=["Helvetica", 10], text_color="#00FF00", justification="left",key="-M908-")]])]])

M910_col = sg.Column([
    [sg.Frame('M910_TD_Temperature', [[sg.Text(M910, font=["Helvetica", 10], text_color="#00FF00", justification="left",key="-M910-")]])]])

M911_col = sg.Column([
    [sg.Frame('M911_TSA_Temperature', [[sg.Text(M911, font=["Helvetica", 10], text_color="#00FF00", justification="left",key="-M911-")]])]])

M912_col = sg.Column([
    [sg.Frame('M912_TB_Temperature', [[sg.Text(M912, font=["Helvetica", 10], text_color="#00FF00", justification="left",key="-M912-")]])]])

M913_col = sg.Column([
    [sg.Frame('M913_E_G1_Pressure', [[sg.Text(M913, font=["Helvetica", 10], text_color="#00FF00", justification="left",key="-M913-")]])]])

M914_col = sg.Column([
    [sg.Frame('M914_E_G2_Pressure', [[sg.Text(M914, font=["Helvetica", 10], text_color="#00FF00", justification="left",key="-M914-")]])]])

M915_col = sg.Column([
    [sg.Frame('M915_TF_Cond_Pressure', [[sg.Text(M915, font=["Helvetica", 10], text_color="#00FF00", justification="left",key="-M915-")]])]])

M916_col = sg.Column([
    [sg.Frame('M916_TF_Cond_Pressure', [[sg.Text(M916, font=["Helvetica", 10], text_color="#00FF00", justification="left",key="-M916-")]])]])

M917_col = sg.Column([
    [sg.Frame('M917_TD_Level', [[sg.Text(M917, font=["Helvetica", 10], text_color="#00FF00", justification="left",key="-M917-")]])]])


TS_col = sg.Column([
    [sg.Frame('TimeStamp',[[sg.Text(ts, font=["Helvetica", 10], text_color="#00EE00", justification="left",key="-ts-")]])]])


layout = [
    [[sg.Button('Exit')],sg.Text('Hydrovolta Hydraulics Subsystem',size=(40, 1), font=('Any 15')),sg.Push()],
    [sg.Image(size=(800,500),filename="hyd3.png")],
    [[M901_col, TS_col,M902_col,M903_col,M904_col,M905_col,M908_col, M910_col, M911_col]],
    [M912_col, M913_col, M914_col, M915_col, M916_col, M917_col],
    [M901_btn]
##    [[M901_col, TS_col],[M902_col,M903_col]],
##    [M904_col,M905_col],
    
]

#WINDOW

window = sg.Window("Hydraulics Dash", layout,grab_anywhere=True).Finalize()
window.Maximize()

#EVENT

while True:

    event, values = window.read(timeout=10)
    

    try:
        
        cursor.execute("""select DeviceId, ts, [ADAM-4017+_1:AI0_100mV],[ADAM-4017+_1:AI1_100mV],[ADAM-4017+_1:AI2_100mV],[ADAM-4017+_1:AI3_100mV],
                [ADAM-4017+_1:AI4_100mV],[ADAM-4017+_1:AI5_100mV],[ADAM-4017+_1:AI6_100mV],
                M901_TSA_pH, M902_TSA_pressure, M903_TSA_Flow, M904_TSA_Cond, M905_TSA_Level, M908_TE_LEVEL,
                M910_TD_Temperature, M911_TSA_Temperature, M912_TB_Temperature, M913_E_G1_Pressure, M914_E_G2_Pressure, M915_TF_Cond,
                M916_TF_pressure, M917_TD_Level, M918_TC_Level, M919_E_Conducitivity, M920_Drain_pressure, M921_TD_pH, M922_TD_pressure, M923_TD_Flow,
                M926_TC_pressure_231, M927_TC_Flow, M928_TC_Cond, M930_Drain_Flow, M932_C1Loop_Flow, M933_D2In_pressure,
                M934_D2In_Flow, M936_C1In_Pressure, M937_C2Out_Conductivity, M938_C2Loop_Flow, M939_D3In_pressure, M942_C2In_pressure from [dbo].[demoTable] ORDER BY ts DESC""")

    except:

        print("Read timeout")

    hyd_vals = cursor.fetchone()
    
    devId = hyd_vals[0]
    ts = hyd_vals[1]
    AI0 = hyd_vals[2]
    AI1 = hyd_vals[3]
    AI2 = hyd_vals[4]
    AI3 = hyd_vals[5]
    AI4 = hyd_vals[6]
    AI5 = hyd_vals[7]
    AI6 = hyd_vals[8]
    M901 = hyd_vals[9]
    M902 = hyd_vals[10]
    M903 = hyd_vals[11]
    M904 = hyd_vals[12]
    M905 = hyd_vals[13]
    M908 = hyd_vals[14]
    M910 = hyd_vals[15]
    M911 = hyd_vals[16]
    M912 = hyd_vals[17]
    M913 = hyd_vals[18]
    M914 = hyd_vals[19]
    M915 = hyd_vals[20]
    M916 = hyd_vals[21]
    M917 = hyd_vals[22]
    M918 = hyd_vals[23]
    M919 = hyd_vals[24]
    M920 = hyd_vals[25]
    M921 = hyd_vals[26]
    M922 = hyd_vals[27]
    M923 = hyd_vals[28]
    M926 = hyd_vals[29]
    M927 = hyd_vals[30]
    M928 = hyd_vals[31]
    M930 = hyd_vals[32]
    M932 = hyd_vals[33]
    M933 = hyd_vals[34]
    M934 = hyd_vals[35]
    M936 = hyd_vals[36]
    M937 = hyd_vals[37]
    M938 = hyd_vals[38]
    M939 = hyd_vals[39]
    M942 = hyd_vals[40]

    #print(hyd_vals)
    
    
    window['-ts-'].Update(ts)
    window['-M901-'].Update(M901)
    window['-M902-'].Update(M902)
    window['-M903-'].Update(M903)
    window['-M904-'].Update(M904)
    window['-M905-'].Update(M905)
    window['-M908-'].Update(M908)
    window['-M910-'].Update(M910)
    window['-M911-'].Update(M911)
    window['-M912-'].Update(M912)
    window.refresh()
    if event == "Exit" or event == sg.WIN_CLOSED:
        break




window.close()
