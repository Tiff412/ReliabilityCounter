# -*- coding: utf-8 -*-

import sys
from PyQt5 import QtWidgets
import os
import UI

class ReliabilityApp (QtWidgets.QMainWindow, UI.Ui_Reliability):
    def __init__(self):
        # ��� ����� ����� ��� ������� � ����������, �������
        # � �.�. � ����� design.py
        super().__init__()
        self.setupUi(self)  # ��� ����� ��� ������������� ������ �������
#         self.buttonProcess.clicked.connect(countReliability)
        self.initUI()
        self.initConnectors()

    def initUI(self):

        self.statusBar.showMessage('Приветствую!')

        self.setGeometry(300, 300, 250, 150)
        self.show()

    def initConnectors(self):
        self.buttonProcess.clicked.connect(self.countReliability)
        
    def workTime_change(self):
        self.fullWork_value.valueChanged()
        
    def countReliability(self):
        self.statusBar.showMessage("Message in statusbar.")
        self.show()

def main():
    app = QtWidgets.QApplication(sys.argv)  # ����� ��������� QApplication
    window = ReliabilityApp()  # ������ ������ ������ ReliabilityApp
    window.show()  # ���������� ����
    app.exec()  # � ��������� ����������

if __name__ == '__main__':  # ���� �� ��������� ���� ��������, � �� �����������
    main()  # �� ��������� ������� main()
