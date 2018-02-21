# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'TF.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
from time import sleep  # noqa
import requests as rq
import login_thread
import search_thread
import raid_thread
import json
import imgs_rc  # noqa
import sys
import os
reload(sys)
sys.setdefaultencoding('utf-8')
sess = rq.Session()
try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8

    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)


class Ui_MainWindow(QtGui.QMainWindow, object):
    def setupUi(self, MainWindow):
        self.default_workspace = "/root/.trav_farmer/"
        # login thread
        self.login_thread = login_thread.Login_Thread()
        self.search_thread = search_thread.Search_Thread()
        self.raid_thread = raid_thread.Raid_Thread()
        try:
            os.mkdir(self.default_workspace)
        except:
            pass
        self.logged_in = False
        self.se_started = False
        self.raid_started = False
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(762, 350)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/newPrefix/logo.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.tabWidget = QtGui.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(10, 10, 741, 331))
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.settings_tab = QtGui.QWidget()
        self.settings_tab.setObjectName(_fromUtf8("settings_tab"))
        self.tabWidget_2 = QtGui.QTabWidget(self.settings_tab)
        self.tabWidget_2.setGeometry(QtCore.QRect(18, 60, 701, 231))
        self.tabWidget_2.setObjectName(_fromUtf8("tabWidget_2"))
        self.searcher_tab = QtGui.QWidget()
        self.searcher_tab.setObjectName(_fromUtf8("searcher_tab"))
        self.max_pl_pop_label = QtGui.QLabel(self.searcher_tab)
        self.max_pl_pop_label.setGeometry(QtCore.QRect(20, 30, 111, 16))
        self.max_pl_pop_label.setObjectName(_fromUtf8("max_pl_pop_label"))
        self.max_vl_pop_label = QtGui.QLabel(self.searcher_tab)
        self.max_vl_pop_label.setGeometry(QtCore.QRect(20, 60, 111, 16))
        self.max_vl_pop_label.setObjectName(_fromUtf8("max_vl_pop_label"))
        self.Ignore_alliance_label = QtGui.QLabel(self.searcher_tab)
        self.Ignore_alliance_label.setGeometry(QtCore.QRect(350, 28, 81, 16))
        self.Ignore_alliance_label.setObjectName(_fromUtf8("Ignore_alliance_label"))
        self.Ignore_players_label = QtGui.QLabel(self.searcher_tab)
        self.Ignore_players_label.setGeometry(QtCore.QRect(530, 28, 81, 16))
        self.Ignore_players_label.setObjectName(_fromUtf8("Ignore_players_label"))
        self.from_page_label = QtGui.QLabel(self.searcher_tab)
        self.from_page_label.setGeometry(QtCore.QRect(20, 90, 121, 16))
        self.from_page_label.setObjectName(_fromUtf8("from_page_label"))
        self.pages_count_label = QtGui.QLabel(self.searcher_tab)
        self.pages_count_label.setGeometry(QtCore.QRect(20, 120, 61, 16))
        self.pages_count_label.setObjectName(_fromUtf8("pages_count_label"))
        self.x_label = QtGui.QLabel(self.searcher_tab)
        self.x_label.setGeometry(QtCore.QRect(70, 170, 16, 16))
        self.x_label.setObjectName(_fromUtf8("x_label"))
        self.y_label = QtGui.QLabel(self.searcher_tab)
        self.y_label.setGeometry(QtCore.QRect(140, 170, 16, 16))
        self.y_label.setObjectName(_fromUtf8("y_label"))
        self.max_pl_pop_field = QtGui.QLineEdit(self.searcher_tab)
        self.max_pl_pop_field.setGeometry(QtCore.QRect(180, 30, 71, 21))
        self.max_pl_pop_field.setObjectName(_fromUtf8("max_pl_pop_field"))
        self.max_vl_pop_field = QtGui.QLineEdit(self.searcher_tab)
        self.max_vl_pop_field.setGeometry(QtCore.QRect(180, 60, 71, 21))
        self.max_vl_pop_field.setObjectName(_fromUtf8("max_vl_pop_field"))
        self.from_page_field = QtGui.QLineEdit(self.searcher_tab)
        self.from_page_field.setGeometry(QtCore.QRect(180, 90, 71, 21))
        self.from_page_field.setObjectName(_fromUtf8("from_page_field"))
        self.pages_count_field = QtGui.QLineEdit(self.searcher_tab)
        self.pages_count_field.setGeometry(QtCore.QRect(180, 120, 71, 21))
        self.pages_count_field.setObjectName(_fromUtf8("pages_count_field"))
        self.ignore_alliance_field = QtGui.QPlainTextEdit(self.searcher_tab)
        self.ignore_alliance_field.setGeometry(QtCore.QRect(317, 60, 141, 81))
        self.ignore_alliance_field.setObjectName(_fromUtf8("ignore_alliance_field"))
        self.ignore_players_field = QtGui.QPlainTextEdit(self.searcher_tab)
        self.ignore_players_field.setGeometry(QtCore.QRect(497, 60, 141, 81))
        self.ignore_players_field.setObjectName(_fromUtf8("ignore_players_field"))
        self.x_field = QtGui.QLineEdit(self.searcher_tab)
        self.x_field.setGeometry(QtCore.QRect(90, 167, 41, 23))
        self.x_field.setObjectName(_fromUtf8("x_field"))
        self.y_field = QtGui.QLineEdit(self.searcher_tab)
        self.y_field.setGeometry(QtCore.QRect(160, 167, 41, 23))
        self.y_field.setObjectName(_fromUtf8("y_field"))
        self.tabWidget_2.addTab(self.searcher_tab, _fromUtf8(""))
        self.raider_tab = QtGui.QWidget()
        self.raider_tab.setObjectName(_fromUtf8("raider_tab"))
        self.t1_label = QtGui.QLabel(self.raider_tab)
        self.t1_label.setGeometry(QtCore.QRect(201, 42, 16, 16))
        self.t1_label.setObjectName(_fromUtf8("t1_label"))
        self.t2_label = QtGui.QLabel(self.raider_tab)
        self.t2_label.setGeometry(QtCore.QRect(270, 42, 16, 16))
        self.t2_label.setObjectName(_fromUtf8("t2_label"))
        self.t3_label = QtGui.QLabel(self.raider_tab)
        self.t3_label.setGeometry(QtCore.QRect(335, 42, 16, 16))
        self.t3_label.setObjectName(_fromUtf8("t3_label"))
        self.t4_label = QtGui.QLabel(self.raider_tab)
        self.t4_label.setGeometry(QtCore.QRect(400, 42, 16, 16))
        self.t4_label.setObjectName(_fromUtf8("t4_label"))
        self.t5_label = QtGui.QLabel(self.raider_tab)
        self.t5_label.setGeometry(QtCore.QRect(459, 42, 16, 16))
        self.t5_label.setObjectName(_fromUtf8("t5_label"))
        self.t6_label = QtGui.QLabel(self.raider_tab)
        self.t6_label.setGeometry(QtCore.QRect(200, 90, 16, 16))
        self.t6_label.setObjectName(_fromUtf8("t6_label"))
        self.t7_label = QtGui.QLabel(self.raider_tab)
        self.t7_label.setGeometry(QtCore.QRect(270, 90, 16, 16))
        self.t7_label.setObjectName(_fromUtf8("t7_label"))
        self.t8_label = QtGui.QLabel(self.raider_tab)
        self.t8_label.setGeometry(QtCore.QRect(334, 90, 16, 16))
        self.t8_label.setObjectName(_fromUtf8("t8_label"))
        self.t9_label = QtGui.QLabel(self.raider_tab)
        self.t9_label.setGeometry(QtCore.QRect(400, 90, 16, 16))
        self.t9_label.setObjectName(_fromUtf8("t9_label"))
        self.t10_label = QtGui.QLabel(self.raider_tab)
        self.t10_label.setGeometry(QtCore.QRect(456, 90, 16, 16))
        self.t10_label.setObjectName(_fromUtf8("t10_label"))
        self.t1_field = QtGui.QLineEdit(self.raider_tab)
        self.t1_field.setGeometry(QtCore.QRect(191, 60, 31, 23))
        self.t1_field.setObjectName(_fromUtf8("t1_field"))
        self.t2_field = QtGui.QLineEdit(self.raider_tab)
        self.t2_field.setGeometry(QtCore.QRect(260, 60, 31, 23))
        self.t2_field.setObjectName(_fromUtf8("t2_field"))
        self.t3_field = QtGui.QLineEdit(self.raider_tab)
        self.t3_field.setGeometry(QtCore.QRect(325, 60, 30, 23))
        self.t3_field.setObjectName(_fromUtf8("t3_field"))
        self.t4_field = QtGui.QLineEdit(self.raider_tab)
        self.t4_field.setGeometry(QtCore.QRect(390, 60, 30, 23))
        self.t4_field.setObjectName(_fromUtf8("t4_field"))
        self.t5_field = QtGui.QLineEdit(self.raider_tab)
        self.t5_field.setGeometry(QtCore.QRect(450, 60, 30, 23))
        self.t5_field.setObjectName(_fromUtf8("t5_field"))
        self.t6_field = QtGui.QLineEdit(self.raider_tab)
        self.t6_field.setGeometry(QtCore.QRect(190, 110, 30, 23))
        self.t6_field.setObjectName(_fromUtf8("t6_field"))
        self.t7_field = QtGui.QLineEdit(self.raider_tab)
        self.t7_field.setGeometry(QtCore.QRect(260, 110, 30, 23))
        self.t7_field.setObjectName(_fromUtf8("t7_field"))
        self.t8_field = QtGui.QLineEdit(self.raider_tab)
        self.t8_field.setGeometry(QtCore.QRect(325, 110, 30, 23))
        self.t8_field.setObjectName(_fromUtf8("t8_field"))
        self.t9_field = QtGui.QLineEdit(self.raider_tab)
        self.t9_field.setGeometry(QtCore.QRect(390, 110, 30, 23))
        self.t9_field.setObjectName(_fromUtf8("t9_field"))
        self.t10_field = QtGui.QLineEdit(self.raider_tab)
        self.t10_field.setGeometry(QtCore.QRect(450, 110, 30, 23))
        self.t10_field.setObjectName(_fromUtf8("t10_field"))
        self.tabWidget_2.addTab(self.raider_tab, _fromUtf8(""))
        self.workspace_path_label = QtGui.QLabel(self.settings_tab)
        self.workspace_path_label.setGeometry(QtCore.QRect(20, 20, 81, 16))
        self.workspace_path_label.setObjectName(_fromUtf8("workspace_path_label"))
        self.workspace_path_field = QtGui.QLineEdit(self.settings_tab)
        self.workspace_path_field.setGeometry(QtCore.QRect(110, 17, 361, 23))
        self.workspace_path_field.setObjectName(_fromUtf8("workspace_path_field"))
        self.save_btn = QtGui.QPushButton(self.settings_tab)
        self.save_btn.setGeometry(QtCore.QRect(540, 15, 85, 27))
        self.save_btn.setObjectName(_fromUtf8("save_btn"))
        self.save_noti_label = QtGui.QLabel(self.settings_tab)
        self.save_noti_label.setGeometry(QtCore.QRect(680, 22, 41, 16))
        self.save_noti_label.setText(_fromUtf8(""))
        self.save_noti_label.setObjectName(_fromUtf8("save_noti_label"))
        self.tabWidget.addTab(self.settings_tab, _fromUtf8(""))
        self.login_tab = QtGui.QWidget()
        self.login_tab.setObjectName(_fromUtf8("login_tab"))
        self.server_label = QtGui.QLabel(self.login_tab)
        self.server_label.setGeometry(QtCore.QRect(60, 60, 31, 21))
        self.server_label.setObjectName(_fromUtf8("server_label"))
        self.username_label = QtGui.QLabel(self.login_tab)
        self.username_label.setGeometry(QtCore.QRect(60, 91, 51, 20))
        self.username_label.setObjectName(_fromUtf8("username_label"))
        self.password_label = QtGui.QLabel(self.login_tab)
        self.password_label.setGeometry(QtCore.QRect(60, 123, 51, 16))
        self.password_label.setObjectName(_fromUtf8("password_label"))
        self.server_field = QtGui.QLineEdit(self.login_tab)
        self.server_field.setGeometry(QtCore.QRect(130, 60, 151, 23))
        self.server_field.setObjectName(_fromUtf8("server_field"))
        self.username_field = QtGui.QLineEdit(self.login_tab)
        self.username_field.setGeometry(QtCore.QRect(130, 90, 151, 23))
        self.username_field.setObjectName(_fromUtf8("username_field"))
        self.password_field = QtGui.QLineEdit(self.login_tab)
        self.password_field.setGeometry(QtCore.QRect(130, 120, 151, 23))
        self.password_field.setEchoMode(QtGui.QLineEdit.Password)
        self.password_field.setObjectName(_fromUtf8("password_field"))
        self.login_btn = QtGui.QPushButton(self.login_tab)
        self.login_btn.setGeometry(QtCore.QRect(160, 170, 85, 27))
        self.login_btn.setObjectName(_fromUtf8("login_btn"))
        self.logo_label = QtGui.QLabel(self.login_tab)
        self.logo_label.setGeometry(QtCore.QRect(380, 20, 321, 241))
        self.logo_label.setText(_fromUtf8(""))
        self.logo_label.setPixmap(QtGui.QPixmap(_fromUtf8(":/newPrefix/logo.png")))
        self.logo_label.setObjectName(_fromUtf8("logo_label"))
        self.tabWidget.addTab(self.login_tab, _fromUtf8(""))
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.log_box = QtGui.QPlainTextEdit(self.tab)
        self.log_box.setGeometry(QtCore.QRect(20, 50, 541, 231))
        self.log_box.setUndoRedoEnabled(False)
        self.log_box.setReadOnly(True)
        self.log_box.setObjectName(_fromUtf8("log_box"))
        self.label = QtGui.QLabel(self.tab)
        self.label.setGeometry(QtCore.QRect(21, 20, 46, 13))
        self.label.setObjectName(_fromUtf8("label"))
        self.start_search_btn = QtGui.QPushButton(self.tab)
        self.start_search_btn.setGeometry(QtCore.QRect(600, 50, 85, 27))
        self.start_search_btn.setObjectName(_fromUtf8("start_search_btn"))
        self.stop_search_btn = QtGui.QPushButton(self.tab)
        self.stop_search_btn.setGeometry(QtCore.QRect(600, 80, 85, 27))
        self.stop_search_btn.setObjectName(_fromUtf8("stop_search_btn"))
        self.start_raid_btn = QtGui.QPushButton(self.tab)
        self.start_raid_btn.setGeometry(QtCore.QRect(600, 130, 85, 27))
        self.start_raid_btn.setObjectName(_fromUtf8("start_raid_btn"))
        self.stop_raid_btn = QtGui.QPushButton(self.tab)
        self.stop_raid_btn.setGeometry(QtCore.QRect(600, 160, 85, 27))
        self.stop_raid_btn.setObjectName(_fromUtf8("stop_raid_btn"))
        self.clear_log_btn = QtGui.QPushButton(self.tab)
        self.clear_log_btn.setGeometry(QtCore.QRect(600, 210, 85, 27))
        self.clear_log_btn.setObjectName(_fromUtf8("clear_log_btn"))
        self.tabWidget.addTab(self.tab, _fromUtf8(""))
        self.about_page = QtGui.QWidget()
        self.about_page.setObjectName(_fromUtf8("about_page"))
        self.coded_by_label = QtGui.QLabel(self.about_page)
        self.coded_by_label.setGeometry(QtCore.QRect(250, 90, 260, 21))
        self.coded_by_label.setObjectName(_fromUtf8("coded_by_label"))
        self.visist_me_label = QtGui.QLabel(self.about_page)
        self.visist_me_label.setGeometry(QtCore.QRect(256, 130, 260, 20))
        self.visist_me_label.setObjectName(_fromUtf8("visist_me_label"))
        self.tabWidget.addTab(self.about_page, _fromUtf8(""))
        MainWindow.setCentralWidget(self.centralwidget)
        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        self.tabWidget_2.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Travian Farmer", None))
        self.max_pl_pop_label.setText(_translate("MainWindow", "Max Player Population", None))
        self.max_vl_pop_label.setText(_translate("MainWindow", "Max Village Population", None))
        self.Ignore_alliance_label.setText(_translate("MainWindow", "Ignore Alliance", None))
        self.Ignore_players_label.setText(_translate("MainWindow", "Ignore Players", None))
        self.from_page_label.setText(_translate("MainWindow", "Start Search From Page", None))
        self.pages_count_label.setText(_translate("MainWindow", "Pages Count", None))
        self.x_label.setText(_translate("MainWindow", "X", None))
        self.y_label.setText(_translate("MainWindow", "Y", None))
        self.max_pl_pop_field.setText(_translate("MainWindow", "5500", None))
        self.max_vl_pop_field.setText(_translate("MainWindow", "1500", None))
        self.from_page_field.setText(_translate("MainWindow", "1", None))
        self.pages_count_field.setText(_translate("MainWindow", "1", None))
        self.ignore_alliance_field.setPlainText(_translate("MainWindow", "ally1,ally2,ally3...", None))
        self.ignore_players_field.setPlainText(_translate("MainWindow", "player1,player2,player3...", None))
        self.x_field.setText(_translate("MainWindow", "0", None))
        self.y_field.setText(_translate("MainWindow", "0", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.searcher_tab), _translate("MainWindow", "Searcher", None))
        self.t1_label.setText(_translate("MainWindow", "t1", None))
        self.t2_label.setText(_translate("MainWindow", "t2", None))
        self.t3_label.setText(_translate("MainWindow", "t3", None))
        self.t4_label.setText(_translate("MainWindow", "t4", None))
        self.t5_label.setText(_translate("MainWindow", "t5", None))
        self.t6_label.setText(_translate("MainWindow", "t6", None))
        self.t7_label.setText(_translate("MainWindow", "t7", None))
        self.t8_label.setText(_translate("MainWindow", "t8", None))
        self.t9_label.setText(_translate("MainWindow", "t9", None))
        self.t10_label.setText(_translate("MainWindow", "t10", None))
        self.t1_field.setText(_translate("MainWindow", "3", None))
        self.t2_field.setText(_translate("MainWindow", "0", None))
        self.t3_field.setText(_translate("MainWindow", "0", None))
        self.t4_field.setText(_translate("MainWindow", "0", None))
        self.t5_field.setText(_translate("MainWindow", "0", None))
        self.t6_field.setText(_translate("MainWindow", "0", None))
        self.t7_field.setText(_translate("MainWindow", "0", None))
        self.t8_field.setText(_translate("MainWindow", "0", None))
        self.t9_field.setText(_translate("MainWindow", "0", None))
        self.t10_field.setText(_translate("MainWindow", "0", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.raider_tab), _translate("MainWindow", "Raider", None))
        self.workspace_path_label.setText(_translate("MainWindow", "Workspace Path ", None))
        self.workspace_path_field.setText(_translate("MainWindow", "~/.trav_farmer/", None))
        self.save_btn.setText(_translate("MainWindow", "Save Settings", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.settings_tab), _translate("MainWindow", "Settings", None))
        self.server_label.setText(_translate("MainWindow", "Server", None))
        self.username_label.setText(_translate("MainWindow", "Username", None))
        self.password_label.setText(_translate("MainWindow", "Password", None))
        self.server_field.setPlaceholderText(_translate("MainWindow", "Server: EX:  tx3.travian.sy", None))
        self.username_field.setPlaceholderText(_translate("MainWindow", "Username", None))
        self.password_field.setPlaceholderText(_translate("MainWindow", "Password", None))
        self.login_btn.setText(_translate("MainWindow", "Login", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.login_tab), _translate("MainWindow", "Login", None))
        self.label.setText(_translate("MainWindow", "Log Box", None))
        self.start_search_btn.setText(_translate("MainWindow", "Search", None))
        self.stop_search_btn.setText(_translate("MainWindow", "Stop Searching", None))
        self.start_raid_btn.setText(_translate("MainWindow", "Raid", None))
        self.stop_raid_btn.setText(_translate("MainWindow", "Stop Raiding", None))
        self.clear_log_btn.setText(_translate("MainWindow", "Clear Log", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Searcher - Raider - Log", None))
        self.coded_by_label.setText(_translate("MainWindow", "This is a free Program Coded by: @i127001", None))
        self.visist_me_label.setText(_translate("MainWindow", "Vists me at: https://twitter.com/i127001", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.about_page), _translate("MainWindow", "About", None))
        try:
            self.load_conf()
        except Exception as e:
            print(e)
            pass
        # Signals
        # save signal
        self.connect(self.save_btn, QtCore.SIGNAL('clicked()'), self.save_settings)
        # login signals
        self.connect(self.login_btn, QtCore.SIGNAL('clicked()'), self.login)
        self.connect(self.login_btn, QtCore.SIGNAL('login()'), self.login)
        self.connect(self.login_thread, QtCore.SIGNAL('login_status(bool)'), self.login_status)
        # Search signals
        self.connect(self.start_search_btn, QtCore.SIGNAL('clicked()'), self.search)
        self.connect(self.start_search_btn, QtCore.SIGNAL("search()"), self.search)
        self.connect(self.search_thread, QtCore.SIGNAL('search_status(QString)'), self.search_status)
        # Raid signals
        self.connect(self.start_raid_btn, QtCore.SIGNAL('clicked()'), self.raid)
        self.connect(self.start_raid_btn, QtCore.SIGNAL("raid()"), self.raid)
        self.connect(self.raid_thread, QtCore.SIGNAL('raid_status(QString)'), self.raid_status)
        # stop searching
        self.connect(self.stop_search_btn, QtCore.SIGNAL("clicked()"), self.stop_search)
        # stop raiding
        self.connect(self.stop_raid_btn, QtCore.SIGNAL("clicked()"), self.stop_raid)
        # Clear log
        self.connect(self.clear_log_btn, QtCore.SIGNAL("clicked()"), self.clear_log)

    def stop_raid(self):
        if(self.raid_started):
            # self.search_thread.stop = True
            # self.search_thread.stop()
            # self.search_thread.quit()
            self.raid_started = False
            self.raid_thread.terminate()
            self.log_box.appendPlainText("\n\nRaiding Stopped !!\n")
        else:
            self.log_box.appendPlainText("\n\nRaiding dose not started yet !!\n")

    def raid(self):
        if(self.logged_in):
            self.save_settings()
            self.log_box.appendPlainText("\n\nRaiding Started, please wait ...\n")
            self.raid_thread.get_data(sess, self.settings_info)
            self.raid_thread.start()
            self.raid_started = True
            self.save_noti_label.setText(_translate("MainWindow", "", None))
        else:
            self.log_box.appendPlainText("\n\nYou are not Logged in !,  Login and try again\n")

    def raid_status(self, log):
        log = QtCore.QString(str(log).encode('utf-8'))
        self.log_box.appendPlainText(log)

    def stop_search(self):
        if(self.se_started):
            # self.search_thread.stop = True
            # self.search_thread.stop()
            # self.search_thread.quit()
            self.se_started = False
            self.search_thread.terminate()
            self.log_box.appendPlainText("\n\nSearching Stopped !!\n")
        else:
            self.log_box.appendPlainText("\n\nSearching dose not started yet !!\n")

    def search(self):
        if(self.logged_in):
            self.save_settings()
            self.log_box.appendPlainText("\n\nSearching Started, please wait ...\n")
            self.search_thread.get_data(sess, self.settings_info)
            self.search_thread.start()
            self.se_started = True
            self.save_noti_label.setText(_translate("MainWindow", "", None))
        else:
            self.log_box.appendPlainText("\n\nYou are not Logged in !,  Login and try again\n")

    def search_status(self, log):
        log = QtCore.QString(log)
        self.log_box.appendPlainText(log)

    def login(self):
        self.save_settings()
        self.settings_info['password'] = str(self.password_field.text())
        self.login_thread.get_data(sess, self.settings_info)
        self.login_thread.start()
        self.save_noti_label.setText(_translate("MainWindow", "", None))
        pass

    def login_status(self, status):
        if(status is True):
            self.log_box.clear()
            self.log_box.appendPlainText("Logged In!\nServer: %s\nUser: %s\n-------\n" % (self.settings_info['server'], self.settings_info['username']))
            self.tabWidget.setCurrentIndex(2)
            self.sess = self.login_thread.sess
            # print(self.login_thread.sess)
            # print(self.sess)
            self.logged_in = True
        else:
            self.logged_in = False
            self.log_box.clear()
            self.log_box.appendPlainText("Unable to login to [%s] USER: [%s]!\n-------\n" % (self.settings_info['server'], self.settings_info['username']))
            self.tabWidget.setCurrentIndex(2)

    def load_conf(self):
        f = open(self.default_workspace + "conf_TF.conf", 'r')
        conf_data_str = f.readlines()[0]
        f.close()
        self.conf_data = json.loads(conf_data_str)
        self.workspace_path_field.setText(_translate("MainWindow", str(self.default_workspace), None))
        self.max_pl_pop_field.setText(_translate("MainWindow", str(self.conf_data['max_pl_pop']), None))
        self.max_vl_pop_field.setText(_translate("MainWindow", str(self.conf_data['max_vl_pop']), None))
        self.from_page_field.setText(_translate("MainWindow", str(self.conf_data['from_page']), None))
        self.pages_count_field.setText(_translate("MainWindow", str(self.conf_data['pages_count']), None))
        self.x_field.setText(_translate("MainWindow", str(self.conf_data['x_cap']), None))
        self.y_field.setText(_translate("MainWindow", str(self.conf_data['y_cap']), None))
        self.ignore_alliance_field.setPlainText(_translate("MainWindow", str(self.conf_data['ignore_alliance']), None))
        self.ignore_players_field.setPlainText(_translate("MainWindow", str(self.conf_data['ignore_players']), None))
        self.t1_field.setText(_translate("MainWindow", str(self.conf_data['t1']), None))
        self.t2_field.setText(_translate("MainWindow", str(self.conf_data['t2']), None))
        self.t3_field.setText(_translate("MainWindow", str(self.conf_data['t3']), None))
        self.t4_field.setText(_translate("MainWindow", str(self.conf_data['t4']), None))
        self.t5_field.setText(_translate("MainWindow", str(self.conf_data['t5']), None))
        self.t6_field.setText(_translate("MainWindow", str(self.conf_data['t6']), None))
        self.t7_field.setText(_translate("MainWindow", str(self.conf_data['t7']), None))
        self.t8_field.setText(_translate("MainWindow", str(self.conf_data['t8']), None))
        self.t9_field.setText(_translate("MainWindow", str(self.conf_data['t9']), None))
        self.t10_field.setText(_translate("MainWindow", str(self.conf_data['t10']), None))
        self.server_field.setText(_translate("MainWindow", str(self.conf_data['server']), None))
        self.username_field.setText(_translate("MainWindow", str(self.conf_data['username']), None))

    def save_settings(self):
        self.settings_info = {
            "workspace_path": str(self.default_workspace),
            "max_pl_pop": int(self.max_pl_pop_field.text()),
            "max_vl_pop": int(self.max_vl_pop_field.text()),
            "from_page": int(self.from_page_field.text()),
            "pages_count": int(self.pages_count_field.text()),
            "ignore_alliance": str(self.ignore_alliance_field.toPlainText()),
            "ignore_players": str(self.ignore_players_field.toPlainText()),
            "x_cap": int(self.x_field.text()),
            "y_cap": int(self.y_field.text()),
            "t1": str(self.t1_field.text()),
            "t2": str(self.t2_field.text()),
            "t3": str(self.t3_field.text()),
            "t4": str(self.t4_field.text()),
            "t5": str(self.t5_field.text()),
            "t6": str(self.t6_field.text()),
            "t7": str(self.t7_field.text()),
            "t8": str(self.t8_field.text()),
            "t9": str(self.t9_field.text()),
            "t10": str(self.t10_field.text()),
            "t11": "0",
            "server": str(self.server_field.text()),
            "username": str(self.username_field.text()),
        }
        to_save = str(json.dumps(self.settings_info))
        f = open(self.default_workspace + "conf_TF.conf", 'w')
        f.write(to_save)
        f.close()
        self.save_noti_label.setText(_translate("MainWindow", "Saved !", None))

    def clear_log(self):
        self.log_box.clear()
        self.log_box.appendPlainText("Log Cleared\n---------\n")
if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    w = Ui_MainWindow()
    w.setupUi(w)
    w.setFixedSize(w.size())
    w.show()
    app.exec_()
