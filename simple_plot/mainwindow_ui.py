# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/maciek/Dokumenty/OpenSource/simple-plot/simple_plot/mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1212, 684)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icon.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.central_widget = QtWidgets.QWidget(MainWindow)
        self.central_widget.setObjectName("central_widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.central_widget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.sidebar = QtWidgets.QGridLayout()
        self.sidebar.setObjectName("sidebar")
        self.xsymbol_label = QtWidgets.QLabel(self.central_widget)
        self.xsymbol_label.setObjectName("xsymbol_label")
        self.sidebar.addWidget(self.xsymbol_label, 1, 0, 1, 1)
        self.yheader = QtWidgets.QLabel(self.central_widget)
        self.yheader.setObjectName("yheader")
        self.sidebar.addWidget(self.yheader, 4, 0, 1, 2, QtCore.Qt.AlignHCenter)
        self.xunitlabel = QtWidgets.QLabel(self.central_widget)
        self.xunitlabel.setObjectName("xunitlabel")
        self.sidebar.addWidget(self.xunitlabel, 3, 0, 1, 1)
        self.xsymbol = QtWidgets.QLineEdit(self.central_widget)
        self.xsymbol.setObjectName("xsymbol")
        self.sidebar.addWidget(self.xsymbol, 1, 1, 1, 1)
        self.widget = QtWidgets.QWidget(self.central_widget)
        self.widget.setObjectName("widget")
        self.sidebar.addWidget(self.widget, 11, 0, 1, 2)
        self.yunit_label = QtWidgets.QLabel(self.central_widget)
        self.yunit_label.setObjectName("yunit_label")
        self.sidebar.addWidget(self.yunit_label, 7, 0, 1, 1)
        self.yunit = QtWidgets.QLineEdit(self.central_widget)
        self.yunit.setObjectName("yunit")
        self.sidebar.addWidget(self.yunit, 7, 1, 1, 1)
        self.xunit = QtWidgets.QLineEdit(self.central_widget)
        self.xunit.setObjectName("xunit")
        self.sidebar.addWidget(self.xunit, 3, 1, 1, 1)
        self.ysymbol_label = QtWidgets.QLabel(self.central_widget)
        self.ysymbol_label.setObjectName("ysymbol_label")
        self.sidebar.addWidget(self.ysymbol_label, 5, 0, 1, 1)
        self.yname = QtWidgets.QLineEdit(self.central_widget)
        self.yname.setText("")
        self.yname.setObjectName("yname")
        self.sidebar.addWidget(self.yname, 6, 1, 1, 1)
        self.ysymbol = QtWidgets.QLineEdit(self.central_widget)
        self.ysymbol.setObjectName("ysymbol")
        self.sidebar.addWidget(self.ysymbol, 5, 1, 1, 1)
        self.xheader = QtWidgets.QLabel(self.central_widget)
        self.xheader.setObjectName("xheader")
        self.sidebar.addWidget(self.xheader, 0, 0, 1, 2, QtCore.Qt.AlignHCenter)
        self.xname_label = QtWidgets.QLabel(self.central_widget)
        self.xname_label.setObjectName("xname_label")
        self.sidebar.addWidget(self.xname_label, 2, 0, 1, 1)
        self.xname = QtWidgets.QLineEdit(self.central_widget)
        self.xname.setObjectName("xname")
        self.sidebar.addWidget(self.xname, 2, 1, 1, 1)
        self.yname_label = QtWidgets.QLabel(self.central_widget)
        self.yname_label.setObjectName("yname_label")
        self.sidebar.addWidget(self.yname_label, 6, 0, 1, 1)
        self.fit_header = QtWidgets.QLabel(self.central_widget)
        self.fit_header.setObjectName("fit_header")
        self.sidebar.addWidget(self.fit_header, 8, 0, 1, 2, QtCore.Qt.AlignHCenter)
        self.intercept = QtWidgets.QLabel(self.central_widget)
        self.intercept.setText("")
        self.intercept.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextSelectableByKeyboard|QtCore.Qt.TextSelectableByMouse)
        self.intercept.setObjectName("intercept")
        self.sidebar.addWidget(self.intercept, 10, 1, 1, 1)
        self.slope = QtWidgets.QLabel(self.central_widget)
        self.slope.setText("")
        self.slope.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextSelectableByKeyboard|QtCore.Qt.TextSelectableByMouse)
        self.slope.setObjectName("slope")
        self.sidebar.addWidget(self.slope, 9, 1, 1, 1)
        self.alabel = QtWidgets.QLabel(self.central_widget)
        self.alabel.setObjectName("alabel")
        self.sidebar.addWidget(self.alabel, 9, 0, 1, 1)
        self.blabel = QtWidgets.QLabel(self.central_widget)
        self.blabel.setObjectName("blabel")
        self.sidebar.addWidget(self.blabel, 10, 0, 1, 1)
        self.sidebar.setRowStretch(11, 1)
        self.horizontalLayout.addLayout(self.sidebar)
        self.data_table = QtWidgets.QTableWidget(self.central_widget)
        self.data_table.setRowCount(1)
        self.data_table.setColumnCount(2)
        self.data_table.setObjectName("data_table")
        self.horizontalLayout.addWidget(self.data_table)
        self.plot_layout = QtWidgets.QVBoxLayout()
        self.plot_layout.setObjectName("plot_layout")
        self.horizontalLayout.addLayout(self.plot_layout)
        self.horizontalLayout.setStretch(1, 1)
        self.horizontalLayout.setStretch(2, 3)
        MainWindow.setCentralWidget(self.central_widget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1212, 34))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.xsymbol_label.setBuddy(self.xsymbol)
        self.xunitlabel.setBuddy(self.xunit)
        self.yunit_label.setBuddy(self.yunit)
        self.ysymbol_label.setBuddy(self.ysymbol)
        self.xname_label.setBuddy(self.xname)
        self.yname_label.setBuddy(self.yname)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.xsymbol, self.xname)
        MainWindow.setTabOrder(self.xname, self.xunit)
        MainWindow.setTabOrder(self.xunit, self.ysymbol)
        MainWindow.setTabOrder(self.ysymbol, self.yname)
        MainWindow.setTabOrder(self.yname, self.yunit)
        MainWindow.setTabOrder(self.yunit, self.data_table)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Simple Plot"))
        self.xsymbol_label.setText(_translate("MainWindow", "Symbol"))
        self.yheader.setText(_translate("MainWindow", "Vertical Axis"))
        self.xunitlabel.setText(_translate("MainWindow", "Unit"))
        self.xsymbol.setText(_translate("MainWindow", "x"))
        self.yunit_label.setText(_translate("MainWindow", "Unit"))
        self.ysymbol_label.setText(_translate("MainWindow", "Symbol"))
        self.ysymbol.setText(_translate("MainWindow", "y"))
        self.xheader.setText(_translate("MainWindow", "Horizontal Axis"))
        self.xname_label.setText(_translate("MainWindow", "Name"))
        self.yname_label.setText(_translate("MainWindow", "Name"))
        self.fit_header.setText(_translate("MainWindow", "Fit Results"))
        self.alabel.setText(_translate("MainWindow", "Slope:"))
        self.blabel.setText(_translate("MainWindow", "Intercept:"))
