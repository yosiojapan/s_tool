# yjp_ModelCheck manual

The following text is a machine translation.

## summary

`ModelCheck` is a MEL script for checking models in Maya.  
This script checks the model history, duplicate node names, unwanted nodes, texture settings,  
joints left/right misalignment, etc., and lists errors.

## usage rules

### Running Scripts

1. run the script S_TOOL > Modeling > `ModelCheck`.
2. When the script is executed, a window for model checking appears.

### Window Operations

- `ymc File folder` : Select the YMC file containing the check rules.
- `Check` : Perform model checks.
- `Allow selected errors` : Add the selected errors to the allow list.  
It is recorded in the scene in the note of the `_ModelCheck` node.
- `Reset allowed errors` : Delete the entire permit list.
- `ymc Save` : Saves the current settings to a YMC file.

### edit section

- `Pre-treatment MEL` : Enter the MEL script to run before checking. Separate with `;`.
- `Post-processing MEL` : Enter the MEL script to run after the check. Separate with `;`.
- `Delete node name` : Enter the name of the node to be deleted. Separate by `,`.
- `Delete Type` : Enter the node type to be deleted.
- `Delete plugin` : Enter the plugins to be deleted. Separate by `,`.
- `Required Joints` : Enter required joints. Separate by `,`.
- `Unchecked node` : Enter nodes not to be checked. Separate by `,`.
- `Required group node` : Enter the required group nodes. Separate by `,`.
- `Required Locator` : Enter the required locators. Separate by `,`.
- `Required Mesh` : Enter the required meshes. Separate by `,`.
- `Mesh Prefixes` : Enter the mesh prefix.
- `Mesh suffix` : Enter the mesh suffix.
- `Material Prefixes` : Enter the material prefix.
- `Material suffix` : Enter the material suffix.
- `Texture type` : Enter the texture type. Separate by `,`.
- `Texture size type` : Enter the texture size type. Separate by `,`.
- `Joint Prefix` : Enter the prefix of the joint.
- `Joint Suffix` : Enter the suffix of the joint.
- `JointRoot` : Enter the joint route.
- `Maximum number of joints` : Enter the maximum number of joints.
- `Non-binding joints` : Enter non-binding joints. Separate them with `,`.
- `Symmetry Check L` : Enter a symmetry check for the left side, e.g., L.
- `Symmetry Check R` : Enter the right symmetry check, e.g. R.
- `segmentScaleCompensate` : turn on or off segment scale compensation.

### error log

- `error log list` : Errors in the check result will be listed. You can select an error to view the details.

## Function Description

### yjp_HistoryCheck

Check the history of the specified object to see if there is any unwanted history.

### yjp_doModelCheck

Run a model check and list errors.

### yjp_ModelCheckPermit

Add the selected errors to the allow list.

### yjp_ModelCheckSave

Saves the current settings to a YMC file.

### yjp_ModelCheckYMCLoad

Load settings from a YMC file.

### yjp_ModelCheck

Displays a window for model checking.

## precautions

- Be sure to save the scene you are working on before executing the script.
- Note that the execution of the script may delete nodes in the scene.
