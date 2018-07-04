# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'SubModuleWindow.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Reliability(object):
    def setupUi(self, Reliability):
        
        Reliability.setObjectName("Reliability")
        Reliability.resize(640, 440)
        Reliability.setMinimumSize(QtCore.QSize(640, 440))
        
        self.centralWidget = QtWidgets.QWidget(Reliability)
        self.centralWidget.setObjectName("centralWidget")
        self.centralWidget.setMinimumSize(QtCore.QSize(640, 56))
        
        self.mainHorizontalLayout = QtWidgets.QHBoxLayout(Reliability)
        self.mainHorizontalLayout.setObjectName("mainHorizontalLayout")
        self.centralWidget.setLayout(self.mainHorizontalLayout)
        
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        
        # Work Propreties
        self.workPropreties_groupBox = QtWidgets.QGroupBox(Reliability)
        self.workPropreties_groupBox.setMinimumSize(QtCore.QSize(620, 80))
        self.workPropreties_groupBox.setObjectName("workPropreties_groupBox")
        self.workPropreties_groupBox.setStyleSheet('''QGroupBox {font-weight: bold;}''')
        
#         self.horizontalLayout_9 = QtWidgets.QHBoxLayout(self.workPropreties_groupBox)
#         self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        
        self.workPropreties_hLayout = QtWidgets.QHBoxLayout(self.workPropreties_groupBox)
        self.workPropreties_hLayout.setObjectName("workPropreties_hLayout")
        
        self.FullWork_groupBox = QtWidgets.QGroupBox(self.workPropreties_groupBox)
        self.FullWork_groupBox.setMinimumSize(QtCore.QSize(200, 50))
        self.FullWork_groupBox.setObjectName("FullWork_groupBox")
        
        self.fullWork_value = QtWidgets.QDoubleSpinBox(self.FullWork_groupBox)
        self.fullWork_value.setGeometry(QtCore.QRect(10, 20, 151, 21))
        self.fullWork_value.setMaximum(100.0)
        self.fullWork_value.setSingleStep(0.01)
        self.fullWork_value.setObjectName("fullWork_value")
        
        self.PartWork_groupBox = QtWidgets.QGroupBox(self.workPropreties_groupBox)
        self.PartWork_groupBox.setMinimumSize(QtCore.QSize(200, 50))
        self.PartWork_groupBox.setObjectName("PartWork_groupBox")
        
        self.partWork_value = QtWidgets.QDoubleSpinBox(self.PartWork_groupBox)
        self.partWork_value.setGeometry(QtCore.QRect(10, 20, 151, 21))
        self.partWork_value.setMaximum(100.0)
        self.partWork_value.setSingleStep(0.01)
        self.partWork_value.setObjectName("partWork_value")
        
        self.Sleep_groupBox = QtWidgets.QGroupBox(self.workPropreties_groupBox)
        self.Sleep_groupBox.setMinimumSize(QtCore.QSize(200, 50))
        self.Sleep_groupBox.setObjectName("Sleep_groupBox")
        
        self.sleep_value = QtWidgets.QDoubleSpinBox(self.Sleep_groupBox)
        self.sleep_value.setGeometry(QtCore.QRect(10, 20, 151, 21))
        self.sleep_value.setMaximum(100.0)
        self.sleep_value.setSingleStep(0.01)
        self.sleep_value.setObjectName("sleep_value")
        
        self.workPropreties_hLayout.addWidget(self.FullWork_groupBox)
        self.workPropreties_hLayout.addWidget(self.PartWork_groupBox)
        self.workPropreties_hLayout.addWidget(self.Sleep_groupBox)
#         self.horizontalLayout_9.addLayout(self.workPropreties_hLayout)
        # ---
        
        # Reliability elements parameters
        self.Reliabiliry_groupBox = QtWidgets.QGroupBox(Reliability)
        self.Reliabiliry_groupBox.setMinimumSize(QtCore.QSize(620, 200))
        self.Reliabiliry_groupBox.setObjectName("Reliabiliry_groupBox")
        
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.Reliabiliry_groupBox)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        
        self.relStrategy_label = QtWidgets.QLabel(self.Reliabiliry_groupBox)
        self.relStrategy_label.setObjectName("relStrategy_label")
        
        self.reliabilityStrategy = QtWidgets.QComboBox(self.Reliabiliry_groupBox)
        self.reliabilityStrategy.setObjectName("reliabilityStrategy")
        self.reliabilityStrategy.addItem("0")
        self.reliabilityStrategy.addItem("1")
        self.reliabilityStrategy.addItem("2")
        self.reliabilityStrategy.addItem("3")
        
        self.horizontalLayout.addWidget(self.relStrategy_label)
        self.horizontalLayout.addWidget(self.reliabilityStrategy)
        
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        
        self.numbRes_label = QtWidgets.QLabel(self.Reliabiliry_groupBox)
        self.numbRes_label.setObjectName("numbRes_label")
        
        self.spinBox_RedundancyNumber = QtWidgets.QSpinBox(self.Reliabiliry_groupBox)
        self.spinBox_RedundancyNumber.setMaximum(2)
        self.spinBox_RedundancyNumber.setProperty("value", 1)
        self.spinBox_RedundancyNumber.setObjectName("spinBox_RedundancyNumber")
        
        self.horizontalLayout_4.addWidget(self.numbRes_label)
        self.horizontalLayout_4.addWidget(self.spinBox_RedundancyNumber)
        
        self.element_hLayout = QtWidgets.QHBoxLayout()
        self.element_hLayout.setObjectName("element_hLayout")
        
        self.element_Propreties = QtWidgets.QTabWidget(self.Reliabiliry_groupBox)
        self.element_Propreties.setMinimumSize(QtCore.QSize(600, 80))
        self.element_Propreties.setObjectName("element_Propreties")
        
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.element_Propreties.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.element_Propreties.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.element_Propreties.addTab(self.tab_3, "")
        
        # ---
        self.mainElement_layout = QtWidgets.QGridLayout(self.tab)
#         self.mainElement_layout.setContentsMargins(0, 0, 0, 0)
        self.mainElement_layout.setObjectName("mainElement_layout")
        
        self.fullRelMainElement_groupBox = QtWidgets.QGroupBox(Reliability)
        self.fullRelMainElement_groupBox.setMinimumSize(QtCore.QSize(180, 40))
        self.fullRelMainElement_groupBox.setObjectName("fullRelMainElement_groupBox")
        
        self.horizontalLayout_mf = QtWidgets.QHBoxLayout(self.fullRelMainElement_groupBox)
        self.horizontalLayout_mf.setObjectName("horizontalLayout_mf")
        
        self.spinBox_fullRelMainElement = QtWidgets.QDoubleSpinBox(self.fullRelMainElement_groupBox)
        self.spinBox_fullRelMainElement.setMaximum(10.0)
        self.spinBox_fullRelMainElement.setSingleStep(0.1)
        self.spinBox_fullRelMainElement.setProperty("value", 1.0)
        self.spinBox_fullRelMainElement.setObjectName("spinBox_fullRelMainElement")
        
        self.spinBox_fullRelPowerMainElement = QtWidgets.QSpinBox(self.fullRelMainElement_groupBox)
        self.spinBox_fullRelPowerMainElement.setMaximum(0)
        self.spinBox_fullRelPowerMainElement.setMinimum(-12)
        self.spinBox_fullRelPowerMainElement.setSingleStep(1)
        self.spinBox_fullRelPowerMainElement.setProperty("value", -6)
        self.spinBox_fullRelPowerMainElement.setObjectName("spinBox_fullRelPowerMainElement")
        
        self.horizontalLayout_mf.addWidget(self.spinBox_fullRelMainElement)
        self.horizontalLayout_mf.addWidget(self.spinBox_fullRelPowerMainElement)
        
        self.partRelMainElement_groupBox = QtWidgets.QGroupBox(Reliability)
        self.partRelMainElement_groupBox.setMinimumSize(QtCore.QSize(180, 40))
        self.partRelMainElement_groupBox.setObjectName("partRelMainElement_groupBox")
        
        self.horizontalLayout_mp = QtWidgets.QHBoxLayout(self.partRelMainElement_groupBox)
        self.horizontalLayout_mp.setObjectName("horizontalLayout_mp")
        
        self.spinBox_partRelMainElement = QtWidgets.QDoubleSpinBox(self.partRelMainElement_groupBox)
        self.spinBox_partRelMainElement.setMaximum(10.0)
        self.spinBox_partRelMainElement.setSingleStep(0.1)
        self.spinBox_partRelMainElement.setProperty("value", 1.0)
        self.spinBox_partRelMainElement.setObjectName("spinBox_partRelMainElement")
        
        self.spinBox_partRelPowerMainElement = QtWidgets.QSpinBox(self.partRelMainElement_groupBox)
        self.spinBox_partRelPowerMainElement.setMaximum(0)
        self.spinBox_partRelPowerMainElement.setMinimum(-12)
        self.spinBox_partRelPowerMainElement.setSingleStep(1)
        self.spinBox_partRelPowerMainElement.setProperty("value", -6)
        self.spinBox_partRelPowerMainElement.setObjectName("spinBox_partRelPowerMainElement")
        
        self.horizontalLayout_mp.addWidget(self.spinBox_partRelMainElement)
        self.horizontalLayout_mp.addWidget(self.spinBox_partRelPowerMainElement)
        
        self.sleepRelMainElement_groupBox = QtWidgets.QGroupBox(Reliability)
        self.sleepRelMainElement_groupBox.setMinimumSize(QtCore.QSize(180, 40))
        self.sleepRelMainElement_groupBox.setObjectName("sleepRelMainElement_groupBox")
        
        self.horizontalLayout_ms = QtWidgets.QHBoxLayout(self.sleepRelMainElement_groupBox)
        self.horizontalLayout_ms.setObjectName("horizontalLayout_ms")
        
        self.spinBox_sleepRelMainElement = QtWidgets.QDoubleSpinBox(self.sleepRelMainElement_groupBox)
        self.spinBox_sleepRelMainElement.setMaximum(10.0)
        self.spinBox_sleepRelMainElement.setSingleStep(0.1)
        self.spinBox_sleepRelMainElement.setProperty("value", 1.0)
        self.spinBox_sleepRelMainElement.setObjectName("spinBox_sleepRelMainElement")
        
        self.spinBox_sleepRelPowerMainElement = QtWidgets.QSpinBox(self.sleepRelMainElement_groupBox)
        self.spinBox_sleepRelPowerMainElement.setMaximum(0)
        self.spinBox_sleepRelPowerMainElement.setMinimum(-12)
        self.spinBox_sleepRelPowerMainElement.setSingleStep(1)
        self.spinBox_sleepRelPowerMainElement.setProperty("value", -6)
        self.spinBox_sleepRelPowerMainElement.setObjectName("spinBox_sleepRelPowerMainElement")
        
        self.horizontalLayout_ms.addWidget(self.spinBox_sleepRelMainElement)
        self.horizontalLayout_ms.addWidget(self.spinBox_sleepRelPowerMainElement)
        
        self.mainElement_layout.addWidget(self.fullRelMainElement_groupBox, 0, 0)
        self.mainElement_layout.addWidget(self.partRelMainElement_groupBox, 0, 1)
        self.mainElement_layout.addWidget(self.sleepRelMainElement_groupBox, 0, 2)
        
        # ---
        self.redElement1_layout = QtWidgets.QGridLayout(self.tab_2)
#         self.redElement1_layout.setContentsMargins(0, 0, 0, 0)
        self.redElement1_layout.setObjectName("redElement1_layout")
        
        self.fullRelredElement1_groupBox = QtWidgets.QGroupBox(Reliability)
        self.fullRelredElement1_groupBox.setMinimumSize(QtCore.QSize(180, 40))
        self.fullRelredElement1_groupBox.setObjectName("fullRelredElement1_groupBox")
        
        self.horizontalLayout_r1f = QtWidgets.QHBoxLayout(self.fullRelredElement1_groupBox)
        self.horizontalLayout_r1f.setObjectName("horizontalLayout_r1f")
        
        self.spinBox_fullRelredElement1 = QtWidgets.QDoubleSpinBox(self.fullRelredElement1_groupBox)
        self.spinBox_fullRelredElement1.setMaximum(10.0)
        self.spinBox_fullRelredElement1.setSingleStep(0.1)
        self.spinBox_fullRelredElement1.setProperty("value", 1.0)
        self.spinBox_fullRelredElement1.setObjectName("spinBox_fullRelredElement1")
        
        self.spinBox_fullRelPowerredElement1 = QtWidgets.QSpinBox(self.fullRelredElement1_groupBox)
        self.spinBox_fullRelPowerredElement1.setMaximum(0)
        self.spinBox_fullRelPowerredElement1.setMinimum(-12)
        self.spinBox_fullRelPowerredElement1.setSingleStep(1)
        self.spinBox_fullRelPowerredElement1.setProperty("value", -6)
        self.spinBox_fullRelPowerredElement1.setObjectName("spinBox_fullRelPowerredElement1")
        
        self.horizontalLayout_r1f.addWidget(self.spinBox_fullRelredElement1)
        self.horizontalLayout_r1f.addWidget(self.spinBox_fullRelPowerredElement1)
        
        self.partRelredElement1_groupBox = QtWidgets.QGroupBox(Reliability)
        self.partRelredElement1_groupBox.setMinimumSize(QtCore.QSize(180, 40))
        self.partRelredElement1_groupBox.setObjectName("partRelredElement1_groupBox")
        
        self.horizontalLayout_r1p = QtWidgets.QHBoxLayout(self.partRelredElement1_groupBox)
        self.horizontalLayout_r1p.setObjectName("horizontalLayout_r1p")
        
        self.spinBox_partRelredElement1 = QtWidgets.QDoubleSpinBox(self.partRelredElement1_groupBox)
        self.spinBox_partRelredElement1.setMaximum(10.0)
        self.spinBox_partRelredElement1.setSingleStep(0.1)
        self.spinBox_partRelredElement1.setProperty("value", 1.0)
        self.spinBox_partRelredElement1.setObjectName("spinBox_partRelredElement1")
        
        self.spinBox_partRelPowerredElement1 = QtWidgets.QSpinBox(self.partRelredElement1_groupBox)
        self.spinBox_partRelPowerredElement1.setMaximum(0)
        self.spinBox_partRelPowerredElement1.setMinimum(-12)
        self.spinBox_partRelPowerredElement1.setSingleStep(1)
        self.spinBox_partRelPowerredElement1.setProperty("value", -6)
        self.spinBox_partRelPowerredElement1.setObjectName("spinBox_partRelPowerredElement1")
        
        self.horizontalLayout_r1p.addWidget(self.spinBox_partRelredElement1)
        self.horizontalLayout_r1p.addWidget(self.spinBox_partRelPowerredElement1)
        
        self.sleepRelredElement1_groupBox = QtWidgets.QGroupBox(Reliability)
        self.sleepRelredElement1_groupBox.setMinimumSize(QtCore.QSize(180, 40))
        self.sleepRelredElement1_groupBox.setObjectName("sleepRelredElement1_groupBox")
        
        self.horizontalLayout_r1s = QtWidgets.QHBoxLayout(self.sleepRelredElement1_groupBox)
        self.horizontalLayout_r1s.setObjectName("horizontalLayout_r1s")
        
        self.spinBox_sleepRelredElement1 = QtWidgets.QDoubleSpinBox(self.sleepRelredElement1_groupBox)
        self.spinBox_sleepRelredElement1.setMaximum(10.0)
        self.spinBox_sleepRelredElement1.setSingleStep(0.1)
        self.spinBox_sleepRelredElement1.setProperty("value", 1.0)
        self.spinBox_sleepRelredElement1.setObjectName("spinBox_sleepRelredElement1")
        
        self.spinBox_sleepRelPowerredElement1 = QtWidgets.QSpinBox(self.sleepRelredElement1_groupBox)
        self.spinBox_sleepRelPowerredElement1.setMaximum(0)
        self.spinBox_sleepRelPowerredElement1.setMinimum(-12)
        self.spinBox_sleepRelPowerredElement1.setSingleStep(1)
        self.spinBox_sleepRelPowerredElement1.setProperty("value", -6)
        self.spinBox_sleepRelPowerredElement1.setObjectName("spinBox_sleepRelPowerredElement1")
        
        self.horizontalLayout_r1s.addWidget(self.spinBox_sleepRelredElement1)
        self.horizontalLayout_r1s.addWidget(self.spinBox_sleepRelPowerredElement1)
        
        self.redElement1_layout.addWidget(self.fullRelredElement1_groupBox, 0, 0)
        self.redElement1_layout.addWidget(self.partRelredElement1_groupBox, 0, 1)
        self.redElement1_layout.addWidget(self.sleepRelredElement1_groupBox, 0, 2)
        
        
        # ---
        self.redElement2_layout = QtWidgets.QGridLayout(self.tab_3)
#         self.redElement2_layout.setContentsMargins(0, 0, 0, 0)
        self.redElement2_layout.setObjectName("redElement2_layout")
        
        self.fullRelredElement2_groupBox = QtWidgets.QGroupBox(Reliability)
        self.fullRelredElement2_groupBox.setMinimumSize(QtCore.QSize(180, 40))
        self.fullRelredElement2_groupBox.setObjectName("fullRelredElement2_groupBox")
        
        self.horizontalLayout_r2f = QtWidgets.QHBoxLayout(self.fullRelredElement2_groupBox)
        self.horizontalLayout_r2f.setObjectName("horizontalLayout_r2f")
        
        self.spinBox_fullRelredElement2 = QtWidgets.QDoubleSpinBox(self.fullRelredElement2_groupBox)
        self.spinBox_fullRelredElement2.setMaximum(10.0)
        self.spinBox_fullRelredElement2.setSingleStep(0.1)
        self.spinBox_fullRelredElement2.setProperty("value", 1.0)
        self.spinBox_fullRelredElement2.setObjectName("spinBox_fullRelredElement2")
        
        self.spinBox_fullRelPowerredElement2 = QtWidgets.QSpinBox(self.fullRelredElement2_groupBox)
        self.spinBox_fullRelPowerredElement2.setMaximum(0)
        self.spinBox_fullRelPowerredElement2.setMinimum(-12)
        self.spinBox_fullRelPowerredElement2.setSingleStep(1)
        self.spinBox_fullRelPowerredElement2.setProperty("value", -6)
        self.spinBox_fullRelPowerredElement2.setObjectName("spinBox_fullRelPowerredElement2")
        
        self.horizontalLayout_r2f.addWidget(self.spinBox_fullRelredElement2)
        self.horizontalLayout_r2f.addWidget(self.spinBox_fullRelPowerredElement2)
        
        self.partRelredElement2_groupBox = QtWidgets.QGroupBox(Reliability)
        self.partRelredElement2_groupBox.setMinimumSize(QtCore.QSize(180, 40))
        self.partRelredElement2_groupBox.setObjectName("partRelredElement2_groupBox")
        
        self.horizontalLayout_r2p = QtWidgets.QHBoxLayout(self.partRelredElement2_groupBox)
        self.horizontalLayout_r2p.setObjectName("horizontalLayout_r2p")
        
        self.spinBox_partRelredElement2 = QtWidgets.QDoubleSpinBox(self.partRelredElement2_groupBox)
        self.spinBox_partRelredElement2.setMaximum(10.0)
        self.spinBox_partRelredElement2.setSingleStep(0.1)
        self.spinBox_partRelredElement2.setProperty("value", 1.0)
        self.spinBox_partRelredElement2.setObjectName("spinBox_partRelredElement2")
        
        self.spinBox_partRelPowerredElement2 = QtWidgets.QSpinBox(self.partRelredElement2_groupBox)
        self.spinBox_partRelPowerredElement2.setMaximum(0)
        self.spinBox_partRelPowerredElement2.setMinimum(-12)
        self.spinBox_partRelPowerredElement2.setSingleStep(1)
        self.spinBox_partRelPowerredElement2.setProperty("value", -6)
        self.spinBox_partRelPowerredElement2.setObjectName("spinBox_partRelPowerredElement2")
        
        self.horizontalLayout_r2p.addWidget(self.spinBox_partRelredElement2)
        self.horizontalLayout_r2p.addWidget(self.spinBox_partRelPowerredElement2)
        
        self.sleepRelredElement2_groupBox = QtWidgets.QGroupBox(Reliability)
        self.sleepRelredElement2_groupBox.setMinimumSize(QtCore.QSize(180, 40))
        self.sleepRelredElement2_groupBox.setObjectName("sleepRelredElement2_groupBox")
        
        self.horizontalLayout_r2s = QtWidgets.QHBoxLayout(self.sleepRelredElement2_groupBox)
        self.horizontalLayout_r2s.setObjectName("horizontalLayout_r2s")
        
        self.spinBox_sleepRelredElement2 = QtWidgets.QDoubleSpinBox(self.sleepRelredElement2_groupBox)
        self.spinBox_sleepRelredElement2.setMaximum(10.0)
        self.spinBox_sleepRelredElement2.setSingleStep(0.1)
        self.spinBox_sleepRelredElement2.setProperty("value", 1.0)
        self.spinBox_sleepRelredElement2.setObjectName("spinBox_sleepRelredElement2")
        
        self.spinBox_sleepRelPowerredElement2 = QtWidgets.QSpinBox(self.sleepRelredElement2_groupBox)
        self.spinBox_sleepRelPowerredElement2.setMaximum(0)
        self.spinBox_sleepRelPowerredElement2.setMinimum(-12)
        self.spinBox_sleepRelPowerredElement2.setSingleStep(1)
        self.spinBox_sleepRelPowerredElement2.setProperty("value", -6)
        self.spinBox_sleepRelPowerredElement2.setObjectName("spinBox_sleepRelPowerredElement2")
        
        self.horizontalLayout_r2s.addWidget(self.spinBox_sleepRelredElement2)
        self.horizontalLayout_r2s.addWidget(self.spinBox_sleepRelPowerredElement2)
        
        self.redElement2_layout.addWidget(self.fullRelredElement2_groupBox, 0, 0)
        self.redElement2_layout.addWidget(self.partRelredElement2_groupBox, 0, 1)
        self.redElement2_layout.addWidget(self.sleepRelredElement2_groupBox, 0, 2)
        
#         ---

        self.element_hLayout.addWidget(self.element_Propreties)
        
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        
        self.workTime_label = QtWidgets.QLabel(self.Reliabiliry_groupBox)
        self.workTime_label.setObjectName("workTime_label")
        
        self.spinBox_workCycles = QtWidgets.QDoubleSpinBox(self.Reliabiliry_groupBox)
        self.spinBox_workCycles.setMaximum(100000.0)
        self.spinBox_workCycles.setSingleStep(0.01)
        self.spinBox_workCycles.setProperty("value", 1000.0)
        self.spinBox_workCycles.setObjectName("spinBox_workCycles")
        
        self.workCycles_label = QtWidgets.QLabel(self.Reliabiliry_groupBox)
        self.workCycles_label.setObjectName("workCycles_label")
        self.workCycles_label.setMaximumSize(QtCore.QSize(80, 80))
        
        self.spinBox_CycleTime = QtWidgets.QSpinBox(self.Reliabiliry_groupBox)
        self.spinBox_CycleTime.setMaximum(100000)
        self.spinBox_CycleTime.setSingleStep(1)
        self.spinBox_CycleTime.setProperty("value", 100)
        self.spinBox_CycleTime.setObjectName("spinBox_CycleTime")
        
        self.CycleTime_labelms = QtWidgets.QLabel(self.Reliabiliry_groupBox)
        self.CycleTime_labelms.setObjectName("CycleTime_labelms")
        self.CycleTime_labelms.setMaximumSize(QtCore.QSize(20, 20))
        
        self.output_groupBox = QtWidgets.QGroupBox(self.workPropreties_groupBox)
        self.output_groupBox.setMinimumSize(QtCore.QSize(620, 50))
        self.output_groupBox.setObjectName("Output_groupBox")
        
        self.output_hLayout = QtWidgets.QHBoxLayout(self.output_groupBox)
        self.output_hLayout.setObjectName("output_hLayout")
        
        self.buttonProcess = QtWidgets.QPushButton(self.output_groupBox)
        self.buttonProcess.setMinimumHeight(40)
        self.buttonProcess.setObjectName("buttonProcess")
        
        self.Process_textBrowser = QtWidgets.QTextBrowser(self.output_groupBox)
        self.Process_textBrowser.setMaximumSize(QtCore.QSize(500, 40))
        self.Process_textBrowser.setObjectName("Process_textBrowser")
        
        self.output_hLayout.addWidget(self.buttonProcess)
        self.output_hLayout.addWidget(self.Process_textBrowser)
        
        self.horizontalLayout_8.addWidget(self.workTime_label)
        self.horizontalLayout_8.addWidget(self.spinBox_workCycles)
        self.horizontalLayout_8.addWidget(self.workCycles_label, 0, QtCore.Qt.AlignRight)
        self.horizontalLayout_8.addWidget(self.spinBox_CycleTime)
        self.horizontalLayout_8.addWidget(self.CycleTime_labelms, 0, QtCore.Qt.AlignRight)
        
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.verticalLayout_2.addLayout(self.horizontalLayout_4)
        self.verticalLayout_2.addLayout(self.element_hLayout)
        self.verticalLayout_2.addLayout(self.output_hLayout)
        
        self.verticalLayout.addWidget(self.workPropreties_groupBox)
        self.verticalLayout.addWidget(self.Reliabiliry_groupBox)
        self.verticalLayout.addLayout(self.horizontalLayout_8)
        self.verticalLayout.addWidget(self.output_groupBox)
        self.mainHorizontalLayout.addLayout(self.verticalLayout)
        
        self.statusBar = QtWidgets.QStatusBar(Reliability)
        self.statusBar.setObjectName("statusBar")
        self.statusBar.setStyleSheet('''QStatusBar{background:rgba(220,220,220,255);color:black;font-weight:bold;}''')
        Reliability.setStatusBar(self.statusBar)

        Reliability.setCentralWidget(self.centralWidget)
        self.retranslateUi(Reliability)
        self.element_Propreties.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Reliability)

    def retranslateUi(self, Reliability):
        _translate = QtCore.QCoreApplication.translate
        
        Reliability.setWindowTitle(_translate("Reliability", "Расчет надежности модуля"))
        
        self.workPropreties_groupBox.setTitle(_translate("Reliability", "Параметры нагрузки элементов (в процентах времени работы)"))
        self.FullWork_groupBox.setTitle(_translate("Reliability", "Полная нагрузка"))
        self.PartWork_groupBox.setTitle(_translate("Reliability", "Частичная нагрузка"))
        self.Sleep_groupBox.setTitle(_translate("Reliability", "Простой"))
        self.Reliabiliry_groupBox.setTitle(_translate("Reliability", "Резервирование"))
        
        self.relStrategy_label.setText(_translate("Reliability", "Выбор стратегии резервирования для модуля:"))
        self.reliabilityStrategy.setItemText(0, _translate("Reliability", "Отсутствие резервирования"))
        self.reliabilityStrategy.setItemText(1, _translate("Reliability", "Горячее резервирование"))
        self.reliabilityStrategy.setItemText(2, _translate("Reliability", "Теплое резервирование"))
        self.reliabilityStrategy.setItemText(3, _translate("Reliability", "Холодное резервирование"))
        
        self.numbRes_label.setText(_translate("Reliability", "Количество резеврных элементов"))
        
        self.element_Propreties.setTabText(self.element_Propreties.indexOf(self.tab), _translate("Reliability", "Основной элемент"))
        self.fullRelMainElement_groupBox.setTitle(_translate("Reliability", "Полная нагрузка"))
        self.partRelMainElement_groupBox.setTitle(_translate("Reliability", "Частичная нагрузка"))
        self.sleepRelMainElement_groupBox.setTitle(_translate("Reliability", "Простой"))
        self.element_Propreties.setTabText(self.element_Propreties.indexOf(self.tab_2), _translate("Reliability", "Запасной элемент №1"))
        self.fullRelredElement1_groupBox.setTitle(_translate("Reliability", "Полная нагрузка"))
        self.partRelredElement1_groupBox.setTitle(_translate("Reliability", "Частичная нагрузка"))
        self.sleepRelredElement1_groupBox.setTitle(_translate("Reliability", "Простой"))
        self.element_Propreties.setTabText(self.element_Propreties.indexOf(self.tab_3), _translate("Reliability", "Запасной элемент №2"))
        self.fullRelredElement2_groupBox.setTitle(_translate("Reliability", "Полная нагрузка"))
        self.partRelredElement2_groupBox.setTitle(_translate("Reliability", "Частичная нагрузка"))
        self.sleepRelredElement2_groupBox.setTitle(_translate("Reliability", "Простой"))
        
        self.workTime_label.setText(_translate("Reliability", "Время работы подсистемы"))
        self.workCycles_label.setText(_translate("Reliability", "Заданий по "))
        self.CycleTime_labelms.setText(_translate("Reliability", "мкс"))
        
        self.output_groupBox.setTitle(_translate("Reliability", "Вывод"))
        self.buttonProcess.setText(_translate("Reliability", "Расчитать"))
        
        
    def shadowUnusable(self, Reliability):
        if self.reliabilityStrategy.currentIndex() == 0 :
            self.spinBox_RedundancyNumber.setEnabled(False)
            
