# Mini Project
import warnings
warnings.filterwarnings("ignore")
import sys
import csv
import operator
import pandas as pd
import numpy as np
import os.path
from PyQt5 import QtWidgets
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5 import QtCore, QtGui
from matplotlib import pyplot as plt
import random
from statistics import mean,median 
import math
from scipy import interpolate
from scipy.interpolate import UnivariateSpline
import time
from time import strftime
import dropbox
from datetime import date

import re
import sqlite3

b = 0
lu = 0
d = 0
gender = 0
br0 = 0
br1 = 0
br2 = 0
br3 = 0
di = 0
di1 = 0
di2 = 0
di3 = 0
lun = 0
lun1 = 0
lun2 = 0
lun3 = 0
q1 = 0
q2 = 0
q3 = 0
q4 = 0
q11 = 0
q22 = 0
q33 = 0
q44 = 0
q111 = 0
q222 = 0
q333 = 0
q444 = 0
idd = 1
csvname = str
blueflag=0
gok=0
flagg=0

def resource_path(relative_path):
        """ Get absolute path to resource, works for dev and for PyInstaller """
        try:
            # PyInstaller creates a temp folder and stores path in _MEIPASS
            base_path = sys._MEIPASS
        except Exception:
            base_path = os.path.abspath(".")

        return os.path.join(base_path, relative_path)

class Window(QtWidgets.QWidget):    
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        
        self.bl1 = QtWidgets.QLabel('  ')
        
        self.l1 = QtWidgets.QLabel('Simulation of Virtual Diabetic Patient')
        self.l1.setAlignment(Qt.AlignCenter)
        self.l1.setFont(QtGui.QFont("Arial", 22, QtGui.QFont.Black))
        self.l1.setFixedHeight(30)
        
        self.pic = QtWidgets.QLabel(self)
        pixmap = QPixmap(resource_path("KLELogo.png"))
        self.pic.setPixmap(pixmap)
        self.pic.setAlignment(Qt.AlignCenter)
        self.pic.setFixedSize(80,80)
        
        self.pic1 = QtWidgets.QLabel(self)
        pixmap1 = QPixmap(resource_path("diabetes_logo.png"))
        self.pic1.setPixmap(pixmap1)
        self.pic1.setAlignment(Qt.AlignCenter)
        self.pic1.setFixedSize(80,80)
        
        self.l2 = QtWidgets.QLabel('Enter the details of a diabetic patient')
        self.l2.setAlignment(Qt.AlignCenter)
        self.l2.setFont(QFont('Arial', 16))
        self.l2.setFixedHeight(30)
        
        datetime = QDateTime.currentDateTime()
        time = datetime.toString()
        self.date = QtWidgets.QLabel(time)
        self.date.setAlignment(Qt.AlignCenter)
        
        self.gender = QComboBox()
        self.gender.addItem('Male')
        self.gender.addItem('Female')
        self.gender.activated.connect(self.gender_selection)
        
        self.breakfast = QComboBox()
        self.breakfast.addItems(['05','06','07','08','09','10','11'])
        self.breakfast.activated[str].connect(self.breakfast_time_selection)
        
        self.lunch = QComboBox()
        self.lunch.addItems(['12','13','14','15','16'])
        self.lunch.activated[str].connect(self.lunch_time_selection)
        
        self.dinner = QComboBox()
        self.dinner.addItems(['19','20','21','22','23'])
        self.dinner.activated[str].connect(self.dinner_time_selection)
        
        self.la0 = QtWidgets.QLabel('Name                                                    ')
        self.le0 = QtWidgets.QLineEdit('')
        self.la1 = QtWidgets.QLabel('Age(in years)                                        ')
        self.le1 = QtWidgets.QLineEdit('')
        self.laa = QtWidgets.QLabel('Weight(in kg)                                        ')
        self.lee = QtWidgets.QLineEdit('')
        self.lh = QtWidgets.QLabel('Height(in cms)                                      ')
        self.lhe = QtWidgets.QLineEdit('')
        self.la2 = QtWidgets.QLabel('Gender ')
        self.la3 = QtWidgets.QLabel('Breakfast Time (in 24 hrs)')
        self.la3a = QtWidgets.QLabel('Breakfast              ')
        self.la3a.setFont(QtGui.QFont("Arial", 14,  QtGui.QFont.Black))
        self.la4 = QtWidgets.QLabel('Lunch Time (in 24 hrs)')
        self.la4a = QtWidgets.QLabel('Lunch                  ')
        self.la4a.setFont(QtGui.QFont("Arial", 14,  QtGui.QFont.Black))
        self.la5 = QtWidgets.QLabel('Dinner Time (in 24 hrs)')
        self.la5a = QtWidgets.QLabel('Dinner                 ')
        self.la5a.setFont(QtGui.QFont("Arial", 14,  QtGui.QFont.Black))
        self.b = QtWidgets.QPushButton('Simulate')
        self.b.setFixedSize(100, 40)
        self.b1 = QtWidgets.QPushButton('Share')
        self.b1.setFixedSize(100, 40)

        
        self.bc1 = QtWidgets.QLabel('Milk')
        self.bc2 = QtWidgets.QLabel('Bread')
        self.bc3 = QtWidgets.QLabel('Fruits')
        self.bc4 = QtWidgets.QLabel('Foods')
        
        
        #BREAKFAST MENU
        self.m = QComboBox()
        self.m.addItem('Whole Milk')
        self.m.addItem('Tea')
        self.m.addItem('Tea and Biscuits')
        self.m.addItem('Curd')
        self.m.activated.connect(self.br_food_selection)
        
        self.bb1 = QComboBox()
        self.bb1.addItem('Breads')
        self.bb1.addItem('Buns')
        self.bb1.activated.connect(self.br_food_selection1)
        
        self.f = QComboBox()
        self.f.addItem('Apples')
        self.f.addItem('Oranges')
        self.f.addItem('Banana')
        self.f.addItem('Mangoes')
        self.f.activated.connect(self.br_food_selection2)
        
        self.fd = QComboBox()
        self.fd.addItem('Idlis')
        self.fd.addItem('Dosa')
        self.fd.addItem('Poha')
        self.fd.addItem('Puri & Vegetables')
        self.fd.activated.connect(self.br_food_selection3)
        
        #LUNCH MENU
        self.c = QComboBox()
        self.c.addItem('Rajmah')
        self.c.addItem('Lentils')
        self.c.addItem('Green Gram')
        self.c.activated.connect(self.lu_food_selection)
        
        self.br = QComboBox()
        self.br.addItem('Chapati')
        self.br.addItem('Naan')
        self.br.addItem('Paratha')
        self.br.activated.connect(self.lu_food_selection1)
        
        self.r = QComboBox()
        self.r.addItem('Plain Rice')
        self.r.addItem('Brown Rice')
        self.r.addItem('Basmati Rice')
        self.r.activated.connect(self.lu_food_selection2)
        
        self.v = QComboBox()
        self.v.addItem('Potato')
        self.v.addItem('Peas')
        self.v.addItem('Cabbage')
        self.v.activated.connect(self.lu_food_selection3)
        
        #DINNER MENU
        self.cc = QComboBox()
        self.cc.addItem('Rajmah')
        self.cc.addItem('Lentils')
        self.cc.addItem('Green Gram')
        self.cc.activated.connect(self.di_food_selection)
        
        self.brr = QComboBox()
        self.brr.addItem('Chapati')
        self.brr.addItem('Naan')
        self.brr.addItem('Paratha')
        self.brr.activated.connect(self.di_food_selection1)
        
        self.rr = QComboBox()
        self.rr.addItem('Plain Rice')
        self.rr.addItem('Brown Rice')
        self.rr.addItem('Basmati Rice')
        self.rr.activated.connect(self.di_food_selection2)
        
        self.vv = QComboBox()
        self.vv.addItem('Potato')
        self.vv.addItem('Peas')
        self.vv.addItem('Cabbage')
        self.vv.activated.connect(self.di_food_selection3)
        
        self.lc1 = QtWidgets.QLabel('Pulses')
        self.lc2 = QtWidgets.QLabel('Breads')
        self.lc3 = QtWidgets.QLabel('Rice')
        self.lc4 = QtWidgets.QLabel('Vegetables')
        
        self.dc1 = QtWidgets.QLabel('Pulses')
        self.dc2 = QtWidgets.QLabel('Breads')
        self.dc3 = QtWidgets.QLabel('Rice')
        self.dc4 = QtWidgets.QLabel('Vegetables')
        
        #quantities menu breakfast
        self.q1 = QComboBox()
        self.q1.addItem('01 Cup')
        self.q1.addItem('02')
        self.q1.addItem('03')
        self.q1.addItem('04')
        self.q1.addItem('05')
        self.q1.activated.connect(self.q1_selection)
        
        self.q2 = QComboBox()
        self.q2.addItem('01 piece ')
        self.q2.addItem('02')
        self.q2.addItem('03')
        self.q2.addItem('04')
        self.q2.addItem('05')
        self.q2.activated.connect(self.q2_selection)
        
        self.q3 = QComboBox()
        self.q3.addItem('01 piece ')
        self.q3.addItem('02')
        self.q3.addItem('03')
        self.q3.addItem('04')
        self.q3.addItem('05')
        self.q3.activated.connect(self.q3_selection)
        
        self.q4 = QComboBox()
        self.q4.addItem('01 piece ')
        self.q4.addItem('02')
        self.q4.addItem('03')
        self.q4.addItem('04')
        self.q4.addItem('05')
        self.q4.activated.connect(self.q4_selection)
        
        #quantities menu lunch
        self.q11 = QComboBox()
        self.q11.addItem('01 Bowl(145 gm) ')
        self.q11.addItem('02')
        self.q11.addItem('03')
        self.q11.addItem('04')
        self.q11.addItem('05')
        self.q11.activated.connect(self.q11_selection)
        
        self.q22 = QComboBox()
        self.q22.addItem('01 piece ')
        self.q22.addItem('02')
        self.q22.addItem('03')
        self.q22.addItem('04')
        self.q22.addItem('05')
        self.q22.activated.connect(self.q22_selection)
        
        self.q33 = QComboBox()
        self.q33.addItem('01 Bowl(154 gm) ')
        self.q33.addItem('02')
        self.q33.addItem('03')
        self.q33.addItem('04')
        self.q33.addItem('05')
        self.q33.activated.connect(self.q33_selection)
        
        self.q44 = QComboBox()
        self.q44.addItem('01 Bowl(100 gm) ')
        self.q44.addItem('02')
        self.q44.addItem('03')
        self.q44.addItem('04')
        self.q44.addItem('05')
        self.q44.activated.connect(self.q44_selection)
        
        #quantities menu dinner
        self.q111 = QComboBox()
        self.q111.addItem('01 Bowl(145 gm) ')
        self.q111.addItem('02')
        self.q111.addItem('03')
        self.q111.addItem('04')
        self.q111.addItem('05')
        self.q111.activated.connect(self.q111_selection)
        
        self.q222 = QComboBox()
        self.q222.addItem('01 piece ')
        self.q222.addItem('02')
        self.q222.addItem('03')
        self.q222.addItem('04')
        self.q222.addItem('05')
        self.q222.activated.connect(self.q222_selection)
        
        self.q333 = QComboBox()
        self.q333.addItem('01 Bowl(154 gm) ')
        self.q333.addItem('02')
        self.q333.addItem('03')
        self.q333.addItem('04')
        self.q333.addItem('05')
        self.q333.activated.connect(self.q333_selection)
        
        self.q444 = QComboBox()
        self.q444.addItem('01 Bowl(100 gm) ')
        self.q444.addItem('02')
        self.q444.addItem('03')
        self.q444.addItem('04')
        self.q444.addItem('05')
        self.q444.activated.connect(self.q444_selection)
        
        h_bo = QtWidgets.QHBoxLayout()
        h_bo.addWidget(self.la0)
        h_bo.addWidget(self.le0)
        
        h_boxx = QtWidgets.QHBoxLayout()
        h_boxx.addWidget(self.la1)
        h_boxx.addWidget(self.le1)
        
        h_boxxx = QtWidgets.QHBoxLayout()
        h_boxxx.addWidget(self.laa)
        h_boxxx.addWidget(self.lee)
        
        h_bb = QtWidgets.QHBoxLayout()
        h_bb.addWidget(self.lh)
        h_bb.addWidget(self.lhe)
        
        h_box0 = QtWidgets.QHBoxLayout()
        h_box0.addWidget(self.la2)
        h_box0.addWidget(self.gender)
        
        h_box1 = QtWidgets.QHBoxLayout()
        h_box1.addWidget(self.la3)
        h_box1.addWidget(self.breakfast)
        
        h_bc = QtWidgets.QHBoxLayout()            #BREAKFAST CATEGORIES BOX
        h_bc.addWidget(self.bc1)
        h_bc.addWidget(self.bc2)
        h_bc.addWidget(self.bc3)
        h_bc.addWidget(self.bc4)
        
        h_bc1 = QtWidgets.QHBoxLayout()            #BREAKFAST CATEGORIES MENU BOX
        h_bc1.addWidget(self.m)
        h_bc1.addWidget(self.bb1)
        h_bc1.addWidget(self.f)
        h_bc1.addWidget(self.fd)
        
        h_lc = QtWidgets.QHBoxLayout()            #LUNCH CATEGORIES BOX
        h_lc.addWidget(self.lc1)
        h_lc.addWidget(self.lc2)
        h_lc.addWidget(self.lc3)
        h_lc.addWidget(self.lc4)
        
        h_lc1 = QtWidgets.QHBoxLayout()            #LUNCH CATEGORIES MENU BOX
        h_lc1.addWidget(self.c)
        h_lc1.addWidget(self.br)
        h_lc1.addWidget(self.r)
        h_lc1.addWidget(self.v)
        
        h_dc = QtWidgets.QHBoxLayout()            #DINNER CATEGORIES BOX
        h_dc.addWidget(self.dc1)
        h_dc.addWidget(self.dc2)
        h_dc.addWidget(self.dc3)
        h_dc.addWidget(self.dc4)
        
        h_dc1 = QtWidgets.QHBoxLayout()            #DINNER CATEGORIES MENU BOX
        h_dc1.addWidget(self.cc)
        h_dc1.addWidget(self.brr)
        h_dc1.addWidget(self.rr)
        h_dc1.addWidget(self.vv)
        
        h_bq = QtWidgets.QHBoxLayout()             #QUANTITIES BREAKFAST BOX
        h_bq.addWidget(self.q1)
        h_bq.addWidget(self.q2)
        h_bq.addWidget(self.q3)
        h_bq.addWidget(self.q4)
        
        h_lq = QtWidgets.QHBoxLayout()             #QUANTITIES LUNCH BOX
        h_lq.addWidget(self.q11)
        h_lq.addWidget(self.q22)
        h_lq.addWidget(self.q33)
        h_lq.addWidget(self.q44)
        
        h_dq = QtWidgets.QHBoxLayout()             #QUANTITIES DINNER BOX
        h_dq.addWidget(self.q111)
        h_dq.addWidget(self.q222)
        h_dq.addWidget(self.q333)
        h_dq.addWidget(self.q444)
        
        h_box2 = QtWidgets.QHBoxLayout()
        h_box2.addWidget(self.la4)
        h_box2.addWidget(self.lunch)
        
        
        h_box3 = QtWidgets.QHBoxLayout()
        h_box3.addWidget(self.la5)
        h_box3.addWidget(self.dinner)
        
        pbox = QtWidgets.QHBoxLayout()
        pbox.addWidget(self.pic)
        
        lbox = QtWidgets.QVBoxLayout()
        lbox.addWidget(self.bl1)
        lbox.addWidget(self.bl1)
        lbox.addWidget(self.bl1)
        lbox.addWidget(self.l1)
        
        pbox1 = QtWidgets.QHBoxLayout()
        pbox1.addWidget(self.pic1)
        
        ubox = QtWidgets.QHBoxLayout()
        ubox.addLayout(pbox)
        ubox.addLayout(lbox)
        ubox.addLayout(pbox1)

        
        v1_box = QtWidgets.QVBoxLayout()
        v1_box.addLayout(ubox)
        v1_box.addWidget(self.bl1)
        v1_box.addWidget(self.bl1)
        v1_box.addWidget(self.bl1)
        v1_box.addWidget(self.l2)
        v1_box.addWidget(self.bl1)
        v1_box.addLayout(h_bo)
        v1_box.addLayout(h_boxx)
        v1_box.addLayout(h_boxxx)
        v1_box.addLayout(h_bb)
        v1_box.addLayout(h_box0)
        v1_box.addWidget(self.bl1)                 #space
        v1_box.addWidget(self.la3a)
        v1_box.addLayout(h_box1)
        v1_box.addLayout(h_bc)
        v1_box.addLayout(h_bc1)
        v1_box.addLayout(h_bq)
        v1_box.addWidget(self.bl1)                 #space
        v1_box.addWidget(self.la4a)
        v1_box.addLayout(h_box2)
        v1_box.addLayout(h_lc)
        v1_box.addLayout(h_lc1)
        v1_box.addLayout(h_lq)
        v1_box.addWidget(self.bl1)                  #space
        v1_box.addWidget(self.la5a)
        v1_box.addLayout(h_box3)
        v1_box.addLayout(h_dc)
        v1_box.addLayout(h_dc1)
        v1_box.addLayout(h_dq)
        v1_box.addWidget(self.bl1)
        v1_box.addWidget(self.b, alignment=QtCore.Qt.AlignCenter)
        v1_box.addWidget(self.b1, alignment=QtCore.Qt.AlignRight)
        v1_box.addWidget(self.bl1)

        
        v_box = QtWidgets.QVBoxLayout()
        v_box.addLayout(v1_box)
        
        self.setLayout(v_box)
        self.setWindowTitle("Simulator")
        self.setFixedSize(800,700)
        
        self.b.clicked.connect(self.btn_click)
        self.b1.clicked.connect(self.share_click)
        
        self.show()
        
    def gender_selection(self, i):
        global gender
        gender = self.gender.currentIndex()
        
    def breakfast_time_selection(self, text):
        global b
        b = int(text)
        
    def lunch_time_selection(self, text):
        global lu
        lu = int(text)
        
    def dinner_time_selection(self, text):
        global d
        d = int(text)
        
    def br_food_selection(self, i):
        global br0
        br0 = self.m.currentIndex() + 1
        
    def br_food_selection1(self, j):
        global br1
        br1 = self.bb1.currentIndex() + 1
        
    def br_food_selection2(self, k):
        global br2
        br2 = self.f.currentIndex() + 1
        
    def br_food_selection3(self, l):
        global br3
        br3 = self.fd.currentIndex() + 1   
        
    def lu_food_selection(self, i):
        global lun
        lun = self.c.currentIndex() + 1
        
    def lu_food_selection1(self, i):
        global lun1
        lun1 = self.br.currentIndex() + 1
        
    def lu_food_selection2(self, i):
        global lun2
        lun2 = self.r.currentIndex() + 1
        
    def lu_food_selection3(self, i):
        global lun3
        lun3 = self.v.currentIndex() + 1
        
    def di_food_selection(self, i):
        global di
        di  = self.cc.currentIndex() + 1
        
    def di_food_selection1(self, i):
        global di1
        di1  = self.brr.currentIndex() + 1
        
    def di_food_selection2(self, i):
        global di2
        di2  = self.rr.currentIndex() + 1
        
    def di_food_selection3(self, i):
        global di3
        di3  = self.vv.currentIndex() + 1
        
    def q1_selection(self, i):
        global q1
        q1 = self.q1.currentIndex() + 1
        
    def q2_selection(self, i):
        global q2
        q2 = self.q2.currentIndex() + 1
        
    def q3_selection(self, i):
        global q3
        q3 = self.q3.currentIndex() + 1
        
    def q4_selection(self, i):
        global q4
        q4 = self.q4.currentIndex() + 1
        
    def q11_selection(self, i):
        global q11
        q11 = self.q11.currentIndex() + 1
        
    def q22_selection(self, i):
        global q22
        q22 = self.q22.currentIndex() + 1
        
    def q33_selection(self, i):
        global q33
        q33 = self.q33.currentIndex() + 1
        
    def q44_selection(self, i):
        global q44
        q44 = self.q44.currentIndex() + 1
        
    def q111_selection(self, i):
        global q111
        q111 = self.q111.currentIndex() + 1
        
    def q222_selection(self, i):
        global q222
        q222 = self.q222.currentIndex() + 1
        
    def q333_selection(self, i):
        global q333
        q333 = self.q333.currentIndex() + 1
        
    def q444_selection(self, i):
        global q444
        q444 = self.q444.currentIndex() + 1
        
    def errormsg(self, em):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        error_msg = em

        msg.setText(error_msg)
        msg.setInformativeText("Don't leave the fields blank.")
        msg.setWindowTitle("Error!!!")
        msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)    
        msg.exec_()
        
    def checkid(self, em):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)

        msg.setText("Are you a returning patient ?")
        msg.setInformativeText("Is this your patient id : "+str(em))
        msg.setWindowTitle("Id Verification!!!")
        msg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        ret = msg.exec()
        if ret==QMessageBox.Yes:
            return 1
        elif ret==QMessageBox.No:
            return 0
        
    def checkgestational(self):
        global gok
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)

        msg.setText("Are you a gestational diabetic patient ?")
        msg.setWindowTitle("Gestational Verification!!!")
        msg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        ret = msg.exec()
        if ret==QMessageBox.Yes:
            self.openSecondDialog()
        elif ret==QMessageBox.No:
            gok = 1
            msg.close()
        
    def openSecondDialog(self):
        
        def errormsg2(em):
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            error_msg = em

            msg.setText(error_msg)
            msg.setWindowTitle("Error!!!")
            msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)    
            msg.exec_()
        
        def btn_click2(self):
            global bpv
            global pv
            global gok
            reg = '^[1-9][0-9]*'
            if bp.text()=='' or p.text()=='':
                errormsg2("Please enter valid details!!")
            elif (re.search(reg, bp.text())==None) or (re.search(reg, p.text())==None):
                errormsg2("Please enter valid details!!")
            else:
                bpv = int(bp.text())
                pv = int(p.text())
                print(str(bpv)+" "+str(pv))
                if bpv>50 and bpv<200 and pv>=1 and pv<=10:
                    gok = 1
                    mydialog.close()
                else:
                    errormsg2("Please enter valid details!!")
            
        mydialog = QDialog(self)
        bpl = QtWidgets.QLabel("Blood Pressure(in mm Hg)")
        bp = QtWidgets.QLineEdit('')
        pl = QtWidgets.QLabel("No of Pregnancies before")
        p = QtWidgets.QLineEdit('')
        sb = QtWidgets.QPushButton('SUBMIT')
        sb.clicked.connect(btn_click2)
        h = QtWidgets.QHBoxLayout()
        h.addWidget(bpl)
        h.addWidget(bp)
        h.addWidget(pl)
        h.addWidget(p)
        h.addWidget(sb)
        mydialog.setLayout(h)
        mydialog.setWindowTitle("Additional info for Gestational Patients")
        mydialog.show()                

    def share_click(self):
        global csv_name
        global blueflag
        if blueflag==1:
            if os.name == 'nt':
                cmd = "fsquirt"
                os.system(cmd)
            elif os.name == 'posix':
                cmd = "bluetooth-sendto "+csvname+".csv"
                os.system(cmd)
            blueflag=0
        else:
            self.errormsg("No result to share")
        
    def btn_click(self):
        global idd
        global name
        global gender
        global b
        global lu
        global d
        global br0, br1, br2, br3
        global lun, lun1, lun2, lun3
        global di, di1, di2, di3
        global q1,q2,q3,q4,q11,q22,q33,q44,q111,q222,q333,q444
        global blueflag
        global csvname
        global gok
        global flagg
        regex = '^[A-Za-z][A-Za-z]*'
            
        
        #####   invalid cases   #############   error message   #############
        if (re.search(regex, self.le0.text())==None):
            self.errormsg("Please enter a valid name of the patient!!")
        elif self.le0.text() == '' or self.le1.text() == '' or self.lee.text() == '' or self.lhe.text() == '':
            self.errormsg("You have missed basic details of patient!!")
        elif int(self.lee.text()) >= 120 or int(self.lee.text()) <= 5:
            self.errormsg("The weight values are out of normal range!!")
        elif br0==0 and br1==0 and br2==0 and br3==0 and lun==0 and lun1==0 and lun2==0 and lun3==0 and di==0 and di1==0 and di2==0 and di3==0:
            self.errormsg("You didn't select any food item!!")
        elif br0==0 and br1==0 and br2==0 and br3==0:
            self.errormsg("You didn't select any breakfast food item!!")
        elif br0!=0 and q1==0 or q1!=0 and br0==0:
            self.errormsg("You missed selecting quantities of your breakfast food")
        elif br1!=0 and q2==0 or q2!=0 and br1==0:
            self.errormsg("You missed selecting quantities of your breakfast food")
        elif br2!=0 and q3==0 or q3!=0 and br2==0:
            self.errormsg("You missed selecting quantities of your breakfast food")
        elif br3!=0 and q4==0 or q4!=0 and br3==0:
            self.errormsg("You missed selecting quantities of your breakfast food")
        elif lun==0 and lun1==0 and lun2==0 and lun3==0:
            self.errormsg("You didn't select any lunch food item!!")
        elif lun!=0 and q11==0 or q11!=0 and lun==0:
            self.errormsg("You missed selecting quantities of your lunch food")
        elif lun1!=0 and q22==0 or q22!=0 and lun1==0:
            self.errormsg("You missed selecting quantities of your lunch food")
        elif lun2!=0 and q33==0 or q33!=0 and lun2==0:
            self.errormsg("You missed selecting quantities of your lunch food")
        elif lun3!=0 and q44==0 or q44!=0 and lun3==0:
            self.errormsg("You missed selecting quantities of your lunch food")
        elif di==0 and di1==0 and di2==0 and di3==0:
            self.errormsg("You didn't select any dinner food item!!")
        elif di!=0 and q111==0 or q111!=0 and di==0:
            self.errormsg("You missed selecting quantities of your dinner food")
        elif di1!=0 and q222==0 or q222!=0 and di1==0:
            self.errormsg("You missed selecting quantities of your dinner food")
        elif di2!=0 and q333==0 or q333!=0 and di2==0:
            self.errormsg("You missed selecting quantities of your dinner food")
        elif di3!=0 and q444==0 or q444!=0 and di3==0:
            self.errormsg("You missed selecting quantities of your dinner food")
        elif gender==1 and gok==0:
            self.checkgestational()
        else:
            idd = idd + 1
            name = ''.join(str(ord(c)) for c in self.le0.text())[:6]
            age = int(self.le1.text())
            wgt = int(self.lee.text())
            h = int(self.lhe.text())/100

            today = str(date.today())
            timeh = strftime("%H:%M:%S")
            timeh = timeh.replace(':', '')
            csvname=''.join(str(ord(c)) for c in self.le0.text())[:6] + "0" + timeh
            
            try:
                con = sqlite3.connect('Patients_SQL.db')
                cursor = con.execute("SELECT Id from Patients")
                for row in cursor:
                    if row[0]==name:
                        val = self.checkid(row[0])
                        if val==1:
                            name = row[0]
                            flagg = 1
                            break;
                        else:
                            name = str(int(name) + random.randint(80, 90))
                            flagg = 0
                            break
                con.close()
            
            except sqlite3.Error as error:
                print("Error with sqlite", error)

            bm = {1:12, 2:20 ,3:35, 4:12}
            bmm = {1:40, 2:40, 3:52, 4:36}
            bb = {1:14 ,2:16 }
            bbm = {1:30 ,2:30 }
            fd = {1:8 ,2:17 ,3:46 ,4:51 }
            fdd = {1:69 ,2:66 ,3:72 ,4:57 }
            ff = {1:16 ,2:11 ,3:24 ,4:28 }
            fff = {1:38, 2:44, 3:52, 4:65 }
            
            p = {1:18 ,2:18 ,3:20}
            pp = {1:42, 2:22, 3:48}
            br = {1:14, 2:17, 3:16}
            brr = {1:30 ,2:50 ,3:47}
            r = {1:38, 2:35, 3:38}
            rr = {1:55, 2:55, 3:79}
            v = {1:30, 2:7, 3:3}
            vv = {1:78 ,2:48 ,3:10}
            
            wgt = int(self.lee.text())
            h = int(self.lhe.text())/100
            bmi = wgt / math.sqrt(h)
            
            print(br0)
            print(br1)
            print(br2)
            print(br3)
            
            """
            carb1 = q1*(bm[br0])+q2*(bb[br1])+q3*(ff[br2])+q4*(fd[br3])
            carb2 = q11*(p[lun])+q22*(br[lun1])+q33*(r[lun2])+q44*(v[lun3])
            carb3 = q111*(p[di])+q222*(br[di1])+q333*(r[di2])+q444*(v[di3])
            """
            
            
            if q1==0 or br0==0:
                carb1 = q2*(bb[br1])+q3*(ff[br2])+q4*(fd[br3])
            elif q2==0 or br1==0:
                carb1 = q1*(bm[br0])+q3*(ff[br2])+q4*(fd[br3])
            elif q3==0 or br2==0:
                carb1 = q1*(bm[br0])+q2*(bb[br1])+q4*(fd[br3])
            elif q4==0 or br3==0:
                carb1 = q1*(bm[br0])+q2*(bb[br1])+q3*(ff[br2])
            else:
                carb1 = q1*(bm[br0])+q2*(bb[br1])+q3*(ff[br2])+q4*(fd[br3])
            
            if q11==0 or lun==0:
                carb2 = q22*(br[lun1])+q33*(r[lun2])+q44*(v[lun3])
            elif q22==0 or lun1==0:
                carb2 = q11*(p[lun])+q33*(r[lun2])+q44*(v[lun3])
            elif q33==0 or lun2==0:
                carb2 = q11*(p[lun])+q22*(br[lun1])+q44*(v[lun3])
            elif q44==0 or lun3==0:
                carb2 = q11*(p[lun])+q22*(br[lun1])+q33*(r[lun2])
            else:
                carb2 = q11*(p[lun])+q22*(br[lun1])+q33*(r[lun2])+q44*(v[lun3])
                
            if q111==0 or di==0:
                carb3 = q222*(br[di1])+q333*(r[di2])+q444*(v[di3])
            elif q222==0 or di1==0:
                carb3 = q111*(p[di])+q333*(r[di2])+q444*(v[di3])
            elif q333==0 or di2==0:
                carb3 = q111*(p[di])+q222*(br[di1])+q444*(v[di3])
            elif q444==0 or di3==0:
                carb3 = q111*(p[di])+q222*(br[di1])+q333*(r[di2])
            else:
                carb3 = q111*(p[di])+q222*(br[di1])+q333*(r[di2])+q444*(v[di3])
            
                       
            gi1 = (q1*bm[br0]/carb1*bmm[br0]) + (q2*bb[br1]/carb1*bbm[br1]) + (q3*ff[br2]/carb1*fff[br2]) + (q4*fd[br3]/carb1*fdd[br3])
            gi2 = (q11*p[lun]/carb2*pp[lun]) + (q22*br[lun1]/carb2*brr[lun1]) + (q33*r[lun2]/carb2*rr[lun2]) + (q44*v[lun3]/carb2*vv[lun3])
            gi3 = (q111*p[di]/carb3*pp[di]) + (q222*br[di1]/carb3*brr[di1]) + (q333*r[di2]/carb3*rr[di2]) + (q444*v[di3]/carb3*vv[di3])
            
            if gender == 0:
                gi1 = gi1-(0.46 * bmi)
                gi2 = gi2-(0.46 * bmi)
                gi3 = gi3-(0.46 * bmi)
            elif gender == 1:
                gi1 = gi1-(0.81 * bmi)
                gi2 = gi2-(0.81 * bmi)
                gi3 = gi3-(0.81 * bmi)
            
            gs = (1/wgt) * 17.76
            bgr1 = ((carb1*(gi1/100))/(100*gs))*18
            bgr2 = ((carb2*(gi2/100))/(100*gs))*18
            bgr3 = ((carb3*(gi3/100))/(100*gs))*18
            maxccc=np.array([280,280,280,280,280,280,280,280,280,280,280,280,280,280,280,280,280,280,280,280,280,280,280,280])
            minccc=np.array([100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100])
            #xbxb=np.array([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23])
            minval='lower limit=100'
            maxval='upper limit=280'
            z1='Breakfast'
            z2='Lunch'
            z3='Dinner'
            with open( csvname+'.csv' ,'w', newline='') as csvfile:
                filewriter = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
                filewriter.writerow(["Hrs" , "Glucose Level (mg/dL)"])
                l=[]
                m=[]
                x= []
                y= []
                x_smooth = []
                y_smooth = []
                t = 0
                if gi1 > 70:
                    t = 1
                if gi1 <= 70:
                    t = 2
                t1 = 0
                if gi2 > 70:
                    t1 = 1
                if gi2 <= 70:
                    t1 = 2
                t2 = 0
                if gi3 > 70:
                    t2 = 1
                if gi3 <= 70:
                    t2 = 2
                for i in range(0,24):
                    #if i == b+t or i == lu+t1 or i == d+t2:
                        #l = [random.randrange(160, 180, 3) for i in range(60)]
                    if i >= 22 and i <= 24:
                        if age<6:
                            l = [random.randrange(130, 180, 15) for i in range(60)]
                        elif age>=6 and age<=12:
                            l = [random.randrange(130, 180, 15) for i in range(60)]
                        elif age>=13 and age<=19:
                            l = [random.randrange(130, 180, 15) for i in range(60)]
                        else:
                            l = [random.randrange(130, 180, 6) for i in range(60)]
                    elif i<4:
                        l = [random.randrange(140, 200, 8) for i in range(60)]
                        c=median(l)
                        temp = c
                        c = temp-0.05*temp  

                    elif i<=b:
                        l = [random.randrange(110, 160, 8) for i in range(60)]
                        c=0
                        c=median(l)
                        temp = c
                    elif i>b+t and i<lu+t1:
                        c = 0.075*temp + temp
                        temp = c
                    elif i>lu+t1 and i<d+t2:
                        c = 0.075*temp+ temp
                        temp = c
                    elif i == b+t:
                        c = temp+bgr1
                        temp = c
                    elif i == lu+t1:
                        c = temp+bgr2
                        temp = c
                    elif i == d+t2:
                        c = temp+bgr3
                        temp = c
                    m.append(int(c))
                    filewriter.writerow([i , int(c)])
                    
                y = np.array(m)
                x = np.arange(0, 24, 1)
                fig = plt.figure()
                #fig.patch.set_facecolor()
                ax = fig.add_subplot(111)
                ax1=plt.axes()
                ax.set_facecolor("lightgreen")
                x_smooth = np.linspace(x.min(),x.max(),300)
                spl = UnivariateSpline(x, y)
                plt.plot(x_smooth, spl(x_smooth), 'g', lw = 2)
                #xx1=[b,b]
                #xx2=[lu,lu]
                #xx3=[d,d]
                
                for x1,y3 in zip(x,y):
                        label = "{:.1f}".format(y3)
                        if(x1==b):
                            plt.annotate(label, # this is the text
                                        (x1,y3), # this is the point to label
                                        textcoords="offset points", # how to position the text
                                        xytext=(0,10), # distance from text to points (x,y)
                                        ha='center')
                            #yy1=[85,y3]
                            plt.plot([x1], [y3], marker='o', markersize=5, color="red")
                            #plt.plot(xx1,yy1,color="black")
                            plt.text(x1-0.5,88,z1)
                            
                        elif(x1==lu):
                            plt.annotate(label, # this is the text
                                        (x1,y3), # this is the point to label
                                        textcoords="offset points", # how to position the text
                                        xytext=(0,10), # distance from text to points (x,y)
                                        ha='center')
                            #yy2=[85,y3]
                            plt.plot([x1], [y3], marker='o', markersize=5, color="red")
                            #plt.plot(xx2,yy2,color="black")
                            plt.text(x1-0.5,88,z2)
                        elif(x1==d):
                            plt.annotate(label, # this is the text
                                        (x1,y3), # this is the point to label
                                        textcoords="offset points", # how to position the text
                                        xytext=(0,10), # distance from text to points (x,y)
                                        ha='center')
                            #yy3=[85,y3]
                            plt.plot([x1], [y3], marker='o', markersize=5, color="red")
                            #plt.plot(xx3,yy3,color="black")
                            plt.text(x1-0.5, 88,z3)
            gok=0  
          
            plt.plot(x,minccc,'red')
            plt.plot(x,maxccc,'red')
            plt.xlabel('Time (in hrs)') 
            plt.ylabel('Glucose Level (mg/dL)')
            maxm = "Max BGL is : "+str(np.max(y))
            minm = "Min BGL is : "+str(np.min(y))
            meanm = "Mean BGL is : "+str(round(np.mean(y),2))
            meanmm = round(np.mean(y),2)
            patientid = "Patient Id : "+str(name)
            d1 = date.today()
            date1="Date :"+str(d1)
            plt.text(0, np.max(y)+40, date1)
            plt.text(10, np.max(y)+40, patientid)
            plt.text(0, np.max(y), maxm)
            plt.text(0, np.max(y)-10, minm)
            plt.text(0, np.max(y)-20, meanm)
            plt.text(0, 270,maxval)
            plt.text(0, 90,minval)
            plt.xticks(np.arange(0, 25, 1)) 
            plt.yticks(np.arange(110, np.max(y)+30, 20)) 
            
            plt.show()

            try:
                conn = sqlite3.connect('Patients_SQL.db')
                conn.execute('''CREATE TABLE IF NOT EXISTS Patients (
                                Id TEXT PRIMARY KEY,
                                Age INTEGER NOT NULL,
                                Gender TEXT NOT NULL,
                                Height INTEGER NOT NULL,
                                Weight INTEGER NOT NULL,
                                BCarb INTEGER NOT NULL,
                                LCarb INTEGER NOT NULL,
                                DCarb INTEGER NOT NULL);''')
                if flagg==0:
                    conn.execute("INSERT INTO Patients (Id,Age,Gender,Height,Weight,BCarb,LCarb,DCarb) VALUES (?,?,?,?,?,?,?,?)", (name,age,gender,h,wgt,carb1,carb2,carb3));
                    conn.commit()
                cursor = conn.execute("SELECT Id,Age,Gender,Height,Weight,BCarb,LCarb,DCarb from Patients")
                for row in cursor:
                    print(row[0] + " " + str(row[1]) + " " + row[2] + " " + str(row[3]) + " " + str(row[4]) + " " + str(row[5]) + " " + str(row[6]) + " " + str(row[7]))
                    #print("\n")
                conn.close()
                
            except sqlite3.Error as error:
                print("Error with sqlite", error)
                
            try:
                conn1 = sqlite3.connect('Patients_SQL.db')   
                conn1.execute('''CREATE TABLE IF NOT EXISTS GlucoseConcentration (
                                Id TEXT,
                                Date TEXT,
                                Time TEXT,
                                '0' TEXT NOT NULL,
                                '4' TEXT NOT NULL,
                                '8' TEXT NOT NULL,
                                '12' TEXT NOT NULL,
                                '16' TEXT NOT NULL,
                                '20' TEXT NOT NULL,
                                '23' TEXT NOT NULL,
                                BGL REAL NOT NULL);''')
                                #FOREIGN KEY(Id) REFERENCES Patients(Id));''')
                conn1.execute("INSERT INTO GlucoseConcentration (Id,Date,Time,'0','4','8','12','16','20','23',BGL) VALUES (?,?,?,?,?,?,?,?,?,?,?)", (name,today,timeh,str(y[0]),str(y[4]),str(y[8]),str(y[12]),str(y[16]),str(y[20]),str(y[23]),meanmm));
                conn1.commit()
                conn1.close()

            except sqlite3.Error as error:
                print("Error with sqlite", error)

            del x
            del y
            del x_smooth
            del y_smooth
            del l
    
            blueflag=1
            
            access_token = '_-RInQojwQUAAAAAAAACm-l4OP0CnI42j2vccOdsDYuoaDmvxcGvQvo8xuVVItpu'
            file_from = csvname+'.csv'
            target = "/"+today+"/"              # the target folder
            file_to = target + file_from
            def upload_file(file_from, file_to):
                dbx = dropbox.Dropbox(access_token)
                f = open(file_from, 'rb')
                dbx.files_upload(f.read(), file_to)
            upload_file(file_from,file_to)


app = QtWidgets.QApplication(sys.argv)
a_window = Window()
sys.exit(app.exec_())