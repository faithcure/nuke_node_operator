# -*- coding: utf-8 -*-

################################################################################
## Node operator for Nuke 11+
##
## Created by: Fatih ünal
## WebSite: wwww.fatihunal.net
## e-Mail: fatihunal1989@gmail.com
################################################################################

import nuke
from node_operator_mainwindow import *
import read_node_tab
import create_write_node
import ready_expressions
import general_info
import importlib
importlib.reload(read_node_tab)
importlib.reload(create_write_node)
importlib.reload(ready_expressions)
importlib.reload(general_info)

class nodes_operator(QWidget, Ui_Form):
    def __init__(self):
        super(nodes_operator, self).__init__()
        
        self.setupUi(self)
        self.setWindowTitle("Node(s) Operator (SpreadSheet) v0.1")
        self.close_btn.clicked.connect(self.close_event)
        self.disable_enable_chk.stateChanged.connect(self.disable_enable)
        self.bookmark.stateChanged.connect(self.setBookmark)
        self.hide_input.stateChanged.connect(self.hide_input_def)
        self.thumbnails.stateChanged.connect(self.postage_stamp)
        self.gui.setEnabled(0)
        self.make_italic.setEnabled(0)
        self.make_bold.setEnabled(0)
        self.font_label.setEnabled(0)
        
        # Read node settings
        read_node_tab.nodes_operator_read_node_tab.localization_policy(self, "localizationPolicy")
        read_node_tab.nodes_operator_read_node_tab.update_node(self, "updateLocalization")
        read_node_tab.nodes_operator_read_node_tab.reload_node(self, "reload")
        read_node_tab.nodes_operator_read_node_tab.raw_data(self, "raw")
        read_node_tab.nodes_operator_read_node_tab.premulty(self, "premultiplied")
        read_node_tab.nodes_operator_read_node_tab.auto_alpha(self, "auto_alpha")
        read_node_tab.nodes_operator_read_node_tab.format_settings(self)
        read_node_tab.nodes_operator_read_node_tab.frame_range(self)
        read_node_tab.nodes_operator_read_node_tab.frame_offset(self, "frame_mode", "frame")
        read_node_tab.nodes_operator_read_node_tab.original_range(self, "origfirst", "origlast" )
        read_node_tab.nodes_operator_read_node_tab.colorspace(self, "colorspace")
        read_node_tab.nodes_operator_read_node_tab.loadDataReadNode(self)
        read_node_tab.nodes_operator_read_node_tab.missing_frames(self, "on_error")

        # Write node settings
        create_write_node.write_settings_tab.base_name(self, "name", "Proxy", "DN", "EXR", "Empty", ".####.", "project_directory", "PRXY_EXPORT")

        # Expressions -Text end -Knob values
        ready_expressions.ready_to_expressions.tab_widgets(self)

        # general info
        general_info.general_infos.get_node_count(self)
        general_info.general_infos.get_link_contact(self)
        general_info.general_infos.get_selected_node_count(self)
        general_info.general_infos.get_read_count(self)
        general_info.general_infos.get_write_count(self)
        general_info.general_infos.get_project_dir(self)
        general_info.general_infos.get_project_name(self)
        general_info.general_infos.get_performence_timer(self)
        general_info.general_infos.get_nuke_env(self)
        general_info.general_infos.check_state_pf(self)
        general_info.general_infos.open_close_pf(self)       
        general_info.general_infos.get_spec_system(self)
        general_info.general_infos.set_web_links(self)

        self.use_lifetime.stateChanged.connect(self.uselifetime_state)
        self.lifetime_in_frame.setEnabled(0)       
        self.lifetime_in_frame.setValidator(QIntValidator())
        self.lifetime_out_frame.setValidator(QIntValidator())
        self.lifetime_out_frame.setEnabled(0)
        self.lifetime_in_frame.returnPressed.connect(self.startLifetime)
        self.lifetime_in_frame.textChanged.connect(self.startLifetime)
        self.lifetime_out_frame.returnPressed.connect(self.endLifetime) 
        self.lifetime_out_frame.textChanged.connect(self.endLifetime)
        self.lifeTime_Default.setText("Reset Lifetime")
        self.lifeTime_Default.clicked.connect(self.resetLifetimeSettings)

        # Lifetime End 
        self.color_palatte.clicked.connect(self.changeNodeColor)
        self.color_palatte.setText("Tile Color")
        self.clear_auto_label_btn.clicked.connect(lambda: self.label_input_text.clear())
        self.label_input_text.textChanged.connect(self.appendLabelToNode)
        self.dopesheet.stateChanged.connect(self.dope_sheet)
        self.node_list_table.sortItems(0,Qt.AscendingOrder)
        self.node_list_table.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)
        self.refresh_btn.clicked.connect(self.refresh)
        self.disable_filter_check.stateChanged.connect(self.disabledFilter)
        self.thumb_filter_check.stateChanged.connect(self.thumdnailFilter)
        self.bookmark_filter_check.stateChanged.connect(self.bookmarkFilter)
        self.hide_input_filter_check.stateChanged.connect(self.hideInputFilter)
        self.clearFilter.clicked.connect(self.clearFilterState)
        self.search_tab.textChanged.connect(self.nodesFilter)
        self.loadNodeData() # QtableWidget NodeGraph
        self.node_list_table.clicked.connect(self.focusSelectedNode)
    

    def refresh(self):
            self.close()
            start.form = nodes_operator()
            start.form.show()

    def close_event(self):
            self.close()

    def clearFilterState(self):
        self.disable_filter_check.setChecked(0)
        self.thumb_filter_check.setChecked(0)
        self.bookmark_filter_check.setChecked(0)
        self.hide_input_filter_check.setChecked(0)
        self.search_tab.clear()

    def disabledFilter(self, state):
        for rowList in range(self.node_list_table.rowCount()):
            for columnList in range(self.node_list_table.columnCount()):          
                item = self.node_list_table.cellWidget(rowList,1)
                if state == Qt.Checked:
                    match = "Enabled"  in item.text() 
                    self.node_list_table.setRowHidden(rowList, match)
                else:
                    self.node_list_table.setRowHidden(rowList, 0)

    def thumdnailFilter(self, state):
        try:
            for rowList in range(self.node_list_table.rowCount()):
                for columnList in range(self.node_list_table.columnCount()):          
                    item= self.node_list_table.cellWidget(rowList,4)
                    if state == Qt.Checked:
                        match = "Disabled" in item.text()
                        self.node_list_table.setRowHidden(rowList, match)
                    else:
                        self.node_list_table.setRowHidden(rowList, 0)
        except:
            print ("Attention: Some nodes not 'postage_stamp' knob.")
    
    def bookmarkFilter(self, state):
        try:
            for rowList in range(self.node_list_table.rowCount()):
                for columnList in range(self.node_list_table.columnCount()):          
                    item= self.node_list_table.cellWidget(rowList, 7)
                    if state == Qt.Checked:
                        match = "Disabled" in item.text()
                        self.node_list_table.setRowHidden(rowList, match)
                    else:
                        self.node_list_table.setRowHidden(rowList, 0)
        except AttributeError:
            print ("Attention: Some nodes not 'bookmark' knob.")

    def hideInputFilter(self, state):
        try:
            for rowList in range(self.node_list_table.rowCount()):
                for columnList in range(self.node_list_table.columnCount()):          
                    item= self.node_list_table.cellWidget(rowList, 8)
                    if state == Qt.Checked:
                        match = "Disabled" in item.text()
                        self.node_list_table.setRowHidden(rowList, match)
                    else:
                        self.node_list_table.setRowHidden(rowList, 0)
        except:
            self.hide_input_filter_check.setChecked(0)
            nuke.message('Please "Deselect" Read Nodes or Dots for hide input filter.')
            
    def nodesFilter(self, filterRow):
        for rowList in range(self.node_list_table.rowCount()):
            for columnList in range(self.node_list_table.columnCount()):
                item= self.node_list_table.item(rowList,0)
                #print (item.text().lower())
                match = filterRow.lower() not in item.text().lower()
                self.node_list_table.setRowHidden(rowList, match)
                if not match:
                    break            
    
    def focusSelectedNode(self):
        for n in nuke.allNodes():
            n.setSelected(0)
            nameOfOldSelection = n["name"].getValue()
        currentRow = self.node_list_table.currentRow()
        nodeName = self.node_list_table.item(currentRow,0).text()
        ns = nuke.toNode(nodeName).setSelected(True)
        nuke.zoom(2, [nuke.selectedNode().xpos(), nuke.selectedNode().ypos()])
        for b in nuke.allNodes():
            b.setSelected(1)

    def loadNodeData(self):
            self.node_list_table.setRowCount(len(nuke.selectedNodes()))
            row=0
            for f in nuke.selectedNodes(): #FETCH ALL KNOBS IN MARQUEED NODES...
                knob_dict = {n.name():n.value() for n in f.allKnobs()} 
                self.node_list_table.setItem(row, 0, QTableWidgetItem(str(knob_dict["name"]))) #JUST GET NODE NAME FOR THE FOLLOWING OPERATIONS...
                
    # DISABLE STATEMENT START >>
                if "disable" in knob_dict:
                    disableCheckItem = QCheckBox()
                    disableCheckItem.setFixedWidth(75)
                    if knob_dict["disable"] == False :
                        disableCheckItem.setText("Enabled")                   
                        disableCheckItem.setChecked(0)
                    else:
                        disableCheckItem.setText("Disabled")
                        disableCheckItem.setStyleSheet("background-color: #512f00 ")
                        disableCheckItem.setChecked(1)
                    self.node_list_table.setCellWidget(row, 1, disableCheckItem)
                else:
                    self.node_list_table.setItem(row, 1, QTableWidgetItem(" "))
    # DISABLE STATEMENT FINISH >>
    #
    # POSTAGE_STAMP STATEMENT START >>
                if "postage_stamp" in knob_dict:
                    postageCheckItem = QCheckBox()
                    postageCheckItem.setFixedWidth(75)
                    if knob_dict["postage_stamp"] == False :
                        postageCheckItem.setText("Disabled")                   
                        postageCheckItem.setChecked(0)
                    else:
                        postageCheckItem.setText("Enabled")
                        postageCheckItem.setStyleSheet("background-color: #512f00 ")
                        postageCheckItem.setChecked(1)
                    self.node_list_table.setCellWidget(row, 4, postageCheckItem)
                else:
                    self.node_list_table.setItem(row, 4, QTableWidgetItem(" "))
    # POSTAGE_STAMP STATEMENT FINISH >>
    #
    # MIX STATEMENT START >>
                if "mix" in knob_dict:
                    self.node_list_table.setItem(row, 2, QTableWidgetItem(str(knob_dict["mix"])))
                else:
                    self.node_list_table.setItem(row, 2,  QTableWidgetItem(" "))
                def mixChange():
                    getMixNodeName = self.node_list_table.item(self.node_list_table.currentRow(),0).text()
                    getMixValue = self.node_list_table.item(self.node_list_table.currentRow(), 2).text()
                    nuke.toNode(getMixNodeName)["mix"].setValue(float(getMixValue))
    # MIX STATEMENT END >>
    #
    # LABEL STATEMENT START >>
                if "label" in knob_dict:
                    self.node_list_table.setItem(row, 3, QTableWidgetItem(str(knob_dict["label"])))
                else:
                    self.node_list_table.setItem(row, 3,  QTableWidgetItem(" "))
                def labelChange():
                    getLabelNodeName = self.node_list_table.item(self.node_list_table.currentRow(),0).text()
                    getLabelValue = self.node_list_table.item(self.node_list_table.currentRow(), 3).text()
                    nuke.toNode(getLabelNodeName)["label"].setValue(str(getLabelValue))
    # LABEL STATEMENT END >>
    #
    # COLORSPACE STATEMENT START >>
                if "colorspace" in knob_dict:
                    nukeColorSpaceLut = nuke.root()["monitorLut"].values()
                    colorspaceItem = QComboBox()
                    colorspaceItem.setFixedWidth(85)
                    currentColorspaceItem = [knob_dict["colorspace"]] + nukeColorSpaceLut
                    colorspaceItem.addItems(currentColorspaceItem)
                    self.node_list_table.setCellWidget(row, 5, colorspaceItem)
                else:
                    self.node_list_table.setItem(row, 5,  QTableWidgetItem(" "))
    # COLORSPACE STATEMENT FINISH >>
    #
    # LOCALIZATION STATEMENT START >>
                if "localizationPolicy" in knob_dict:
                    policyItem = QComboBox()
                    currentPolicyItem = [knob_dict["localizationPolicy"], "on", "off", "onDemand","fromAutoLocalizePath"]
                    policyItem.addItems(currentPolicyItem)
                    self.node_list_table.setCellWidget(row, 6, policyItem)
                else:
                    self.node_list_table.setItem(row, 6,  QTableWidgetItem(" "))
    # LOCALIZATION STATEMENT FINISH >>     
    #
    # BOOKMARK STATEMENT START >>
                if "bookmark" in knob_dict:
                    postageCheckItem = QCheckBox()
                    postageCheckItem.setFixedWidth(75)
                    if knob_dict["bookmark"] == False :
                        postageCheckItem.setText("Disabled")                   
                        postageCheckItem.setChecked(0)
                    else:
                        postageCheckItem.setText("Enabled")
                        postageCheckItem.setStyleSheet("background-color: #512f00 ")
                        postageCheckItem.setChecked(1)
                    self.node_list_table.setCellWidget(row, 7, postageCheckItem)
                else:
                    self.node_list_table.setItem(row, 7, QTableWidgetItem(" "))
    # BOOKMARK STATEMENT FINISH >>
    #
    # HIDE_INPUT STATEMENT START >>
                if "hide_input" in knob_dict:
                    postageCheckItem = QCheckBox()
                    postageCheckItem.setFixedWidth(75)
                    if knob_dict["hide_input"] == False :
                        postageCheckItem.setText("Disabled")                   
                        postageCheckItem.setChecked(0)
                    else:
                        postageCheckItem.setText("Enabled")
                        postageCheckItem.setStyleSheet("background-color: #512f00 ")
                        postageCheckItem.setChecked(1)
                    self.node_list_table.setCellWidget(row, 8, postageCheckItem)
                else:
                    self.node_list_table.setItem(row, 8, QTableWidgetItem(" "))
    # HIDE_INPUT STATEMENT FINISH >>
    #
    # LIFETIME STATEMENT START >>
                if "useLifetime" in knob_dict:
                    start_lifetime = knob_dict["lifetimeStart"] 
                    end_lifetime = knob_dict["lifetimeEnd"]
                    all_lifetime = start_lifetime,end_lifetime
                    sk = QLineEdit()
                    
                    #self.node_list_table.setItem(row,9, QTableWidgetItem(str(start_lifetime)+str(end_lifetime)))
                    sk.setPlaceholderText(str(start_lifetime) + " - " + str(end_lifetime))
                    self.node_list_table.setCellWidget(row, 9,sk)
                    
                    self.node_list_table.setItem(row, 9, QTableWidgetItem(str(knob_dict["lifetimeEnd"] )))
                else:
                    self.node_list_table.setItem(row, 9,  QTableWidgetItem("ff "))
                def getLifeTime():
                    getLifeTimeNodeName = self.node_list_table.item(self.node_list_table.currentRow(),0).text()

    # LIFETIME STATEMENT FINISH >>
                row=row+1
    ######################################################################################################################

    # DISABLE / ENABLE SIGNAL-SLOTS -> START >>
            def disableState(stateDisable):
                for dx in stateDisable.indexes():
                    getNodeName = self.node_list_table.item(dx.row(), (int(0)) ).text()
                    def nodeStateCheck(state):  
                        if nuke.toNode(getNodeName)["disable"].value == True:
                            self.node_list_table.cellWidget(dx.row(), (int(1))).setChecked(1)
                        if state == Qt.Checked:
                            nuke.toNode(getNodeName)["disable"].setValue(self.node_list_table.cellWidget(dx.row(), (int(1))).isChecked())
                        else:
                            nuke.toNode(getNodeName)["disable"].setValue(self.node_list_table.cellWidget(dx.row(), (int(1))).isChecked())
                    self.node_list_table.cellWidget(dx.row(), (int(1))).stateChanged.connect(nodeStateCheck)

                    def ifstate (state):#BG COLOR  AND NAME AND iSChecked INFO OF THE NODES
                        if state == Qt.Checked:
                            self.node_list_table.cellWidget(dx.row(), (int(1))).setStyleSheet("background-color: #512f00 ")
                            self.node_list_table.cellWidget(dx.row(), (int(1))).setText("Disabled")
                        else:
                            self.node_list_table.cellWidget(dx.row(), (int(1))).setStyleSheet("background-color: none ")
                            self.node_list_table.cellWidget(dx.row(), (int(1))).setText("Enabled")
                            
                    self.node_list_table.cellWidget(dx.row(), (int(1))).stateChanged.connect(ifstate)      
    # DISABLE / ENABLE SIGNAL-SLOTS -> END >>
    #
    # POSTAGE_STAMP SIGNAL-SLOTS -> START >>
            def postageState(statePostage):
                for px in statePostage.indexes():
                    getNodeName = self.node_list_table.item(px.row(), (int(0)) ).text()

                    def nodePostageCheck(state):  
                        if nuke.toNode(getNodeName)["postage_stamp"].value == True:
                            self.node_list_table.cellWidget(px.row(), (int(4))).setChecked(1)
                        if state == Qt.Checked:
                            nuke.toNode(getNodeName)["postage_stamp"].setValue(self.node_list_table.cellWidget(px.row(), (int(4))).isChecked())
                        else:
                            nuke.toNode(getNodeName)["postage_stamp"].setValue(self.node_list_table.cellWidget(px.row(), (int(4))).isChecked())

                    self.node_list_table.cellWidget(px.row(), (int(4))).stateChanged.connect(nodePostageCheck)

                    def ifstate (state):#BG COLOR  AND NAME AND iSChecked INFO OF THE NODES
                        if state == Qt.Checked:
                            self.node_list_table.cellWidget(px.row(), (int(4))).setStyleSheet("background-color: #512f00 ")
                            self.node_list_table.cellWidget(px.row(), (int(4))).setText("Enabled")
                        else:
                            self.node_list_table.cellWidget(px.row(), (int(4))).setStyleSheet("background-color: none ")
                            self.node_list_table.cellWidget(px.row(), (int(4))).setText("Disabled")
                            
                    self.node_list_table.cellWidget(px.row(), (int(4))).stateChanged.connect(ifstate)      
    #POSTAGE_STAMP SIGNAL-SLOTS -> END >>
    #
    #COLORSPACE SIGNAL-SLOTS -> START >>
            def setColorpaceValue(selectedCC):
                for yx in selectedCC.indexes():
                    getReadNodeName = self.node_list_table.item(yx.row(), (int(0)) ).text()
                    try:
                        def changeCCPolicy():
                            nuke.toNode(getReadNodeName)["colorspace"].setValue(self.node_list_table.cellWidget(yx.row(), (int(5))).currentText())
                        self.node_list_table.cellWidget(yx.row(), (int(5))).currentTextChanged.connect(changeCCPolicy)
                    except:
                        AttributeError
    #COLORSPACE SIGNAL-SLOTS -> END >>   

    #LOCALIZATION SIGNAL-SLOTS -> START >>                
            def getCurrentValueLocalize(selectedIndex):
                for ix in selectedIndex.indexes():
                    getReadNodeName = self.node_list_table.item(ix.row(), (int(0)) ).text()
                    try:
                        def changeLocalizationPolicy():
                            nuke.toNode(getReadNodeName)["localizationPolicy"].setValue(self.node_list_table.cellWidget(ix.row(), (int(6))).currentText())
                        self.node_list_table.cellWidget(ix.row(), (int(6))).currentTextChanged.connect(changeLocalizationPolicy)
                    except:
                        AttributeError
    #LOCALIZATION SIGNAL-SLOTS -> FINISH >>      
    #
    #BOOKMARK SIGNAL-SLOTS -> START >>
            def bookmarkState(stateBookmark):
                for px in stateBookmark.indexes():
                    getNodeName = self.node_list_table.item(px.row(), (int(0)) ).text()
                    def nodeBookmark(state):  
                        if nuke.toNode(getNodeName)["bookmark"].value == True:
                            self.node_list_table.cellWidget(px.row(), (int(7))).setChecked(1)
                        if state == Qt.Checked:
                            nuke.toNode(getNodeName)["bookmark"].setValue(self.node_list_table.cellWidget(px.row(), (int(7))).isChecked())
                        else:
                            nuke.toNode(getNodeName)["bookmark"].setValue(self.node_list_table.cellWidget(px.row(), (int(7))).isChecked())
                    self.node_list_table.cellWidget(px.row(), (int(7))).stateChanged.connect(nodeBookmark)
                    def ifstateBookmark (state):#BG COLOR  AND NAME AND iSChecked INFO OF THE NODES
                        if state == Qt.Checked:
                            self.node_list_table.cellWidget(px.row(), (int(7))).setStyleSheet("background-color: #512f00 ")
                            self.node_list_table.cellWidget(px.row(), (int(7))).setText("Enabled")
                        else:
                            self.node_list_table.cellWidget(px.row(), (int(7))).setStyleSheet("background-color: none ")
                            self.node_list_table.cellWidget(px.row(), (int(7))).setText("Disabled")
                            
                    self.node_list_table.cellWidget(px.row(), (int(7))).stateChanged.connect(ifstateBookmark)      
    #BOOKMARK SIGNAL-SLOTS -> END >>
    #
    #HIDE_INPUT SIGNAL-SLOTS -> START >>
            def hide_input(hide_inputBookmark):
                if not self.node_list_table.cellWidget != 0:
                    for px in hide_inputBookmark.indexes():
                        getNodeName = self.node_list_table.item(px.row(), (int(0)) ).text()
                        def nodeHideInput(state):  
                            if nuke.toNode(getNodeName)["hide_input"].value == True:
                                self.node_list_table.cellWidget(px.row(), (int(8))).setChecked(1)
                            if state == Qt.Checked:
                                nuke.toNode(getNodeName)["hide_input"].setValue(self.node_list_table.cellWidget(px.row(), (int(8))).isChecked())
                            else:
                                nuke.toNode(getNodeName)["hide_input"].setValue(self.node_list_table.cellWidget(px.row(), (int(8))).isChecked())
                        self.node_list_table.cellWidget(px.row(), (int(8))).stateChanged.connect(nodeHideInput)
                        def ifstateHI (state):#BG COLOR  AND NAME AND iSChecked INFO OF THE NODES
                            if state == Qt.Checked:
                                self.node_list_table.cellWidget(px.row(), (int(8))).setStyleSheet("background-color: #512f00 ")
                                self.node_list_table.cellWidget(px.row(), (int(8))).setText("Enabled")
                            else:
                                self.node_list_table.cellWidget(px.row(), (int(8))).setStyleSheet("background-color: none ")
                                self.node_list_table.cellWidget(px.row(), (int(8))).setText("Disabled")
                                
                        self.node_list_table.cellWidget(px.row(), (int(8))).stateChanged.connect(ifstateHI)      
    # HIDE_INPUT SIGNAL-SLOTS -> END >>

            # Filter noOp knobs (ff)     
            for rowList in range(self.node_list_table.rowCount()):
                for columnList in range(self.node_list_table.columnCount()):
                    item = self.node_list_table.item(rowList, 9)
                    if "ff" in item.text():
                        self.node_list_table.setRowHidden(rowList, 9)

            if len(nuke.selectedNodes()) == 0 :    
                print ("No node(s) are selected!")
            else:
                self.node_list_table.selectionModel().selectionChanged.connect(bookmarkState)
                self.node_list_table.itemChanged.connect(getLifeTime)
                self.node_list_table.itemChanged.connect(mixChange)
                self.node_list_table.itemChanged.connect(labelChange)
                self.node_list_table.selectionModel().selectionChanged.connect(hide_input)
                self.node_list_table.selectionModel().selectionChanged.connect(disableState)
                self.node_list_table.selectionModel().selectionChanged.connect(postageState)
                self.node_list_table.selectionModel().selectionChanged.connect(setColorpaceValue)
                self.node_list_table.selectionModel().selectionChanged.connect(getCurrentValueLocalize)

    def disable_enable(self, state):
        ns = nuke.selectedNodes()
        if state == Qt.Checked:
            for i in  ns:
                if i.knob("disable"):
                    i["disable"].setValue(1)
                    print (i.knob("name").value(), "= Disabled")
                else:
                    print (i.knob("name").value(), "= Disble not found")
        else:
            for i in  ns:
                if i.knob("disable"):
                    i["disable"].setValue(0)
                    print (i.knob("name").value(), "= Enabled")
                else:
                    print (i.knob("name").value(), "= Disble not found")
        
    def setBookmark(self, state):
        ns = nuke.selectedNodes()
        if state == Qt.Checked:
            for i in  ns:
                if i.knob("bookmark"):
                    i["bookmark"].setValue(1)
                    print (i.knob("name").value(), "= Bookmark ON")
                else:
                    print (i.knob("name").value(), "= Bookmark not found")
        else:
            for i in  ns:
                if i.knob("bookmark"):
                    i["bookmark"].setValue(0)
                    print (i.knob("name").value(), "= Bookmark OFF")
                else:
                    print (i.knob("name").value(), "= Bookmark not found")
                
    def hide_input_def(self, state):
        ns = nuke.selectedNodes()
        if state == Qt.Checked:
            for i in  ns:
                if i.knob("hide_input"):
                    i["hide_input"].setValue(1)
                    print (i.knob("name").value(), "Hide input on")
                else:
                    print(i.knob("name").value(), "Hide input not found")
        else:
            for i in  ns:
                if i.knob("hide_input"):
                    i["hide_input"].setValue(0)
                    print(i.knob("name").value(), "Hide input off")
                else:
                    print(i.knob("name").value(), "Hide input not found")


    def dope_sheet(self, state):
        ns = nuke.selectedNodes()
        if state == Qt.Checked:
            for i in  ns:
                if i.knob("dope_sheet"):
                    i["dope_sheet"].setValue(1)
                    print (i.knob("name").value(), "Dope sheet on")
                else:
                    print(i.knob("name").value(), "Dope sheet not found")
        else:
            for i in  ns:
                if i.knob("dope_sheet"):
                    i["dope_sheet"].setValue(0)
                    print (i.knob("name").value(), "Dope sheet off")
                else:
                    print(i.knob("name").value(), "Dope sheet not found")
    
    def postage_stamp(self, state):
        ns = nuke.selectedNodes()
        if state == Qt.Checked:
            for i in  ns:
                if i.knob("postage_stamp"):
                    i["postage_stamp"].setValue(1)
                    print (i.knob("name").value(), "Postage stamp on")
                else:
                    print (i.knob("name").value(), "Postage stamp not found")
        else:
            for i in  ns:
                if i.knob("postage_stamp"):
                    i["postage_stamp"].setValue(0)
                    print (i.knob("name").value(), "Postage stamp off")
                else:
                    print (i.knob("name").value(), "Postage stamp not found")


    def uselifetime_state(self, state):
        ns = nuke.selectedNodes()
        if state == Qt.Checked:
            for i in  ns:
                if i.knob("useLifetime"):
                    i["useLifetime"].setValue(1)
                    print (i["name"].getValue(), i["useLifetime"].value()) 
                    self.lifetime_in_frame.setEnabled(1)
                    self.lifetime_out_frame.setEnabled(1)
                else:
                    print (i.knob("name"), "Lifetime not found.")
        else:
            for i in  ns:
                if i.knob("useLifetime"):
                    i["useLifetime"].setValue(0)
                    print (i["name"].getValue(), i["useLifetime"].value())
                    self.lifetime_in_frame.setEnabled(0)
                    self.lifetime_out_frame.setEnabled(0)
                else:
                    print (i.knob("name"), "Lifetime not found.")

        
    def close_event(self):
            self.close()
    
    def startLifetime(self):
        getStartTime = self.lifetime_in_frame.text()
        ns = nuke.selectedNodes()
        for startTime in ns:
            if startTime.knob("lifetimeStart"):
                startTime["lifetimeStart"].setValue(float(getStartTime))
            else:
                AttributeError

            
    def endLifetime(self):
        getEndTime = self.lifetime_out_frame.text()
        ns = nuke.selectedNodes()
        for startTime in ns:
            if startTime.knob("lifetimeEnd"):
                startTime["lifetimeEnd"].setValue(float(getEndTime))
            else:
                AttributeError

    def resetLifetimeSettings(self):
        ns = nuke.selectedNodes()
        for i in  ns:
            if i.knob("useLifetime"):
                i["useLifetime"].setValue(0)
                self.lifetime_in_frame.setEnabled(0)
                self.lifetime_out_frame.setEnabled(0)
        self.lifetime_in_frame.clear()
        self.lifetime_out_frame.clear()
        self.use_lifetime.setChecked(False)

    def appendLabelToNode(self):
        getLabelText = self.label_input_text.toPlainText()
        knob_dict_stack = {n.name():n.value() for n in nuke.selectedNode().allKnobs()} 
        ns = nuke.selectedNodes()
        if "label" in knob_dict_stack:
            for startTime in ns:
                startTime["label"].setValue(getLabelText)
        else:
            print ("Please select supported nodes!.")

    def changeNodeColor(self):
        getColor = nuke.getColor()
        knob_dict_stack = {n.name():n.value() for n in nuke.selectedNode().allKnobs()} 
        ns = nuke.selectedNodes()
        if "tile_color" in knob_dict_stack:
            for startTime in ns:
                startTime["tile_color"].setValue(getColor)
        else:
            print ("Please select supported nodes!.")

def start():
    if len(nuke.selectedNodes()) == 0:
        nuke.message("please select nodes!")
    else:
        start.form = nodes_operator()
  
        start.form.show()
    

    
