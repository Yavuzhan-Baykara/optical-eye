# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'FaultyFabricWindow.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_FaultyFabricWindow(object):
    def setupUi(self, FaultyFabricWindow):
        FaultyFabricWindow.setObjectName("FaultyFabricWindow")
        FaultyFabricWindow.resize(1964, 1005)
        FaultyFabricWindow.setStyleSheet("/* ---------------------------------------------------------------------------\n"
"\n"
"    WARNING! File created programmatically. All changes made in this file will be lost!\n"
"\n"
"    Created by the qtsass compiler v0.3.0\n"
"\n"
"    The definitions are in the \"qdarkstyle.qss._styles.scss\" module\n"
"\n"
"--------------------------------------------------------------------------- */\n"
"/* Light Style - QDarkStyleSheet ------------------------------------------ */\n"
"/*\n"
"\n"
"See Qt documentation:\n"
"\n"
"  - https://doc.qt.io/qt-5/stylesheet.html\n"
"  - https://doc.qt.io/qt-5/stylesheet-reference.html\n"
"  - https://doc.qt.io/qt-5/stylesheet-examples.html\n"
"\n"
"--------------------------------------------------------------------------- */\n"
"/* Reset elements ------------------------------------------------------------\n"
"\n"
"Resetting everything helps to unify styles across different operating systems\n"
"\n"
"--------------------------------------------------------------------------- */\n"
"* {\n"
"  padding: 0px;\n"
"  margin: 0px;\n"
"  border: 0px;\n"
"  border-style: none;\n"
"  border-image: none;\n"
"  outline: 0;\n"
"  font-size: 20px;\n"
"}\n"
"\n"
"/* specific reset for elements inside QToolBar */\n"
"QToolBar * {\n"
"  margin: 0px;\n"
"  padding: 0px;\n"
"}\n"
"\n"
"/* QWidget ----------------------------------------------------------------\n"
"\n"
"--------------------------------------------------------------------------- */\n"
"QWidget {\n"
"  background-color: #19232D;\n"
"  border: 0px solid #455364;\n"
"  padding: 0px;\n"
"  color: #E0E1E3;\n"
"  selection-background-color: #346792;\n"
"  selection-color: #E0E1E3;\n"
"}\n"
"\n"
"QWidget:disabled {\n"
"  background-color: #19232D;\n"
"  color: #9DA9B5;\n"
"  selection-background-color: #26486B;\n"
"  selection-color: #9DA9B5;\n"
"}\n"
"\n"
"QWidget::item:selected {\n"
"  background-color: #346792;\n"
"}\n"
"\n"
"QWidget::item:hover:!selected {\n"
"  background-color: #1A72BB;\n"
"}\n"
"\n"
"/* QMainWindow ------------------------------------------------------------\n"
"\n"
"This adjusts the splitter in the dock widget, not qsplitter\n"
"https://doc.qt.io/qt-5/stylesheet-examples.html#customizing-qmainwindow\n"
"\n"
"--------------------------------------------------------------------------- */\n"
"QMainWindow::separator {\n"
"  background-color: #455364;\n"
"  border: 0px solid #19232D;\n"
"  spacing: 0px;\n"
"  padding: 2px;\n"
"}\n"
"\n"
"QMainWindow::separator:hover {\n"
"  background-color: #60798B;\n"
"  border: 0px solid #1A72BB;\n"
"}\n"
"\n"
"QMainWindow::separator:horizontal {\n"
"  width: 5px;\n"
"  margin-top: 2px;\n"
"  margin-bottom: 2px;\n"
"  image: url(\":/qss_icons/dark/rc/toolbar_separator_vertical.png\");\n"
"}\n"
"\n"
"QMainWindow::separator:vertical {\n"
"  height: 5px;\n"
"  margin-left: 2px;\n"
"  margin-right: 2px;\n"
"  image: url(\":/qss_icons/dark/rc/toolbar_separator_horizontal.png\");\n"
"}\n"
"\n"
"/* QToolTip ---------------------------------------------------------------\n"
"\n"
"https://doc.qt.io/qt-5/stylesheet-examples.html#customizing-qtooltip\n"
"\n"
"--------------------------------------------------------------------------- */\n"
"QToolTip {\n"
"  background-color: #346792;\n"
"  color: #E0E1E3;\n"
"  /* If you remove the border property, background stops working on Windows */\n"
"  border: none;\n"
"  /* Remove padding, for fix combo box tooltip */\n"
"  padding: 0px;\n"
"  /* Remove opacity, fix #174 - may need to use RGBA */\n"
"}\n"
"\n"
"/* QStatusBar -------------------------------------------------------------\n"
"\n"
"https://doc.qt.io/qt-5/stylesheet-examples.html#customizing-qstatusbar\n"
"\n"
"--------------------------------------------------------------------------- */\n"
"QStatusBar {\n"
"  border: 1px solid #455364;\n"
"  /* Fixes Spyder #9120, #9121 */\n"
"  background: #455364;\n"
"  /* Fixes #205, white vertical borders separating items */\n"
"}\n"
"\n"
"QStatusBar::item {\n"
"  border: none;\n"
"}\n"
"\n"
"QStatusBar QToolTip {\n"
"  background-color: #1A72BB;\n"
"  border: 1px solid #19232D;\n"
"  color: #19232D;\n"
"  /* Remove padding, for fix combo box tooltip */\n"
"  padding: 0px;\n"
"  /* Reducing transparency to read better */\n"
"  opacity: 230;\n"
"}\n"
"\n"
"QStatusBar QLabel {\n"
"  /* Fixes Spyder #9120, #9121 */\n"
"  background: transparent;\n"
"}\n"
"\n"
"/* QCheckBox --------------------------------------------------------------\n"
"\n"
"https://doc.qt.io/qt-5/stylesheet-examples.html#customizing-qcheckbox\n"
"\n"
"--------------------------------------------------------------------------- */\n"
"QCheckBox {\n"
"  background-color: #19232D;\n"
"  color: #E0E1E3;\n"
"  spacing: 4px;\n"
"  outline: none;\n"
"  padding-top: 4px;\n"
"  padding-bottom: 4px;\n"
"}\n"
"\n"
"QCheckBox:focus {\n"
"  border: none;\n"
"}\n"
"\n"
"QCheckBox QWidget:disabled {\n"
"  background-color: #19232D;\n"
"  color: #9DA9B5;\n"
"}\n"
"\n"
"QCheckBox::indicator {\n"
"  margin-left: 2px;\n"
"  height: 14px;\n"
"  width: 14px;\n"
"}\n"
"\n"
"\n"
"\n"
"/* QGroupBox --------------------------------------------------------------\n"
"\n"
"https://doc.qt.io/qt-5/stylesheet-examples.html#customizing-qgroupbox\n"
"\n"
"--------------------------------------------------------------------------- */\n"
"QGroupBox {\n"
"  font-weight: bold;\n"
"  border: 1px solid #455364;\n"
"  border-radius: 4px;\n"
"  padding: 2px;\n"
"  margin-top: 6px;\n"
"  margin-bottom: 4px;\n"
"}\n"
"\n"
"QGroupBox::title {\n"
"  subcontrol-origin: margin;\n"
"  subcontrol-position: top left;\n"
"  left: 4px;\n"
"  padding-left: 2px;\n"
"  padding-right: 4px;\n"
"  padding-top: -4px;\n"
"}\n"
"\n"
"QGroupBox::indicator {\n"
"  margin-left: 2px;\n"
"  margin-top: 2px;\n"
"  padding: 0;\n"
"  height: 14px;\n"
"  width: 14px;\n"
"}\n"
"\n"
"QGroupBox::indicator:unchecked {\n"
"  border: none;\n"
"  image: url(\":/qss_icons/dark/rc/checkbox_unchecked.png\");\n"
"}\n"
"\n"
"QGroupBox::indicator:unchecked:hover, QGroupBox::indicator:unchecked:focus, QGroupBox::indicator:unchecked:pressed {\n"
"  border: none;\n"
"  image: url(\":/qss_icons/dark/rc/checkbox_unchecked_focus.png\");\n"
"}\n"
"\n"
"QGroupBox::indicator:unchecked:disabled {\n"
"  image: url(\":/qss_icons/dark/rc/checkbox_unchecked_disabled.png\");\n"
"}\n"
"\n"
"QGroupBox::indicator:checked {\n"
"  border: none;\n"
"  image: url(\":/qss_icons/dark/rc/checkbox_checked.png\");\n"
"}\n"
"\n"
"QGroupBox::indicator:checked:hover, QGroupBox::indicator:checked:focus, QGroupBox::indicator:checked:pressed {\n"
"  border: none;\n"
"  image: url(\":/qss_icons/dark/rc/checkbox_checked_focus.png\");\n"
"}\n"
"\n"
"QGroupBox::indicator:checked:disabled {\n"
"  image: url(\":/qss_icons/dark/rc/checkbox_checked_disabled.png\");\n"
"}\n"
"\n"
"/* QRadioButton -----------------------------------------------------------\n"
"\n"
"https://doc.qt.io/qt-5/stylesheet-examples.html#customizing-qradiobutton\n"
"\n"
"--------------------------------------------------------------------------- */\n"
"QRadioButton {\n"
"  background-color: #19232D;\n"
"  color: #E0E1E3;\n"
"  spacing: 4px;\n"
"  padding-top: 4px;\n"
"  padding-bottom: 4px;\n"
"  border: none;\n"
"  outline: none;\n"
"  font-size: 20px;\n"
"}\n"
"\n"
"QRadioButton:focus {\n"
"  border: none;\n"
"}\n"
"\n"
"QRadioButton:disabled {\n"
"  background-color: #19232D;\n"
"  color: #9DA9B5;\n"
"  border: none;\n"
"  outline: none;\n"
"}\n"
"\n"
"QRadioButton QWidget {\n"
"  background-color: #19232D;\n"
"  color: #E0E1E3;\n"
"  spacing: 0px;\n"
"  padding: 0px;\n"
"  outline: none;\n"
"  border: none;\n"
"}\n"
"\n"
"\n"
"\n"
"/* QMenuBar ---------------------------------------------------------------\n"
"\n"
"https://doc.qt.io/qt-5/stylesheet-examples.html#customizing-qmenubar\n"
"\n"
"--------------------------------------------------------------------------- */\n"
"QMenuBar {\n"
"  background-color: #455364;\n"
"  padding: 2px;\n"
"  border: 1px solid #19232D;\n"
"  color: #E0E1E3;\n"
"  selection-background-color: #1A72BB;\n"
"\n"
"}\n"
"\n"
"QMenuBar:focus {\n"
"  border: 1px solid #346792;\n"
"}\n"
"\n"
"QMenuBar::item {\n"
"  background: transparent;\n"
"  padding: 4px;\n"
"  margin-right: 8px;\n"
"\n"
"}\n"
"\n"
"QMenuBar::item:selected {\n"
"  padding: 4px;\n"
"  background: transparent;\n"
"  border: 0px solid #455364;\n"
"  background-color: #1A72BB;\n"
"}\n"
"\n"
"QMenuBar::item:pressed {\n"
"  padding: 4px;\n"
"  border: 0px solid #455364;\n"
"  background-color: #1A72BB;\n"
"  color: #E0E1E3;\n"
"  margin-bottom: 0px;\n"
"  padding-bottom: 0px;\n"
"\n"
"}\n"
"/* QMenu ------------------------------------------------------------------\n"
"\n"
"https://doc.qt.io/qt-5/stylesheet-examples.html#customizing-qmenu\n"
"\n"
"--------------------------------------------------------------------------- */\n"
"QMenu {\n"
"  border: 0px solid #455364;\n"
"  color: #E0E1E3;\n"
"  margin: 0px;\n"
"  background-color: #37414F;\n"
"  selection-background-color: #1A72BB;\n"
"}\n"
"\n"
"QMenu::separator {\n"
"  height: 1px;\n"
"  background-color: #60798B;\n"
"  color: #E0E1E3;\n"
"}\n"
"\n"
"QMenu::item {\n"
"  background-color: #37414F;\n"
"  padding: 4px 24px 4px 28px;\n"
"  /* Reserve space for selection border */\n"
"  border: 1px transparent #455364;\n"
"}\n"
"\n"
"QMenu::item:selected {\n"
"  color: #E0E1E3;\n"
"  background-color: #1A72BB;\n"
"}\n"
"\n"
"QMenu::item:pressed {\n"
"  background-color: #1A72BB;\n"
"}\n"
"\n"
"QMenu::icon {\n"
"  padding-left: 10px;\n"
"  width: 14px;\n"
"  height: 14px;\n"
"}\n"
"\n"
"QMenu::indicator {\n"
"  padding-left: 8px;\n"
"  width: 12px;\n"
"  height: 12px;\n"
"  /* non-exclusive indicator = check box style indicator (see QActionGroup::setExclusive) */\n"
"  /* exclusive indicator = radio button style indicator (see QActionGroup::setExclusive) */\n"
"}\n"
"\n"
"QMenu::indicator:non-exclusive:unchecked {\n"
"  image: url(\":/qss_icons/dark/rc/checkbox_unchecked.png\");\n"
"}\n"
"\n"
"QMenu::indicator:non-exclusive:unchecked:hover, QMenu::indicator:non-exclusive:unchecked:focus, QMenu::indicator:non-exclusive:unchecked:pressed {\n"
"  border: none;\n"
"  image: url(\":/qss_icons/dark/rc/checkbox_unchecked_focus.png\");\n"
"}\n"
"\n"
"QMenu::indicator:non-exclusive:unchecked:disabled {\n"
"  image: url(\":/qss_icons/dark/rc/checkbox_unchecked_disabled.png\");\n"
"}\n"
"\n"
"QMenu::indicator:non-exclusive:checked {\n"
"  image: url(\":/qss_icons/dark/rc/checkbox_checked.png\");\n"
"}\n"
"\n"
"QMenu::indicator:non-exclusive:checked:hover, QMenu::indicator:non-exclusive:checked:focus, QMenu::indicator:non-exclusive:checked:pressed {\n"
"  border: none;\n"
"  image: url(\":/qss_icons/dark/rc/checkbox_checked_focus.png\");\n"
"}\n"
"\n"
"QMenu::indicator:non-exclusive:checked:disabled {\n"
"  image: url(\":/qss_icons/dark/rc/checkbox_checked_disabled.png\");\n"
"}\n"
"\n"
"QMenu::indicator:non-exclusive:indeterminate {\n"
"  image: url(\":/qss_icons/dark/rc/checkbox_indeterminate.png\");\n"
"}\n"
"\n"
"QMenu::indicator:non-exclusive:indeterminate:disabled {\n"
"  image: url(\":/qss_icons/dark/rc/checkbox_indeterminate_disabled.png\");\n"
"}\n"
"\n"
"QMenu::indicator:non-exclusive:indeterminate:focus, QMenu::indicator:non-exclusive:indeterminate:hover, QMenu::indicator:non-exclusive:indeterminate:pressed {\n"
"  image: url(\":/qss_icons/dark/rc/checkbox_indeterminate_focus.png\");\n"
"}\n"
"\n"
"QMenu::indicator:exclusive:unchecked {\n"
"  image: url(\":/qss_icons/dark/rc/radio_unchecked.png\");\n"
"}\n"
"\n"
"QMenu::indicator:exclusive:unchecked:hover, QMenu::indicator:exclusive:unchecked:focus, QMenu::indicator:exclusive:unchecked:pressed {\n"
"  border: none;\n"
"  outline: none;\n"
"  image: url(\":/qss_icons/dark/rc/radio_unchecked_focus.png\");\n"
"}\n"
"\n"
"QMenu::indicator:exclusive:unchecked:disabled {\n"
"  image: url(\":/qss_icons/dark/rc/radio_unchecked_disabled.png\");\n"
"}\n"
"\n"
"QMenu::indicator:exclusive:checked {\n"
"  border: none;\n"
"  outline: none;\n"
"  image: url(\":/qss_icons/dark/rc/radio_checked.png\");\n"
"}\n"
"\n"
"QMenu::indicator:exclusive:checked:hover, QMenu::indicator:exclusive:checked:focus, QMenu::indicator:exclusive:checked:pressed {\n"
"  border: none;\n"
"  outline: none;\n"
"  image: url(\":/qss_icons/dark/rc/radio_checked_focus.png\");\n"
"}\n"
"\n"
"QMenu::indicator:exclusive:checked:disabled {\n"
"  outline: none;\n"
"  image: url(\":/qss_icons/dark/rc/radio_checked_disabled.png\");\n"
"}\n"
"\n"
"QMenu::right-arrow {\n"
"  margin: 5px;\n"
"  padding-left: 12px;\n"
"  image: url(\":/qss_icons/dark/rc/arrow_right.png\");\n"
"  height: 12px;\n"
"  width: 12px;\n"
"}\n"
"\n"
"/* QAbstractItemView ------------------------------------------------------\n"
"\n"
"https://doc.qt.io/qt-5/stylesheet-examples.html#customizing-qcombobox\n"
"\n"
"--------------------------------------------------------------------------- */\n"
"QAbstractItemView {\n"
"  alternate-background-color: #19232D;\n"
"  color: #E0E1E3;\n"
"  border: 1px solid #455364;\n"
"  border-radius: 4px;\n"
"}\n"
"\n"
"QAbstractItemView QLineEdit {\n"
"  padding: 2px;\n"
"}\n"
"\n"
"/* QAbstractScrollArea ----------------------------------------------------\n"
"\n"
"https://doc.qt.io/qt-5/stylesheet-examples.html#customizing-qabstractscrollarea\n"
"\n"
"--------------------------------------------------------------------------- */\n"
"QAbstractScrollArea {\n"
"  background-color: #19232D;\n"
"  border: 1px solid #455364;\n"
"  border-radius: 4px;\n"
"  /* fix #159 */\n"
"  padding: 2px;\n"
"  /* remove min-height to fix #244 */\n"
"  color: #E0E1E3;\n"
"}\n"
"\n"
"QAbstractScrollArea:disabled {\n"
"  color: #9DA9B5;\n"
"}\n"
"\n"
"/* QScrollArea ------------------------------------------------------------\n"
"\n"
"--------------------------------------------------------------------------- */\n"
"QScrollArea QWidget QWidget:disabled {\n"
"  background-color: #19232D;\n"
"}\n"
"\n"
"/* QScrollBar -------------------------------------------------------------\n"
"\n"
"https://doc.qt.io/qt-5/stylesheet-examples.html#customizing-qscrollbar\n"
"\n"
"--------------------------------------------------------------------------- */\n"
"QScrollBar:horizontal {\n"
"  height: 16px;\n"
"  margin: 2px 16px 2px 16px;\n"
"  border: 1px solid #455364;\n"
"  border-radius: 4px;\n"
"  background-color: #19232D;\n"
"}\n"
"\n"
"QScrollBar:vertical {\n"
"  background-color: #19232D;\n"
"  width: 16px;\n"
"  margin: 16px 2px 16px 2px;\n"
"  border: 1px solid #455364;\n"
"  border-radius: 4px;\n"
"}\n"
"\n"
"QScrollBar::handle:horizontal {\n"
"  background-color: #60798B;\n"
"  border: 1px solid #455364;\n"
"  border-radius: 4px;\n"
"  min-width: 8px;\n"
"}\n"
"\n"
"QScrollBar::handle:horizontal:hover {\n"
"  background-color: #346792;\n"
"  border: #346792;\n"
"  border-radius: 4px;\n"
"  min-width: 8px;\n"
"}\n"
"\n"
"QScrollBar::handle:horizontal:focus {\n"
"  border: 1px solid #1A72BB;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical {\n"
"  background-color: #60798B;\n"
"  border: 1px solid #455364;\n"
"  min-height: 8px;\n"
"  border-radius: 4px;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical:hover {\n"
"  background-color: #346792;\n"
"  border: #346792;\n"
"  border-radius: 4px;\n"
"  min-height: 8px;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical:focus {\n"
"  border: 1px solid #1A72BB;\n"
"}\n"
"\n"
"QScrollBar::add-line:horizontal {\n"
"  margin: 0px 0px 0px 0px;\n"
"  border-image: url(\":/qss_icons/dark/rc/arrow_right_disabled.png\");\n"
"  height: 12px;\n"
"  width: 12px;\n"
"  subcontrol-position: right;\n"
"  subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::add-line:horizontal:hover, QScrollBar::add-line:horizontal:on {\n"
"  border-image: url(\":/qss_icons/dark/rc/arrow_right.png\");\n"
"  height: 12px;\n"
"  width: 12px;\n"
"  subcontrol-position: right;\n"
"  subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::add-line:vertical {\n"
"  margin: 3px 0px 3px 0px;\n"
"  border-image: url(\":/qss_icons/dark/rc/arrow_down_disabled.png\");\n"
"  height: 12px;\n"
"  width: 12px;\n"
"  subcontrol-position: bottom;\n"
"  subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::add-line:vertical:hover, QScrollBar::add-line:vertical:on {\n"
"  border-image: url(\":/qss_icons/dark/rc/arrow_down.png\");\n"
"  height: 12px;\n"
"  width: 12px;\n"
"  subcontrol-position: bottom;\n"
"  subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::sub-line:horizontal {\n"
"  margin: 0px 3px 0px 3px;\n"
"  border-image: url(\":/qss_icons/dark/rc/arrow_left_disabled.png\");\n"
"  height: 12px;\n"
"  width: 12px;\n"
"  subcontrol-position: left;\n"
"  subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::sub-line:horizontal:hover, QScrollBar::sub-line:horizontal:on {\n"
"  border-image: url(\":/qss_icons/dark/rc/arrow_left.png\");\n"
"  height: 12px;\n"
"  width: 12px;\n"
"  subcontrol-position: left;\n"
"  subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::sub-line:vertical {\n"
"  margin: 3px 0px 3px 0px;\n"
"  border-image: url(\":/qss_icons/dark/rc/arrow_up_disabled.png\");\n"
"  height: 12px;\n"
"  width: 12px;\n"
"  subcontrol-position: top;\n"
"  subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::sub-line:vertical:hover, QScrollBar::sub-line:vertical:on {\n"
"  border-image: url(\":/qss_icons/dark/rc/arrow_up.png\");\n"
"  height: 12px;\n"
"  width: 12px;\n"
"  subcontrol-position: top;\n"
"  subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::up-arrow:horizontal, QScrollBar::down-arrow:horizontal {\n"
"  background: none;\n"
"}\n"
"\n"
"QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
"  background: none;\n"
"}\n"
"\n"
"QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal {\n"
"  background: none;\n"
"}\n"
"\n"
"QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
"  background: none;\n"
"}\n"
"\n"
"/* QTextEdit --------------------------------------------------------------\n"
"\n"
"https://doc.qt.io/qt-5/stylesheet-examples.html#customizing-specific-widgets\n"
"\n"
"--------------------------------------------------------------------------- */\n"
"QTextEdit {\n"
"  background-color: #19232D;\n"
"  color: #E0E1E3;\n"
"  border-radius: 4px;\n"
"  border: 1px solid #455364;\n"
"}\n"
"\n"
"QTextEdit:focus {\n"
"  border: 1px solid #1A72BB;\n"
"}\n"
"\n"
"QTextEdit:selected {\n"
"  background: #346792;\n"
"  color: #455364;\n"
"}\n"
"\n"
"/* QPlainTextEdit ---------------------------------------------------------\n"
"\n"
"--------------------------------------------------------------------------- */\n"
"QPlainTextEdit {\n"
"  background-color: #19232D;\n"
"  color: #E0E1E3;\n"
"  border-radius: 4px;\n"
"  border: 1px solid #455364;\n"
"}\n"
"\n"
"QPlainTextEdit:focus {\n"
"  border: 1px solid #1A72BB;\n"
"}\n"
"\n"
"QPlainTextEdit:selected {\n"
"  background: #346792;\n"
"  color: #455364;\n"
"}\n"
"\n"
"/* QSizeGrip --------------------------------------------------------------\n"
"\n"
"https://doc.qt.io/qt-5/stylesheet-examples.html#customizing-qsizegrip\n"
"\n"
"--------------------------------------------------------------------------- */\n"
"QSizeGrip {\n"
"  background: transparent;\n"
"  width: 12px;\n"
"  height: 12px;\n"
"  image: url(\":/qss_icons/dark/rc/window_grip.png\");\n"
"}\n"
"\n"
"/* QStackedWidget ---------------------------------------------------------\n"
"\n"
"--------------------------------------------------------------------------- */\n"
"QStackedWidget {\n"
"  padding: 2px;\n"
"  border: 1px solid #455364;\n"
"  border: 1px solid #19232D;\n"
"}\n"
"\n"
"/* QToolBar ---------------------------------------------------------------\n"
"\n"
"https://doc.qt.io/qt-5/stylesheet-examples.html#customizing-qtoolbar\n"
"\n"
"--------------------------------------------------------------------------- */\n"
"QToolBar {\n"
"  background-color: #455364;\n"
"  border-bottom: 1px solid #19232D;\n"
"  padding: 1px;\n"
"  font-weight: bold;\n"
"  spacing: 2px;\n"
"}\n"
"\n"
"QToolBar:disabled {\n"
"  /* Fixes #272 */\n"
"  background-color: #455364;\n"
"}\n"
"\n"
"QToolBar::handle:horizontal {\n"
"  width: 16px;\n"
"  image: url(\":/qss_icons/dark/rc/toolbar_move_horizontal.png\");\n"
"}\n"
"\n"
"QToolBar::handle:vertical {\n"
"  height: 16px;\n"
"  image: url(\":/qss_icons/dark/rc/toolbar_move_vertical.png\");\n"
"}\n"
"\n"
"QToolBar::separator:horizontal {\n"
"  width: 16px;\n"
"  image: url(\":/qss_icons/dark/rc/toolbar_separator_horizontal.png\");\n"
"}\n"
"\n"
"QToolBar::separator:vertical {\n"
"  height: 16px;\n"
"  image: url(\":/qss_icons/dark/rc/toolbar_separator_vertical.png\");\n"
"}\n"
"\n"
"QToolButton#qt_toolbar_ext_button {\n"
"  background: #455364;\n"
"  border: 0px;\n"
"  color: #E0E1E3;\n"
"  image: url(\":/qss_icons/dark/rc/arrow_right.png\");\n"
"}\n"
"\n"
"/* QAbstractSpinBox -------------------------------------------------------\n"
"\n"
"--------------------------------------------------------------------------- */\n"
"QAbstractSpinBox {\n"
"  background-color: #19232D;\n"
"  border: 1px solid #455364;\n"
"  color: #E0E1E3;\n"
"  /* This fixes 103, 111 */\n"
"  padding-top: 2px;\n"
"  /* This fixes 103, 111 */\n"
"  padding-bottom: 2px;\n"
"  padding-left: 4px;\n"
"  padding-right: 4px;\n"
"  border-radius: 4px;\n"
"  /* min-width: 5px; removed to fix 109 */\n"
"}\n"
"\n"
"QAbstractSpinBox:up-button {\n"
"  background-color: transparent #19232D;\n"
"  subcontrol-origin: border;\n"
"  subcontrol-position: top right;\n"
"  border-left: 1px solid #455364;\n"
"  border-bottom: 1px solid #455364;\n"
"  border-top-left-radius: 0;\n"
"  border-bottom-left-radius: 0;\n"
"  margin: 1px;\n"
"  width: 12px;\n"
"  margin-bottom: -1px;\n"
"}\n"
"\n"
"QAbstractSpinBox::up-arrow, QAbstractSpinBox::up-arrow:disabled, QAbstractSpinBox::up-arrow:off {\n"
"  image: url(\":/qss_icons/dark/rc/arrow_up_disabled.png\");\n"
"  height: 8px;\n"
"  width: 8px;\n"
"}\n"
"\n"
"QAbstractSpinBox::up-arrow:hover {\n"
"  image: url(\":/qss_icons/dark/rc/arrow_up.png\");\n"
"}\n"
"\n"
"QAbstractSpinBox:down-button {\n"
"  background-color: transparent #19232D;\n"
"  subcontrol-origin: border;\n"
"  subcontrol-position: bottom right;\n"
"  border-left: 1px solid #455364;\n"
"  border-top: 1px solid #455364;\n"
"  border-top-left-radius: 0;\n"
"  border-bottom-left-radius: 0;\n"
"  margin: 1px;\n"
"  width: 12px;\n"
"  margin-top: -1px;\n"
"}\n"
"\n"
"QAbstractSpinBox::down-arrow, QAbstractSpinBox::down-arrow:disabled, QAbstractSpinBox::down-arrow:off {\n"
"  image: url(\":/qss_icons/dark/rc/arrow_down_disabled.png\");\n"
"  height: 8px;\n"
"  width: 8px;\n"
"}\n"
"\n"
"QAbstractSpinBox::down-arrow:hover {\n"
"  image: url(\":/qss_icons/dark/rc/arrow_down.png\");\n"
"}\n"
"\n"
"QAbstractSpinBox:hover {\n"
"  border: 1px solid #346792;\n"
"  color: #E0E1E3;\n"
"}\n"
"\n"
"QAbstractSpinBox:focus {\n"
"  border: 1px solid #1A72BB;\n"
"}\n"
"\n"
"QAbstractSpinBox:selected {\n"
"  background: #346792;\n"
"  color: #455364;\n"
"}\n"
"\n"
"/* ------------------------------------------------------------------------ */\n"
"/* DISPLAYS --------------------------------------------------------------- */\n"
"/* ------------------------------------------------------------------------ */\n"
"/* QLabel -----------------------------------------------------------------\n"
"\n"
"https://doc.qt.io/qt-5/stylesheet-examples.html#customizing-qframe\n"
"\n"
"--------------------------------------------------------------------------- */\n"
"QLabel {\n"
"  background-color: #19232D;\n"
"  border: 0px solid #455364;\n"
"  padding: 2px;\n"
"  margin: 0px;\n"
"  color: #E0E1E3;\n"
"  font-size: 20px;\n"
"  border: 2px solid #455364;\n"
"  border-radius: 4px;\n"
"}\n"
"\n"
"QLabel:disabled {\n"
"  background-color: #19232D;\n"
"  border: 0px solid #455364;\n"
"  color: #9DA9B5;\n"
"}\n"
"\n"
"/* QTextBrowser -----------------------------------------------------------\n"
"\n"
"https://doc.qt.io/qt-5/stylesheet-examples.html#customizing-qabstractscrollarea\n"
"\n"
"--------------------------------------------------------------------------- */\n"
"QTextBrowser {\n"
"  background-color: #19232D;\n"
"  border: 1px solid #455364;\n"
"  color: #E0E1E3;\n"
"  border-radius: 4px;\n"
"}\n"
"\n"
"QTextBrowser:disabled {\n"
"  background-color: #19232D;\n"
"  border: 1px solid #455364;\n"
"  color: #9DA9B5;\n"
"  border-radius: 4px;\n"
"}\n"
"\n"
"QTextBrowser:hover, QTextBrowser:!hover, QTextBrowser:selected, QTextBrowser:pressed {\n"
"  border: 1px solid #455364;\n"
"}\n"
"\n"
"/* QGraphicsView ----------------------------------------------------------\n"
"\n"
"--------------------------------------------------------------------------- */\n"
"QGraphicsView {\n"
"  background-color: #19232D;\n"
"  border: 1px solid #455364;\n"
"  color: #E0E1E3;\n"
"  border-radius: 4px;\n"
"}\n"
"\n"
"QGraphicsView:disabled {\n"
"  background-color: #19232D;\n"
"  border: 1px solid #455364;\n"
"  color: #9DA9B5;\n"
"  border-radius: 4px;\n"
"}\n"
"\n"
"QGraphicsView:hover, QGraphicsView:!hover, QGraphicsView:selected, QGraphicsView:pressed {\n"
"  border: 1px solid #455364;\n"
"}\n"
"\n"
"/* QCalendarWidget --------------------------------------------------------\n"
"\n"
"--------------------------------------------------------------------------- */\n"
"QCalendarWidget {\n"
"  border: 1px solid #455364;\n"
"  border-radius: 4px;\n"
"}\n"
"\n"
"QCalendarWidget:disabled {\n"
"  background-color: #19232D;\n"
"  color: #9DA9B5;\n"
"}\n"
"\n"
"/* QLCDNumber -------------------------------------------------------------\n"
"\n"
"--------------------------------------------------------------------------- */\n"
"QLCDNumber {\n"
"  background-color: #19232D;\n"
"  color: #E0E1E3;\n"
"}\n"
"\n"
"QLCDNumber:disabled {\n"
"  background-color: #19232D;\n"
"  color: #9DA9B5;\n"
"}\n"
"\n"
"/* QProgressBar -----------------------------------------------------------\n"
"\n"
"https://doc.qt.io/qt-5/stylesheet-examples.html#customizing-qprogressbar\n"
"\n"
"--------------------------------------------------------------------------- */\n"
"QProgressBar {\n"
"  background-color: #19232D;\n"
"  border: 1px solid #455364;\n"
"  color: #E0E1E3;\n"
"  border-radius: 4px;\n"
"  text-align: center;\n"
"}\n"
"\n"
"QProgressBar:disabled {\n"
"  background-color: #19232D;\n"
"  border: 1px solid #455364;\n"
"  color: #9DA9B5;\n"
"  border-radius: 4px;\n"
"  text-align: center;\n"
"}\n"
"\n"
"QProgressBar::chunk {\n"
"  background-color: #346792;\n"
"  color: #19232D;\n"
"  border-radius: 4px;\n"
"}\n"
"\n"
"QProgressBar::chunk:disabled {\n"
"  background-color: #26486B;\n"
"  color: #9DA9B5;\n"
"  border-radius: 4px;\n"
"}\n"
"\n"
"/* ------------------------------------------------------------------------ */\n"
"/* BUTTONS ---------------------------------------------------------------- */\n"
"/* ------------------------------------------------------------------------ */\n"
"/* QPushButton ------------------------------------------------------------\n"
"\n"
"https://doc.qt.io/qt-5/stylesheet-examples.html#customizing-qpushbutton\n"
"\n"
"--------------------------------------------------------------------------- */\n"
"QPushButton {\n"
"  background-color: #455364;\n"
"  color: #E0E1E3;\n"
"  border-radius: 4px;\n"
"  padding: 2px;\n"
"  outline: none;\n"
"  border: none;\n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"  background-color: #455364;\n"
"  color: #9DA9B5;\n"
"  border-radius: 4px;\n"
"  padding: 2px;\n"
"}\n"
"\n"
"QPushButton:checked {\n"
"  background-color: #60798B;\n"
"  border-radius: 4px;\n"
"  padding: 2px;\n"
"  outline: none;\n"
"}\n"
"\n"
"QPushButton:checked:disabled {\n"
"  background-color: #60798B;\n"
"  color: #9DA9B5;\n"
"  border-radius: 4px;\n"
"  padding: 2px;\n"
"  outline: none;\n"
"}\n"
"\n"
"QPushButton:checked:selected {\n"
"  background: #60798B;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"  background-color: #54687A;\n"
"  color: #E0E1E3;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"  background-color: #60798B;\n"
"}\n"
"\n"
"QPushButton:selected {\n"
"  background: #60798B;\n"
"  color: #E0E1E3;\n"
"}\n"
"\n"
"QPushButton::menu-indicator {\n"
"  subcontrol-origin: padding;\n"
"  subcontrol-position: bottom right;\n"
"  bottom: 4px;\n"
"}\n"
"\n"
"QDialogButtonBox QPushButton {\n"
"  /* Issue #194 #248 - Special case of QPushButton inside dialogs, for better UI */\n"
"  min-width: 80px;\n"
"}\n"
"\n"
"/* QToolButton ------------------------------------------------------------\n"
"\n"
"https://doc.qt.io/qt-5/stylesheet-examples.html#customizing-qtoolbutton\n"
"\n"
"--------------------------------------------------------------------------- */\n"
"QToolButton {\n"
"  background-color: #455364;\n"
"  color: #E0E1E3;\n"
"  border-radius: 4px;\n"
"  padding: 2px;\n"
"  outline: none;\n"
"  border: none;\n"
"  /* The subcontrols below are used only in the DelayedPopup mode */\n"
"  /* The subcontrols below are used only in the MenuButtonPopup mode */\n"
"  /* The subcontrol below is used only in the InstantPopup or DelayedPopup mode */\n"
"}\n"
"\n"
"QToolButton:disabled {\n"
"  background-color: #455364;\n"
"  color: #9DA9B5;\n"
"  border-radius: 4px;\n"
"  padding: 2px;\n"
"}\n"
"\n"
"QToolButton:checked {\n"
"  background-color: #60798B;\n"
"  border-radius: 4px;\n"
"  padding: 2px;\n"
"  outline: none;\n"
"}\n"
"\n"
"QToolButton:checked:disabled {\n"
"  background-color: #60798B;\n"
"  color: #9DA9B5;\n"
"  border-radius: 4px;\n"
"  padding: 2px;\n"
"  outline: none;\n"
"}\n"
"\n"
"QToolButton:checked:hover {\n"
"  background-color: #54687A;\n"
"  color: #E0E1E3;\n"
"}\n"
"\n"
"QToolButton:checked:pressed {\n"
"  background-color: #60798B;\n"
"}\n"
"\n"
"QToolButton:checked:selected {\n"
"  background: #60798B;\n"
"  color: #E0E1E3;\n"
"}\n"
"\n"
"QToolButton:hover {\n"
"  background-color: #54687A;\n"
"  color: #E0E1E3;\n"
"}\n"
"\n"
"QToolButton:pressed {\n"
"  background-color: #60798B;\n"
"}\n"
"\n"
"QToolButton:selected {\n"
"  background: #60798B;\n"
"  color: #E0E1E3;\n"
"}\n"
"\n"
"QToolButton[popupMode=\"0\"] {\n"
"  /* Only for DelayedPopup */\n"
"  padding-right: 2px;\n"
"}\n"
"\n"
"QToolButton[popupMode=\"1\"] {\n"
"  /* Only for MenuButtonPopup */\n"
"  padding-right: 20px;\n"
"}\n"
"\n"
"QToolButton[popupMode=\"1\"]::menu-button {\n"
"  border: none;\n"
"}\n"
"\n"
"QToolButton[popupMode=\"1\"]::menu-button:hover {\n"
"  border: none;\n"
"  border-left: 1px solid #455364;\n"
"  border-radius: 0;\n"
"}\n"
"\n"
"QToolButton[popupMode=\"2\"] {\n"
"  /* Only for InstantPopup */\n"
"  padding-right: 2px;\n"
"}\n"
"\n"
"QToolButton::menu-button {\n"
"  padding: 2px;\n"
"  border-radius: 4px;\n"
"  width: 12px;\n"
"  border: none;\n"
"  outline: none;\n"
"}\n"
"\n"
"QToolButton::menu-button:hover {\n"
"  border: 1px solid #346792;\n"
"}\n"
"\n"
"QToolButton::menu-button:checked:hover {\n"
"  border: 1px solid #346792;\n"
"}\n"
"\n"
"QToolButton::menu-indicator {\n"
"  image: url(\":/qss_icons/dark/rc/arrow_down.png\");\n"
"  height: 8px;\n"
"  width: 8px;\n"
"  top: 0;\n"
"  /* Exclude a shift for better image */\n"
"  left: -2px;\n"
"  /* Shift it a bit */\n"
"}\n"
"\n"
"QToolButton::menu-arrow {\n"
"  image: url(\":/qss_icons/dark/rc/arrow_down.png\");\n"
"  height: 8px;\n"
"  width: 8px;\n"
"}\n"
"\n"
"QToolButton::menu-arrow:hover {\n"
"  image: url(\":/qss_icons/dark/rc/arrow_down_focus.png\");\n"
"}\n"
"\n"
"/* QCommandLinkButton -----------------------------------------------------\n"
"\n"
"--------------------------------------------------------------------------- */\n"
"QCommandLinkButton {\n"
"  background-color: transparent;\n"
"  border: 1px solid #455364;\n"
"  color: #E0E1E3;\n"
"  border-radius: 4px;\n"
"  padding: 0px;\n"
"  margin: 0px;\n"
"}\n"
"\n"
"QCommandLinkButton:disabled {\n"
"  background-color: transparent;\n"
"  color: #9DA9B5;\n"
"}\n"
"\n"
"/* ------------------------------------------------------------------------ */\n"
"/* INPUTS - NO FIELDS ----------------------------------------------------- */\n"
"/* ------------------------------------------------------------------------ */\n"
"/* QComboBox --------------------------------------------------------------\n"
"\n"
"https://doc.qt.io/qt-5/stylesheet-examples.html#customizing-qcombobox\n"
"\n"
"--------------------------------------------------------------------------- */\n"
"QComboBox {\n"
"  border: 1px solid #455364;\n"
"  border-radius: 4px;\n"
"  selection-background-color: #346792;\n"
"  padding-left: 4px;\n"
"  padding-right: 4px;\n"
"  /* padding-right = 36; 4 + 16*2 See scrollbar size */\n"
"  /* changed to 4px to fix #239 */\n"
"  /* Fixes #103, #111 */\n"
"  min-height: 1.5em;\n"
"  /* padding-top: 2px;     removed to fix #132 */\n"
"  /* padding-bottom: 2px;  removed to fix #132 */\n"
"  /* min-width: 75px;      removed to fix #109 */\n"
"  /* Needed to remove indicator - fix #132 */\n"
"}\n"
"\n"
"QComboBox QAbstractItemView {\n"
"  border: 1px solid #455364;\n"
"  border-radius: 0;\n"
"  background-color: #19232D;\n"
"  selection-background-color: #346792;\n"
"}\n"
"\n"
"QComboBox QAbstractItemView:hover {\n"
"  background-color: #19232D;\n"
"  color: #E0E1E3;\n"
"}\n"
"\n"
"QComboBox QAbstractItemView:selected {\n"
"  background: #346792;\n"
"  color: #455364;\n"
"}\n"
"\n"
"QComboBox QAbstractItemView:alternate {\n"
"  background: #19232D;\n"
"}\n"
"\n"
"QComboBox:disabled {\n"
"  background-color: #19232D;\n"
"  color: #9DA9B5;\n"
"}\n"
"\n"
"QComboBox:hover {\n"
"  border: 1px solid #346792;\n"
"}\n"
"\n"
"QComboBox:focus {\n"
"  border: 1px solid #1A72BB;\n"
"}\n"
"\n"
"QComboBox:on {\n"
"  selection-background-color: #346792;\n"
"}\n"
"\n"
"QComboBox::indicator {\n"
"  border: none;\n"
"  border-radius: 0;\n"
"  background-color: transparent;\n"
"  selection-background-color: transparent;\n"
"  color: transparent;\n"
"  selection-color: transparent;\n"
"  /* Needed to remove indicator - fix #132 */\n"
"}\n"
"\n"
"QComboBox::indicator:alternate {\n"
"  background: #19232D;\n"
"}\n"
"\n"
"QComboBox::item {\n"
"  /* Remove to fix #282, #285 and MR #288*/\n"
"  /*&:checked {\n"
"            font-weight: bold;\n"
"        }\n"
"\n"
"        &:selected {\n"
"            border: 0px solid transparent;\n"
"        }\n"
"        */\n"
"}\n"
"\n"
"QComboBox::item:alternate {\n"
"  background: #19232D;\n"
"}\n"
"\n"
"QComboBox::drop-down {\n"
"  subcontrol-origin: padding;\n"
"  subcontrol-position: top right;\n"
"  width: 12px;\n"
"  border-left: 1px solid #455364;\n"
"}\n"
"\n"
"QComboBox::down-arrow {\n"
"  image: url(\":/qss_icons/dark/rc/arrow_down_disabled.png\");\n"
"  height: 8px;\n"
"  width: 8px;\n"
"}\n"
"\n"
"QComboBox::down-arrow:on, QComboBox::down-arrow:hover, QComboBox::down-arrow:focus {\n"
"  image: url(\":/qss_icons/dark/rc/arrow_down.png\");\n"
"}\n"
"\n"
"/* QSlider ----------------------------------------------------------------\n"
"\n"
"https://doc.qt.io/qt-5/stylesheet-examples.html#customizing-qslider\n"
"\n"
"--------------------------------------------------------------------------- */\n"
"QSlider:disabled {\n"
"  background: #19232D;\n"
"}\n"
"\n"
"QSlider:focus {\n"
"  border: none;\n"
"}\n"
"\n"
"QSlider::groove:horizontal {\n"
"  background: #455364;\n"
"  border: 1px solid #455364;\n"
"  height: 4px;\n"
"  margin: 0px;\n"
"  border-radius: 4px;\n"
"}\n"
"\n"
"QSlider::groove:vertical {\n"
"  background: #455364;\n"
"  border: 1px solid #455364;\n"
"  width: 4px;\n"
"  margin: 0px;\n"
"  border-radius: 4px;\n"
"}\n"
"\n"
"QSlider::add-page:vertical {\n"
"  background: #346792;\n"
"  border: 1px solid #455364;\n"
"  width: 4px;\n"
"  margin: 0px;\n"
"  border-radius: 4px;\n"
"}\n"
"\n"
"QSlider::add-page:vertical :disabled {\n"
"  background: #26486B;\n"
"}\n"
"\n"
"QSlider::sub-page:horizontal {\n"
"  background: #346792;\n"
"  border: 1px solid #455364;\n"
"  height: 4px;\n"
"  margin: 0px;\n"
"  border-radius: 4px;\n"
"}\n"
"\n"
"QSlider::sub-page:horizontal:disabled {\n"
"  background: #26486B;\n"
"}\n"
"\n"
"QSlider::handle:horizontal {\n"
"  background: #9DA9B5;\n"
"  border: 1px solid #455364;\n"
"  width: 8px;\n"
"  height: 8px;\n"
"  margin: -8px 0px;\n"
"  border-radius: 4px;\n"
"}\n"
"\n"
"QSlider::handle:horizontal:hover {\n"
"  background: #346792;\n"
"  border: 1px solid #346792;\n"
"}\n"
"\n"
"QSlider::handle:horizontal:focus {\n"
"  border: 1px solid #1A72BB;\n"
"}\n"
"\n"
"QSlider::handle:vertical {\n"
"  background: #9DA9B5;\n"
"  border: 1px solid #455364;\n"
"  width: 8px;\n"
"  height: 8px;\n"
"  margin: 0 -8px;\n"
"  border-radius: 4px;\n"
"}\n"
"\n"
"QSlider::handle:vertical:hover {\n"
"  background: #346792;\n"
"  border: 1px solid #346792;\n"
"}\n"
"\n"
"QSlider::handle:vertical:focus {\n"
"  border: 1px solid #1A72BB;\n"
"}\n"
"\n"
"/* QLineEdit --------------------------------------------------------------\n"
"\n"
"https://doc.qt.io/qt-5/stylesheet-examples.html#customizing-qlineedit\n"
"\n"
"--------------------------------------------------------------------------- */\n"
"QLineEdit {\n"
"  background-color: #19232D;\n"
"  padding-top: 2px;\n"
"  /* This QLineEdit fix  103, 111 */\n"
"  padding-bottom: 2px;\n"
"  /* This QLineEdit fix  103, 111 */\n"
"  padding-left: 4px;\n"
"  padding-right: 4px;\n"
"  border-style: solid;\n"
"  border: 1px solid #455364;\n"
"  border-radius: 4px;\n"
"  color: #E0E1E3;\n"
"  \n"
"}\n"
"\n"
"QLineEdit:disabled {\n"
"  background-color: #19232D;\n"
"  color: #9DA9B5;\n"
"}\n"
"\n"
"QLineEdit:hover {\n"
"  border: 1px solid #346792;\n"
"  color: #E0E1E3;\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"  border: 1px solid #1A72BB;\n"
"}\n"
"\n"
"QLineEdit:selected {\n"
"  background-color: #346792;\n"
"  color: #455364;\n"
"}\n"
"\n"
"/* QTabWiget --------------------------------------------------------------\n"
"\n"
"https://doc.qt.io/qt-5/stylesheet-examples.html#customizing-qtabwidget-and-qtabbar\n"
"\n"
"--------------------------------------------------------------------------- */\n"
"QTabWidget {\n"
"  padding: 2px;\n"
"  selection-background-color: #455364;\n"
"}\n"
"\n"
"QTabWidget QWidget {\n"
"  /* Fixes #189 */\n"
"  border-radius: 4px;\n"
"}\n"
"\n"
"QTabWidget::pane {\n"
"  border: 1px solid #455364;\n"
"  border-radius: 4px;\n"
"  margin: 0px;\n"
"  /* Fixes double border inside pane with pyqt5 */\n"
"  padding: 0px;\n"
"}\n"
"\n"
"QTabWidget::pane:selected {\n"
"  background-color: #455364;\n"
"  border: 1px solid #346792;\n"
"}\n"
"\n"
"/* QTabBar ----------------------------------------------------------------\n"
"\n"
"https://doc.qt.io/qt-5/stylesheet-examples.html#customizing-qtabwidget-and-qtabbar\n"
"\n"
"--------------------------------------------------------------------------- */\n"
"QTabBar, QDockWidget QTabBar {\n"
"  qproperty-drawBase: 0;\n"
"  border-radius: 4px;\n"
"  margin: 0px;\n"
"  padding: 2px;\n"
"  border: 0;\n"
"  /* left: 5px; move to the right by 5px - removed for fix */\n"
"}\n"
"\n"
"QTabBar::close-button, QDockWidget QTabBar::close-button {\n"
"  border: 0;\n"
"  margin: 0;\n"
"  padding: 4px;\n"
"  image: url(\":/qss_icons/dark/rc/window_close.png\");\n"
"}\n"
"\n"
"QTabBar::close-button:hover, QDockWidget QTabBar::close-button:hover {\n"
"  image: url(\":/qss_icons/dark/rc/window_close_focus.png\");\n"
"}\n"
"\n"
"QTabBar::close-button:pressed, QDockWidget QTabBar::close-button:pressed {\n"
"  image: url(\":/qss_icons/dark/rc/window_close_pressed.png\");\n"
"}\n"
"\n"
"QTabBar::tab, QDockWidget QTabBar::tab {\n"
"  /* !selected and disabled ----------------------------------------- */\n"
"  /* selected ------------------------------------------------------- */\n"
"}\n"
"\n"
"QTabBar::tab:top:selected:disabled, QDockWidget QTabBar::tab:top:selected:disabled {\n"
"  border-bottom: 3px solid #26486B;\n"
"  color: #9DA9B5;\n"
"  background-color: #455364;\n"
"}\n"
"\n"
"QTabBar::tab:bottom:selected:disabled, QDockWidget QTabBar::tab:bottom:selected:disabled {\n"
"  border-top: 3px solid #26486B;\n"
"  color: #9DA9B5;\n"
"  background-color: #455364;\n"
"}\n"
"\n"
"QTabBar::tab:left:selected:disabled, QDockWidget QTabBar::tab:left:selected:disabled {\n"
"  border-right: 3px solid #26486B;\n"
"  color: #9DA9B5;\n"
"  background-color: #455364;\n"
"}\n"
"\n"
"QTabBar::tab:right:selected:disabled, QDockWidget QTabBar::tab:right:selected:disabled {\n"
"  border-left: 3px solid #26486B;\n"
"  color: #9DA9B5;\n"
"  background-color: #455364;\n"
"}\n"
"\n"
"QTabBar::tab:top:!selected:disabled, QDockWidget QTabBar::tab:top:!selected:disabled {\n"
"  border-bottom: 3px solid #19232D;\n"
"  color: #9DA9B5;\n"
"  background-color: #19232D;\n"
"}\n"
"\n"
"QTabBar::tab:bottom:!selected:disabled, QDockWidget QTabBar::tab:bottom:!selected:disabled {\n"
"  border-top: 3px solid #19232D;\n"
"  color: #9DA9B5;\n"
"  background-color: #19232D;\n"
"}\n"
"\n"
"QTabBar::tab:left:!selected:disabled, QDockWidget QTabBar::tab:left:!selected:disabled {\n"
"  border-right: 3px solid #19232D;\n"
"  color: #9DA9B5;\n"
"  background-color: #19232D;\n"
"}\n"
"\n"
"QTabBar::tab:right:!selected:disabled, QDockWidget QTabBar::tab:right:!selected:disabled {\n"
"  border-left: 3px solid #19232D;\n"
"  color: #9DA9B5;\n"
"  background-color: #19232D;\n"
"}\n"
"\n"
"QTabBar::tab:top:!selected, QDockWidget QTabBar::tab:top:!selected {\n"
"  border-bottom: 2px solid #19232D;\n"
"  margin-top: 2px;\n"
"}\n"
"\n"
"QTabBar::tab:bottom:!selected, QDockWidget QTabBar::tab:bottom:!selected {\n"
"  border-top: 2px solid #19232D;\n"
"  margin-bottom: 2px;\n"
"}\n"
"\n"
"QTabBar::tab:left:!selected, QDockWidget QTabBar::tab:left:!selected {\n"
"  border-left: 2px solid #19232D;\n"
"  margin-right: 2px;\n"
"}\n"
"\n"
"QTabBar::tab:right:!selected, QDockWidget QTabBar::tab:right:!selected {\n"
"  border-right: 2px solid #19232D;\n"
"  margin-left: 2px;\n"
"}\n"
"\n"
"QTabBar::tab:top, QDockWidget QTabBar::tab:top {\n"
"  background-color: #455364;\n"
"  margin-left: 2px;\n"
"  padding-left: 4px;\n"
"  padding-right: 4px;\n"
"  padding-top: 2px;\n"
"  padding-bottom: 2px;\n"
"  min-width: 5px;\n"
"  border-bottom: 3px solid #455364;\n"
"  border-top-left-radius: 4px;\n"
"  border-top-right-radius: 4px;\n"
"}\n"
"\n"
"QTabBar::tab:top:selected, QDockWidget QTabBar::tab:top:selected {\n"
"  background-color: #54687A;\n"
"  border-bottom: 3px solid #259AE9;\n"
"  border-top-left-radius: 4px;\n"
"  border-top-right-radius: 4px;\n"
"}\n"
"\n"
"QTabBar::tab:top:!selected:hover, QDockWidget QTabBar::tab:top:!selected:hover {\n"
"  border: 1px solid #1A72BB;\n"
"  border-bottom: 3px solid #1A72BB;\n"
"  /* Fixes spyder-ide/spyder#9766 and #243 */\n"
"  padding-left: 3px;\n"
"  padding-right: 3px;\n"
"}\n"
"\n"
"QTabBar::tab:bottom, QDockWidget QTabBar::tab:bottom {\n"
"  border-top: 3px solid #455364;\n"
"  background-color: #455364;\n"
"  margin-left: 2px;\n"
"  padding-left: 4px;\n"
"  padding-right: 4px;\n"
"  padding-top: 2px;\n"
"  padding-bottom: 2px;\n"
"  border-bottom-left-radius: 4px;\n"
"  border-bottom-right-radius: 4px;\n"
"  min-width: 5px;\n"
"}\n"
"\n"
"QTabBar::tab:bottom:selected, QDockWidget QTabBar::tab:bottom:selected {\n"
"  background-color: #54687A;\n"
"  border-top: 3px solid #259AE9;\n"
"  border-bottom-left-radius: 4px;\n"
"  border-bottom-right-radius: 4px;\n"
"}\n"
"\n"
"QTabBar::tab:bottom:!selected:hover, QDockWidget QTabBar::tab:bottom:!selected:hover {\n"
"  border: 1px solid #1A72BB;\n"
"  border-top: 3px solid #1A72BB;\n"
"  /* Fixes spyder-ide/spyder#9766 and #243 */\n"
"  padding-left: 3px;\n"
"  padding-right: 3px;\n"
"}\n"
"\n"
"QTabBar::tab:left, QDockWidget QTabBar::tab:left {\n"
"  background-color: #455364;\n"
"  margin-top: 2px;\n"
"  padding-left: 2px;\n"
"  padding-right: 2px;\n"
"  padding-top: 4px;\n"
"  padding-bottom: 4px;\n"
"  border-top-left-radius: 4px;\n"
"  border-bottom-left-radius: 4px;\n"
"  min-height: 5px;\n"
"}\n"
"\n"
"QTabBar::tab:left:selected, QDockWidget QTabBar::tab:left:selected {\n"
"  background-color: #54687A;\n"
"  border-right: 3px solid #259AE9;\n"
"}\n"
"\n"
"QTabBar::tab:left:!selected:hover, QDockWidget QTabBar::tab:left:!selected:hover {\n"
"  border: 1px solid #1A72BB;\n"
"  border-right: 3px solid #1A72BB;\n"
"  /* Fixes different behavior #271 */\n"
"  margin-right: 0px;\n"
"  padding-right: -1px;\n"
"}\n"
"\n"
"QTabBar::tab:right, QDockWidget QTabBar::tab:right {\n"
"  background-color: #455364;\n"
"  margin-top: 2px;\n"
"  padding-left: 2px;\n"
"  padding-right: 2px;\n"
"  padding-top: 4px;\n"
"  padding-bottom: 4px;\n"
"  border-top-right-radius: 4px;\n"
"  border-bottom-right-radius: 4px;\n"
"  min-height: 5px;\n"
"}\n"
"\n"
"QTabBar::tab:right:selected, QDockWidget QTabBar::tab:right:selected {\n"
"  background-color: #54687A;\n"
"  border-left: 3px solid #259AE9;\n"
"}\n"
"\n"
"QTabBar::tab:right:!selected:hover, QDockWidget QTabBar::tab:right:!selected:hover {\n"
"  border: 1px solid #1A72BB;\n"
"  border-left: 3px solid #1A72BB;\n"
"  /* Fixes different behavior #271 */\n"
"  margin-left: 0px;\n"
"  padding-left: 0px;\n"
"}\n"
"\n"
"QTabBar QToolButton, QDockWidget QTabBar QToolButton {\n"
"  /* Fixes #136 */\n"
"  background-color: #455364;\n"
"  height: 12px;\n"
"  width: 12px;\n"
"}\n"
"\n"
"QTabBar QToolButton:pressed, QDockWidget QTabBar QToolButton:pressed {\n"
"  background-color: #455364;\n"
"}\n"
"\n"
"QTabBar QToolButton:pressed:hover, QDockWidget QTabBar QToolButton:pressed:hover {\n"
"  border: 1px solid #346792;\n"
"}\n"
"\n"
"QTabBar QToolButton::left-arrow:enabled, QDockWidget QTabBar QToolButton::left-arrow:enabled {\n"
"  image: url(\":/qss_icons/dark/rc/arrow_left.png\");\n"
"}\n"
"\n"
"QTabBar QToolButton::left-arrow:disabled, QDockWidget QTabBar QToolButton::left-arrow:disabled {\n"
"  image: url(\":/qss_icons/dark/rc/arrow_left_disabled.png\");\n"
"}\n"
"\n"
"QTabBar QToolButton::right-arrow:enabled, QDockWidget QTabBar QToolButton::right-arrow:enabled {\n"
"  image: url(\":/qss_icons/dark/rc/arrow_right.png\");\n"
"}\n"
"\n"
"QTabBar QToolButton::right-arrow:disabled, QDockWidget QTabBar QToolButton::right-arrow:disabled {\n"
"  image: url(\":/qss_icons/dark/rc/arrow_right_disabled.png\");\n"
"}\n"
"\n"
"/* QDockWiget -------------------------------------------------------------\n"
"\n"
"--------------------------------------------------------------------------- */\n"
"QDockWidget {\n"
"  outline: 1px solid #455364;\n"
"  background-color: #19232D;\n"
"  border: 1px solid #455364;\n"
"  border-radius: 4px;\n"
"  titlebar-close-icon: url(\":/qss_icons/dark/rc/transparent.png\");\n"
"  titlebar-normal-icon: url(\":/qss_icons/dark/rc/transparent.png\");\n"
"}\n"
"\n"
"QDockWidget::title {\n"
"  /* Better size for title bar */\n"
"  padding: 3px;\n"
"  spacing: 4px;\n"
"  border: none;\n"
"  background-color: #455364;\n"
"}\n"
"\n"
"QDockWidget::close-button {\n"
"  icon-size: 12px;\n"
"  border: none;\n"
"  background: transparent;\n"
"  background-image: transparent;\n"
"  border: 0;\n"
"  margin: 0;\n"
"  padding: 0;\n"
"  image: url(\":/qss_icons/dark/rc/window_close.png\");\n"
"}\n"
"\n"
"QDockWidget::close-button:hover {\n"
"  image: url(\":/qss_icons/dark/rc/window_close_focus.png\");\n"
"}\n"
"\n"
"QDockWidget::close-button:pressed {\n"
"  image: url(\":/qss_icons/dark/rc/window_close_pressed.png\");\n"
"}\n"
"\n"
"QDockWidget::float-button {\n"
"  icon-size: 12px;\n"
"  border: none;\n"
"  background: transparent;\n"
"  background-image: transparent;\n"
"  border: 0;\n"
"  margin: 0;\n"
"  padding: 0;\n"
"  image: url(\":/qss_icons/dark/rc/window_undock.png\");\n"
"}\n"
"\n"
"QDockWidget::float-button:hover {\n"
"  image: url(\":/qss_icons/dark/rc/window_undock_focus.png\");\n"
"}\n"
"\n"
"QDockWidget::float-button:pressed {\n"
"  image: url(\":/qss_icons/dark/rc/window_undock_pressed.png\");\n"
"}\n"
"\n"
"/* QTreeView QListView QTableView -----------------------------------------\n"
"\n"
"https://doc.qt.io/qt-5/stylesheet-examples.html#customizing-qtreeview\n"
"https://doc.qt.io/qt-5/stylesheet-examples.html#customizing-qlistview\n"
"https://doc.qt.io/qt-5/stylesheet-examples.html#customizing-qtableview\n"
"\n"
"--------------------------------------------------------------------------- */\n"
"QTreeView:branch:selected, QTreeView:branch:hover {\n"
"  background: url(\":/qss_icons/dark/rc/transparent.png\");\n"
"}\n"
"\n"
"QTreeView:branch:has-siblings:!adjoins-item {\n"
"  border-image: url(\":/qss_icons/dark/rc/branch_line.png\") 0;\n"
"}\n"
"\n"
"QTreeView:branch:has-siblings:adjoins-item {\n"
"  border-image: url(\":/qss_icons/dark/rc/branch_more.png\") 0;\n"
"}\n"
"\n"
"QTreeView:branch:!has-children:!has-siblings:adjoins-item {\n"
"  border-image: url(\":/qss_icons/dark/rc/branch_end.png\") 0;\n"
"}\n"
"\n"
"QTreeView:branch:has-children:!has-siblings:closed, QTreeView:branch:closed:has-children:has-siblings {\n"
"  border-image: none;\n"
"  image: url(\":/qss_icons/dark/rc/branch_closed.png\");\n"
"}\n"
"\n"
"QTreeView:branch:open:has-children:!has-siblings, QTreeView:branch:open:has-children:has-siblings {\n"
"  border-image: none;\n"
"  image: url(\":/qss_icons/dark/rc/branch_open.png\");\n"
"}\n"
"\n"
"QTreeView:branch:has-children:!has-siblings:closed:hover, QTreeView:branch:closed:has-children:has-siblings:hover {\n"
"  image: url(\":/qss_icons/dark/rc/branch_closed_focus.png\");\n"
"}\n"
"\n"
"QTreeView:branch:open:has-children:!has-siblings:hover, QTreeView:branch:open:has-children:has-siblings:hover {\n"
"  image: url(\":/qss_icons/dark/rc/branch_open_focus.png\");\n"
"}\n"
"\n"
"QTreeView::indicator:checked,\n"
"QListView::indicator:checked,\n"
"QTableView::indicator:checked,\n"
"QColumnView::indicator:checked {\n"
"  image: url(\":/qss_icons/dark/rc/checkbox_checked.png\");\n"
"}\n"
"\n"
"QTreeView::indicator:checked:hover, QTreeView::indicator:checked:focus, QTreeView::indicator:checked:pressed,\n"
"QListView::indicator:checked:hover,\n"
"QListView::indicator:checked:focus,\n"
"QListView::indicator:checked:pressed,\n"
"QTableView::indicator:checked:hover,\n"
"QTableView::indicator:checked:focus,\n"
"QTableView::indicator:checked:pressed,\n"
"QColumnView::indicator:checked:hover,\n"
"QColumnView::indicator:checked:focus,\n"
"QColumnView::indicator:checked:pressed {\n"
"  image: url(\":/qss_icons/dark/rc/checkbox_checked_focus.png\");\n"
"}\n"
"\n"
"QTreeView::indicator:unchecked,\n"
"QListView::indicator:unchecked,\n"
"QTableView::indicator:unchecked,\n"
"QColumnView::indicator:unchecked {\n"
"  image: url(\":/qss_icons/dark/rc/checkbox_unchecked.png\");\n"
"}\n"
"\n"
"QTreeView::indicator:unchecked:hover, QTreeView::indicator:unchecked:focus, QTreeView::indicator:unchecked:pressed,\n"
"QListView::indicator:unchecked:hover,\n"
"QListView::indicator:unchecked:focus,\n"
"QListView::indicator:unchecked:pressed,\n"
"QTableView::indicator:unchecked:hover,\n"
"QTableView::indicator:unchecked:focus,\n"
"QTableView::indicator:unchecked:pressed,\n"
"QColumnView::indicator:unchecked:hover,\n"
"QColumnView::indicator:unchecked:focus,\n"
"QColumnView::indicator:unchecked:pressed {\n"
"  image: url(\":/qss_icons/dark/rc/checkbox_unchecked_focus.png\");\n"
"}\n"
"\n"
"QTreeView::indicator:indeterminate,\n"
"QListView::indicator:indeterminate,\n"
"QTableView::indicator:indeterminate,\n"
"QColumnView::indicator:indeterminate {\n"
"  image: url(\":/qss_icons/dark/rc/checkbox_indeterminate.png\");\n"
"}\n"
"\n"
"QTreeView::indicator:indeterminate:hover, QTreeView::indicator:indeterminate:focus, QTreeView::indicator:indeterminate:pressed,\n"
"QListView::indicator:indeterminate:hover,\n"
"QListView::indicator:indeterminate:focus,\n"
"QListView::indicator:indeterminate:pressed,\n"
"QTableView::indicator:indeterminate:hover,\n"
"QTableView::indicator:indeterminate:focus,\n"
"QTableView::indicator:indeterminate:pressed,\n"
"QColumnView::indicator:indeterminate:hover,\n"
"QColumnView::indicator:indeterminate:focus,\n"
"QColumnView::indicator:indeterminate:pressed {\n"
"  image: url(\":/qss_icons/dark/rc/checkbox_indeterminate_focus.png\");\n"
"}\n"
"\n"
"QTreeView,\n"
"QListView,\n"
"QTableView,\n"
"QColumnView {\n"
"  background-color: #19232D;\n"
"  border: 1px solid #455364;\n"
"  color: #E0E1E3;\n"
"  gridline-color: #455364;\n"
"  border-radius: 4px;\n"
"}\n"
"\n"
"QTreeView:disabled,\n"
"QListView:disabled,\n"
"QTableView:disabled,\n"
"QColumnView:disabled {\n"
"  background-color: #19232D;\n"
"  color: #9DA9B5;\n"
"}\n"
"\n"
"QTreeView:selected,\n"
"QListView:selected,\n"
"QTableView:selected,\n"
"QColumnView:selected {\n"
"  background-color: #346792;\n"
"  color: #455364;\n"
"}\n"
"\n"
"QTreeView:focus,\n"
"QListView:focus,\n"
"QTableView:focus,\n"
"QColumnView:focus {\n"
"  border: 1px solid #1A72BB;\n"
"}\n"
"\n"
"QTreeView::item:pressed,\n"
"QListView::item:pressed,\n"
"QTableView::item:pressed,\n"
"QColumnView::item:pressed {\n"
"  background-color: #346792;\n"
"}\n"
"\n"
"QTreeView::item:selected:active,\n"
"QListView::item:selected:active,\n"
"QTableView::item:selected:active,\n"
"QColumnView::item:selected:active {\n"
"  background-color: #346792;\n"
"}\n"
"\n"
"QTreeView::item:selected:!active,\n"
"QListView::item:selected:!active,\n"
"QTableView::item:selected:!active,\n"
"QColumnView::item:selected:!active {\n"
"  color: #E0E1E3;\n"
"  background-color: #37414F;\n"
"}\n"
"\n"
"QTreeView::item:!selected:hover,\n"
"QListView::item:!selected:hover,\n"
"QTableView::item:!selected:hover,\n"
"QColumnView::item:!selected:hover {\n"
"  outline: 0;\n"
"  color: #E0E1E3;\n"
"  background-color: #37414F;\n"
"}\n"
"\n"
"QTableCornerButton::section {\n"
"  background-color: #19232D;\n"
"  border: 1px transparent #455364;\n"
"  border-radius: 0px;\n"
"}\n"
"\n"
"/* QHeaderView ------------------------------------------------------------\n"
"\n"
"https://doc.qt.io/qt-5/stylesheet-examples.html#customizing-qheaderview\n"
"\n"
"--------------------------------------------------------------------------- */\n"
"QHeaderView {\n"
"  background-color: #455364;\n"
"  border: 0px transparent #455364;\n"
"  padding: 0;\n"
"  margin: 0;\n"
"  border-radius: 0;\n"
"}\n"
"\n"
"QHeaderView:disabled {\n"
"  background-color: #455364;\n"
"  border: 1px transparent #455364;\n"
"}\n"
"\n"
"QHeaderView::section {\n"
"  background-color: #455364;\n"
"  color: #E0E1E3;\n"
"  border-radius: 0;\n"
"  text-align: left;\n"
"  font-size: 13px;\n"
"}\n"
"\n"
"QHeaderView::section::horizontal {\n"
"  padding-top: 0;\n"
"  padding-bottom: 0;\n"
"  padding-left: 4px;\n"
"  padding-right: 4px;\n"
"  border-left: 1px solid #19232D;\n"
"}\n"
"\n"
"QHeaderView::section::horizontal::first, QHeaderView::section::horizontal::only-one {\n"
"  border-left: 1px solid #455364;\n"
"}\n"
"\n"
"QHeaderView::section::horizontal:disabled {\n"
"  color: #9DA9B5;\n"
"}\n"
"\n"
"QHeaderView::section::vertical {\n"
"  padding-top: 0;\n"
"  padding-bottom: 0;\n"
"  padding-left: 4px;\n"
"  padding-right: 4px;\n"
"  border-top: 1px solid #19232D;\n"
"}\n"
"\n"
"QHeaderView::section::vertical::first, QHeaderView::section::vertical::only-one {\n"
"  border-top: 1px solid #455364;\n"
"}\n"
"\n"
"QHeaderView::section::vertical:disabled {\n"
"  color: #9DA9B5;\n"
"}\n"
"\n"
"QHeaderView::down-arrow {\n"
"  /* Those settings (border/width/height/background-color) solve bug */\n"
"  /* transparent arrow background and size */\n"
"  background-color: #455364;\n"
"  border: none;\n"
"  height: 12px;\n"
"  width: 12px;\n"
"  padding-left: 2px;\n"
"  padding-right: 2px;\n"
"  image: url(\":/qss_icons/dark/rc/arrow_down.png\");\n"
"}\n"
"\n"
"QHeaderView::up-arrow {\n"
"  background-color: #455364;\n"
"  border: none;\n"
"  height: 12px;\n"
"  width: 12px;\n"
"  padding-left: 2px;\n"
"  padding-right: 2px;\n"
"  image: url(\":/qss_icons/dark/rc/arrow_up.png\");\n"
"}\n"
"\n"
"/* QToolBox --------------------------------------------------------------\n"
"\n"
"https://doc.qt.io/qt-5/stylesheet-examples.html#customizing-qtoolbox\n"
"\n"
"--------------------------------------------------------------------------- */\n"
"QToolBox {\n"
"  padding: 0px;\n"
"  border: 0px;\n"
"  border: 1px solid #455364;\n"
"}\n"
"\n"
"QToolBox:selected {\n"
"  padding: 0px;\n"
"  border: 2px solid #346792;\n"
"}\n"
"\n"
"QToolBox::tab {\n"
"  background-color: #19232D;\n"
"  border: 1px solid #455364;\n"
"  color: #E0E1E3;\n"
"  border-top-left-radius: 4px;\n"
"  border-top-right-radius: 4px;\n"
"}\n"
"\n"
"QToolBox::tab:disabled {\n"
"  color: #9DA9B5;\n"
"}\n"
"\n"
"QToolBox::tab:selected {\n"
"  background-color: #60798B;\n"
"  border-bottom: 2px solid #346792;\n"
"}\n"
"\n"
"QToolBox::tab:selected:disabled {\n"
"  background-color: #455364;\n"
"  border-bottom: 2px solid #26486B;\n"
"}\n"
"\n"
"QToolBox::tab:!selected {\n"
"  background-color: #455364;\n"
"  border-bottom: 2px solid #455364;\n"
"}\n"
"\n"
"QToolBox::tab:!selected:disabled {\n"
"  background-color: #19232D;\n"
"}\n"
"\n"
"QToolBox::tab:hover {\n"
"  border-color: #1A72BB;\n"
"  border-bottom: 2px solid #1A72BB;\n"
"}\n"
"\n"
"QToolBox QScrollArea QWidget QWidget {\n"
"  padding: 0px;\n"
"  border: 0px;\n"
"  background-color: #19232D;\n"
"}\n"
"\n"
"/* QFrame -----------------------------------------------------------------\n"
"\n"
"https://doc.qt.io/qt-5/stylesheet-examples.html#customizing-qframe\n"
"https://doc.qt.io/qt-5/qframe.html#-prop\n"
"https://doc.qt.io/qt-5/qframe.html#details\n"
"https://stackoverflow.com/questions/14581498/qt-stylesheet-for-hline-vline-color\n"
"\n"
"--------------------------------------------------------------------------- */\n"
"/* (dot) .QFrame  fix #141, #126, #123 */\n"
".QFrame {\n"
"  border-radius: 4px;\n"
"  border: 1px solid #455364;\n"
"  /* No frame */\n"
"  /* HLine */\n"
"  /* HLine */\n"
"}\n"
"\n"
".QFrame[frameShape=\"0\"] {\n"
"  border-radius: 4px;\n"
"  border: 1px transparent #455364;\n"
"}\n"
"\n"
".QFrame[frameShape=\"4\"] {\n"
"  max-height: 2px;\n"
"  border: none;\n"
"  background-color: #455364;\n"
"}\n"
"\n"
".QFrame[frameShape=\"5\"] {\n"
"  max-width: 2px;\n"
"  border: none;\n"
"  background-color: #455364;\n"
"}\n"
"\n"
"/* QSplitter --------------------------------------------------------------\n"
"\n"
"https://doc.qt.io/qt-5/stylesheet-examples.html#customizing-qsplitter\n"
"\n"
"--------------------------------------------------------------------------- */\n"
"QSplitter {\n"
"  background-color: #455364;\n"
"  spacing: 0px;\n"
"  padding: 0px;\n"
"  margin: 0px;\n"
"}\n"
"\n"
"QSplitter::handle {\n"
"  background-color: #455364;\n"
"  border: 0px solid #19232D;\n"
"  spacing: 0px;\n"
"  padding: 1px;\n"
"  margin: 0px;\n"
"}\n"
"\n"
"QSplitter::handle:hover {\n"
"  background-color: #9DA9B5;\n"
"}\n"
"\n"
"QSplitter::handle:horizontal {\n"
"  width: 5px;\n"
"  image: url(\":/qss_icons/dark/rc/line_vertical.png\");\n"
"}\n"
"\n"
"QSplitter::handle:vertical {\n"
"  height: 5px;\n"
"  image: url(\":/qss_icons/dark/rc/line_horizontal.png\");\n"
"}\n"
"\n"
"/* QDateEdit, QDateTimeEdit -----------------------------------------------\n"
"\n"
"--------------------------------------------------------------------------- */\n"
"QDateEdit, QDateTimeEdit {\n"
"  selection-background-color: #346792;\n"
"  border-style: solid;\n"
"  border: 1px solid #455364;\n"
"  border-radius: 4px;\n"
"  /* This fixes 103, 111 */\n"
"  padding-top: 2px;\n"
"  /* This fixes 103, 111 */\n"
"  padding-bottom: 2px;\n"
"  padding-left: 4px;\n"
"  padding-right: 4px;\n"
"  min-width: 10px;\n"
"}\n"
"\n"
"QDateEdit:on, QDateTimeEdit:on {\n"
"  selection-background-color: #346792;\n"
"}\n"
"\n"
"QDateEdit::drop-down, QDateTimeEdit::drop-down {\n"
"  subcontrol-origin: padding;\n"
"  subcontrol-position: top right;\n"
"  width: 12px;\n"
"  border-left: 1px solid #455364;\n"
"}\n"
"\n"
"QDateEdit::down-arrow, QDateTimeEdit::down-arrow {\n"
"  image: url(\":/qss_icons/dark/rc/arrow_down_disabled.png\");\n"
"  height: 8px;\n"
"  width: 8px;\n"
"}\n"
"\n"
"QDateEdit::down-arrow:on, QDateEdit::down-arrow:hover, QDateEdit::down-arrow:focus, QDateTimeEdit::down-arrow:on, QDateTimeEdit::down-arrow:hover, QDateTimeEdit::down-arrow:focus {\n"
"  image: url(\":/qss_icons/dark/rc/arrow_down.png\");\n"
"}\n"
"\n"
"QDateEdit QAbstractItemView, QDateTimeEdit QAbstractItemView {\n"
"  background-color: #19232D;\n"
"  border-radius: 4px;\n"
"  border: 1px solid #455364;\n"
"  selection-background-color: #346792;\n"
"}\n"
"\n"
"/* QAbstractView ----------------------------------------------------------\n"
"\n"
"--------------------------------------------------------------------------- */\n"
"QAbstractView:hover {\n"
"  border: 1px solid #346792;\n"
"  color: #E0E1E3;\n"
"}\n"
"\n"
"QAbstractView:selected {\n"
"  background: #346792;\n"
"  color: #455364;\n"
"}\n"
"\n"
"/* PlotWidget -------------------------------------------------------------\n"
"\n"
"--------------------------------------------------------------------------- */\n"
"PlotWidget {\n"
"  /* Fix cut labels in plots #134 */\n"
"  padding: 0px;\n"
"}")
        self.centralwidget = QtWidgets.QWidget(FaultyFabricWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setMinimumSize(QtCore.QSize(475, 450))
        self.groupBox_2.setObjectName("groupBox_2")
        self.text_Hata_Sinif_2 = QtWidgets.QLabel(self.groupBox_2)
        self.text_Hata_Sinif_2.setGeometry(QtCore.QRect(300, 390, 161, 37))
        self.text_Hata_Sinif_2.setText("")
        self.text_Hata_Sinif_2.setObjectName("text_Hata_Sinif_2")
        self.label_Hata_Alani_2 = QtWidgets.QLabel(self.groupBox_2)
        self.label_Hata_Alani_2.setGeometry(QtCore.QRect(20, 290, 261, 37))
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.label_Hata_Alani_2.setFont(font)
        self.label_Hata_Alani_2.setStyleSheet("color:white;")
        self.label_Hata_Alani_2.setObjectName("label_Hata_Alani_2")
        self.text_Hata_Alan_2 = QtWidgets.QLabel(self.groupBox_2)
        self.text_Hata_Alan_2.setGeometry(QtCore.QRect(300, 290, 161, 37))
        self.text_Hata_Alan_2.setText("")
        self.text_Hata_Alan_2.setObjectName("text_Hata_Alan_2")
        self.label_Hata_Eni_2 = QtWidgets.QLabel(self.groupBox_2)
        self.label_Hata_Eni_2.setGeometry(QtCore.QRect(20, 190, 261, 37))
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.label_Hata_Eni_2.setFont(font)
        self.label_Hata_Eni_2.setStyleSheet("color:white;")
        self.label_Hata_Eni_2.setObjectName("label_Hata_Eni_2")
        self.text_Hata_Eni_2 = QtWidgets.QLabel(self.groupBox_2)
        self.text_Hata_Eni_2.setGeometry(QtCore.QRect(300, 190, 161, 37))
        self.text_Hata_Eni_2.setText("")
        self.text_Hata_Eni_2.setObjectName("text_Hata_Eni_2")
        self.label_Hata_metre_2 = QtWidgets.QLabel(self.groupBox_2)
        self.label_Hata_metre_2.setGeometry(QtCore.QRect(20, 340, 261, 37))
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.label_Hata_metre_2.setFont(font)
        self.label_Hata_metre_2.setStyleSheet("color:white;")
        self.label_Hata_metre_2.setObjectName("label_Hata_metre_2")
        self.label_Hata_Sinifi_2 = QtWidgets.QLabel(self.groupBox_2)
        self.label_Hata_Sinifi_2.setGeometry(QtCore.QRect(20, 390, 261, 37))
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.label_Hata_Sinifi_2.setFont(font)
        self.label_Hata_Sinifi_2.setStyleSheet("color:white;")
        self.label_Hata_Sinifi_2.setObjectName("label_Hata_Sinifi_2")
        self.text_Hata_Boyu_2 = QtWidgets.QLabel(self.groupBox_2)
        self.text_Hata_Boyu_2.setGeometry(QtCore.QRect(300, 240, 161, 37))
        self.text_Hata_Boyu_2.setText("")
        self.text_Hata_Boyu_2.setObjectName("text_Hata_Boyu_2")
        self.Metre_Label_2 = QtWidgets.QLabel(self.groupBox_2)
        self.Metre_Label_2.setGeometry(QtCore.QRect(300, 340, 161, 37))
        self.Metre_Label_2.setText("")
        self.Metre_Label_2.setObjectName("Metre_Label_2")
        self.label_Hata_Boyu_2 = QtWidgets.QLabel(self.groupBox_2)
        self.label_Hata_Boyu_2.setGeometry(QtCore.QRect(20, 240, 261, 37))
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.label_Hata_Boyu_2.setFont(font)
        self.label_Hata_Boyu_2.setStyleSheet("color:white;")
        self.label_Hata_Boyu_2.setObjectName("label_Hata_Boyu_2")
        self.label_Hata_Goster_2 = QtWidgets.QLabel(self.groupBox_2)
        self.label_Hata_Goster_2.setGeometry(QtCore.QRect(88, 20, 300, 150))
        self.label_Hata_Goster_2.setStyleSheet("")
        self.label_Hata_Goster_2.setText("")
        self.label_Hata_Goster_2.setObjectName("label_Hata_Goster_2")
        self.gridLayout.addWidget(self.groupBox_2, 0, 1, 1, 1)
        self.groupBox_7 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_7.setTitle("")
        self.groupBox_7.setObjectName("groupBox_7")
        self.groupBox_8 = QtWidgets.QGroupBox(self.groupBox_7)
        self.groupBox_8.setGeometry(QtCore.QRect(40, 130, 361, 181))
        self.groupBox_8.setObjectName("groupBox_8")
        self.Ikaz_Durum = QtWidgets.QLabel(self.groupBox_8)
        self.Ikaz_Durum.setGeometry(QtCore.QRect(180, 40, 151, 41))
        self.Ikaz_Durum.setObjectName("Ikaz_Durum")
        self.Ikaz_label = QtWidgets.QLabel(self.groupBox_8)
        self.Ikaz_label.setGeometry(QtCore.QRect(20, 40, 141, 41))
        self.Ikaz_label.setObjectName("Ikaz_label")
        self.ikaz_button = QtWidgets.QPushButton(self.groupBox_8)
        self.ikaz_button.setGeometry(QtCore.QRect(20, 100, 311, 41))
        self.ikaz_button.setObjectName("ikaz_button")
        self.groupBox_9 = QtWidgets.QGroupBox(self.groupBox_7)
        self.groupBox_9.setGeometry(QtCore.QRect(40, 320, 361, 161))
        self.groupBox_9.setObjectName("groupBox_9")
        self.text_Metre_Durumu = QtWidgets.QLabel(self.groupBox_9)
        self.text_Metre_Durumu.setGeometry(QtCore.QRect(180, 90, 151, 41))
        self.text_Metre_Durumu.setObjectName("text_Metre_Durumu")
        self.label_Metre_Durumu = QtWidgets.QLabel(self.groupBox_9)
        self.label_Metre_Durumu.setGeometry(QtCore.QRect(20, 90, 151, 41))
        self.label_Metre_Durumu.setObjectName("label_Metre_Durumu")
        self.label_Dok_Hizi = QtWidgets.QLabel(self.groupBox_9)
        self.label_Dok_Hizi.setGeometry(QtCore.QRect(20, 30, 151, 41))
        self.label_Dok_Hizi.setObjectName("label_Dok_Hizi")
        self.text_Dok_Hizi = QtWidgets.QLabel(self.groupBox_9)
        self.text_Dok_Hizi.setGeometry(QtCore.QRect(180, 30, 151, 41))
        self.text_Dok_Hizi.setObjectName("text_Dok_Hizi")
        self.groupBox_10 = QtWidgets.QGroupBox(self.groupBox_7)
        self.groupBox_10.setGeometry(QtCore.QRect(40, 490, 361, 281))
        self.groupBox_10.setObjectName("groupBox_10")
        self.label_Detect_Delik = QtWidgets.QLabel(self.groupBox_10)
        self.label_Detect_Delik.setGeometry(QtCore.QRect(20, 30, 151, 41))
        self.label_Detect_Delik.setObjectName("label_Detect_Delik")
        self.text_Detect_Delik = QtWidgets.QLabel(self.groupBox_10)
        self.text_Detect_Delik.setGeometry(QtCore.QRect(180, 30, 151, 41))
        self.text_Detect_Delik.setObjectName("text_Detect_Delik")
        self.label_Detect_Leke = QtWidgets.QLabel(self.groupBox_10)
        self.label_Detect_Leke.setGeometry(QtCore.QRect(20, 90, 151, 41))
        self.label_Detect_Leke.setObjectName("label_Detect_Leke")
        self.text_Detect_Leke = QtWidgets.QLabel(self.groupBox_10)
        self.text_Detect_Leke.setGeometry(QtCore.QRect(180, 90, 151, 41))
        self.text_Detect_Leke.setObjectName("text_Detect_Leke")
        self.label_Detect_kirik = QtWidgets.QLabel(self.groupBox_10)
        self.label_Detect_kirik.setGeometry(QtCore.QRect(20, 150, 151, 41))
        self.label_Detect_kirik.setObjectName("label_Detect_kirik")
        self.text_Detect_Kirik = QtWidgets.QLabel(self.groupBox_10)
        self.text_Detect_Kirik.setGeometry(QtCore.QRect(180, 150, 151, 41))
        self.text_Detect_Kirik.setObjectName("text_Detect_Kirik")
        self.label_Detect_Diger = QtWidgets.QLabel(self.groupBox_10)
        self.label_Detect_Diger.setGeometry(QtCore.QRect(20, 210, 151, 41))
        self.label_Detect_Diger.setObjectName("label_Detect_Diger")
        self.text_Detect_Diger = QtWidgets.QLabel(self.groupBox_10)
        self.text_Detect_Diger.setGeometry(QtCore.QRect(180, 210, 151, 41))
        self.text_Detect_Diger.setObjectName("text_Detect_Diger")
        self.groupBox_11 = QtWidgets.QGroupBox(self.groupBox_7)
        self.groupBox_11.setGeometry(QtCore.QRect(40, 20, 361, 101))
        self.groupBox_11.setObjectName("groupBox_11")
        self.system_close = QtWidgets.QPushButton(self.groupBox_11)
        self.system_close.setGeometry(QtCore.QRect(183, 30, 161, 41))
        self.system_close.setObjectName("system_close")
        self.label = QtWidgets.QLabel(self.groupBox_11)
        self.label.setGeometry(QtCore.QRect(20, 30, 141, 41))
        self.label.setObjectName("label")
        self.left_pushButton = QtWidgets.QPushButton(self.groupBox_7)
        self.left_pushButton.setGeometry(QtCore.QRect(100, 790, 64, 64))
        self.left_pushButton.setText("")
        self.left_pushButton.setObjectName("left_pushButton")
        self.home_pushButton = QtWidgets.QPushButton(self.groupBox_7)
        self.home_pushButton.setGeometry(QtCore.QRect(186, 790, 64, 64))
        self.home_pushButton.setText("")
        self.home_pushButton.setObjectName("home_pushButton")
        self.righr_pushButton = QtWidgets.QPushButton(self.groupBox_7)
        self.righr_pushButton.setGeometry(QtCore.QRect(270, 790, 64, 64))
        self.righr_pushButton.setText("")
        self.righr_pushButton.setObjectName("righr_pushButton")
        self.gridLayout.addWidget(self.groupBox_7, 0, 4, 2, 1)
        self.groupBox_4 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_4.setMinimumSize(QtCore.QSize(475, 450))
        self.groupBox_4.setObjectName("groupBox_4")
        self.text_Hata_Sinif_4 = QtWidgets.QLabel(self.groupBox_4)
        self.text_Hata_Sinif_4.setGeometry(QtCore.QRect(300, 390, 161, 37))
        self.text_Hata_Sinif_4.setText("")
        self.text_Hata_Sinif_4.setObjectName("text_Hata_Sinif_4")
        self.label_Hata_Alani_4 = QtWidgets.QLabel(self.groupBox_4)
        self.label_Hata_Alani_4.setGeometry(QtCore.QRect(20, 290, 261, 37))
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.label_Hata_Alani_4.setFont(font)
        self.label_Hata_Alani_4.setStyleSheet("color:white;")
        self.label_Hata_Alani_4.setObjectName("label_Hata_Alani_4")
        self.text_Hata_Alan_4 = QtWidgets.QLabel(self.groupBox_4)
        self.text_Hata_Alan_4.setGeometry(QtCore.QRect(300, 290, 161, 37))
        self.text_Hata_Alan_4.setText("")
        self.text_Hata_Alan_4.setObjectName("text_Hata_Alan_4")
        self.label_Hata_Eni_4 = QtWidgets.QLabel(self.groupBox_4)
        self.label_Hata_Eni_4.setGeometry(QtCore.QRect(20, 190, 261, 37))
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.label_Hata_Eni_4.setFont(font)
        self.label_Hata_Eni_4.setStyleSheet("color:white;")
        self.label_Hata_Eni_4.setObjectName("label_Hata_Eni_4")
        self.text_Hata_Eni_4 = QtWidgets.QLabel(self.groupBox_4)
        self.text_Hata_Eni_4.setGeometry(QtCore.QRect(300, 190, 161, 37))
        self.text_Hata_Eni_4.setText("")
        self.text_Hata_Eni_4.setObjectName("text_Hata_Eni_4")
        self.label_Hata_metre_4 = QtWidgets.QLabel(self.groupBox_4)
        self.label_Hata_metre_4.setGeometry(QtCore.QRect(20, 340, 261, 37))
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.label_Hata_metre_4.setFont(font)
        self.label_Hata_metre_4.setStyleSheet("color:white;")
        self.label_Hata_metre_4.setObjectName("label_Hata_metre_4")
        self.label_Hata_Sinifi_4 = QtWidgets.QLabel(self.groupBox_4)
        self.label_Hata_Sinifi_4.setGeometry(QtCore.QRect(20, 390, 261, 37))
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.label_Hata_Sinifi_4.setFont(font)
        self.label_Hata_Sinifi_4.setStyleSheet("color:white;")
        self.label_Hata_Sinifi_4.setObjectName("label_Hata_Sinifi_4")
        self.text_Hata_Boyu_4 = QtWidgets.QLabel(self.groupBox_4)
        self.text_Hata_Boyu_4.setGeometry(QtCore.QRect(300, 240, 161, 37))
        self.text_Hata_Boyu_4.setText("")
        self.text_Hata_Boyu_4.setObjectName("text_Hata_Boyu_4")
        self.Metre_Label_4 = QtWidgets.QLabel(self.groupBox_4)
        self.Metre_Label_4.setGeometry(QtCore.QRect(300, 340, 161, 37))
        self.Metre_Label_4.setText("")
        self.Metre_Label_4.setObjectName("Metre_Label_4")
        self.label_Hata_Boyu_4 = QtWidgets.QLabel(self.groupBox_4)
        self.label_Hata_Boyu_4.setGeometry(QtCore.QRect(20, 240, 261, 37))
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.label_Hata_Boyu_4.setFont(font)
        self.label_Hata_Boyu_4.setStyleSheet("color:white;")
        self.label_Hata_Boyu_4.setObjectName("label_Hata_Boyu_4")
        self.label_Hata_Goster_4 = QtWidgets.QLabel(self.groupBox_4)
        self.label_Hata_Goster_4.setGeometry(QtCore.QRect(88, 20, 300, 150))
        self.label_Hata_Goster_4.setStyleSheet("")
        self.label_Hata_Goster_4.setText("")
        self.label_Hata_Goster_4.setObjectName("label_Hata_Goster_4")
        self.gridLayout.addWidget(self.groupBox_4, 1, 0, 1, 1)
        self.groupBox_3 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_3.setMinimumSize(QtCore.QSize(475, 450))
        self.groupBox_3.setObjectName("groupBox_3")
        self.text_Hata_Sinif_3 = QtWidgets.QLabel(self.groupBox_3)
        self.text_Hata_Sinif_3.setGeometry(QtCore.QRect(300, 390, 161, 37))
        self.text_Hata_Sinif_3.setText("")
        self.text_Hata_Sinif_3.setObjectName("text_Hata_Sinif_3")
        self.label_Hata_Alani_3 = QtWidgets.QLabel(self.groupBox_3)
        self.label_Hata_Alani_3.setGeometry(QtCore.QRect(20, 290, 261, 37))
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.label_Hata_Alani_3.setFont(font)
        self.label_Hata_Alani_3.setStyleSheet("color:white;")
        self.label_Hata_Alani_3.setObjectName("label_Hata_Alani_3")
        self.text_Hata_Alan_3 = QtWidgets.QLabel(self.groupBox_3)
        self.text_Hata_Alan_3.setGeometry(QtCore.QRect(300, 290, 161, 37))
        self.text_Hata_Alan_3.setText("")
        self.text_Hata_Alan_3.setObjectName("text_Hata_Alan_3")
        self.label_Hata_Eni_3 = QtWidgets.QLabel(self.groupBox_3)
        self.label_Hata_Eni_3.setGeometry(QtCore.QRect(20, 190, 261, 37))
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.label_Hata_Eni_3.setFont(font)
        self.label_Hata_Eni_3.setStyleSheet("color:white;")
        self.label_Hata_Eni_3.setObjectName("label_Hata_Eni_3")
        self.text_Hata_Eni_3 = QtWidgets.QLabel(self.groupBox_3)
        self.text_Hata_Eni_3.setGeometry(QtCore.QRect(300, 190, 161, 37))
        self.text_Hata_Eni_3.setText("")
        self.text_Hata_Eni_3.setObjectName("text_Hata_Eni_3")
        self.label_Hata_metre_3 = QtWidgets.QLabel(self.groupBox_3)
        self.label_Hata_metre_3.setGeometry(QtCore.QRect(20, 340, 261, 37))
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.label_Hata_metre_3.setFont(font)
        self.label_Hata_metre_3.setStyleSheet("color:white;")
        self.label_Hata_metre_3.setObjectName("label_Hata_metre_3")
        self.label_Hata_Sinifi_3 = QtWidgets.QLabel(self.groupBox_3)
        self.label_Hata_Sinifi_3.setGeometry(QtCore.QRect(20, 390, 261, 37))
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.label_Hata_Sinifi_3.setFont(font)
        self.label_Hata_Sinifi_3.setStyleSheet("color:white;")
        self.label_Hata_Sinifi_3.setObjectName("label_Hata_Sinifi_3")
        self.text_Hata_Boyu_3 = QtWidgets.QLabel(self.groupBox_3)
        self.text_Hata_Boyu_3.setGeometry(QtCore.QRect(300, 240, 161, 37))
        self.text_Hata_Boyu_3.setText("")
        self.text_Hata_Boyu_3.setObjectName("text_Hata_Boyu_3")
        self.Metre_Label_3 = QtWidgets.QLabel(self.groupBox_3)
        self.Metre_Label_3.setGeometry(QtCore.QRect(300, 340, 161, 37))
        self.Metre_Label_3.setText("")
        self.Metre_Label_3.setObjectName("Metre_Label_3")
        self.label_Hata_Boyu_3 = QtWidgets.QLabel(self.groupBox_3)
        self.label_Hata_Boyu_3.setGeometry(QtCore.QRect(20, 240, 261, 37))
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.label_Hata_Boyu_3.setFont(font)
        self.label_Hata_Boyu_3.setStyleSheet("color:white;")
        self.label_Hata_Boyu_3.setObjectName("label_Hata_Boyu_3")
        self.label_Hata_Goster_3 = QtWidgets.QLabel(self.groupBox_3)
        self.label_Hata_Goster_3.setGeometry(QtCore.QRect(88, 20, 300, 150))
        self.label_Hata_Goster_3.setStyleSheet("")
        self.label_Hata_Goster_3.setText("")
        self.label_Hata_Goster_3.setObjectName("label_Hata_Goster_3")
        self.gridLayout.addWidget(self.groupBox_3, 0, 2, 1, 1)
        self.groupBox_6 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_6.setMinimumSize(QtCore.QSize(475, 450))
        self.groupBox_6.setObjectName("groupBox_6")
        self.text_Hata_Sinif_6 = QtWidgets.QLabel(self.groupBox_6)
        self.text_Hata_Sinif_6.setGeometry(QtCore.QRect(300, 390, 161, 37))
        self.text_Hata_Sinif_6.setText("")
        self.text_Hata_Sinif_6.setObjectName("text_Hata_Sinif_6")
        self.label_Hata_Alani_6 = QtWidgets.QLabel(self.groupBox_6)
        self.label_Hata_Alani_6.setGeometry(QtCore.QRect(20, 290, 261, 37))
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.label_Hata_Alani_6.setFont(font)
        self.label_Hata_Alani_6.setStyleSheet("color:white;")
        self.label_Hata_Alani_6.setObjectName("label_Hata_Alani_6")
        self.text_Hata_Alan_6 = QtWidgets.QLabel(self.groupBox_6)
        self.text_Hata_Alan_6.setGeometry(QtCore.QRect(300, 290, 161, 37))
        self.text_Hata_Alan_6.setText("")
        self.text_Hata_Alan_6.setObjectName("text_Hata_Alan_6")
        self.label_Hata_Eni_6 = QtWidgets.QLabel(self.groupBox_6)
        self.label_Hata_Eni_6.setGeometry(QtCore.QRect(20, 190, 261, 37))
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.label_Hata_Eni_6.setFont(font)
        self.label_Hata_Eni_6.setStyleSheet("color:white;")
        self.label_Hata_Eni_6.setObjectName("label_Hata_Eni_6")
        self.text_Hata_Eni_6 = QtWidgets.QLabel(self.groupBox_6)
        self.text_Hata_Eni_6.setGeometry(QtCore.QRect(300, 190, 161, 37))
        self.text_Hata_Eni_6.setText("")
        self.text_Hata_Eni_6.setObjectName("text_Hata_Eni_6")
        self.label_Hata_metre_6 = QtWidgets.QLabel(self.groupBox_6)
        self.label_Hata_metre_6.setGeometry(QtCore.QRect(20, 340, 261, 37))
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.label_Hata_metre_6.setFont(font)
        self.label_Hata_metre_6.setStyleSheet("color:white;")
        self.label_Hata_metre_6.setObjectName("label_Hata_metre_6")
        self.label_Hata_Sinifi_6 = QtWidgets.QLabel(self.groupBox_6)
        self.label_Hata_Sinifi_6.setGeometry(QtCore.QRect(20, 390, 261, 37))
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.label_Hata_Sinifi_6.setFont(font)
        self.label_Hata_Sinifi_6.setStyleSheet("color:white;")
        self.label_Hata_Sinifi_6.setObjectName("label_Hata_Sinifi_6")
        self.text_Hata_Boyu_6 = QtWidgets.QLabel(self.groupBox_6)
        self.text_Hata_Boyu_6.setGeometry(QtCore.QRect(300, 240, 161, 37))
        self.text_Hata_Boyu_6.setText("")
        self.text_Hata_Boyu_6.setObjectName("text_Hata_Boyu_6")
        self.Metre_Label_6 = QtWidgets.QLabel(self.groupBox_6)
        self.Metre_Label_6.setGeometry(QtCore.QRect(300, 340, 161, 37))
        self.Metre_Label_6.setText("")
        self.Metre_Label_6.setObjectName("Metre_Label_6")
        self.label_Hata_Boyu_6 = QtWidgets.QLabel(self.groupBox_6)
        self.label_Hata_Boyu_6.setGeometry(QtCore.QRect(20, 240, 261, 37))
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.label_Hata_Boyu_6.setFont(font)
        self.label_Hata_Boyu_6.setStyleSheet("color:white;")
        self.label_Hata_Boyu_6.setObjectName("label_Hata_Boyu_6")
        self.label_Hata_Goster_6 = QtWidgets.QLabel(self.groupBox_6)
        self.label_Hata_Goster_6.setGeometry(QtCore.QRect(88, 20, 300, 150))
        self.label_Hata_Goster_6.setStyleSheet("")
        self.label_Hata_Goster_6.setText("")
        self.label_Hata_Goster_6.setObjectName("label_Hata_Goster_6")
        self.gridLayout.addWidget(self.groupBox_6, 1, 2, 1, 1)
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setMinimumSize(QtCore.QSize(475, 450))
        self.groupBox.setObjectName("groupBox")
        self.text_Hata_Sinif_1 = QtWidgets.QLabel(self.groupBox)
        self.text_Hata_Sinif_1.setGeometry(QtCore.QRect(300, 390, 161, 37))
        self.text_Hata_Sinif_1.setText("")
        self.text_Hata_Sinif_1.setObjectName("text_Hata_Sinif_1")
        self.label_Hata_Alani_1 = QtWidgets.QLabel(self.groupBox)
        self.label_Hata_Alani_1.setGeometry(QtCore.QRect(20, 290, 261, 37))
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.label_Hata_Alani_1.setFont(font)
        self.label_Hata_Alani_1.setStyleSheet("color:white;")
        self.label_Hata_Alani_1.setObjectName("label_Hata_Alani_1")
        self.text_Hata_Alan_1 = QtWidgets.QLabel(self.groupBox)
        self.text_Hata_Alan_1.setGeometry(QtCore.QRect(300, 290, 161, 37))
        self.text_Hata_Alan_1.setText("")
        self.text_Hata_Alan_1.setObjectName("text_Hata_Alan_1")
        self.label_Hata_Eni_1 = QtWidgets.QLabel(self.groupBox)
        self.label_Hata_Eni_1.setGeometry(QtCore.QRect(20, 190, 261, 37))
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.label_Hata_Eni_1.setFont(font)
        self.label_Hata_Eni_1.setStyleSheet("color:white;")
        self.label_Hata_Eni_1.setObjectName("label_Hata_Eni_1")
        self.text_Hata_Eni_1 = QtWidgets.QLabel(self.groupBox)
        self.text_Hata_Eni_1.setGeometry(QtCore.QRect(300, 190, 161, 37))
        self.text_Hata_Eni_1.setText("")
        self.text_Hata_Eni_1.setObjectName("text_Hata_Eni_1")
        self.label_Hata_metre_1 = QtWidgets.QLabel(self.groupBox)
        self.label_Hata_metre_1.setGeometry(QtCore.QRect(20, 340, 261, 37))
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.label_Hata_metre_1.setFont(font)
        self.label_Hata_metre_1.setStyleSheet("color:white;")
        self.label_Hata_metre_1.setObjectName("label_Hata_metre_1")
        self.label_Hata_Sinifi_1 = QtWidgets.QLabel(self.groupBox)
        self.label_Hata_Sinifi_1.setGeometry(QtCore.QRect(20, 390, 261, 37))
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.label_Hata_Sinifi_1.setFont(font)
        self.label_Hata_Sinifi_1.setStyleSheet("color:white;")
        self.label_Hata_Sinifi_1.setObjectName("label_Hata_Sinifi_1")
        self.text_Hata_Boyu_1 = QtWidgets.QLabel(self.groupBox)
        self.text_Hata_Boyu_1.setGeometry(QtCore.QRect(300, 240, 161, 37))
        self.text_Hata_Boyu_1.setText("")
        self.text_Hata_Boyu_1.setObjectName("text_Hata_Boyu_1")
        self.Metre_Label_1 = QtWidgets.QLabel(self.groupBox)
        self.Metre_Label_1.setGeometry(QtCore.QRect(300, 340, 161, 37))
        self.Metre_Label_1.setText("")
        self.Metre_Label_1.setObjectName("Metre_Label_1")
        self.label_Hata_Boyu_1 = QtWidgets.QLabel(self.groupBox)
        self.label_Hata_Boyu_1.setGeometry(QtCore.QRect(20, 240, 261, 37))
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.label_Hata_Boyu_1.setFont(font)
        self.label_Hata_Boyu_1.setStyleSheet("color:white;")
        self.label_Hata_Boyu_1.setObjectName("label_Hata_Boyu_1")
        self.label_Hata_Goster_1 = QtWidgets.QLabel(self.groupBox)
        self.label_Hata_Goster_1.setGeometry(QtCore.QRect(88, 20, 300, 150))
        self.label_Hata_Goster_1.setStyleSheet("")
        self.label_Hata_Goster_1.setText("")
        self.label_Hata_Goster_1.setObjectName("label_Hata_Goster_1")
        self.gridLayout.addWidget(self.groupBox, 0, 0, 1, 1)
        self.groupBox_5 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_5.setMinimumSize(QtCore.QSize(475, 450))
        self.groupBox_5.setObjectName("groupBox_5")
        self.text_Hata_Sinif_5 = QtWidgets.QLabel(self.groupBox_5)
        self.text_Hata_Sinif_5.setGeometry(QtCore.QRect(300, 390, 161, 37))
        self.text_Hata_Sinif_5.setText("")
        self.text_Hata_Sinif_5.setObjectName("text_Hata_Sinif_5")
        self.label_Hata_Alani_5 = QtWidgets.QLabel(self.groupBox_5)
        self.label_Hata_Alani_5.setGeometry(QtCore.QRect(20, 290, 261, 37))
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.label_Hata_Alani_5.setFont(font)
        self.label_Hata_Alani_5.setStyleSheet("color:white;")
        self.label_Hata_Alani_5.setObjectName("label_Hata_Alani_5")
        self.text_Hata_Alan_5 = QtWidgets.QLabel(self.groupBox_5)
        self.text_Hata_Alan_5.setGeometry(QtCore.QRect(300, 290, 161, 37))
        self.text_Hata_Alan_5.setText("")
        self.text_Hata_Alan_5.setObjectName("text_Hata_Alan_5")
        self.label_Hata_Eni_5 = QtWidgets.QLabel(self.groupBox_5)
        self.label_Hata_Eni_5.setGeometry(QtCore.QRect(20, 190, 261, 37))
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.label_Hata_Eni_5.setFont(font)
        self.label_Hata_Eni_5.setStyleSheet("color:white;")
        self.label_Hata_Eni_5.setObjectName("label_Hata_Eni_5")
        self.text_Hata_Eni_5 = QtWidgets.QLabel(self.groupBox_5)
        self.text_Hata_Eni_5.setGeometry(QtCore.QRect(300, 190, 161, 37))
        self.text_Hata_Eni_5.setText("")
        self.text_Hata_Eni_5.setObjectName("text_Hata_Eni_5")
        self.label_Hata_metre_5 = QtWidgets.QLabel(self.groupBox_5)
        self.label_Hata_metre_5.setGeometry(QtCore.QRect(20, 340, 261, 37))
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.label_Hata_metre_5.setFont(font)
        self.label_Hata_metre_5.setStyleSheet("color:white;")
        self.label_Hata_metre_5.setObjectName("label_Hata_metre_5")
        self.label_Hata_Sinifi_5 = QtWidgets.QLabel(self.groupBox_5)
        self.label_Hata_Sinifi_5.setGeometry(QtCore.QRect(20, 390, 261, 37))
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.label_Hata_Sinifi_5.setFont(font)
        self.label_Hata_Sinifi_5.setStyleSheet("color:white;")
        self.label_Hata_Sinifi_5.setObjectName("label_Hata_Sinifi_5")
        self.text_Hata_Boyu_5 = QtWidgets.QLabel(self.groupBox_5)
        self.text_Hata_Boyu_5.setGeometry(QtCore.QRect(300, 240, 161, 37))
        self.text_Hata_Boyu_5.setText("")
        self.text_Hata_Boyu_5.setObjectName("text_Hata_Boyu_5")
        self.Metre_Label_5 = QtWidgets.QLabel(self.groupBox_5)
        self.Metre_Label_5.setGeometry(QtCore.QRect(300, 340, 161, 37))
        self.Metre_Label_5.setText("")
        self.Metre_Label_5.setObjectName("Metre_Label_5")
        self.label_Hata_Boyu_5 = QtWidgets.QLabel(self.groupBox_5)
        self.label_Hata_Boyu_5.setGeometry(QtCore.QRect(20, 240, 261, 37))
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.label_Hata_Boyu_5.setFont(font)
        self.label_Hata_Boyu_5.setStyleSheet("color:white;")
        self.label_Hata_Boyu_5.setObjectName("label_Hata_Boyu_5")
        self.label_Hata_Goster_5 = QtWidgets.QLabel(self.groupBox_5)
        self.label_Hata_Goster_5.setGeometry(QtCore.QRect(88, 20, 300, 150))
        self.label_Hata_Goster_5.setStyleSheet("")
        self.label_Hata_Goster_5.setText("")
        self.label_Hata_Goster_5.setObjectName("label_Hata_Goster_5")
        self.gridLayout.addWidget(self.groupBox_5, 1, 1, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 0, 3, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 0, 5, 1, 1)
        FaultyFabricWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(FaultyFabricWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1964, 43))
        self.menubar.setObjectName("menubar")
        self.menuCamera = QtWidgets.QMenu(self.menubar)
        self.menuCamera.setTitle("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Icon/MainWindow/mmm.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.menuCamera.setIcon(icon)
        self.menuCamera.setObjectName("menuCamera")
        self.menuKameralar = QtWidgets.QMenu(self.menubar)
        self.menuKameralar.setObjectName("menuKameralar")
        self.menuVeri_Taban = QtWidgets.QMenu(self.menubar)
        self.menuVeri_Taban.setObjectName("menuVeri_Taban")
        self.menuAdmin_Paneli = QtWidgets.QMenu(self.menubar)
        self.menuAdmin_Paneli.setObjectName("menuAdmin_Paneli")
        self.menuHakk_nda = QtWidgets.QMenu(self.menubar)
        self.menuHakk_nda.setObjectName("menuHakk_nda")
        FaultyFabricWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(FaultyFabricWindow)
        self.statusbar.setObjectName("statusbar")
        FaultyFabricWindow.setStatusBar(self.statusbar)
        self.actioncikis = QtWidgets.QAction(FaultyFabricWindow)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("Icon/MainWindow/close.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actioncikis.setIcon(icon1)
        self.actioncikis.setObjectName("actioncikis")
        self.actionKameralar = QtWidgets.QAction(FaultyFabricWindow)
        self.actionKameralar.setObjectName("actionKameralar")
        self.actionVeri_Taban = QtWidgets.QAction(FaultyFabricWindow)
        self.actionVeri_Taban.setObjectName("actionVeri_Taban")
        self.actionAdmin_Paneli = QtWidgets.QAction(FaultyFabricWindow)
        self.actionAdmin_Paneli.setObjectName("actionAdmin_Paneli")
        self.actionHakk_nda = QtWidgets.QAction(FaultyFabricWindow)
        self.actionHakk_nda.setObjectName("actionHakk_nda")
        self.menuCamera.addAction(self.actioncikis)
        self.menuKameralar.addAction(self.actionKameralar)
        self.menuVeri_Taban.addAction(self.actionVeri_Taban)
        self.menuAdmin_Paneli.addAction(self.actionAdmin_Paneli)
        self.menuHakk_nda.addAction(self.actionHakk_nda)
        self.menubar.addAction(self.menuCamera.menuAction())
        self.menubar.addAction(self.menuKameralar.menuAction())
        self.menubar.addAction(self.menuVeri_Taban.menuAction())
        self.menubar.addAction(self.menuAdmin_Paneli.menuAction())
        self.menubar.addAction(self.menuHakk_nda.menuAction())

        self.retranslateUi(FaultyFabricWindow)
        QtCore.QMetaObject.connectSlotsByName(FaultyFabricWindow)

    def retranslateUi(self, FaultyFabricWindow):
        _translate = QtCore.QCoreApplication.translate
        FaultyFabricWindow.setWindowTitle(_translate("FaultyFabricWindow", "Hatalı_Kumaşlar"))
        self.groupBox_2.setTitle(_translate("FaultyFabricWindow", "Hata 2"))
        self.label_Hata_Alani_2.setText(_translate("FaultyFabricWindow", "Hata Alanı(mm2) :"))
        self.label_Hata_Eni_2.setText(_translate("FaultyFabricWindow", "Hata Eni(mm) :"))
        self.label_Hata_metre_2.setText(_translate("FaultyFabricWindow", "Hatanın Geldiği Metre(m) :"))
        self.label_Hata_Sinifi_2.setText(_translate("FaultyFabricWindow", "Hatanın Sınıfı :"))
        self.label_Hata_Boyu_2.setText(_translate("FaultyFabricWindow", "Hata Boyu(mm) :"))
        self.groupBox_8.setTitle(_translate("FaultyFabricWindow", "İkaz Durumu"))
        self.Ikaz_Durum.setText(_translate("FaultyFabricWindow", "KAPALI"))
        self.Ikaz_label.setText(_translate("FaultyFabricWindow", "İkaz Durumu"))
        self.ikaz_button.setText(_translate("FaultyFabricWindow", "ALARMI KAPAT"))
        self.groupBox_9.setTitle(_translate("FaultyFabricWindow", "Sayaç Durumu"))
        self.text_Metre_Durumu.setText(_translate("FaultyFabricWindow", "0"))
        self.label_Metre_Durumu.setText(_translate("FaultyFabricWindow", "Metre Durumu"))
        self.label_Dok_Hizi.setText(_translate("FaultyFabricWindow", "Makine Hızı"))
        self.text_Dok_Hizi.setText(_translate("FaultyFabricWindow", "0"))
        self.groupBox_10.setTitle(_translate("FaultyFabricWindow", "Hata Durumu"))
        self.label_Detect_Delik.setText(_translate("FaultyFabricWindow", "Hatalı Delik"))
        self.text_Detect_Delik.setText(_translate("FaultyFabricWindow", "0"))
        self.label_Detect_Leke.setText(_translate("FaultyFabricWindow", "Hatalı Leke"))
        self.text_Detect_Leke.setText(_translate("FaultyFabricWindow", "0"))
        self.label_Detect_kirik.setText(_translate("FaultyFabricWindow", "Hatalı Kırık"))
        self.text_Detect_Kirik.setText(_translate("FaultyFabricWindow", "0"))
        self.label_Detect_Diger.setText(_translate("FaultyFabricWindow", "Diğer Hatalar"))
        self.text_Detect_Diger.setText(_translate("FaultyFabricWindow", "0"))
        self.groupBox_11.setTitle(_translate("FaultyFabricWindow", "Sistem Durumu"))
        self.system_close.setText(_translate("FaultyFabricWindow", "DURDUR"))
        self.label.setText(_translate("FaultyFabricWindow", "Hedefleme"))
        self.groupBox_4.setTitle(_translate("FaultyFabricWindow", "Hata 4"))
        self.label_Hata_Alani_4.setText(_translate("FaultyFabricWindow", "Hata Alanı(mm2) :"))
        self.label_Hata_Eni_4.setText(_translate("FaultyFabricWindow", "Hata Eni(mm) :"))
        self.label_Hata_metre_4.setText(_translate("FaultyFabricWindow", "Hatanın Geldiği Metre(m) :"))
        self.label_Hata_Sinifi_4.setText(_translate("FaultyFabricWindow", "Hatanın Sınıfı :"))
        self.label_Hata_Boyu_4.setText(_translate("FaultyFabricWindow", "Hata Boyu(mm) :"))
        self.groupBox_3.setTitle(_translate("FaultyFabricWindow", "Hata 3"))
        self.label_Hata_Alani_3.setText(_translate("FaultyFabricWindow", "Hata Alanı(mm2) :"))
        self.label_Hata_Eni_3.setText(_translate("FaultyFabricWindow", "Hata Eni(mm) :"))
        self.label_Hata_metre_3.setText(_translate("FaultyFabricWindow", "Hatanın Geldiği Metre(m) :"))
        self.label_Hata_Sinifi_3.setText(_translate("FaultyFabricWindow", "Hatanın Sınıfı :"))
        self.label_Hata_Boyu_3.setText(_translate("FaultyFabricWindow", "Hata Boyu(mm) :"))
        self.groupBox_6.setTitle(_translate("FaultyFabricWindow", "Hata 6"))
        self.label_Hata_Alani_6.setText(_translate("FaultyFabricWindow", "Hata Alanı(mm2) :"))
        self.label_Hata_Eni_6.setText(_translate("FaultyFabricWindow", "Hata Eni(mm) :"))
        self.label_Hata_metre_6.setText(_translate("FaultyFabricWindow", "Hatanın Geldiği Metre(m) :"))
        self.label_Hata_Sinifi_6.setText(_translate("FaultyFabricWindow", "Hatanın Sınıfı :"))
        self.label_Hata_Boyu_6.setText(_translate("FaultyFabricWindow", "Hata Boyu(mm) :"))
        self.groupBox.setTitle(_translate("FaultyFabricWindow", "Hata 1"))
        self.label_Hata_Alani_1.setText(_translate("FaultyFabricWindow", "Hata Alanı(mm2) :"))
        self.label_Hata_Eni_1.setText(_translate("FaultyFabricWindow", "Hata Eni(mm) :"))
        self.label_Hata_metre_1.setText(_translate("FaultyFabricWindow", "Hatanın Geldiği Metre(m) :"))
        self.label_Hata_Sinifi_1.setText(_translate("FaultyFabricWindow", "Hatanın Sınıfı :"))
        self.label_Hata_Boyu_1.setText(_translate("FaultyFabricWindow", "Hata Boyu(mm) :"))
        self.groupBox_5.setTitle(_translate("FaultyFabricWindow", "Hata 5"))
        self.label_Hata_Alani_5.setText(_translate("FaultyFabricWindow", "Hata Alanı(mm2) :"))
        self.label_Hata_Eni_5.setText(_translate("FaultyFabricWindow", "Hata Eni(mm) :"))
        self.label_Hata_metre_5.setText(_translate("FaultyFabricWindow", "Hatanın Geldiği Metre(m) :"))
        self.label_Hata_Sinifi_5.setText(_translate("FaultyFabricWindow", "Hatanın Sınıfı :"))
        self.label_Hata_Boyu_5.setText(_translate("FaultyFabricWindow", "Hata Boyu(mm) :"))
        self.menuKameralar.setTitle(_translate("FaultyFabricWindow", "Kameralar"))
        self.menuVeri_Taban.setTitle(_translate("FaultyFabricWindow", "Veri Tabanı"))
        self.menuAdmin_Paneli.setTitle(_translate("FaultyFabricWindow", "Admin Paneli"))
        self.menuHakk_nda.setTitle(_translate("FaultyFabricWindow", "Hakkında"))
        self.actioncikis.setText(_translate("FaultyFabricWindow", "Çıkış"))
        self.actionKameralar.setText(_translate("FaultyFabricWindow", "Kameralar"))
        self.actionVeri_Taban.setText(_translate("FaultyFabricWindow", "Veri Tabanı"))
        self.actionAdmin_Paneli.setText(_translate("FaultyFabricWindow", "Admin Paneli"))
        self.actionHakk_nda.setText(_translate("FaultyFabricWindow", "Hakkında"))

