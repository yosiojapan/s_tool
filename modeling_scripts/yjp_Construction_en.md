# Construction

## Overview

`Construction` is a tool to edit the intermediate model of a selected mesh object.
Using a dedicated view camera, you can edit only the movement of vertices while moving the bound model.

## usage rules

1. Select Mesh Object

2. Run the script : S_TOOL > Modeling > Construction

3. Window

- After executing the script, a new window will appear.
- Clicking the "Position change" button in the window changes the Y position of the joint.
- Clicking the "Close" button closes the window and resets the settings.
- Only move vertices in the window should be edited.

## Details of Functions

- `Processing selected objects` :
  - Checks if the selected mesh objects have skin clusters, and if not, removes them from the list.
  - Set backface culling for each object.

- `Set Display Layer` :
  - Creates a temporary display layer and adds selected objects to it.
  - Create a new display layer and add objects to it, if necessary.

- `View Camera Setup` :
  - Duplicates the view camera and displays it in the window.
  - Show selected objects and fit the view.

## Notes

- `Selected Objects` :
  - Always select mesh objects before running the script.
  - Only objects with skin clusters will be processed.

## Troubleshooting

- `Error message` :
  
  - Please select a mesh": displayed if no mesh object is selected.
  - Select an object with intermediate objects": displayed if an object with skin clusters is not selected.

- `Problem with display layer` :

  - If objects are not added to the display layer, re-run the script.

## Additional Information

- `Related Procedures` :.
  - `yjp_constructionHide` : hides the intermediate object and removes the layer.
  - `yjp_constructionPosChange` : change the Y position of a joint.
