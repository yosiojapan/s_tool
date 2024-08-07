# S_TOOL

![Static Badge](https://img.shields.io/badge/Maya-MEL-orange)
![Static Badge](https://img.shields.io/badge/Maya-python-blue)
![License: MIT](https://img.shields.io/badge/license-MIT-blue.svg)

Please note that the following may be difficult to understand due to machine translation.  
[日本語README](./README_ja.md)

## Overview

- This is a Maya tool created through self-study.
- It may have bugs. Please save and run it before use.
- The author assumes no responsibility for any damages or issues arising from the use of this script, so please use it at your own risk.
- The Maya version is 2020. Only BoneDynamics_ui has been tested to work in 2022.
- There are also tools that use MEL and plugins from other creators to increase efficiency.
- Please download other creators' MEL scripts individually.
- There are also old MEL scripts. Some may already exist as Maya's default features.

## Installation Method

- Place the folder in your preferred location
- Run the batch file such as StartMaya2025_sTool.bat with the installed Maya version name.
- When you launch the batch file, the S_TOOL menu will be displayed.

## Scripts to Use

- MEL
- python (in progress)

## Composition

There are tools in each folder.

- `anim_scripts` : Animation related (including sRig)
- `clip_scripts` : Clip related (folder excluded from batch as it's unnecessary)
- `common_scripts` : Miscellaneous MEL scripts
- `DL_scripts` : Place for downloaded MEL scripts
- `file_scripts` : File related MEL scripts
- `joint_scripts` : Joint related
- `material_scripts` : Material related
- `modeling_scripts` : Modeling related
- `module_scripts` : MEL scripts used by multiple MEL scripts. Not used directly.
- `plug-ins` : Place for plugins from masters
  - Please try adding `boneDynamicsNode.mll`, `rotationDriver.py`, `weightDriver.mll`, etc.
- `projects_scripts` : Place for custom MEL scripts
- `py_scripts` : Place for python tools
  - Includes `dwpicker` and `expcol`
- `rig_module_scripts` : MEL scripts for rig. Not used directly.
- `rig_scripts` : Original rig called sRig
- `weight_scripts` : Weight related

## About the Folders

> If not needed, you can delete or rename the folder to only load the necessary MEL scripts.  
However, please do not delete the `module_scripts` and `py_scripts` folders.

If you use `rig_scripts`, you will also use `rig_module_scripts`.

## Function Description

### Modeling

- `Mirror` : Object mirroring and face mirroring can be done
- `VertexSymmetryMove` : Vertex Symmetry [**Readme**](./modeling_scripts/yjp_VertexSymmetryMove_en.md)
- `UVSymmetryMove` : UV vertex mirror
- `VertexSnap`: Snaps the vertices of the next selected object to the first selected object with an approximate value.  
Vertex selection is also OK [**Readme**](./modeling_scripts/yjp_VertexSnap_en.md)
- ~~`VertexSnapPlus` : Select and snap the vertices of two meshes. It also aligns normals and weights. [**Readme**](./modeling_scripts/yjp_VertexSnapPlus_en.md)~~
- `SepalateMaterial` : Separates the faces of the selected object by material unit
- `Construction` : Opens a view to edit the intermediate objects of bound meshes [**Readme**](./modeling_scripts/yjp_Construction_en.md)
- `WorldCenterPivot` : Set the pivot to the world center
- `FreezeChannel` : Keeps the specified coordinates and freezes the transform
- `OutLineObjectCreate` : Creates the outline mesh of the specified object
- `curve_cv_select` : Select the CV of the curve
- `RefreshVertexOfFBX` : Fixes some bugs in the model data of FBX
- `VertexNormalCTRL` : VertexNormalCopyとVertexNormalPasteのUI
- `VertexNormalCopy` : Copy Normals
- `VertexNormalPaste` : Paste Normals
- `ModelCheck` : Checks the data within the model scene [**Readme**](./modeling_scripts/yjp_ModelCheck_en.md)

---

- `mCombine` : Unknown link [**movie**](https://vimeo.com/47843888)

### Texture

- `ChangeTexPathtolocal` : Changes the texture path to a local path
- `UpdateTexturesAuto` : This is a MEL script that reflects texture updates in Maya, but it may not be needed anymore.
~~- UVpattern~~

### Joint

- `RelocationJoint` : Rescales adjusted joints to scale 1.
- `yjp_preferredAngleZero` : Sets the preferredAngle to 0.

---

- `templateSkeletonLE` : Creates and rebuilds joint chains.  
Since the download location is unknown for MEL from the Maya 6.0 era, we will keep it here.
- `cometJointOrient` : Edits the joint orientation MEL  
This one also no longer has a link.  
- LMrigger : cometJointOrient's advanced version [Download here](https://luismiherrera.gumroad.com/l/LMrigger?layout=profile)

### Weight

- `PaintSikinWeightButton` : Weight brush UI. Only switches the weight amount with a button.
- `WeightEdit` : Adjusts the weight per vertex unit with a slider [**Readme**](./weight_scripts/yjp_WeightEdit_en.md)
- `ShellWeight` : Has a bug. Selects connected polygons and binds them to a joint with a weight of 1 when multiple vertices and one joint are selected and executed.
- `VUW_Symmetry` : Weight symmetry [**Readme**](./weight_scripts/yjp_VUW_Symmetry_en.md)
- `yjp_BindPoseCoordinateCheck` : Checks if the bind pose shifts.
- `yjp_SeparateMeshWeight` : Copies the weight if there is a skincluster.
- `yjp_ShellWeight` : Selects connected polygons and binds them to a joint with a weight of 1 when multiple vertices and one joint are selected and executed.
- `DoraSkinWeightImpExp` : MEL that can save and load weights [Download here](http://dorayuki.com/doramaya/doraskinweightimpexp.html)  
Please place `DoraSkinWeightImpExp.mel` in the `DL_scripts` folder.  
Other MEL scripts that use DoraSkinWeightImpExp are as follows:
  - `DuplicateMeshSkin` : Duplicates and maintains weights
  - `CombineMeshSkin` : Merges the selected two objects and their weights
  - `SeparateMeshSkin` : Separates the selected faces and maintains weights
  - `QuickDoraSkinWeightExport` : Saves weights in wds format by object name
  - `QuickDoraSkinWeightImport` : Loads weights by ID after searching for the object name's weights
  - `DetachBindShelf` : Saves bind information and detaches. Rebinds with the object name shelf
  - `ReBind` : Deletes history and rebinding
  - `RebindShelf` : Deletes history, saves to shelf, and rebinding
  - `ImitateBind` : Binds the second selected object with the bind information of the first selected object.
  - `DoraVertexWeightPaste` : Pastes weights to the selected vertices
  - `DoraVertexWeightCopy` : Copies the weights of the selected vertices

### sRig

- `sRig` : Rig creation [**Readme**](./rig_scripts/yjp_sRig_en.md)
- `sRig CTRL Edit` : Edit the curve of the rig controller [**Readme**](./rig_scripts/yjp_sRg_CTRL_Edit_en.md)
- `Loads file and Replace sRigCTRL` : Load a file and replace the rig controller
- ~~`CTRL List` : List of rig controllers. Controller selection tool~~
- `sRig Checker` : Check if there are any errors in the sRig [**Readme**](./rig_scripts/yjp_sRig_rigchecker_en.md)
- `sRig PoseMirror` : Mirror the pose of the sRig controller [**Readme**](./rig_scripts/yjp_poseMirror_en.md)
- `sRig CTRL AllSelect` : Select all character controllers
- `FK to IK` : Convert FKctrl to IKctrl
- `FK to IK AllFrame` : Convert all FKctrl to IKctrl in the timeslider range
- `IK_to_FK` : Convert IKctrl to FKctrl
- `IK to FK AllFrame` : Convert all IKctrl to FKctrl in the timeslider range
- `IK Length Limit 0.0` : Match the controller to the length of the stretched IK joint
- `IK Length Limit 1.0` : Match the controller to the length of the stretched IK joint and bend it a little
- `Constraint Table Edit` : Tool to create a csv file and apply multiple parent constraints [**Readme**](./rig_scripts/yjp_ConstraintTableEdit_en.md)
- `sRig_ConstraintSwitch` : Switch the parent of multiple controllers after selecting them and the timeslider range
  - Switches to the parent set in the rig for each number
- `sRig Motion Check` : Search for errors in the motion created with sRig.

### Animation

- `Pose Copy Paste` : Copies and pastes the pose of the selected node [**Readme**](./anim_scripts/yjp_PoseCopyPaste_en.md)
- `TRS Copy Paste` : Bakes the object to follow another object [**Readme**](./anim_scripts/yjp_TRS_CopyPaste_en.md)
- `Every Frame MEL` : Executes MEL written for every frame [**Readme**](./anim_scripts/yjp_EveryFrameMEL_en.md)
- `Time Offset 0` : Aligns all keys in the scene to frame 0
- `Time Offset UI` : Shifts all keys in the scene
- `FBX Animation Convert` : Transfers alpha animation, UV animation, and visibility animation in the scene to a different node channel. The value is multiplied by 100. [**Readme**](./anim_scripts/yjp_FBXAnimationConvert_en.md)
- `Add Const Node` : Adds a locator to constrain the selected node
- `anim cutOut Of Range` : Deletes keys outside the range selected in the timeline
- `Smooth Curve` : Smooths the keys of the curve
- `Loop Curve` : Adjusts the first and last frames of the curve to create a loop motion
- `Animation Work Tool` : Animation toolset
- `MotionCopy` : Mainly transfers motion to sRig [**Readme**](./anim_scripts/yjp_MotionCopy_en.md)
- `FPS 30` : Sets FPS to 30
- `sRig_GlobalFollow` : Prevents slipping between the ground controller and the ground when the ground controller moves [**Readme**](./anim_scripts/yjp_GlobalFollow_en.md)

---

- `oaSmoothKeys` : Smooths the selected keys [highend3](https://www.highend3d.com/maya/script/oasmoothkeys-for-maya)
- `DWpicker` : Rig Picker [Download Dreamwall Picker here](https://github.com/DreamWall-Animation/dwpicker)
- `BoneDynamics_ui` : A tool that allows for easy addition, editing, baking, saving, and loading using the `boneDynamicsNode` that automates the dynamics. [**Readme**](./py_scripts/bdn/yjp_boneDynamicsNode_ui_en.md)  
[boneDynamicsNode is available for download here](https://github.com/akasaki1211/boneDynamicsNode)  
Place `boneDynamicsNode.mll` in the plug-ins folder.  
[Download maya_expressionCollision from here](https://github.com/akasaki1211/maya_expressionCollision)  
We also place expcol in the py_scripts folder.

### File

- `Open project folder` : Open the project folder
- `Run MEL to MB` : Execute any MEL in sequence across multiple scenes
- `Scene Search` : Execute any MEL in sequence across multiple scenes and investigate
- `MB To MA` : Save mb in the folder as ma
- `FBX To MB` : Save fbx in the folder as mb
- `MA to MB` : Save ma in the folder as mb
- `MB To FBX` : Save mb,ma in the folder as fbx
- `ATOM Export` : ATOM Export

### Etc

- `MEL_LanguageEdit` : Switches the tool description between English and Japanese
- `Cameras follow` : Creates a view that follows the selected node
- `All Back ground Color` : Changes the background color of all cameras in the scene
- `Replaces Word` : Replaces all node names in the scene. Enter the search word on the left and the replacement word on the right
- `Same name node check` : Searches and selects nodes with the same name, including shapes
- `Rename Nodes with the Same Name` : Automatically renames all nodes with the same name in the scene

---

- `View Capture` : ViewCapture
- `Box Capture` : Captures from 6 directions
- `View To Shelf` : Saves the view state to the shelf
- `View Show Custom` : View Edit Window
- `Show all layers` : Displays all layers

---

- `ALL Import Reference` : Import all references in the scene
- `Reference SetAttr Remove` : Remove edited reference information

---

- `Unknown Plugin Delete` : Deletes unused plugins from the scene
- `Window Delete` : Closes most windows

- `Hide Remove Reference` : Deletes all unloaded references
- `Delete Reference` : Checks transform nodes for references and deletes isolated reference nodes
- `Render Layer Delete` : Deletes render layers
- `ReLoadMenu` : Reloads the STOOL menu
- `CleanUp Scene Model` : Optimizes after deleting references, unnecessary plugins, unknown nodes, etc.
- `Node UnLock` : Unlocks all nodes when multiple nodes are selected and executed

### DLscript

## Adding MEL

Make the procedure name and the mel file name the same.  
Place it in the `projects_scripts` folder.  
Then it will be added to the DL_scripts menu.  
If you want to add a MEL with arguments, please place it in the `module_scripts` folder.

## License

- Please refer to the License file.

## Support

Support is not available in general.

As of 2024/8/1, I will be leaving Maya, so the next revision date is undecided.
