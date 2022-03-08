#!/usr/bin/env python3

import json
import subprocess
from openpyxl import load_workbook

def Update_excel():
    wb = load_workbook('SurveyData.xlsx')
    ws = wb.active

    with open('SurveyTemp.json', encoding="utf8") as f:
        j = json.load(f)

    data = (j['A'], j['B'], j['C'], j['D'], j['E'], j['F'])

    ws.append(data)
    wb.save("SurveyData.xlsx")
    bashCommand = "scp ./SurveyData.xlsx pi@192.168.101.107:/home/pi/SurveyData.xlsx" # just a placeholder for an scp line that will cp
                       # the xlsx file to a server.
    subprocess.check_call(bashCommand.split())

Update_excel()
