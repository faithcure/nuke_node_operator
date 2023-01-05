# -*- coding: utf-8 -*-

################################################################################
## Node operator for Nuke 11+
##
## Created by: Fatih ünal
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.setEnabled(True)
        Form.resize(548, 847)
        self.verticalLayout_2 = QVBoxLayout(Form)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.tabWidget = QTabWidget(Form)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setTabPosition(QTabWidget.North)
        self.tabWidget.setTabShape(QTabWidget.Rounded)
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.verticalLayout_3 = QVBoxLayout(self.tab)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.disable_enable_chk = QCheckBox(self.tab)
        self.disable_enable_chk.setObjectName(u"disable_enable_chk")

        self.horizontalLayout_4.addWidget(self.disable_enable_chk)

        self.hide_input = QCheckBox(self.tab)
        self.hide_input.setObjectName(u"hide_input")

        self.horizontalLayout_4.addWidget(self.hide_input)


        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.bookmark = QCheckBox(self.tab)
        self.bookmark.setObjectName(u"bookmark")

        self.horizontalLayout_5.addWidget(self.bookmark)

        self.dopesheet = QCheckBox(self.tab)
        self.dopesheet.setObjectName(u"dopesheet")

        self.horizontalLayout_5.addWidget(self.dopesheet)


        self.verticalLayout.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.gui = QCheckBox(self.tab)
        self.gui.setObjectName(u"gui")

        self.horizontalLayout_6.addWidget(self.gui)

        self.thumbnails = QCheckBox(self.tab)
        self.thumbnails.setObjectName(u"thumbnails")

        self.horizontalLayout_6.addWidget(self.thumbnails)


        self.verticalLayout.addLayout(self.horizontalLayout_6)

        self.line_2 = QFrame(self.tab)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.HLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.verticalLayout.addWidget(self.line_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.use_lifetime = QCheckBox(self.tab)
        self.use_lifetime.setObjectName(u"use_lifetime")

        self.horizontalLayout_3.addWidget(self.use_lifetime)

        self.lifetime_in_frame = QLineEdit(self.tab)
        self.lifetime_in_frame.setObjectName(u"lifetime_in_frame")
        self.lifetime_in_frame.setAutoFillBackground(False)
        self.lifetime_in_frame.setClearButtonEnabled(False)

        self.horizontalLayout_3.addWidget(self.lifetime_in_frame)

        self.label_2 = QLabel(self.tab)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_3.addWidget(self.label_2)

        self.lifetime_out_frame = QLineEdit(self.tab)
        self.lifetime_out_frame.setObjectName(u"lifetime_out_frame")

        self.horizontalLayout_3.addWidget(self.lifetime_out_frame)

        self.lifeTime_Default = QPushButton(self.tab)
        self.lifeTime_Default.setObjectName(u"lifeTime_Default")

        self.horizontalLayout_3.addWidget(self.lifeTime_Default)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.label_4 = QLabel(self.tab)
        self.label_4.setObjectName(u"label_4")

        self.verticalLayout_7.addWidget(self.label_4)

        self.label_input_text = QTextEdit(self.tab)
        self.label_input_text.setObjectName(u"label_input_text")
        self.label_input_text.setMaximumSize(QSize(16777215, 70))
        self.label_input_text.setFrameShadow(QFrame.Plain)

        self.verticalLayout_7.addWidget(self.label_input_text, 0, Qt.AlignTop)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.font_label = QLabel(self.tab)
        self.font_label.setObjectName(u"font_label")
        self.font_label.setMaximumSize(QSize(50, 16777215))

        self.horizontalLayout_8.addWidget(self.font_label)

        self.font_section = QComboBox(self.tab)
        self.font_section.setObjectName(u"font_section")

        self.horizontalLayout_8.addWidget(self.font_section)

        self.make_bold = QPushButton(self.tab)
        self.make_bold.setObjectName(u"make_bold")

        self.horizontalLayout_8.addWidget(self.make_bold)

        self.make_italic = QPushButton(self.tab)
        self.make_italic.setObjectName(u"make_italic")

        self.horizontalLayout_8.addWidget(self.make_italic)

        self.color_palatte = QPushButton(self.tab)
        self.color_palatte.setObjectName(u"color_palatte")

        self.horizontalLayout_8.addWidget(self.color_palatte)

        self.clear_auto_label_btn = QPushButton(self.tab)
        self.clear_auto_label_btn.setObjectName(u"clear_auto_label_btn")
        self.clear_auto_label_btn.setMinimumSize(QSize(150, 0))
        self.clear_auto_label_btn.setStyleSheet(u"background-color: rgb(168, 132, 25);")

        self.horizontalLayout_8.addWidget(self.clear_auto_label_btn)


        self.verticalLayout_7.addLayout(self.horizontalLayout_8)


        self.verticalLayout.addLayout(self.verticalLayout_7)

        self.dockWidget = QDockWidget(self.tab)
        self.dockWidget.setObjectName(u"dockWidget")
        self.dockWidget.setAutoFillBackground(False)
        self.dockWidgetContents_2 = QWidget()
        self.dockWidgetContents_2.setObjectName(u"dockWidgetContents_2")
        self.horizontalLayout_14 = QHBoxLayout(self.dockWidgetContents_2)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.label = QLabel(self.dockWidgetContents_2)
        self.label.setObjectName(u"label")

        self.verticalLayout_6.addWidget(self.label)

        self.line = QFrame(self.dockWidgetContents_2)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_6.addWidget(self.line)

        self.node_list_table = QTableWidget(self.dockWidgetContents_2)
        if (self.node_list_table.columnCount() < 10):
            self.node_list_table.setColumnCount(10)
        __qtablewidgetitem = QTableWidgetItem()
        self.node_list_table.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.node_list_table.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.node_list_table.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.node_list_table.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.node_list_table.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.node_list_table.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.node_list_table.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.node_list_table.setHorizontalHeaderItem(7, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.node_list_table.setHorizontalHeaderItem(8, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.node_list_table.setHorizontalHeaderItem(9, __qtablewidgetitem9)
        self.node_list_table.setObjectName(u"node_list_table")
        self.node_list_table.setStyleSheet(u"")
        self.node_list_table.setAlternatingRowColors(True)
        self.node_list_table.setSelectionMode(QAbstractItemView.SingleSelection)
        self.node_list_table.setSelectionBehavior(QAbstractItemView.SelectItems)
        self.node_list_table.setSortingEnabled(False)
        self.node_list_table.setCornerButtonEnabled(True)
        self.node_list_table.horizontalHeader().setCascadingSectionResizes(True)
        self.node_list_table.horizontalHeader().setHighlightSections(True)
        self.node_list_table.horizontalHeader().setStretchLastSection(True)
        self.node_list_table.verticalHeader().setProperty("showSortIndicator", True)

        self.verticalLayout_6.addWidget(self.node_list_table)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.disable_filter_check = QCheckBox(self.dockWidgetContents_2)
        self.disable_filter_check.setObjectName(u"disable_filter_check")

        self.horizontalLayout_2.addWidget(self.disable_filter_check)

        self.thumb_filter_check = QCheckBox(self.dockWidgetContents_2)
        self.thumb_filter_check.setObjectName(u"thumb_filter_check")

        self.horizontalLayout_2.addWidget(self.thumb_filter_check)

        self.bookmark_filter_check = QCheckBox(self.dockWidgetContents_2)
        self.bookmark_filter_check.setObjectName(u"bookmark_filter_check")

        self.horizontalLayout_2.addWidget(self.bookmark_filter_check)

        self.hide_input_filter_check = QCheckBox(self.dockWidgetContents_2)
        self.hide_input_filter_check.setObjectName(u"hide_input_filter_check")

        self.horizontalLayout_2.addWidget(self.hide_input_filter_check)

        self.search_tab = QLineEdit(self.dockWidgetContents_2)
        self.search_tab.setObjectName(u"search_tab")

        self.horizontalLayout_2.addWidget(self.search_tab)

        self.clearFilter = QPushButton(self.dockWidgetContents_2)
        self.clearFilter.setObjectName(u"clearFilter")

        self.horizontalLayout_2.addWidget(self.clearFilter)


        self.verticalLayout_6.addLayout(self.horizontalLayout_2)


        self.horizontalLayout_14.addLayout(self.verticalLayout_6)

        self.dockWidget.setWidget(self.dockWidgetContents_2)

        self.verticalLayout.addWidget(self.dockWidget)


        self.verticalLayout_3.addLayout(self.verticalLayout)

        self.tabWidget.addTab(self.tab, "")
        self.tab_5 = QWidget()
        self.tab_5.setObjectName(u"tab_5")
        self.verticalLayout_5 = QVBoxLayout(self.tab_5)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.groupBox = QGroupBox(self.tab_5)
        self.groupBox.setObjectName(u"groupBox")
        self.verticalLayout_4 = QVBoxLayout(self.groupBox)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(1, -1, -1, -1)
        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.first_frame_range_line = QLineEdit(self.groupBox)
        self.first_frame_range_line.setObjectName(u"first_frame_range_line")

        self.gridLayout_2.addWidget(self.first_frame_range_line, 3, 1, 1, 1)

        self.localisation_on_off = QComboBox(self.groupBox)
        self.localisation_on_off.setObjectName(u"localisation_on_off")

        self.gridLayout_2.addWidget(self.localisation_on_off, 1, 1, 1, 1)

        self.update_btn = QPushButton(self.groupBox)
        self.update_btn.setObjectName(u"update_btn")

        self.gridLayout_2.addWidget(self.update_btn, 1, 2, 1, 1)

        self.format_box = QComboBox(self.groupBox)
        self.format_box.setObjectName(u"format_box")

        self.gridLayout_2.addWidget(self.format_box, 2, 1, 1, 1)

        self.orginal_range_out = QLineEdit(self.groupBox)
        self.orginal_range_out.setObjectName(u"orginal_range_out")

        self.gridLayout_2.addWidget(self.orginal_range_out, 5, 2, 1, 1)

        self.label_6 = QLabel(self.groupBox)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setMaximumSize(QSize(100, 16777215))

        self.gridLayout_2.addWidget(self.label_6, 2, 0, 1, 1)

        self.label_10 = QLabel(self.groupBox)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setMaximumSize(QSize(100, 16777215))

        self.gridLayout_2.addWidget(self.label_10, 6, 0, 1, 1)

        self.format_size_label = QLabel(self.groupBox)
        self.format_size_label.setObjectName(u"format_size_label")

        self.gridLayout_2.addWidget(self.format_size_label, 2, 2, 1, 1)

        self.label_7 = QLabel(self.groupBox)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setMaximumSize(QSize(100, 16777215))

        self.gridLayout_2.addWidget(self.label_7, 3, 0, 1, 1)

        self.last_frame_range_line = QLineEdit(self.groupBox)
        self.last_frame_range_line.setObjectName(u"last_frame_range_line")

        self.gridLayout_2.addWidget(self.last_frame_range_line, 3, 3, 1, 1)

        self.raw_data = QCheckBox(self.groupBox)
        self.raw_data.setObjectName(u"raw_data")

        self.gridLayout_2.addWidget(self.raw_data, 6, 4, 1, 1)

        self.set_frame_lineedit = QLineEdit(self.groupBox)
        self.set_frame_lineedit.setObjectName(u"set_frame_lineedit")

        self.gridLayout_2.addWidget(self.set_frame_lineedit, 4, 2, 1, 1)

        self.frame_mode_combo = QComboBox(self.groupBox)
        self.frame_mode_combo.addItem("")
        self.frame_mode_combo.addItem("")
        self.frame_mode_combo.addItem("")
        self.frame_mode_combo.setObjectName(u"frame_mode_combo")

        self.gridLayout_2.addWidget(self.frame_mode_combo, 4, 1, 1, 1)

        self.set_frame_before = QComboBox(self.groupBox)
        self.set_frame_before.addItem("")
        self.set_frame_before.addItem("")
        self.set_frame_before.addItem("")
        self.set_frame_before.addItem("")
        self.set_frame_before.setObjectName(u"set_frame_before")

        self.gridLayout_2.addWidget(self.set_frame_before, 3, 2, 1, 1)

        self.auto_alpha = QCheckBox(self.groupBox)
        self.auto_alpha.setObjectName(u"auto_alpha")

        self.gridLayout_2.addWidget(self.auto_alpha, 6, 3, 1, 1)

        self.label_9 = QLabel(self.groupBox)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setMaximumSize(QSize(100, 16777215))

        self.gridLayout_2.addWidget(self.label_9, 5, 0, 1, 1)

        self.premulty = QCheckBox(self.groupBox)
        self.premulty.setObjectName(u"premulty")

        self.gridLayout_2.addWidget(self.premulty, 6, 2, 1, 1)

        self.set_frame_after = QComboBox(self.groupBox)
        self.set_frame_after.addItem("")
        self.set_frame_after.addItem("")
        self.set_frame_after.addItem("")
        self.set_frame_after.addItem("")
        self.set_frame_after.setObjectName(u"set_frame_after")

        self.gridLayout_2.addWidget(self.set_frame_after, 3, 4, 1, 1)

        self.original_range_in = QLineEdit(self.groupBox)
        self.original_range_in.setObjectName(u"original_range_in")

        self.gridLayout_2.addWidget(self.original_range_in, 5, 1, 1, 1)

        self.color_space = QComboBox(self.groupBox)
        self.color_space.addItem("")
        self.color_space.setObjectName(u"color_space")

        self.gridLayout_2.addWidget(self.color_space, 6, 1, 1, 1)

        self.label_5 = QLabel(self.groupBox)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMaximumSize(QSize(100, 16777215))

        self.gridLayout_2.addWidget(self.label_5, 1, 0, 1, 1)

        self.label_8 = QLabel(self.groupBox)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setMaximumSize(QSize(100, 16777215))

        self.gridLayout_2.addWidget(self.label_8, 4, 0, 1, 1)

        self.label_70 = QLabel(self.groupBox)
        self.label_70.setObjectName(u"label_70")

        self.gridLayout_2.addWidget(self.label_70, 7, 0, 1, 1)

        self.reload_btn = QPushButton(self.groupBox)
        self.reload_btn.setObjectName(u"reload_btn")

        self.gridLayout_2.addWidget(self.reload_btn, 1, 3, 1, 1)

        self.missing_frame_combo = QComboBox(self.groupBox)
        self.missing_frame_combo.addItem("")
        self.missing_frame_combo.addItem("")
        self.missing_frame_combo.addItem("")
        self.missing_frame_combo.addItem("")
        self.missing_frame_combo.setObjectName(u"missing_frame_combo")

        self.gridLayout_2.addWidget(self.missing_frame_combo, 7, 1, 1, 1)

        self.gridLayout_2.setColumnStretch(1, 6)

        self.verticalLayout_4.addLayout(self.gridLayout_2)


        self.verticalLayout_5.addWidget(self.groupBox)

        self.line_4 = QFrame(self.tab_5)
        self.line_4.setObjectName(u"line_4")
        self.line_4.setFrameShape(QFrame.HLine)
        self.line_4.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_5.addWidget(self.line_4)

        self.verticalLayout_10 = QVBoxLayout()
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.read_node_dock = QDockWidget(self.tab_5)
        self.read_node_dock.setObjectName(u"read_node_dock")
        self.dockWidgetContents = QWidget()
        self.dockWidgetContents.setObjectName(u"dockWidgetContents")
        self.verticalLayout_11 = QVBoxLayout(self.dockWidgetContents)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.read_meta_table = QTableWidget(self.dockWidgetContents)
        if (self.read_meta_table.columnCount() < 9):
            self.read_meta_table.setColumnCount(9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.read_meta_table.setHorizontalHeaderItem(0, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.read_meta_table.setHorizontalHeaderItem(1, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.read_meta_table.setHorizontalHeaderItem(2, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.read_meta_table.setHorizontalHeaderItem(3, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        self.read_meta_table.setHorizontalHeaderItem(4, __qtablewidgetitem14)
        __qtablewidgetitem15 = QTableWidgetItem()
        self.read_meta_table.setHorizontalHeaderItem(5, __qtablewidgetitem15)
        __qtablewidgetitem16 = QTableWidgetItem()
        self.read_meta_table.setHorizontalHeaderItem(6, __qtablewidgetitem16)
        __qtablewidgetitem17 = QTableWidgetItem()
        self.read_meta_table.setHorizontalHeaderItem(7, __qtablewidgetitem17)
        __qtablewidgetitem18 = QTableWidgetItem()
        self.read_meta_table.setHorizontalHeaderItem(8, __qtablewidgetitem18)
        self.read_meta_table.setObjectName(u"read_meta_table")
        self.read_meta_table.setAlternatingRowColors(True)
        self.read_meta_table.setSelectionMode(QAbstractItemView.SingleSelection)
        self.read_meta_table.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.read_meta_table.setTextElideMode(Qt.ElideMiddle)
        self.read_meta_table.setGridStyle(Qt.SolidLine)
        self.read_meta_table.horizontalHeader().setCascadingSectionResizes(True)
        self.read_meta_table.horizontalHeader().setStretchLastSection(True)
        self.read_meta_table.verticalHeader().setCascadingSectionResizes(True)
        self.read_meta_table.verticalHeader().setStretchLastSection(False)

        self.verticalLayout_11.addWidget(self.read_meta_table)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.warning_read_tab = QLabel(self.dockWidgetContents)
        self.warning_read_tab.setObjectName(u"warning_read_tab")

        self.horizontalLayout_10.addWidget(self.warning_read_tab)

        self.checl_warning = QPushButton(self.dockWidgetContents)
        self.checl_warning.setObjectName(u"checl_warning")

        self.horizontalLayout_10.addWidget(self.checl_warning, 0, Qt.AlignRight)


        self.verticalLayout_11.addLayout(self.horizontalLayout_10)

        self.read_node_dock.setWidget(self.dockWidgetContents)

        self.verticalLayout_10.addWidget(self.read_node_dock)


        self.verticalLayout_5.addLayout(self.verticalLayout_10)

        self.tabWidget.addTab(self.tab_5, "")
        self.tab_4 = QWidget()
        self.tab_4.setObjectName(u"tab_4")
        self.verticalLayout_8 = QVBoxLayout(self.tab_4)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.groupBox_4 = QGroupBox(self.tab_4)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.groupBox_4.setFlat(True)
        self.verticalLayout_19 = QVBoxLayout(self.groupBox_4)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.verticalLayout_19.setContentsMargins(0, 9, 0, 0)
        self.mainLayout = QVBoxLayout()
        self.mainLayout.setObjectName(u"mainLayout")
        self.prxy_render_options_grp = QGroupBox(self.groupBox_4)
        self.prxy_render_options_grp.setObjectName(u"prxy_render_options_grp")
        self.prxy_render_options_grp.setFlat(True)
        self.verticalLayout_9 = QVBoxLayout(self.prxy_render_options_grp)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(-1, 9, -1, -1)
        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.verticalLayout_12 = QVBoxLayout()
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.label_3 = QLabel(self.prxy_render_options_grp)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout_12.addWidget(self.label_3)

        self.label_11 = QLabel(self.prxy_render_options_grp)
        self.label_11.setObjectName(u"label_11")

        self.verticalLayout_12.addWidget(self.label_11)

        self.is_denoise = QCheckBox(self.prxy_render_options_grp)
        self.is_denoise.setObjectName(u"is_denoise")

        self.verticalLayout_12.addWidget(self.is_denoise)


        self.horizontalLayout_12.addLayout(self.verticalLayout_12)

        self.verticalLayout_13 = QVBoxLayout()
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.current_locatipn_label = QLabel(self.prxy_render_options_grp)
        self.current_locatipn_label.setObjectName(u"current_locatipn_label")

        self.verticalLayout_13.addWidget(self.current_locatipn_label)

        self.horizontalLayout_15 = QHBoxLayout()
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.suffix_line_edit = QLineEdit(self.prxy_render_options_grp)
        self.suffix_line_edit.setObjectName(u"suffix_line_edit")
        self.suffix_line_edit.setEnabled(True)

        self.horizontalLayout_15.addWidget(self.suffix_line_edit)

        self.file_type_combo = QComboBox(self.prxy_render_options_grp)
        self.file_type_combo.addItem("")
        self.file_type_combo.addItem("")
        self.file_type_combo.addItem("")
        self.file_type_combo.addItem("")
        self.file_type_combo.addItem("")
        self.file_type_combo.setObjectName(u"file_type_combo")
        self.file_type_combo.setMinimumSize(QSize(100, 0))

        self.horizontalLayout_15.addWidget(self.file_type_combo)


        self.verticalLayout_13.addLayout(self.horizontalLayout_15)

        self.horizontalLayout_16 = QHBoxLayout()
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_16.addItem(self.horizontalSpacer_2)


        self.verticalLayout_13.addLayout(self.horizontalLayout_16)


        self.horizontalLayout_12.addLayout(self.verticalLayout_13)


        self.verticalLayout_9.addLayout(self.horizontalLayout_12)


        self.mainLayout.addWidget(self.prxy_render_options_grp)

        self.locate_grp_bx = QGroupBox(self.groupBox_4)
        self.locate_grp_bx.setObjectName(u"locate_grp_bx")
        self.locate_grp_bx.setFlat(False)
        self.locate_grp_bx.setCheckable(False)
        self.verticalLayout_14 = QVBoxLayout(self.locate_grp_bx)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalLayout_15 = QVBoxLayout()
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.horizontalLayout_17 = QHBoxLayout()
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.label_22 = QLabel(self.locate_grp_bx)
        self.label_22.setObjectName(u"label_22")

        self.horizontalLayout_17.addWidget(self.label_22)

        self.location_line_edit = QLineEdit(self.locate_grp_bx)
        self.location_line_edit.setObjectName(u"location_line_edit")

        self.horizontalLayout_17.addWidget(self.location_line_edit)

        self.select_btn = QPushButton(self.locate_grp_bx)
        self.select_btn.setObjectName(u"select_btn")

        self.horizontalLayout_17.addWidget(self.select_btn)


        self.verticalLayout_15.addLayout(self.horizontalLayout_17)


        self.verticalLayout_14.addLayout(self.verticalLayout_15)

        self.verticalLayout_16 = QVBoxLayout()
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.groupBox_2 = QGroupBox(self.locate_grp_bx)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setMinimumSize(QSize(0, 0))
        self.verticalLayout_17 = QVBoxLayout(self.groupBox_2)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.verticalLayout_18 = QVBoxLayout()
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.horizontalLayout_18 = QHBoxLayout()
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.label_15 = QLabel(self.groupBox_2)
        self.label_15.setObjectName(u"label_15")

        self.horizontalLayout_18.addWidget(self.label_15)


        self.verticalLayout_18.addLayout(self.horizontalLayout_18)

        self.line_5 = QFrame(self.groupBox_2)
        self.line_5.setObjectName(u"line_5")
        self.line_5.setFrameShape(QFrame.HLine)
        self.line_5.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_18.addWidget(self.line_5)

        self.horizontalLayout_19 = QHBoxLayout()
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.label_12 = QLabel(self.groupBox_2)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setMaximumSize(QSize(110, 16777215))

        self.horizontalLayout_19.addWidget(self.label_12)

        self.label_13 = QLabel(self.groupBox_2)
        self.label_13.setObjectName(u"label_13")

        self.horizontalLayout_19.addWidget(self.label_13)


        self.verticalLayout_18.addLayout(self.horizontalLayout_19)

        self.line_3 = QFrame(self.groupBox_2)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setFrameShape(QFrame.HLine)
        self.line_3.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_18.addWidget(self.line_3)

        self.horizontalLayout_20 = QHBoxLayout()
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.label_14 = QLabel(self.groupBox_2)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setMaximumSize(QSize(110, 16777215))

        self.horizontalLayout_20.addWidget(self.label_14)

        self.label_16 = QLabel(self.groupBox_2)
        self.label_16.setObjectName(u"label_16")

        self.horizontalLayout_20.addWidget(self.label_16)


        self.verticalLayout_18.addLayout(self.horizontalLayout_20)

        self.line_6 = QFrame(self.groupBox_2)
        self.line_6.setObjectName(u"line_6")
        self.line_6.setFrameShape(QFrame.HLine)
        self.line_6.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_18.addWidget(self.line_6)

        self.horizontalLayout_21 = QHBoxLayout()
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.label_17 = QLabel(self.groupBox_2)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setMaximumSize(QSize(110, 16777215))

        self.horizontalLayout_21.addWidget(self.label_17)

        self.label_18 = QLabel(self.groupBox_2)
        self.label_18.setObjectName(u"label_18")

        self.horizontalLayout_21.addWidget(self.label_18)


        self.verticalLayout_18.addLayout(self.horizontalLayout_21)

        self.line_7 = QFrame(self.groupBox_2)
        self.line_7.setObjectName(u"line_7")
        self.line_7.setFrameShape(QFrame.HLine)
        self.line_7.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_18.addWidget(self.line_7)

        self.horizontalLayout_22 = QHBoxLayout()
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.label_19 = QLabel(self.groupBox_2)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setMaximumSize(QSize(110, 16777215))

        self.horizontalLayout_22.addWidget(self.label_19)

        self.label_20 = QLabel(self.groupBox_2)
        self.label_20.setObjectName(u"label_20")

        self.horizontalLayout_22.addWidget(self.label_20)


        self.verticalLayout_18.addLayout(self.horizontalLayout_22)

        self.line_9 = QFrame(self.groupBox_2)
        self.line_9.setObjectName(u"line_9")
        self.line_9.setFrameShape(QFrame.HLine)
        self.line_9.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_18.addWidget(self.line_9)

        self.horizontalLayout_25 = QHBoxLayout()
        self.horizontalLayout_25.setObjectName(u"horizontalLayout_25")
        self.horizontalLayout_26 = QHBoxLayout()
        self.horizontalLayout_26.setObjectName(u"horizontalLayout_26")
        self.label_21 = QLabel(self.groupBox_2)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setMaximumSize(QSize(110, 16777215))

        self.horizontalLayout_26.addWidget(self.label_21)

        self.last_path_label = QLabel(self.groupBox_2)
        self.last_path_label.setObjectName(u"last_path_label")

        self.horizontalLayout_26.addWidget(self.last_path_label)


        self.horizontalLayout_25.addLayout(self.horizontalLayout_26)


        self.verticalLayout_18.addLayout(self.horizontalLayout_25)


        self.verticalLayout_17.addLayout(self.verticalLayout_18)


        self.verticalLayout_16.addWidget(self.groupBox_2)


        self.verticalLayout_14.addLayout(self.verticalLayout_16)


        self.mainLayout.addWidget(self.locate_grp_bx)


        self.verticalLayout_19.addLayout(self.mainLayout)

        self.horizontalLayout_24 = QHBoxLayout()
        self.horizontalLayout_24.setObjectName(u"horizontalLayout_24")
        self.write_node_name_check = QCheckBox(self.groupBox_4)
        self.write_node_name_check.setObjectName(u"write_node_name_check")

        self.horizontalLayout_24.addWidget(self.write_node_name_check)

        self.write_node_name = QLineEdit(self.groupBox_4)
        self.write_node_name.setObjectName(u"write_node_name")

        self.horizontalLayout_24.addWidget(self.write_node_name)


        self.verticalLayout_19.addLayout(self.horizontalLayout_24)

        self.line_8 = QFrame(self.groupBox_4)
        self.line_8.setObjectName(u"line_8")
        self.line_8.setFrameShape(QFrame.HLine)
        self.line_8.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_19.addWidget(self.line_8)

        self.horizontalLayout_23 = QHBoxLayout()
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.default_btn = QPushButton(self.groupBox_4)
        self.default_btn.setObjectName(u"default_btn")

        self.horizontalLayout_23.addWidget(self.default_btn)

        self.get_folder_btn = QPushButton(self.groupBox_4)
        self.get_folder_btn.setObjectName(u"get_folder_btn")

        self.horizontalLayout_23.addWidget(self.get_folder_btn)

        self.create_write_node_btn = QPushButton(self.groupBox_4)
        self.create_write_node_btn.setObjectName(u"create_write_node_btn")

        self.horizontalLayout_23.addWidget(self.create_write_node_btn)


        self.verticalLayout_19.addLayout(self.horizontalLayout_23)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_19.addItem(self.verticalSpacer)


        self.verticalLayout_8.addWidget(self.groupBox_4)

        self.tabWidget.addTab(self.tab_4, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.verticalLayout_20 = QVBoxLayout(self.tab_2)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.toolBox_2 = QToolBox(self.tab_2)
        self.toolBox_2.setObjectName(u"toolBox_2")
        self.toolBox_2.setAutoFillBackground(True)
        self.toolBox_2.setFrameShape(QFrame.NoFrame)
        self.toolBox_2.setFrameShadow(QFrame.Plain)
        self.toolBox_2.setLineWidth(0)
        self.toolBox_2Page1 = QWidget()
        self.toolBox_2Page1.setObjectName(u"toolBox_2Page1")
        self.toolBox_2Page1.setGeometry(QRect(0, -329, 489, 1056))
        self.verticalLayout_21 = QVBoxLayout(self.toolBox_2Page1)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.groupBox_3 = QGroupBox(self.toolBox_2Page1)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.horizontalLayout_27 = QHBoxLayout(self.groupBox_3)
        self.horizontalLayout_27.setObjectName(u"horizontalLayout_27")
        self.verticalLayout_23 = QVBoxLayout()
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.label_24 = QLabel(self.groupBox_3)
        self.label_24.setObjectName(u"label_24")

        self.verticalLayout_23.addWidget(self.label_24)

        self.label_23 = QLabel(self.groupBox_3)
        self.label_23.setObjectName(u"label_23")

        self.verticalLayout_23.addWidget(self.label_23)


        self.horizontalLayout_27.addLayout(self.verticalLayout_23)

        self.verticalLayout_22 = QVBoxLayout()
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.lineEdit_2 = QLineEdit(self.groupBox_3)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setMaximumSize(QSize(320, 16777215))
        self.lineEdit_2.setDragEnabled(True)

        self.verticalLayout_22.addWidget(self.lineEdit_2)

        self.lineEdit = QLineEdit(self.groupBox_3)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setMaximumSize(QSize(200, 16777215))
        self.lineEdit.setDragEnabled(True)

        self.verticalLayout_22.addWidget(self.lineEdit)


        self.horizontalLayout_27.addLayout(self.verticalLayout_22)

        self.horizontalSpacer_3 = QSpacerItem(8, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_27.addItem(self.horizontalSpacer_3)

        self.randm_img = QLabel(self.groupBox_3)
        self.randm_img.setObjectName(u"randm_img")

        self.horizontalLayout_27.addWidget(self.randm_img)


        self.verticalLayout_21.addWidget(self.groupBox_3)

        self.groupBox_5 = QGroupBox(self.toolBox_2Page1)
        self.groupBox_5.setObjectName(u"groupBox_5")
        self.horizontalLayout_28 = QHBoxLayout(self.groupBox_5)
        self.horizontalLayout_28.setObjectName(u"horizontalLayout_28")
        self.verticalLayout_27 = QVBoxLayout()
        self.verticalLayout_27.setObjectName(u"verticalLayout_27")
        self.label_27 = QLabel(self.groupBox_5)
        self.label_27.setObjectName(u"label_27")

        self.verticalLayout_27.addWidget(self.label_27)

        self.label_26 = QLabel(self.groupBox_5)
        self.label_26.setObjectName(u"label_26")

        self.verticalLayout_27.addWidget(self.label_26)


        self.horizontalLayout_28.addLayout(self.verticalLayout_27)

        self.verticalLayout_24 = QVBoxLayout()
        self.verticalLayout_24.setObjectName(u"verticalLayout_24")
        self.lineEdit_4 = QLineEdit(self.groupBox_5)
        self.lineEdit_4.setObjectName(u"lineEdit_4")
        self.lineEdit_4.setMaximumSize(QSize(320, 16777215))
        self.lineEdit_4.setDragEnabled(True)

        self.verticalLayout_24.addWidget(self.lineEdit_4)

        self.lineEdit_3 = QLineEdit(self.groupBox_5)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        self.lineEdit_3.setMaximumSize(QSize(200, 16777215))
        self.lineEdit_3.setDragEnabled(True)

        self.verticalLayout_24.addWidget(self.lineEdit_3)


        self.horizontalLayout_28.addLayout(self.verticalLayout_24)

        self.horizontalSpacer_4 = QSpacerItem(8, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_28.addItem(self.horizontalSpacer_4)

        self.noise_img = QLabel(self.groupBox_5)
        self.noise_img.setObjectName(u"noise_img")

        self.horizontalLayout_28.addWidget(self.noise_img)


        self.verticalLayout_21.addWidget(self.groupBox_5)

        self.groupBox_6 = QGroupBox(self.toolBox_2Page1)
        self.groupBox_6.setObjectName(u"groupBox_6")
        self.horizontalLayout_30 = QHBoxLayout(self.groupBox_6)
        self.horizontalLayout_30.setObjectName(u"horizontalLayout_30")
        self.verticalLayout_28 = QVBoxLayout()
        self.verticalLayout_28.setObjectName(u"verticalLayout_28")
        self.label_28 = QLabel(self.groupBox_6)
        self.label_28.setObjectName(u"label_28")

        self.verticalLayout_28.addWidget(self.label_28)

        self.label_29 = QLabel(self.groupBox_6)
        self.label_29.setObjectName(u"label_29")

        self.verticalLayout_28.addWidget(self.label_29)


        self.horizontalLayout_30.addLayout(self.verticalLayout_28)

        self.verticalLayout_25 = QVBoxLayout()
        self.verticalLayout_25.setObjectName(u"verticalLayout_25")
        self.lineEdit_6 = QLineEdit(self.groupBox_6)
        self.lineEdit_6.setObjectName(u"lineEdit_6")
        self.lineEdit_6.setMaximumSize(QSize(320, 16777215))
        self.lineEdit_6.setDragEnabled(True)

        self.verticalLayout_25.addWidget(self.lineEdit_6)

        self.lineEdit_5 = QLineEdit(self.groupBox_6)
        self.lineEdit_5.setObjectName(u"lineEdit_5")
        self.lineEdit_5.setMaximumSize(QSize(200, 16777215))
        self.lineEdit_5.setDragEnabled(True)

        self.verticalLayout_25.addWidget(self.lineEdit_5)


        self.horizontalLayout_30.addLayout(self.verticalLayout_25)

        self.horizontalSpacer_5 = QSpacerItem(8, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_30.addItem(self.horizontalSpacer_5)

        self.sinus_img = QLabel(self.groupBox_6)
        self.sinus_img.setObjectName(u"sinus_img")

        self.horizontalLayout_30.addWidget(self.sinus_img)


        self.verticalLayout_21.addWidget(self.groupBox_6)

        self.groupBox_8 = QGroupBox(self.toolBox_2Page1)
        self.groupBox_8.setObjectName(u"groupBox_8")
        self.horizontalLayout_32 = QHBoxLayout(self.groupBox_8)
        self.horizontalLayout_32.setObjectName(u"horizontalLayout_32")
        self.verticalLayout_29 = QVBoxLayout()
        self.verticalLayout_29.setObjectName(u"verticalLayout_29")
        self.label_31 = QLabel(self.groupBox_8)
        self.label_31.setObjectName(u"label_31")

        self.verticalLayout_29.addWidget(self.label_31)

        self.label_30 = QLabel(self.groupBox_8)
        self.label_30.setObjectName(u"label_30")

        self.verticalLayout_29.addWidget(self.label_30)


        self.horizontalLayout_32.addLayout(self.verticalLayout_29)

        self.verticalLayout_26 = QVBoxLayout()
        self.verticalLayout_26.setObjectName(u"verticalLayout_26")
        self.lineEdit_8 = QLineEdit(self.groupBox_8)
        self.lineEdit_8.setObjectName(u"lineEdit_8")
        self.lineEdit_8.setMaximumSize(QSize(320, 16777215))
        self.lineEdit_8.setDragEnabled(True)

        self.verticalLayout_26.addWidget(self.lineEdit_8)

        self.lineEdit_7 = QLineEdit(self.groupBox_8)
        self.lineEdit_7.setObjectName(u"lineEdit_7")
        self.lineEdit_7.setMaximumSize(QSize(200, 16777215))
        self.lineEdit_7.setDragEnabled(True)

        self.verticalLayout_26.addWidget(self.lineEdit_7)


        self.horizontalLayout_32.addLayout(self.verticalLayout_26)

        self.horizontalSpacer_6 = QSpacerItem(8, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_32.addItem(self.horizontalSpacer_6)

        self.tris_img = QLabel(self.groupBox_8)
        self.tris_img.setObjectName(u"tris_img")

        self.horizontalLayout_32.addWidget(self.tris_img)


        self.verticalLayout_21.addWidget(self.groupBox_8)

        self.groupBox_9 = QGroupBox(self.toolBox_2Page1)
        self.groupBox_9.setObjectName(u"groupBox_9")
        self.horizontalLayout_33 = QHBoxLayout(self.groupBox_9)
        self.horizontalLayout_33.setObjectName(u"horizontalLayout_33")
        self.verticalLayout_56 = QVBoxLayout()
        self.verticalLayout_56.setObjectName(u"verticalLayout_56")
        self.label_56 = QLabel(self.groupBox_9)
        self.label_56.setObjectName(u"label_56")

        self.verticalLayout_56.addWidget(self.label_56)

        self.label_57 = QLabel(self.groupBox_9)
        self.label_57.setObjectName(u"label_57")

        self.verticalLayout_56.addWidget(self.label_57)


        self.horizontalLayout_33.addLayout(self.verticalLayout_56)

        self.verticalLayout_30 = QVBoxLayout()
        self.verticalLayout_30.setObjectName(u"verticalLayout_30")
        self.lineEdit_9 = QLineEdit(self.groupBox_9)
        self.lineEdit_9.setObjectName(u"lineEdit_9")
        self.lineEdit_9.setMaximumSize(QSize(320, 16777215))
        self.lineEdit_9.setDragEnabled(True)

        self.verticalLayout_30.addWidget(self.lineEdit_9)

        self.lineEdit_10 = QLineEdit(self.groupBox_9)
        self.lineEdit_10.setObjectName(u"lineEdit_10")
        self.lineEdit_10.setMaximumSize(QSize(200, 16777215))
        self.lineEdit_10.setDragEnabled(True)

        self.verticalLayout_30.addWidget(self.lineEdit_10)


        self.horizontalLayout_33.addLayout(self.verticalLayout_30)

        self.horizontalSpacer_7 = QSpacerItem(8, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_33.addItem(self.horizontalSpacer_7)

        self.sqr_img = QLabel(self.groupBox_9)
        self.sqr_img.setObjectName(u"sqr_img")

        self.horizontalLayout_33.addWidget(self.sqr_img)


        self.verticalLayout_21.addWidget(self.groupBox_9)

        self.groupBox_13 = QGroupBox(self.toolBox_2Page1)
        self.groupBox_13.setObjectName(u"groupBox_13")
        self.horizontalLayout_34 = QHBoxLayout(self.groupBox_13)
        self.horizontalLayout_34.setObjectName(u"horizontalLayout_34")
        self.verticalLayout_39 = QVBoxLayout()
        self.verticalLayout_39.setObjectName(u"verticalLayout_39")
        self.label_32 = QLabel(self.groupBox_13)
        self.label_32.setObjectName(u"label_32")

        self.verticalLayout_39.addWidget(self.label_32)

        self.label_33 = QLabel(self.groupBox_13)
        self.label_33.setObjectName(u"label_33")

        self.verticalLayout_39.addWidget(self.label_33)


        self.horizontalLayout_34.addLayout(self.verticalLayout_39)

        self.verticalLayout_32 = QVBoxLayout()
        self.verticalLayout_32.setObjectName(u"verticalLayout_32")
        self.lineEdit_13 = QLineEdit(self.groupBox_13)
        self.lineEdit_13.setObjectName(u"lineEdit_13")
        self.lineEdit_13.setMaximumSize(QSize(320, 16777215))
        self.lineEdit_13.setDragEnabled(True)

        self.verticalLayout_32.addWidget(self.lineEdit_13)

        self.lineEdit_14 = QLineEdit(self.groupBox_13)
        self.lineEdit_14.setObjectName(u"lineEdit_14")
        self.lineEdit_14.setMaximumSize(QSize(200, 16777215))
        self.lineEdit_14.setDragEnabled(True)

        self.verticalLayout_32.addWidget(self.lineEdit_14)


        self.horizontalLayout_34.addLayout(self.verticalLayout_32)

        self.horizontalSpacer_8 = QSpacerItem(8, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_34.addItem(self.horizontalSpacer_8)

        self.saw_right_inner_img = QLabel(self.groupBox_13)
        self.saw_right_inner_img.setObjectName(u"saw_right_inner_img")

        self.horizontalLayout_34.addWidget(self.saw_right_inner_img)


        self.verticalLayout_21.addWidget(self.groupBox_13)

        self.groupBox_10 = QGroupBox(self.toolBox_2Page1)
        self.groupBox_10.setObjectName(u"groupBox_10")
        self.horizontalLayout_35 = QHBoxLayout(self.groupBox_10)
        self.horizontalLayout_35.setObjectName(u"horizontalLayout_35")
        self.verticalLayout_46 = QVBoxLayout()
        self.verticalLayout_46.setObjectName(u"verticalLayout_46")
        self.label_40 = QLabel(self.groupBox_10)
        self.label_40.setObjectName(u"label_40")

        self.verticalLayout_46.addWidget(self.label_40)

        self.label_41 = QLabel(self.groupBox_10)
        self.label_41.setObjectName(u"label_41")

        self.verticalLayout_46.addWidget(self.label_41)


        self.horizontalLayout_35.addLayout(self.verticalLayout_46)

        self.verticalLayout_33 = QVBoxLayout()
        self.verticalLayout_33.setObjectName(u"verticalLayout_33")
        self.lineEdit_15 = QLineEdit(self.groupBox_10)
        self.lineEdit_15.setObjectName(u"lineEdit_15")
        self.lineEdit_15.setMaximumSize(QSize(320, 16777215))
        self.lineEdit_15.setDragEnabled(True)

        self.verticalLayout_33.addWidget(self.lineEdit_15)

        self.lineEdit_16 = QLineEdit(self.groupBox_10)
        self.lineEdit_16.setObjectName(u"lineEdit_16")
        self.lineEdit_16.setMaximumSize(QSize(200, 16777215))
        self.lineEdit_16.setDragEnabled(True)

        self.verticalLayout_33.addWidget(self.lineEdit_16)


        self.horizontalLayout_35.addLayout(self.verticalLayout_33)

        self.horizontalSpacer_9 = QSpacerItem(8, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_35.addItem(self.horizontalSpacer_9)

        self.saw_right_img = QLabel(self.groupBox_10)
        self.saw_right_img.setObjectName(u"saw_right_img")

        self.horizontalLayout_35.addWidget(self.saw_right_img)


        self.verticalLayout_21.addWidget(self.groupBox_10)

        self.groupBox_11 = QGroupBox(self.toolBox_2Page1)
        self.groupBox_11.setObjectName(u"groupBox_11")
        self.horizontalLayout_36 = QHBoxLayout(self.groupBox_11)
        self.horizontalLayout_36.setObjectName(u"horizontalLayout_36")
        self.verticalLayout_47 = QVBoxLayout()
        self.verticalLayout_47.setObjectName(u"verticalLayout_47")
        self.label_42 = QLabel(self.groupBox_11)
        self.label_42.setObjectName(u"label_42")

        self.verticalLayout_47.addWidget(self.label_42)

        self.label_43 = QLabel(self.groupBox_11)
        self.label_43.setObjectName(u"label_43")

        self.verticalLayout_47.addWidget(self.label_43)


        self.horizontalLayout_36.addLayout(self.verticalLayout_47)

        self.verticalLayout_34 = QVBoxLayout()
        self.verticalLayout_34.setObjectName(u"verticalLayout_34")
        self.lineEdit_17 = QLineEdit(self.groupBox_11)
        self.lineEdit_17.setObjectName(u"lineEdit_17")
        self.lineEdit_17.setMaximumSize(QSize(320, 16777215))
        self.lineEdit_17.setDragEnabled(True)

        self.verticalLayout_34.addWidget(self.lineEdit_17)

        self.lineEdit_18 = QLineEdit(self.groupBox_11)
        self.lineEdit_18.setObjectName(u"lineEdit_18")
        self.lineEdit_18.setMaximumSize(QSize(200, 16777215))
        self.lineEdit_18.setDragEnabled(True)

        self.verticalLayout_34.addWidget(self.lineEdit_18)


        self.horizontalLayout_36.addLayout(self.verticalLayout_34)

        self.horizontalSpacer_10 = QSpacerItem(8, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_36.addItem(self.horizontalSpacer_10)

        self.saw_right_curve_img = QLabel(self.groupBox_11)
        self.saw_right_curve_img.setObjectName(u"saw_right_curve_img")

        self.horizontalLayout_36.addWidget(self.saw_right_curve_img)


        self.verticalLayout_21.addWidget(self.groupBox_11)

        self.groupBox_12 = QGroupBox(self.toolBox_2Page1)
        self.groupBox_12.setObjectName(u"groupBox_12")
        self.horizontalLayout_37 = QHBoxLayout(self.groupBox_12)
        self.horizontalLayout_37.setObjectName(u"horizontalLayout_37")
        self.verticalLayout_50 = QVBoxLayout()
        self.verticalLayout_50.setObjectName(u"verticalLayout_50")
        self.label_46 = QLabel(self.groupBox_12)
        self.label_46.setObjectName(u"label_46")

        self.verticalLayout_50.addWidget(self.label_46)

        self.label_47 = QLabel(self.groupBox_12)
        self.label_47.setObjectName(u"label_47")

        self.verticalLayout_50.addWidget(self.label_47)


        self.horizontalLayout_37.addLayout(self.verticalLayout_50)

        self.verticalLayout_35 = QVBoxLayout()
        self.verticalLayout_35.setObjectName(u"verticalLayout_35")
        self.lineEdit_19 = QLineEdit(self.groupBox_12)
        self.lineEdit_19.setObjectName(u"lineEdit_19")
        self.lineEdit_19.setMaximumSize(QSize(320, 16777215))
        self.lineEdit_19.setDragEnabled(True)

        self.verticalLayout_35.addWidget(self.lineEdit_19)

        self.lineEdit_20 = QLineEdit(self.groupBox_12)
        self.lineEdit_20.setObjectName(u"lineEdit_20")
        self.lineEdit_20.setMaximumSize(QSize(200, 16777215))
        self.lineEdit_20.setDragEnabled(True)

        self.verticalLayout_35.addWidget(self.lineEdit_20)


        self.horizontalLayout_37.addLayout(self.verticalLayout_35)

        self.horizontalSpacer_11 = QSpacerItem(8, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_37.addItem(self.horizontalSpacer_11)

        self.saw_left_curve_img = QLabel(self.groupBox_12)
        self.saw_left_curve_img.setObjectName(u"saw_left_curve_img")

        self.horizontalLayout_37.addWidget(self.saw_left_curve_img)


        self.verticalLayout_21.addWidget(self.groupBox_12)

        self.groupBox_14 = QGroupBox(self.toolBox_2Page1)
        self.groupBox_14.setObjectName(u"groupBox_14")
        self.horizontalLayout_38 = QHBoxLayout(self.groupBox_14)
        self.horizontalLayout_38.setObjectName(u"horizontalLayout_38")
        self.verticalLayout_51 = QVBoxLayout()
        self.verticalLayout_51.setObjectName(u"verticalLayout_51")
        self.label_48 = QLabel(self.groupBox_14)
        self.label_48.setObjectName(u"label_48")

        self.verticalLayout_51.addWidget(self.label_48)

        self.label_49 = QLabel(self.groupBox_14)
        self.label_49.setObjectName(u"label_49")

        self.verticalLayout_51.addWidget(self.label_49)


        self.horizontalLayout_38.addLayout(self.verticalLayout_51)

        self.verticalLayout_36 = QVBoxLayout()
        self.verticalLayout_36.setObjectName(u"verticalLayout_36")
        self.lineEdit_21 = QLineEdit(self.groupBox_14)
        self.lineEdit_21.setObjectName(u"lineEdit_21")
        self.lineEdit_21.setMaximumSize(QSize(320, 16777215))
        self.lineEdit_21.setDragEnabled(True)

        self.verticalLayout_36.addWidget(self.lineEdit_21)

        self.lineEdit_22 = QLineEdit(self.groupBox_14)
        self.lineEdit_22.setObjectName(u"lineEdit_22")
        self.lineEdit_22.setMaximumSize(QSize(200, 16777215))
        self.lineEdit_22.setDragEnabled(True)

        self.verticalLayout_36.addWidget(self.lineEdit_22)


        self.horizontalLayout_38.addLayout(self.verticalLayout_36)

        self.horizontalSpacer_12 = QSpacerItem(8, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_38.addItem(self.horizontalSpacer_12)

        self.boing_img = QLabel(self.groupBox_14)
        self.boing_img.setObjectName(u"boing_img")

        self.horizontalLayout_38.addWidget(self.boing_img)


        self.verticalLayout_21.addWidget(self.groupBox_14)

        self.groupBox_15 = QGroupBox(self.toolBox_2Page1)
        self.groupBox_15.setObjectName(u"groupBox_15")
        self.horizontalLayout_39 = QHBoxLayout(self.groupBox_15)
        self.horizontalLayout_39.setObjectName(u"horizontalLayout_39")
        self.verticalLayout_52 = QVBoxLayout()
        self.verticalLayout_52.setObjectName(u"verticalLayout_52")
        self.label_50 = QLabel(self.groupBox_15)
        self.label_50.setObjectName(u"label_50")

        self.verticalLayout_52.addWidget(self.label_50)

        self.label_51 = QLabel(self.groupBox_15)
        self.label_51.setObjectName(u"label_51")

        self.verticalLayout_52.addWidget(self.label_51)


        self.horizontalLayout_39.addLayout(self.verticalLayout_52)

        self.verticalLayout_37 = QVBoxLayout()
        self.verticalLayout_37.setObjectName(u"verticalLayout_37")
        self.lineEdit_23 = QLineEdit(self.groupBox_15)
        self.lineEdit_23.setObjectName(u"lineEdit_23")
        self.lineEdit_23.setMaximumSize(QSize(320, 16777215))
        self.lineEdit_23.setDragEnabled(True)

        self.verticalLayout_37.addWidget(self.lineEdit_23)

        self.lineEdit_24 = QLineEdit(self.groupBox_15)
        self.lineEdit_24.setObjectName(u"lineEdit_24")
        self.lineEdit_24.setMaximumSize(QSize(200, 16777215))
        self.lineEdit_24.setDragEnabled(True)

        self.verticalLayout_37.addWidget(self.lineEdit_24)


        self.horizontalLayout_39.addLayout(self.verticalLayout_37)

        self.horizontalSpacer_13 = QSpacerItem(8, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_39.addItem(self.horizontalSpacer_13)

        self.blip_img = QLabel(self.groupBox_15)
        self.blip_img.setObjectName(u"blip_img")

        self.horizontalLayout_39.addWidget(self.blip_img)


        self.verticalLayout_21.addWidget(self.groupBox_15)

        self.groupBox_16 = QGroupBox(self.toolBox_2Page1)
        self.groupBox_16.setObjectName(u"groupBox_16")
        self.horizontalLayout_40 = QHBoxLayout(self.groupBox_16)
        self.horizontalLayout_40.setObjectName(u"horizontalLayout_40")
        self.verticalLayout_55 = QVBoxLayout()
        self.verticalLayout_55.setObjectName(u"verticalLayout_55")
        self.label_54 = QLabel(self.groupBox_16)
        self.label_54.setObjectName(u"label_54")

        self.verticalLayout_55.addWidget(self.label_54)

        self.label_55 = QLabel(self.groupBox_16)
        self.label_55.setObjectName(u"label_55")

        self.verticalLayout_55.addWidget(self.label_55)


        self.horizontalLayout_40.addLayout(self.verticalLayout_55)

        self.verticalLayout_38 = QVBoxLayout()
        self.verticalLayout_38.setObjectName(u"verticalLayout_38")
        self.lineEdit_25 = QLineEdit(self.groupBox_16)
        self.lineEdit_25.setObjectName(u"lineEdit_25")
        self.lineEdit_25.setMaximumSize(QSize(320, 16777215))
        self.lineEdit_25.setDragEnabled(True)

        self.verticalLayout_38.addWidget(self.lineEdit_25)

        self.lineEdit_26 = QLineEdit(self.groupBox_16)
        self.lineEdit_26.setObjectName(u"lineEdit_26")
        self.lineEdit_26.setMaximumSize(QSize(200, 16777215))
        self.lineEdit_26.setDragEnabled(True)

        self.verticalLayout_38.addWidget(self.lineEdit_26)


        self.horizontalLayout_40.addLayout(self.verticalLayout_38)

        self.horizontalSpacer_14 = QSpacerItem(8, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_40.addItem(self.horizontalSpacer_14)

        self.sine_blip_img = QLabel(self.groupBox_16)
        self.sine_blip_img.setObjectName(u"sine_blip_img")

        self.horizontalLayout_40.addWidget(self.sine_blip_img)


        self.verticalLayout_21.addWidget(self.groupBox_16)

        self.toolBox_2.addItem(self.toolBox_2Page1, u"Expressions")

        self.verticalLayout_20.addWidget(self.toolBox_2)

        self.tabWidget.addTab(self.tab_2, "")
        self.tab_6 = QWidget()
        self.tab_6.setObjectName(u"tab_6")
        self.verticalLayout_31 = QVBoxLayout(self.tab_6)
        self.verticalLayout_31.setObjectName(u"verticalLayout_31")
        self.groupBox_17 = QGroupBox(self.tab_6)
        self.groupBox_17.setObjectName(u"groupBox_17")
        self.verticalLayout_43 = QVBoxLayout(self.groupBox_17)
        self.verticalLayout_43.setObjectName(u"verticalLayout_43")
        self.horizontalLayout_29 = QHBoxLayout()
        self.horizontalLayout_29.setObjectName(u"horizontalLayout_29")
        self.verticalLayout_41 = QVBoxLayout()
        self.verticalLayout_41.setObjectName(u"verticalLayout_41")
        self.label_34 = QLabel(self.groupBox_17)
        self.label_34.setObjectName(u"label_34")

        self.verticalLayout_41.addWidget(self.label_34)

        self.label_53 = QLabel(self.groupBox_17)
        self.label_53.setObjectName(u"label_53")

        self.verticalLayout_41.addWidget(self.label_53)

        self.label_52 = QLabel(self.groupBox_17)
        self.label_52.setObjectName(u"label_52")

        self.verticalLayout_41.addWidget(self.label_52)

        self.label_60 = QLabel(self.groupBox_17)
        self.label_60.setObjectName(u"label_60")

        self.verticalLayout_41.addWidget(self.label_60)

        self.label_25 = QLabel(self.groupBox_17)
        self.label_25.setObjectName(u"label_25")

        self.verticalLayout_41.addWidget(self.label_25)

        self.label_44 = QLabel(self.groupBox_17)
        self.label_44.setObjectName(u"label_44")

        self.verticalLayout_41.addWidget(self.label_44)

        self.label_45 = QLabel(self.groupBox_17)
        self.label_45.setObjectName(u"label_45")

        self.verticalLayout_41.addWidget(self.label_45)


        self.horizontalLayout_29.addLayout(self.verticalLayout_41)

        self.verticalLayout_42 = QVBoxLayout()
        self.verticalLayout_42.setObjectName(u"verticalLayout_42")
        self.node_count_label = QLabel(self.groupBox_17)
        self.node_count_label.setObjectName(u"node_count_label")

        self.verticalLayout_42.addWidget(self.node_count_label)

        self.read_node_count_lbl = QLabel(self.groupBox_17)
        self.read_node_count_lbl.setObjectName(u"read_node_count_lbl")

        self.verticalLayout_42.addWidget(self.read_node_count_lbl)

        self.write_node_count_lbl = QLabel(self.groupBox_17)
        self.write_node_count_lbl.setObjectName(u"write_node_count_lbl")

        self.verticalLayout_42.addWidget(self.write_node_count_lbl)

        self.selected_node_cnt_lbl = QLabel(self.groupBox_17)
        self.selected_node_cnt_lbl.setObjectName(u"selected_node_cnt_lbl")

        self.verticalLayout_42.addWidget(self.selected_node_cnt_lbl)

        self.project_dir_lbl = QLabel(self.groupBox_17)
        self.project_dir_lbl.setObjectName(u"project_dir_lbl")

        self.verticalLayout_42.addWidget(self.project_dir_lbl)

        self.project_name_lbl = QLabel(self.groupBox_17)
        self.project_name_lbl.setObjectName(u"project_name_lbl")

        self.verticalLayout_42.addWidget(self.project_name_lbl)

        self.nuke_env_lbl = QLabel(self.groupBox_17)
        self.nuke_env_lbl.setObjectName(u"nuke_env_lbl")

        self.verticalLayout_42.addWidget(self.nuke_env_lbl)


        self.horizontalLayout_29.addLayout(self.verticalLayout_42)

        self.horizontalSpacer_15 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_29.addItem(self.horizontalSpacer_15)


        self.verticalLayout_43.addLayout(self.horizontalLayout_29)


        self.verticalLayout_31.addWidget(self.groupBox_17)

        self.groupBox_7 = QGroupBox(self.tab_6)
        self.groupBox_7.setObjectName(u"groupBox_7")
        self.verticalLayout_45 = QVBoxLayout(self.groupBox_7)
        self.verticalLayout_45.setObjectName(u"verticalLayout_45")
        self.horizontalLayout_49 = QHBoxLayout()
        self.horizontalLayout_49.setObjectName(u"horizontalLayout_49")
        self.verticalLayout_53 = QVBoxLayout()
        self.verticalLayout_53.setObjectName(u"verticalLayout_53")
        self.label_39 = QLabel(self.groupBox_7)
        self.label_39.setObjectName(u"label_39")

        self.verticalLayout_53.addWidget(self.label_39)

        self.label_35 = QLabel(self.groupBox_7)
        self.label_35.setObjectName(u"label_35")

        self.verticalLayout_53.addWidget(self.label_35)

        self.label_64 = QLabel(self.groupBox_7)
        self.label_64.setObjectName(u"label_64")

        self.verticalLayout_53.addWidget(self.label_64)

        self.label_68 = QLabel(self.groupBox_7)
        self.label_68.setObjectName(u"label_68")

        self.verticalLayout_53.addWidget(self.label_68)


        self.horizontalLayout_49.addLayout(self.verticalLayout_53)

        self.verticalLayout_49 = QVBoxLayout()
        self.verticalLayout_49.setObjectName(u"verticalLayout_49")
        self.mem_free_label = QLabel(self.groupBox_7)
        self.mem_free_label.setObjectName(u"mem_free_label")

        self.verticalLayout_49.addWidget(self.mem_free_label)

        self.mem_usage_lbl = QLabel(self.groupBox_7)
        self.mem_usage_lbl.setObjectName(u"mem_usage_lbl")

        self.verticalLayout_49.addWidget(self.mem_usage_lbl)

        self.cpu_core_lbl = QLabel(self.groupBox_7)
        self.cpu_core_lbl.setObjectName(u"cpu_core_lbl")

        self.verticalLayout_49.addWidget(self.cpu_core_lbl)

        self.pc_name_lbl = QLabel(self.groupBox_7)
        self.pc_name_lbl.setObjectName(u"pc_name_lbl")

        self.verticalLayout_49.addWidget(self.pc_name_lbl)


        self.horizontalLayout_49.addLayout(self.verticalLayout_49)

        self.horizontalSpacer_16 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_49.addItem(self.horizontalSpacer_16)


        self.verticalLayout_45.addLayout(self.horizontalLayout_49)

        self.line_15 = QFrame(self.groupBox_7)
        self.line_15.setObjectName(u"line_15")
        self.line_15.setFrameShape(QFrame.HLine)
        self.line_15.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_45.addWidget(self.line_15)

        self.label_36 = QLabel(self.groupBox_7)
        self.label_36.setObjectName(u"label_36")

        self.verticalLayout_45.addWidget(self.label_36)

        self.label_65 = QLabel(self.groupBox_7)
        self.label_65.setObjectName(u"label_65")

        self.verticalLayout_45.addWidget(self.label_65)

        self.label_67 = QLabel(self.groupBox_7)
        self.label_67.setObjectName(u"label_67")

        self.verticalLayout_45.addWidget(self.label_67)

        self.line_19 = QFrame(self.groupBox_7)
        self.line_19.setObjectName(u"line_19")
        self.line_19.setFrameShape(QFrame.HLine)
        self.line_19.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_45.addWidget(self.line_19)

        self.line_16 = QFrame(self.groupBox_7)
        self.line_16.setObjectName(u"line_16")
        self.line_16.setFrameShape(QFrame.HLine)
        self.line_16.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_45.addWidget(self.line_16)

        self.horizontalLayout_41 = QHBoxLayout()
        self.horizontalLayout_41.setObjectName(u"horizontalLayout_41")
        self.checkBox = QCheckBox(self.groupBox_7)
        self.checkBox.setObjectName(u"checkBox")

        self.horizontalLayout_41.addWidget(self.checkBox)

        self.line_18 = QFrame(self.groupBox_7)
        self.line_18.setObjectName(u"line_18")
        self.line_18.setFrameShape(QFrame.VLine)
        self.line_18.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_41.addWidget(self.line_18)

        self.more_prf_link = QPushButton(self.groupBox_7)
        self.more_prf_link.setObjectName(u"more_prf_link")

        self.horizontalLayout_41.addWidget(self.more_prf_link)


        self.verticalLayout_45.addLayout(self.horizontalLayout_41)


        self.verticalLayout_31.addWidget(self.groupBox_7)

        self.groupBox_18 = QGroupBox(self.tab_6)
        self.groupBox_18.setObjectName(u"groupBox_18")
        self.verticalLayout_44 = QVBoxLayout(self.groupBox_18)
        self.verticalLayout_44.setObjectName(u"verticalLayout_44")
        self.verticalLayout_40 = QVBoxLayout()
        self.verticalLayout_40.setObjectName(u"verticalLayout_40")
        self.horizontalLayout_31 = QHBoxLayout()
        self.horizontalLayout_31.setObjectName(u"horizontalLayout_31")
        self.label_59 = QLabel(self.groupBox_18)
        self.label_59.setObjectName(u"label_59")

        self.horizontalLayout_31.addWidget(self.label_59)

        self.label_61 = QLabel(self.groupBox_18)
        self.label_61.setObjectName(u"label_61")
        self.label_61.setOpenExternalLinks(False)

        self.horizontalLayout_31.addWidget(self.label_61)


        self.verticalLayout_40.addLayout(self.horizontalLayout_31)

        self.line_13 = QFrame(self.groupBox_18)
        self.line_13.setObjectName(u"line_13")
        self.line_13.setFrameShape(QFrame.HLine)
        self.line_13.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_40.addWidget(self.line_13)

        self.horizontalLayout_43 = QHBoxLayout()
        self.horizontalLayout_43.setObjectName(u"horizontalLayout_43")
        self.label_38 = QLabel(self.groupBox_18)
        self.label_38.setObjectName(u"label_38")

        self.horizontalLayout_43.addWidget(self.label_38)

        self.label_62 = QLabel(self.groupBox_18)
        self.label_62.setObjectName(u"label_62")

        self.horizontalLayout_43.addWidget(self.label_62)


        self.verticalLayout_40.addLayout(self.horizontalLayout_43)

        self.line_11 = QFrame(self.groupBox_18)
        self.line_11.setObjectName(u"line_11")
        self.line_11.setFrameShape(QFrame.HLine)
        self.line_11.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_40.addWidget(self.line_11)

        self.horizontalLayout_45 = QHBoxLayout()
        self.horizontalLayout_45.setObjectName(u"horizontalLayout_45")
        self.label_66 = QLabel(self.groupBox_18)
        self.label_66.setObjectName(u"label_66")

        self.horizontalLayout_45.addWidget(self.label_66)

        self.youtube = QLabel(self.groupBox_18)
        self.youtube.setObjectName(u"youtube")

        self.horizontalLayout_45.addWidget(self.youtube)


        self.verticalLayout_40.addLayout(self.horizontalLayout_45)

        self.line_12 = QFrame(self.groupBox_18)
        self.line_12.setObjectName(u"line_12")
        self.line_12.setFrameShape(QFrame.HLine)
        self.line_12.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_40.addWidget(self.line_12)

        self.horizontalLayout_46 = QHBoxLayout()
        self.horizontalLayout_46.setObjectName(u"horizontalLayout_46")
        self.label_37 = QLabel(self.groupBox_18)
        self.label_37.setObjectName(u"label_37")

        self.horizontalLayout_46.addWidget(self.label_37)

        self.gitup = QLabel(self.groupBox_18)
        self.gitup.setObjectName(u"gitup")

        self.horizontalLayout_46.addWidget(self.gitup)


        self.verticalLayout_40.addLayout(self.horizontalLayout_46)

        self.line_10 = QFrame(self.groupBox_18)
        self.line_10.setObjectName(u"line_10")
        self.line_10.setFrameShape(QFrame.HLine)
        self.line_10.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_40.addWidget(self.line_10)

        self.horizontalLayout_51 = QHBoxLayout()
        self.horizontalLayout_51.setObjectName(u"horizontalLayout_51")
        self.label_69 = QLabel(self.groupBox_18)
        self.label_69.setObjectName(u"label_69")

        self.horizontalLayout_51.addWidget(self.label_69)

        self.nukepedia_lbl = QLabel(self.groupBox_18)
        self.nukepedia_lbl.setObjectName(u"nukepedia_lbl")

        self.horizontalLayout_51.addWidget(self.nukepedia_lbl)


        self.verticalLayout_40.addLayout(self.horizontalLayout_51)

        self.line_17 = QFrame(self.groupBox_18)
        self.line_17.setObjectName(u"line_17")
        self.line_17.setFrameShape(QFrame.HLine)
        self.line_17.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_40.addWidget(self.line_17)

        self.horizontalLayout_44 = QHBoxLayout()
        self.horizontalLayout_44.setObjectName(u"horizontalLayout_44")
        self.label_58 = QLabel(self.groupBox_18)
        self.label_58.setObjectName(u"label_58")

        self.horizontalLayout_44.addWidget(self.label_58)

        self.label_63 = QLabel(self.groupBox_18)
        self.label_63.setObjectName(u"label_63")

        self.horizontalLayout_44.addWidget(self.label_63)


        self.verticalLayout_40.addLayout(self.horizontalLayout_44)

        self.line_14 = QFrame(self.groupBox_18)
        self.line_14.setObjectName(u"line_14")
        self.line_14.setFrameShape(QFrame.HLine)
        self.line_14.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_40.addWidget(self.line_14)


        self.verticalLayout_44.addLayout(self.verticalLayout_40)


        self.verticalLayout_31.addWidget(self.groupBox_18)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_31.addItem(self.verticalSpacer_2)

        self.tabWidget.addTab(self.tab_6, "")

        self.verticalLayout_2.addWidget(self.tabWidget)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.app_tuts = QPushButton(Form)
        self.app_tuts.setObjectName(u"app_tuts")
        self.app_tuts.setMaximumSize(QSize(45, 16777215))

        self.horizontalLayout.addWidget(self.app_tuts)

        self.refresh_btn = QPushButton(Form)
        self.refresh_btn.setObjectName(u"refresh_btn")

        self.horizontalLayout.addWidget(self.refresh_btn)

        self.close_btn = QPushButton(Form)
        self.close_btn.setObjectName(u"close_btn")

        self.horizontalLayout.addWidget(self.close_btn)


        self.verticalLayout_2.addLayout(self.horizontalLayout)


        self.retranslateUi(Form)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.disable_enable_chk.setText(QCoreApplication.translate("Form", u"Disable / Enable", None))
        self.hide_input.setText(QCoreApplication.translate("Form", u"Hide Input", None))
        self.bookmark.setText(QCoreApplication.translate("Form", u"Bookmark", None))
        self.dopesheet.setText(QCoreApplication.translate("Form", u"Dope Sheet", None))
        self.gui.setText(QCoreApplication.translate("Form", u"$gui", None))
        self.thumbnails.setText(QCoreApplication.translate("Form", u"Thumbnails ON/OF", None))
        self.use_lifetime.setText(QCoreApplication.translate("Form", u"Use Lifetime", None))
        self.lifetime_in_frame.setPlaceholderText(QCoreApplication.translate("Form", u"Input frame", None))
        self.label_2.setText("")
        self.lifetime_out_frame.setPlaceholderText(QCoreApplication.translate("Form", u"Output frame", None))
        self.lifeTime_Default.setText(QCoreApplication.translate("Form", u"Default", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"Label", None))
        self.font_label.setText(QCoreApplication.translate("Form", u"Font:", None))
        self.make_bold.setText(QCoreApplication.translate("Form", u"Bold", None))
        self.make_italic.setText(QCoreApplication.translate("Form", u"Italic", None))
        self.color_palatte.setText(QCoreApplication.translate("Form", u"Set Color", None))
        self.clear_auto_label_btn.setText(QCoreApplication.translate("Form", u"Clear auto label", None))
        self.dockWidget.setWindowTitle(QCoreApplication.translate("Form", u"Nodes settings (Dockable)", None))
        self.label.setText(QCoreApplication.translate("Form", u"Selected Nodes: ", None))
        ___qtablewidgetitem = self.node_list_table.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Form", u"Node Name", None));
        ___qtablewidgetitem1 = self.node_list_table.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Form", u"Disabled", None));
        ___qtablewidgetitem2 = self.node_list_table.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Form", u"Mix", None));
        ___qtablewidgetitem3 = self.node_list_table.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("Form", u"Label", None));
        ___qtablewidgetitem4 = self.node_list_table.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("Form", u"Thumbnail", None));
        ___qtablewidgetitem5 = self.node_list_table.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("Form", u"Color Space", None));
        ___qtablewidgetitem6 = self.node_list_table.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("Form", u"Localized", None));
        ___qtablewidgetitem7 = self.node_list_table.horizontalHeaderItem(7)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("Form", u"Bookmark", None));
        ___qtablewidgetitem8 = self.node_list_table.horizontalHeaderItem(8)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("Form", u"Hide Input", None));
        ___qtablewidgetitem9 = self.node_list_table.horizontalHeaderItem(9)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("Form", u"Lifetime", None));
        self.disable_filter_check.setText(QCoreApplication.translate("Form", u"Disabled", None))
        self.thumb_filter_check.setText(QCoreApplication.translate("Form", u"Thumbnails", None))
        self.bookmark_filter_check.setText(QCoreApplication.translate("Form", u"Bookmark", None))
        self.hide_input_filter_check.setText(QCoreApplication.translate("Form", u"Hide input", None))
        self.search_tab.setPlaceholderText(QCoreApplication.translate("Form", u"Find Node", None))
        self.clearFilter.setText(QCoreApplication.translate("Form", u"Clear", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("Form", u"Node Settings", None))
        self.groupBox.setTitle(QCoreApplication.translate("Form", u"Read node settings:", None))
        self.update_btn.setText(QCoreApplication.translate("Form", u"Update", None))
        self.label_6.setText(QCoreApplication.translate("Form", u"Format", None))
        self.label_10.setText(QCoreApplication.translate("Form", u"Colorspace", None))
        self.format_size_label.setText(QCoreApplication.translate("Form", u"Check root format!", None))
        self.label_7.setText(QCoreApplication.translate("Form", u"Frame Range", None))
        self.raw_data.setText(QCoreApplication.translate("Form", u"Raw Data", None))
        self.frame_mode_combo.setItemText(0, QCoreApplication.translate("Form", u"offset", None))
        self.frame_mode_combo.setItemText(1, QCoreApplication.translate("Form", u"start at", None))
        self.frame_mode_combo.setItemText(2, QCoreApplication.translate("Form", u"expression", None))

        self.set_frame_before.setItemText(0, QCoreApplication.translate("Form", u"hold", None))
        self.set_frame_before.setItemText(1, QCoreApplication.translate("Form", u"loop", None))
        self.set_frame_before.setItemText(2, QCoreApplication.translate("Form", u"bounce", None))
        self.set_frame_before.setItemText(3, QCoreApplication.translate("Form", u"black", None))

        self.auto_alpha.setText(QCoreApplication.translate("Form", u"Auto Alpha", None))
        self.label_9.setText(QCoreApplication.translate("Form", u"Original range           ", None))
        self.premulty.setText(QCoreApplication.translate("Form", u"Premultiplied", None))
        self.set_frame_after.setItemText(0, QCoreApplication.translate("Form", u"hold", None))
        self.set_frame_after.setItemText(1, QCoreApplication.translate("Form", u"loop", None))
        self.set_frame_after.setItemText(2, QCoreApplication.translate("Form", u"bounce", None))
        self.set_frame_after.setItemText(3, QCoreApplication.translate("Form", u"black", None))

        self.color_space.setItemText(0, QCoreApplication.translate("Form", u"Default", None))

        self.label_5.setText(QCoreApplication.translate("Form", u"Localization", None))
        self.label_8.setText(QCoreApplication.translate("Form", u"Frame", None))
        self.label_70.setText(QCoreApplication.translate("Form", u"Missing frames", None))
        self.reload_btn.setText(QCoreApplication.translate("Form", u"Reload", None))
        self.missing_frame_combo.setItemText(0, QCoreApplication.translate("Form", u"error", None))
        self.missing_frame_combo.setItemText(1, QCoreApplication.translate("Form", u"black", None))
        self.missing_frame_combo.setItemText(2, QCoreApplication.translate("Form", u"checkerboard", None))
        self.missing_frame_combo.setItemText(3, QCoreApplication.translate("Form", u"nearest frame", None))

#if QT_CONFIG(accessibility)
        self.read_node_dock.setAccessibleName("")
#endif // QT_CONFIG(accessibility)
        self.read_node_dock.setWindowTitle(QCoreApplication.translate("Form", u"Read node file settings (metadata)", None))
        ___qtablewidgetitem10 = self.read_meta_table.horizontalHeaderItem(0)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("Form", u"Name", None));
        ___qtablewidgetitem11 = self.read_meta_table.horizontalHeaderItem(1)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("Form", u"Extension", None));
        ___qtablewidgetitem12 = self.read_meta_table.horizontalHeaderItem(2)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("Form", u"Localized", None));
        ___qtablewidgetitem13 = self.read_meta_table.horizontalHeaderItem(3)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("Form", u"Resolution", None));
        ___qtablewidgetitem14 = self.read_meta_table.horizontalHeaderItem(4)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("Form", u"Codec", None));
        ___qtablewidgetitem15 = self.read_meta_table.horizontalHeaderItem(5)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("Form", u"Created Date", None));
        ___qtablewidgetitem16 = self.read_meta_table.horizontalHeaderItem(6)
        ___qtablewidgetitem16.setText(QCoreApplication.translate("Form", u"File Path", None));
        ___qtablewidgetitem17 = self.read_meta_table.horizontalHeaderItem(7)
        ___qtablewidgetitem17.setText(QCoreApplication.translate("Form", u"File size", None));
        ___qtablewidgetitem18 = self.read_meta_table.horizontalHeaderItem(8)
        ___qtablewidgetitem18.setText(QCoreApplication.translate("Form", u"Explore", None));
        self.warning_read_tab.setText(QCoreApplication.translate("Form", u"Status: ", None))
        self.checl_warning.setText(QCoreApplication.translate("Form", u"Check Warning", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_5), QCoreApplication.translate("Form", u"Read Node ", None))
        self.prxy_render_options_grp.setTitle(QCoreApplication.translate("Form", u"Proxy Render Options", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"Shot Name", None))
        self.label_11.setText(QCoreApplication.translate("Form", u"Line Suffix", None))
#if QT_CONFIG(tooltip)
        self.is_denoise.setToolTip(QCoreApplication.translate("Form", u"if active: Insert \"DN\" info to render name.", None))
#endif // QT_CONFIG(tooltip)
        self.is_denoise.setText(QCoreApplication.translate("Form", u"isDenoise?", None))
        self.current_locatipn_label.setText(QCoreApplication.translate("Form", u"SHOT_NAME_CURR", None))
#if QT_CONFIG(tooltip)
        self.suffix_line_edit.setToolTip(QCoreApplication.translate("Form", u"If Empty there is not any changes of the current name.", None))
#endif // QT_CONFIG(tooltip)
        self.file_type_combo.setItemText(0, QCoreApplication.translate("Form", u"exr", None))
        self.file_type_combo.setItemText(1, QCoreApplication.translate("Form", u"tga", None))
        self.file_type_combo.setItemText(2, QCoreApplication.translate("Form", u"dpx", None))
        self.file_type_combo.setItemText(3, QCoreApplication.translate("Form", u"tiff", None))
        self.file_type_combo.setItemText(4, QCoreApplication.translate("Form", u"jpg", None))

#if QT_CONFIG(tooltip)
        self.file_type_combo.setToolTip(QCoreApplication.translate("Form", u"Select file type. Make sure what is enough for you.", None))
#endif // QT_CONFIG(tooltip)
        self.locate_grp_bx.setTitle(QCoreApplication.translate("Form", u"Location Setting", None))
        self.label_22.setText(QCoreApplication.translate("Form", u"Input specific  path: ", None))
#if QT_CONFIG(tooltip)
        self.location_line_edit.setToolTip(QCoreApplication.translate("Form", u"Change manually direction of the render node.", None))
#endif // QT_CONFIG(tooltip)
        self.select_btn.setText(QCoreApplication.translate("Form", u"Select", None))
        self.groupBox_2.setTitle("")
        self.label_15.setText(QCoreApplication.translate("Form", u"LAST CHECK", None))
        self.label_12.setText(QCoreApplication.translate("Form", u"File Name:", None))
        self.label_13.setText(QCoreApplication.translate("Form", u"SHOT_NAME_INFO", None))
        self.label_14.setText(QCoreApplication.translate("Form", u"Denoise: ", None))
        self.label_16.setText(QCoreApplication.translate("Form", u"DENOISE_NAME_INFO", None))
        self.label_17.setText(QCoreApplication.translate("Form", u"File Type:", None))
        self.label_18.setText(QCoreApplication.translate("Form", u"FILE_TYPE_INFO", None))
        self.label_19.setText(QCoreApplication.translate("Form", u"Individual Suffix:", None))
        self.label_20.setText(QCoreApplication.translate("Form", u"IN_SUF_INF", None))
        self.label_21.setText(QCoreApplication.translate("Form", u"Path: ", None))
        self.last_path_label.setText(QCoreApplication.translate("Form", u"LAST_PATH", None))
#if QT_CONFIG(tooltip)
        self.write_node_name_check.setToolTip(QCoreApplication.translate("Form", u"Change write node name if you want!", None))
#endif // QT_CONFIG(tooltip)
        self.write_node_name_check.setText(QCoreApplication.translate("Form", u"Specific write node name:", None))
#if QT_CONFIG(tooltip)
        self.default_btn.setToolTip(QCoreApplication.translate("Form", u"Set back to default settings.", None))
#endif // QT_CONFIG(tooltip)
        self.default_btn.setText(QCoreApplication.translate("Form", u"Create Matte Write", None))
#if QT_CONFIG(tooltip)
        self.get_folder_btn.setToolTip(QCoreApplication.translate("Form", u"Get current script directory.", None))
#endif // QT_CONFIG(tooltip)
        self.get_folder_btn.setText(QCoreApplication.translate("Form", u"Explore", None))
#if QT_CONFIG(tooltip)
        self.create_write_node_btn.setToolTip(QCoreApplication.translate("Form", u"Create write node with current settings.", None))
#endif // QT_CONFIG(tooltip)
        self.create_write_node_btn.setText(QCoreApplication.translate("Form", u"Create", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), QCoreApplication.translate("Form", u"Write Node", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("Form", u"Randomize", None))
        self.label_24.setText(QCoreApplication.translate("Form", u"Formula:", None))
        self.label_23.setText(QCoreApplication.translate("Form", u"Quick Wave", None))
        self.lineEdit_2.setText(QCoreApplication.translate("Form", u"random((frame+offset)/waveLength) * (maxVal-minVal) + minVal", None))
        self.lineEdit.setText(QCoreApplication.translate("Form", u"random((frame)/10)", None))
        self.randm_img.setText("")
        self.groupBox_5.setTitle(QCoreApplication.translate("Form", u"Noise", None))
        self.label_27.setText(QCoreApplication.translate("Form", u"Formula:", None))
        self.label_26.setText(QCoreApplication.translate("Form", u"Quick Wave", None))
        self.lineEdit_4.setText(QCoreApplication.translate("Form", u"(noise((frame+offset)/waveLength)+1)/2 * (maxVal-minVal) + minVal", None))
        self.lineEdit_3.setText(QCoreApplication.translate("Form", u"(noise((frame)/10)+1)/2", None))
        self.noise_img.setText("")
        self.groupBox_6.setTitle(QCoreApplication.translate("Form", u"Sine", None))
        self.label_28.setText(QCoreApplication.translate("Form", u"Formula:", None))
        self.label_29.setText(QCoreApplication.translate("Form", u"Quick Wave", None))
        self.lineEdit_6.setText(QCoreApplication.translate("Form", u"(sin(2*pi*(frame+offset)/waveLength)+1)/2 * (maxVal-minVal) + minVal", None))
        self.lineEdit_5.setText(QCoreApplication.translate("Form", u"(sin(2*pi*(frame)/24)+1)/2", None))
        self.sinus_img.setText("")
        self.groupBox_8.setTitle(QCoreApplication.translate("Form", u"Triangle", None))
        self.label_31.setText(QCoreApplication.translate("Form", u"Formula:", None))
        self.label_30.setText(QCoreApplication.translate("Form", u"Quick Wave", None))
        self.lineEdit_8.setText(QCoreApplication.translate("Form", u"(asin(sin(2*pi*(frame+offset)/waveLength))/pi+0.5) * (maxVal-minVal) + minVal", None))
        self.lineEdit_7.setText(QCoreApplication.translate("Form", u"(asin(sin(2*pi*(frame)/24))/pi+0.5)", None))
        self.tris_img.setText("")
        self.groupBox_9.setTitle(QCoreApplication.translate("Form", u"Square", None))
        self.label_56.setText(QCoreApplication.translate("Form", u"Formula:", None))
        self.label_57.setText(QCoreApplication.translate("Form", u"Quick Wave", None))
        self.lineEdit_9.setText(QCoreApplication.translate("Form", u"int(sin(2*pi*(frame+offset)/waveLength)+1) * (maxVal-minVal) + minVal", None))
        self.lineEdit_10.setText(QCoreApplication.translate("Form", u"int(sin(2*pi*(frame)/24)+1)", None))
        self.sqr_img.setText("")
        self.groupBox_13.setTitle(QCoreApplication.translate("Form", u"Saw Right Inner", None))
        self.label_32.setText(QCoreApplication.translate("Form", u"Formula:", None))
        self.label_33.setText(QCoreApplication.translate("Form", u"Quick Wave", None))
        self.lineEdit_13.setText(QCoreApplication.translate("Form", u"(exp(2*pi*((frame+offset) % waveLength)/waveLength)-1)/exp(2*pi) * (maxVal-minVal) + minVal", None))
        self.lineEdit_14.setText(QCoreApplication.translate("Form", u"(exp(2*pi*((frame) % 24)/24)-1)/exp(2*pi)", None))
        self.saw_right_inner_img.setText("")
        self.groupBox_10.setTitle(QCoreApplication.translate("Form", u"Saw Right", None))
        self.label_40.setText(QCoreApplication.translate("Form", u"Formula:", None))
        self.label_41.setText(QCoreApplication.translate("Form", u"Quick Wave", None))
        self.lineEdit_15.setText(QCoreApplication.translate("Form", u"((frame+offset) % waveLength)/waveLength * (maxVal-minVal) + minVal", None))
        self.lineEdit_16.setText(QCoreApplication.translate("Form", u"((frame) % 24)/24", None))
        self.saw_right_img.setText("")
        self.groupBox_11.setTitle(QCoreApplication.translate("Form", u"Saw Right Curve", None))
        self.label_42.setText(QCoreApplication.translate("Form", u"Formula:", None))
        self.label_43.setText(QCoreApplication.translate("Form", u"Quick Wave", None))
        self.lineEdit_17.setText(QCoreApplication.translate("Form", u"sin((pi*(frame+offset)/(2*waveLength)) % (pi/2)) * (maxVal-minVal) + minVal", None))
        self.lineEdit_18.setText(QCoreApplication.translate("Form", u"sin((pi*(frame)/(2*24)) % (pi/2))", None))
        self.saw_right_curve_img.setText("")
        self.groupBox_12.setTitle(QCoreApplication.translate("Form", u"Saw Left Curve", None))
        self.label_46.setText(QCoreApplication.translate("Form", u"Formula:", None))
        self.label_47.setText(QCoreApplication.translate("Form", u"Quick Wave", None))
        self.lineEdit_19.setText(QCoreApplication.translate("Form", u"cos((pi*(frame+offset)/(2*waveLength)) % (pi/2)) * (maxVal-minVal) + minVal", None))
        self.lineEdit_20.setText(QCoreApplication.translate("Form", u"cos((pi*(frame)/(2*24)) % (pi/2))", None))
        self.saw_left_curve_img.setText("")
        self.groupBox_14.setTitle(QCoreApplication.translate("Form", u"Bounce", None))
        self.label_48.setText(QCoreApplication.translate("Form", u"Formula:", None))
        self.label_49.setText(QCoreApplication.translate("Form", u"Quick Wave", None))
        self.lineEdit_21.setText(QCoreApplication.translate("Form", u"abs(sin(pi*(frame + offset)/waveLength))* (maxVal-minVal) + minVal", None))
        self.lineEdit_22.setText(QCoreApplication.translate("Form", u"abs(sin(pi*(frame)/24))", None))
        self.boing_img.setText("")
        self.groupBox_15.setTitle(QCoreApplication.translate("Form", u"Blip", None))
        self.label_50.setText(QCoreApplication.translate("Form", u"Formula:", None))
        self.label_51.setText(QCoreApplication.translate("Form", u"Quick Wave", None))
        self.lineEdit_23.setText(QCoreApplication.translate("Form", u"((frame+(offset+waveLength)) % (waveLength+blipLength)/(waveLength)) *(waveLength/blipLength) - (waveLength/blipLength) >= 0 ? maxVal : minVal", None))
        self.lineEdit_24.setText(QCoreApplication.translate("Form", u"((frame+20) % (20+5)/(20)) *(20/5) - (20/5) >= 0 ? 1 : 0", None))
        self.blip_img.setText("")
        self.groupBox_16.setTitle(QCoreApplication.translate("Form", u"Sine Blip", None))
        self.label_54.setText(QCoreApplication.translate("Form", u"Formula:", None))
        self.label_55.setText(QCoreApplication.translate("Form", u"Quick Wave", None))
        self.lineEdit_25.setText(QCoreApplication.translate("Form", u"((int((frame+offset) % waveLength)) >= 0 ? ((int((frame+offset) % waveLength)) <= (0+(blipLength-1)) ? ((sin(pi*((frame+offset) % waveLength)/blipLength)/2+1/2) * (2*maxVal-2*minVal) + (2*minVal-maxVal)) : minVal)  : minVal)", None))
        self.lineEdit_26.setText(QCoreApplication.translate("Form", u"((int(frame % 20)) >= 0 ? ((int(frame % 20)) <= (5-1) ? ((sin(pi*(frame % 20)/5)/2+1/2) * (2*1-2*0) + (2*0-1)) : 0)  : 0)", None))
        self.sine_blip_img.setText("")
        self.toolBox_2.setItemText(self.toolBox_2.indexOf(self.toolBox_2Page1), QCoreApplication.translate("Form", u"Expressions", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("Form", u"Expressions", None))
        self.groupBox_17.setTitle(QCoreApplication.translate("Form", u"Comp Info", None))
        self.label_34.setText(QCoreApplication.translate("Form", u"Node Count:", None))
        self.label_53.setText(QCoreApplication.translate("Form", u"Read node count:", None))
        self.label_52.setText(QCoreApplication.translate("Form", u"Write node count:", None))
        self.label_60.setText(QCoreApplication.translate("Form", u"Selected Node count:", None))
        self.label_25.setText(QCoreApplication.translate("Form", u"Project Path:", None))
        self.label_44.setText(QCoreApplication.translate("Form", u"Project Name:", None))
        self.label_45.setText(QCoreApplication.translate("Form", u"Nuke Env:", None))
        self.node_count_label.setText("")
        self.read_node_count_lbl.setText("")
        self.write_node_count_lbl.setText("")
        self.selected_node_cnt_lbl.setText("")
        self.project_dir_lbl.setText("")
        self.project_name_lbl.setText("")
        self.nuke_env_lbl.setText("")
        self.groupBox_7.setTitle(QCoreApplication.translate("Form", u"Performance", None))
        self.label_39.setText(QCoreApplication.translate("Form", u"Free space of memory:", None))
        self.label_35.setText(QCoreApplication.translate("Form", u"Memory usage:", None))
        self.label_64.setText(QCoreApplication.translate("Form", u"Cpu core:", None))
        self.label_68.setText(QCoreApplication.translate("Form", u"Pc name:", None))
        self.mem_free_label.setText(QCoreApplication.translate("Form", u"TextLabel", None))
        self.mem_usage_lbl.setText(QCoreApplication.translate("Form", u"TextLabel", None))
        self.cpu_core_lbl.setText(QCoreApplication.translate("Form", u"TextLabel", None))
        self.pc_name_lbl.setText(QCoreApplication.translate("Form", u"TextLabel", None))
        self.label_36.setText(QCoreApplication.translate("Form", u"This \"performance\" panel shown from os system profiling. You can use \"profile\" node.", None))
        self.label_65.setText(QCoreApplication.translate("Form", u"Please check for more information about \"Profiling\" settings. You can see blow button for formation.", None))
        self.label_67.setText(QCoreApplication.translate("Form", u"... or use performance timer but I don't recommended it for windows.", None))
        self.checkBox.setText(QCoreApplication.translate("Form", u"Performance timer ON/OFF", None))
        self.more_prf_link.setText(QCoreApplication.translate("Form", u"More profiling information", None))
        self.groupBox_18.setTitle(QCoreApplication.translate("Form", u"Help", None))
        self.label_59.setText(QCoreApplication.translate("Form", u"Author", None))
        self.label_61.setText(QCoreApplication.translate("Form", u"www.fatihunal.net", None))
        self.label_38.setText(QCoreApplication.translate("Form", u"Email:", None))
        self.label_62.setText(QCoreApplication.translate("Form", u"fatihunal1989@gmail.com", None))
        self.label_66.setText(QCoreApplication.translate("Form", u"Tutorials:", None))
        self.youtube.setText(QCoreApplication.translate("Form", u"youtube", None))
        self.label_37.setText(QCoreApplication.translate("Form", u"Github:", None))
        self.gitup.setText(QCoreApplication.translate("Form", u"gitup", None))
        self.label_69.setText(QCoreApplication.translate("Form", u"Nukepedia:", None))
        self.nukepedia_lbl.setText(QCoreApplication.translate("Form", u"nuke_pedia", None))
        self.label_58.setText(QCoreApplication.translate("Form", u"Special thanks:", None))
        self.label_63.setText(QCoreApplication.translate("Form", u"www.cameroncarson.com (expressions)", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_6), QCoreApplication.translate("Form", u"General Info", None))
        self.app_tuts.setText(QCoreApplication.translate("Form", u"?", None))
        self.refresh_btn.setText(QCoreApplication.translate("Form", u"Refresh", None))
        self.close_btn.setText(QCoreApplication.translate("Form", u"CLOSE", None))
    # retranslateUi

