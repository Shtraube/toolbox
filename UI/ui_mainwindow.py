# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 6.8.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QKeySequenceEdit, QLabel,
    QLineEdit, QMainWindow, QMenuBar, QPushButton,
    QSizePolicy, QSpinBox, QStatusBar, QToolButton,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setWindowModality(Qt.WindowModality.NonModal)
        MainWindow.resize(684, 440)
        MainWindow.setMinimumSize(QSize(684, 440))
        MainWindow.setMaximumSize(QSize(684, 440))
        font = QFont()
        font.setPointSize(12)
        font.setWeight(QFont.DemiBold)
        font.setStyleStrategy(QFont.PreferAntialias)
        MainWindow.setFont(font)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonIconOnly)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(500, 330, 171, 41))
        self.label_7 = QLabel(self.centralwidget)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(10, 10, 661, 161))
        self.label_7.setFrameShape(QFrame.Shape.Box)
        self.label_7.setLineWidth(2)
        self.pushButton_2 = QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(539, 270, 108, 28))
        self.toolButton = QToolButton(self.centralwidget)
        self.toolButton.setObjectName(u"toolButton")
        self.toolButton.setGeometry(QRect(512, 270, 28, 28))
        self.lineEdit = QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(130, 270, 381, 28))
        self.lineEdit.setInputMask(u"")
        self.lineEdit.setText(u"")
        self.lineEdit.setReadOnly(True)
        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(20, 270, 111, 28))
        self.label_4.setWordWrap(True)
        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(20, 190, 621, 71))
        self.label_5.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)
        self.label_5.setWordWrap(True)
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(20, 110, 158, 41))
        self.label_3.setTextFormat(Qt.TextFormat.PlainText)
        self.label_3.setWordWrap(True)
        self.keySequenceEdit = QKeySequenceEdit(self.centralwidget)
        self.keySequenceEdit.setObjectName(u"keySequenceEdit")
        self.keySequenceEdit.setGeometry(QRect(190, 120, 461, 28))
        self.keySequenceEdit.setMaximumSequenceLength(1)
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(20, 80, 104, 28))
        self.spinBox_2 = QSpinBox(self.centralwidget)
        self.spinBox_2.setObjectName(u"spinBox_2")
        self.spinBox_2.setGeometry(QRect(190, 80, 461, 28))
        self.spinBox_2.setMinimum(1)
        self.spinBox_2.setMaximum(3000)
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(20, 50, 105, 28))
        self.spinBox = QSpinBox(self.centralwidget)
        self.spinBox.setObjectName(u"spinBox")
        self.spinBox.setGeometry(QRect(190, 50, 461, 28))
        self.spinBox.setAccelerated(False)
        self.spinBox.setMinimum(1)
        self.spinBox.setMaximum(3000)
        self.label_6 = QLabel(self.centralwidget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(20, 20, 561, 22))
        self.label_6.setMaximumSize(QSize(16777215, 30))
        self.label_6.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)
        self.label_8 = QLabel(self.centralwidget)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(10, 180, 661, 141))
        self.label_8.setFrameShape(QFrame.Shape.Box)
        self.label_8.setLineWidth(2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.label_8.raise_()
        self.pushButton.raise_()
        self.label_7.raise_()
        self.pushButton_2.raise_()
        self.toolButton.raise_()
        self.lineEdit.raise_()
        self.label_4.raise_()
        self.label_5.raise_()
        self.label_3.raise_()
        self.keySequenceEdit.raise_()
        self.label_2.raise_()
        self.spinBox_2.raise_()
        self.label.raise_()
        self.spinBox.raise_()
        self.label_6.raise_()
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 684, 33))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"\u042f\u0449\u0438\u043a", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0430\u043a\u0440\u044b\u0442\u044c \u043f\u0440\u0438\u043b\u043e\u0436\u0435\u043d\u0438\u0435", None))
        self.label_7.setText("")
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"\u0423\u043f\u043e\u0440\u044f\u0434\u043e\u0447\u0438\u0442\u044c", None))
        self.toolButton.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u0423\u043a\u0430\u0436\u0438\u0442\u0435 \u043f\u0443\u0442\u044c...", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0431\u043e\u0440 \u043f\u0430\u043f\u043a\u0438", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"\u0424\u0443\u043d\u043a\u0446\u0438\u044f \u043f\u043e \u043f\u0435\u0440\u0435\u043d\u043e\u0441\u0443 \u0444\u0430\u0439\u043b\u043e\u0432 \u0432 \u0443\u043a\u0430\u0437\u0430\u043d\u043d\u043e\u0439 \u043f\u0430\u043f\u043a\u0435 \u0432 \u043d\u043e\u0432\u044b\u0435 \u043f\u0430\u043f\u043a\u0438 \u0441\u043e\u0433\u043b\u0430\u0441\u043d\u043e \u0442\u0438\u043f\u0443 \u043a\u0430\u0436\u0434\u043e\u0433\u043e \u0444\u0430\u0439\u043b\u0430. \u041f\u0440\u0438\u043c\u0435\u043d\u044f\u0439\u0442\u0435 \u044d\u0442\u0443 \u0444\u0443\u043d\u043a\u0446\u0438\u044e \u0441 \u043e\u0441\u0442\u043e\u0440\u043e\u0436\u043d\u043e\u0441\u0442\u044c\u044e: \u043d\u0435 \u0443\u043f\u043e\u0440\u044f\u0434\u043e\u0447\u0438\u0432\u0430\u0439\u0442\u0435 \u043f\u0430\u043f\u043a\u0438, \u0441\u043e\u0434\u0435\u0440\u0436\u0430\u0449\u0438\u0435 \u0441\u0438\u0441\u0442\u0435\u043c\u043d\u044b\u0435 \u0444\u0430\u0439\u043b\u044b \u0438\u043b\u0438 \u0444\u0430\u0439\u043b\u044b \u043f\u0440\u0438\u043b\u043e\u0436"
                        "\u0435\u043d\u0438\u0439", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\u041a\u043e\u043c\u0431\u0438\u043d\u0430\u0446\u0438\u044f \u043a\u043b\u0430\u0432\u0438\u0448 \u0434\u043b\u044f \u043f\u043e\u0438\u0441\u043a\u0430 \u043a\u0443\u0440\u0441\u043e\u0440\u0430", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u041a\u043e\u043e\u0440\u0434\u0438\u043d\u0430\u0442\u0430 Y", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u041a\u043e\u043e\u0440\u0434\u0438\u043d\u0430\u0442\u0430 \u0425", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"\u0424\u0443\u043d\u043a\u0446\u0438\u044f \u043f\u0435\u0440\u0435\u043c\u0435\u0449\u0435\u043d\u0438\u044f \u043a\u0443\u0440\u0441\u043e\u0440\u0430 \u043c\u044b\u0448\u0438 \u043f\u043e \u0437\u0430\u0434\u0430\u043d\u043d\u044b\u043c \u043a\u043e\u043e\u0440\u0434\u0438\u043d\u0430\u0442\u0430\u043c", None))
        self.label_8.setText("")
    # retranslateUi

