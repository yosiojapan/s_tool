# FBXAnimationConvert

## Overview

`FBXAnimationConvert` is a MEL script that outputs the animation information of the selected nodes in FBX format. This script processes information such as visibility, material alpha, texture color gain, and UV animation, and converts it into a format suitable for use in Unity.

## Usage

1. **Node Selection**: Select the node you want to output.
2. **Script Execution**: Execute the `FBXAnimationConvert` command.

## Processing Details

### 1. Node Selection and Duplicate Check

- Get the selected node and check for duplicate node names.

### 2. Deletion of Existing FBXAnimationConvert Nodes

- Delete the existing `FBXAnimationConvert` node and its related nodes.

### 3. Creation of Output Locator

- Create a new `FBXAnimationConvert` group and process the visibility information of the selected node.

### 4. Processing of Material Alpha Information

- Search for Lambert and Phong type materials and process if there is alpha animation.

### 5. Processing of Texture Nodes

- Process the animation information of texture nodes such as color gain and alpha gain.

### 6. Processing of UV Animation

- Process the UV animation information of the `place2dTexture` node.

## Precautions

- If the Scale Factor setting of Unity's FBXImporter is 1, change 100 to 1 in the script.
- Reference nodes are not processed.

## Output Messages

- The progress of each step is output to the console during script execution.
- When the processing is complete, "Animation Conversion Completed" is displayed.
