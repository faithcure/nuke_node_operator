# Node(s) Operator (Spread Sheet) for NUKE BETA*
___

### Node Operator [Spread Sheet] Specifications:

NODE SETTINGS TAB
Change the values of all or selected Nodes knobs at once.
Set labels and colors of all or selected Nodes at once.
Listing the selected Nodes in order and making the desired settings in the table.
Ability to quickly reach the Node(s) sought in a corrupted or complex flow.
Simple Node search/filter feature.

----
READ NODE TAB
Changing settings specific to Read Nodes only.
Ability to change the values of all or selected Read Nodes at once.
The ability to see the metadata of sequences or encodes (Resolution, Size, Created Date-Time, ifLocalized, extension, etc.) and explore.
Check Warning of the all Nodes. [Dir Check]

----
WRITE NODE TAB
Comprehensive Write node creation capability.
Creating a write node suitable for the set project or your own pipeline.
Ability to create write nodes for Mattes.
Personal write node creation feature.
Ability to navigate to the selected Write node directory.

-----
EXPRESSIONS AND GENERAL INFO TAB
Ready to use animation expressions. [TCL Expressions]
Displaying features such as node count, read-write number indicator, project path, project name etc...
See performance profiling features such as processor and ram to use.
Performance timers features. 

... and more to be published very soon.
I will also consider any requests you want to add.
Thank you for your interest.
This script will you make your job little bit easer. 

HOW TO INSTALL
---
#### If you have existing "menu.py" or "init.py" please dont touch them! or clone and save.

Just do this:

```python
# creating menu.py file for the Nuke plugin path like; .nuke
import nuke
import node_operator_main_v01
import importlib

toolbar = nuke.menu("Nodes")
i = toolbar.addMenu("Studio")
# reload node operator
def start_NOP():
    importlib.reload(node_operator_main_v01)
    node_operator_main_v01.start()
i.addCommand("Node Operator v0.1", "start_NOP()")
```
    
If you have existing **"init.py"** file please open it and put the following codes. So, there is no **"init.py"** file please copy and past into **".nuke"** folder directly. :
```python
# adding the plugin path in to init.py
import nuke
import os
nuke.pluginAddPath('nodes_operator')
```
You can create/use your own menu! 
The reload proccess reload again node operator window. When you are change anything in the code just reload script. No reStart the nuke everytime.
___

HOW TO USE
---
Video tutorial is coming soon.

