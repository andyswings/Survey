#!/usr/bin/env python3

import sys
import json
from PyQt5 import QtWidgets
import Survey
import SurveyUpdate as su
from datetime import date
import time

class SurveyWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(SurveyWindow, self).__init__()
        self.ui = Survey.Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.btnFinish.setStyleSheet("background: green; border: 1px solid black")
        self.ui.btnFinish.clicked.connect(self.Finish)
        self.btnBlu(self.ui.btn1V, self.ui.btn2V, self.ui.btn3V, self.ui.btn4V, self.ui.btn5V)
        self.btnBlu(self.ui.btn1F, self.ui.btn2F, self.ui.btn3F, self.ui.btn4F, self.ui.btn5F)
        self.btnBlu(self.ui.btn1P, self.ui.btn2P, self.ui.btn3P, self.ui.btn4P, self.ui.btn5P)

        self.ui.btnStaff.clicked.connect(self.Staff)
        self.ui.btnStudent.clicked.connect(self.Student)
        self.ui.btnGuest.clicked.connect(self.Guest)
        self.ui.btnBreakfast.clicked.connect(self.Breakfast)
        self.ui.btnLunch.clicked.connect(self.Lunch)
        self.ui.btnSupper.clicked.connect(self.Supper)

        self.ui.btn1V.clicked.connect(self.oneV)
        self.ui.btn2V.clicked.connect(self.twoV)
        self.ui.btn3V.clicked.connect(self.threeV)
        self.ui.btn4V.clicked.connect(self.fourV)
        self.ui.btn5V.clicked.connect(self.fiveV)

        self.ui.btn1F.clicked.connect(self.oneF)
        self.ui.btn2F.clicked.connect(self.twoF)
        self.ui.btn3F.clicked.connect(self.threeF)
        self.ui.btn4F.clicked.connect(self.fourF)
        self.ui.btn5F.clicked.connect(self.fiveF)

        self.ui.btn1P.clicked.connect(self.oneP)
        self.ui.btn2P.clicked.connect(self.twoP)
        self.ui.btn3P.clicked.connect(self.threeP)
        self.ui.btn4P.clicked.connect(self.fourP)
        self.ui.btn5P.clicked.connect(self.fiveP)

        self.ui.btnExit.clicked.connect(lambda:self.close()) # Remove this line when finished testing

    def oneV(self):
        # self.ui.btn1V.setChecked(True)
        self.unCheckALL(self.ui.btn2V, self.ui.btn3V, self.ui.btn4V, self.ui.btn5V)
        self.btnBlu(self.ui.btn1V, self.ui.btn2V, self.ui.btn3V, self.ui.btn4V, self.ui.btn5V)
        self.WriteChoice('D', 1)
        self.WriteChoice('V', 1)
        self.threeORnot()
        # time.sleep(0.3)

    def oneF(self):
        # self.ui.btn1F.setChecked(True)
        self.unCheckALL(self.ui.btn2F, self.ui.btn3F, self.ui.btn4F, self.ui.btn5F)
        self.btnBlu(self.ui.btn1F, self.ui.btn2F, self.ui.btn3F, self.ui.btn4F, self.ui.btn5F)
        self.WriteChoice('E', 1)
        self.WriteChoice('T', 1)
        self.threeORnot()
        # time.sleep(0.3)

    def oneP(self):
        # self.ui.btn1P.setChecked(True)
        self.unCheckALL(self.ui.btn2P, self.ui.btn3P, self.ui.btn4P, self.ui.btn5P)
        self.btnBlu(self.ui.btn1P, self.ui.btn2P, self.ui.btn3P, self.ui.btn4P, self.ui.btn5P)
        self.WriteChoice('F', 1)
        self.WriteChoice('P', 1)
        self.threeORnot()
        # time.sleep(0.3)

    def twoV(self):
        # self.ui.btn2V.setChecked(True)
        self.unCheckALL(self.ui.btn1V, self.ui.btn3V, self.ui.btn4V, self.ui.btn5V)
        # self.btnBlu(self.ui.btn1V, self.ui.btn2V, self.ui.btn3V, self.ui.btn4V, self.ui.btn5V)
        self.WriteChoice('D', 2)
        self.WriteChoice('V', 1)
        self.threeORnot()
        # time.sleep(0.3)

    def twoF(self):
        # self.ui.btn2F.setChecked(True)
        self.unCheckALL(self.ui.btn1F, self.ui.btn3F, self.ui.btn4F, self.ui.btn5F)
        # self.btnBlu(self.ui.btn1F, self.ui.btn2F, self.ui.btn3F, self.ui.btn4F, self.ui.btn5F)
        self.WriteChoice('E', 2)
        self.WriteChoice('T', 1)
        self.threeORnot()
        # time.sleep(0.3)

    def twoP(self):
        # self.ui.btn2P.setChecked(True)
        self.unCheckALL(self.ui.btn1P, self.ui.btn3P, self.ui.btn4P, self.ui.btn5P)
        # self.btnBlu(self.ui.btn1P, self.ui.btn2P, self.ui.btn3P, self.ui.btn4P, self.ui.btn5P)
        self.WriteChoice('F', 2)
        self.WriteChoice('P', 1)
        self.threeORnot()
        # time.sleep(0.3)

    def threeV(self):
        # self.ui.btn3V.setChecked(True)
        self.unCheckALL(self.ui.btn1V, self.ui.btn2V, self.ui.btn4V, self.ui.btn5V)
        # self.btnBlu(self.ui.btn1V, self.ui.btn2V, self.ui.btn3V, self.ui.btn4V, self.ui.btn5V)
        self.WriteChoice('D', 3)
        self.WriteChoice('V', 1)
        self.threeORnot()
        # time.sleep(0.3)

    def threeF(self):
        # self.ui.btn3F.setChecked(True)
        self.unCheckALL(self.ui.btn1F, self.ui.btn2F, self.ui.btn4F, self.ui.btn5F)
        # self.btnBlu(self.ui.btn1F, self.ui.btn2F, self.ui.btn3F, self.ui.btn4F, self.ui.btn5F)
        self.WriteChoice('E', 3)
        self.WriteChoice('T', 1)
        self.threeORnot()
        # time.sleep(0.3)

    def threeP(self):
        # self.ui.btn3P.setChecked(True)
        self.unCheckALL(self.ui.btn1P, self.ui.btn2P, self.ui.btn4P, self.ui.btn5P)
        # self.btnBlu(self.ui.btn1P, self.ui.btn2P, self.ui.btn3P, self.ui.btn4P, self.ui.btn5P)
        self.WriteChoice('F', 3)
        self.WriteChoice('P', 1)
        self.threeORnot()
        # time.sleep(0.3)

    def fourV(self):
        # self.ui.btn4V.setChecked(True)
        self.unCheckALL(self.ui.btn1V, self.ui.btn2V, self.ui.btn3V, self.ui.btn5V)
        # self.btnBlu(self.ui.btn1V, self.ui.btn2V, self.ui.btn3V, self.ui.btn4V, self.ui.btn5V)
        self.WriteChoice('D', 4)
        self.WriteChoice('V', 1)
        self.threeORnot()
        # time.sleep(0.3)

    def fourF(self):
        # self.ui.btn4F.setChecked(True)
        self.unCheckALL(self.ui.btn1F, self.ui.btn2F, self.ui.btn3F, self.ui.btn5F)
        # self.btnBlu(self.ui.btn1F, self.ui.btn2F, self.ui.btn3F, self.ui.btn4F, self.ui.btn5F)
        self.WriteChoice('E', 4)
        self.WriteChoice('T', 1)
        self.threeORnot()
        # time.sleep(0.3)

    def fourP(self):
        # self.ui.btn4P.setChecked(True)
        self.unCheckALL(self.ui.btn1P, self.ui.btn2P, self.ui.btn3P, self.ui.btn5P)
        # self.btnBlu(self.ui.btn1P, self.ui.btn2P, self.ui.btn3P, self.ui.btn4P, self.ui.btn5P)
        self.WriteChoice('F', 4)
        self.WriteChoice('P', 1)
        self.threeORnot()
        # time.sleep(0.3)

    def fiveV(self):
        # self.ui.btn5V.setChecked(True)
        self.unCheckALL(self.ui.btn1V, self.ui.btn2V, self.ui.btn3V, self.ui.btn4V)
        # self.btnBlu(self.ui.btn1V, self.ui.btn2V, self.ui.btn3V, self.ui.btn4V, self.ui.btn5V)
        self.WriteChoice('D', 5)
        self.WriteChoice('V', 1)
        self.threeORnot()
        # time.sleep(0.3)

    def fiveF(self):
        # self.ui.btn5F.setChecked(True)
        self.unCheckALL(self.ui.btn1F, self.ui.btn2F, self.ui.btn3F, self.ui.btn4F)
        # self.btnBlu(self.ui.btn1F, self.ui.btn2F, self.ui.btn3F, self.ui.btn4F, self.ui.btn5F)
        self.WriteChoice('E', 5)
        self.WriteChoice('T', 1)
        self.threeORnot()
        # time.sleep(0.3)

    def fiveP(self):
        # self.ui.btn5P.setChecked(True)
        self.unCheckALL(self.ui.btn1P, self.ui.btn2P, self.ui.btn3P, self.ui.btn4P)
        # self.btnBlu(self.ui.btn1P, self.ui.btn2P, self.ui.btn3P, self.ui.btn4P, self.ui.btn5P)
        self.WriteChoice('F', 5)
        self.WriteChoice('P', 1)
        self.threeORnot()
        # time.sleep(0.3)

    def Breakfast(self):
        self.ui.btnBreakfast.setChecked(True)
        self.unCheckALL(self.ui.btnLunch, self.ui.btnSupper)
        self.WriteChoice('B', 'Breakfast')
        time.sleep(0.3)
        self.gotoQuestionPage()

    def Lunch(self):
        self.ui.btnLunch.setChecked(True)
        self.unCheckALL(self.ui.btnBreakfast, self.ui.btnSupper)
        self.WriteChoice('B', 'Lunch')
        time.sleep(0.3)
        self.gotoQuestionPage()

    def Supper(self):
        self.ui.btnSupper.setChecked(True)
        self.unCheckALL(self.ui.btnLunch, self.ui.btnBreakfast)
        self.WriteChoice('B', 'Supper')
        time.sleep(0.3)
        self.gotoQuestionPage()

    def Staff(self):
        self.ui.btnStaff.setChecked(True)
        self.unCheckALL(self.ui.btnStudent, self.ui.btnGuest)
        self.WriteChoice('C', 'Staff')
        time.sleep(0.3)
        self.gotoMealPage()

    def Student(self):
        self.ui.btnStudent.setChecked(True)
        self.unCheckALL(self.ui.btnStaff, self.ui.btnGuest)
        self.WriteChoice('C', 'Student')
        time.sleep(0.3)
        self.gotoMealPage()

    def Guest(self):
        self.ui.btnGuest.setChecked(True)
        self.unCheckALL(self.ui.btnStaff, self.ui.btnStudent)
        self.WriteChoice('C', 'Guest')
        time.sleep(0.3)
        self.gotoMealPage()

    def ClearBtns(self):
        self.ui.btnSupper.setChecked(False)
        self.unCheckALL(self.ui.btnSupper, self.ui.btnBreakfast, self.ui.btnLunch)
        self.unCheckALL(self.ui.btnGuest, self.ui.btnStaff, self.ui.btnStudent)
        self.unCheckALL(self.ui.btn1P, self.ui.btn2P, self.ui.btn3P, self.ui.btn4P, self.ui.btn5P)
        self.unCheckALL(self.ui.btn1F, self.ui.btn2F, self.ui.btn3F, self.ui.btn4F, self.ui.btn5F)
        self.unCheckALL(self.ui.btn1V, self.ui.btn2V, self.ui.btn3V, self.ui.btn4V, self.ui.btn5V)
        self.btnBlu(self.ui.btn1P, self.ui.btn2P, self.ui.btn3P, self.ui.btn4P, self.ui.btn5P)
        self.btnBlu(self.ui.btn1F, self.ui.btn2F, self.ui.btn3F, self.ui.btn4F, self.ui.btn5F)
        self.btnBlu(self.ui.btn1V, self.ui.btn2V, self.ui.btn3V, self.ui.btn4V, self.ui.btn5V)
        self.WriteChoice('P', 0)
        self.WriteChoice('V', 0)
        self.WriteChoice('T', 0)

    def unCheckALL(self, *args):
        for arg in args:
            arg.setChecked(False)

    def WriteChoice(self, colum, valus):
        with open('SurveyTemp.json') as f:
            data = json.load(f)
        data.update([(colum, valus)])
        with open("SurveyTemp.json", "w+") as f:
            json.dump(data, f)

    def Finish(self):
        today = date.today()
        t = today.strftime('%d/%m')
        self.WriteChoice('A', str(t))
        su.Update_excel()
        self.ClearBtns()
        self.gotoStartPage()

    def threeORnot(self):
        with open('SurveyTemp.json') as f:
            data = json.load(f)
        if data['P'] + data['T'] + data['V'] == 3:
            self.ui.stackedWidget.setCurrentIndex(3)
        else:
            pass

    def btnBlu(self, *args):
        for arg in args:
            if arg.isChecked():
                arg.setStyleSheet("background: blue; border: 1px solid black")
            else:
                arg.setStyleSheet("")

    def gotoStartPage(self):
        self.ui.stackedWidget.setCurrentIndex(0)

    def gotoMealPage(self):
        self.ui.stackedWidget.setCurrentIndex(1)

    def gotoQuestionPage(self):
        self.ui.stackedWidget.setCurrentIndex(2)

    def gotoThanksPage(self):
        self.ui.stackedWidget.setCurrentIndex(3)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = SurveyWindow()
    # window.show()
    window.showFullScreen()
    sys.exit(app.exec())
