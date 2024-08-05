# yjp_VertexSnap

## Overview

`yjp_VertexSnap` is a MEL script for snapping selected vertices.  
This script can either average the position of selected vertices or snap to the position of the first vertex.  
It also provides an option to select vertices on border edges.

### Process Flow

1. retrieve the selected object or vertex.
2. if the option to select border edge vertices is enabled, retrieve the border edge vertices.
3. get the position of each vertex, compare it to the other vertices, and perform snap processing if the positions match within the specified threshold.
4. snap processing can either average the vertex position or move it to the first vertex position.

## UI Configuration

- Average : checkbox: selects if the vertex position is averaged or not.
- BorderEdge : checkbox: select whether to select the vertices of the border edge.
- Threshold : field: set the threshold for comparing vertex positions.
- Apply : button: to apply the snap process.
- Close : button: closes the window.

## HOW TO USE

1. run `S_TOOL` > `Modeling` > `VertexSnap` to display the UI.
Set checkboxes and threshold fields as needed.
Click the `Apply` button to perform the snap process.
When the process is complete, click the `Close` button to close the window.

### `yjp_VertexSnap`

This function creates a user interface and provides a button to perform the snap process.

## Notes

- Before executing the script, you must select the vertices you want to snap.
- If the option to select border edge vertices is enabled, only the border edge vertices of the selected object will be snapped to.
