def loadNodeData(self):
        import nuke
        self.node_list_table.setRowCount(len(nuke.selectedNodes()))
        row=0
        for f in nuke.selectedNodes(): #FETCH ALL KNOBS IN MARQUEED NODES...
            knob_dict = {n.name():n.value() for n in f.allKnobs()} 
            self.node_list_table.setItem(row, 0, QTableWidgetItem(str(knob_dict["name"]))) #JUST GET NODE NAME FOR THE FOLLOWING OPERATIONS...
                    
#DISABLE STATEMENT START >>
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
#DISABLE STATEMENT FINISH >>
#
#POSTAGE_STAMP STATEMENT START >>
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
#POSTAGE_STAMP STATEMENT FINISH >>
#
#MIX STATEMENT START >>
            if "mix" in knob_dict:
                self.node_list_table.setItem(row, 2, QTableWidgetItem(str(knob_dict["mix"])))
            else:
                self.node_list_table.setItem(row, 2,  QTableWidgetItem(" "))
            def mixChange():
                getMixNodeName = self.node_list_table.item(self.node_list_table.currentRow(),0).text()
                getMixValue = self.node_list_table.item(self.node_list_table.currentRow(), 2).text()
                nuke.toNode(getMixNodeName)["mix"].setValue(float(getMixValue))
#MIX STATEMENT END >>
#
#LABEL STATEMENT START >>
            if "label" in knob_dict:
                self.node_list_table.setItem(row, 3, QTableWidgetItem(str(knob_dict["label"])))
            else:
                self.node_list_table.setItem(row, 3,  QTableWidgetItem(" "))
            def labelChange():
                getLabelNodeName = self.node_list_table.item(self.node_list_table.currentRow(),0).text()
                getLabelValue = self.node_list_table.item(self.node_list_table.currentRow(), 3).text()
                nuke.toNode(getLabelNodeName)["label"].setValue(str(getLabelValue))
#LABEL STATEMENT END >>
#
#COLORSPACE STATEMENT START >>
            if "colorspace" in knob_dict:
                nukeColorSpaceLut = nuke.root()["monitorLut"].values()
                colorspaceItem = QComboBox()
                colorspaceItem.setFixedWidth(85)
                currentColorspaceItem = [knob_dict["colorspace"]] + nukeColorSpaceLut
                colorspaceItem.addItems(currentColorspaceItem)
                self.node_list_table.setCellWidget(row, 5, colorspaceItem)
            else:
                self.node_list_table.setItem(row, 5,  QTableWidgetItem(" "))
#COLORSPACE STATEMENT FINISH >>
#
#LOCALIZATION STATEMENT START >>
            if "localizationPolicy" in knob_dict:
                policyItem = QComboBox()
                currentPolicyItem = [knob_dict["localizationPolicy"], "on", "off", "onDemand","fromAutoLocalizePath"]
                policyItem.addItems(currentPolicyItem)
                self.node_list_table.setCellWidget(row, 6, policyItem)
            else:
                self.node_list_table.setItem(row, 6,  QTableWidgetItem(" "))
#LOCALIZATION STATEMENT FINISH >>     
#
#BOOKMARK STATEMENT START >>
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
#BOOKMARK STATEMENT FINISH >>
#
#HIDE_INPUT STATEMENT START >>
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
#HIDE_INPUT STATEMENT FINISH >>
#
#LIFETIME STATEMENT START >>
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
                lifeTimeStart = nuke.toNode(getLifeTimeNodeName)["lifetimeStart"].value()
                lifeTimeEnd = nuke.toNode(getLifeTimeNodeName)["lifetimeEnd"].value()
        

#LIFETIME STATEMENT FINISH >>
            row=row+1
######################################################################################################################

#DISABLE / ENABLE SIGNAL-SLOTS -> START >>
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
#DISABLE / ENABLE SIGNAL-SLOTS -> END >>
#
#POSTAGE_STAMP SIGNAL-SLOTS -> START >>
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
#HIDE_INPUT SIGNAL-SLOTS -> END >>
            
        self.node_list_table.selectionModel().selectionChanged.connect(bookmarkState)
        self.node_list_table.itemChanged.connect(getLifeTime)
        self.node_list_table.itemChanged.connect(mixChange)
        self.node_list_table.itemChanged.connect(labelChange)
        self.node_list_table.selectionModel().selectionChanged.connect(hide_input)
        self.node_list_table.selectionModel().selectionChanged.connect(disableState)
        self.node_list_table.selectionModel().selectionChanged.connect(postageState)
        self.node_list_table.selectionModel().selectionChanged.connect(setColorpaceValue)
        self.node_list_table.selectionModel().selectionChanged.connect(getCurrentValueLocalize)
