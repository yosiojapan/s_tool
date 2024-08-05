# yjp_PoseCopyPaste manual

The following text is a machine translation.

## summary

`PoseCopyPaste` is a MEL primarily for copying and pasting poses in sRig.  
It provides the ability to select a character's rig controller and save and load poses.

## usage rules

### Window Operations

When the script is executed, a window appears for copying and pasting poses.

### Window Configuration

- `Path Field` : Specify the path of the folder where the pose data will be saved.
- `Recent Paths` : You can choose from a list of recently used paths.
You can paste the same structure saved in other projects as long as it has the same name. Example: hand pose transplant
- `Selection Type` : All objects, selected objects, or objects in a hierarchy.
- `Option` : There are check boxes for meshes, joints, curves, groups, locators, visibility, and UV animation.
- `Paste Type` : Choose to paste in local or world coordinate system.
- `Each Button` : There are buttons for saving poses and selecting all controllers.

### Save Pose

1. Click the Save Pose button.
2. A dialog box for entering a name for the pose will appear. Enter a name and press OK.
3. Pose data is saved in the specified path.
4. Captured images of views are also saved and thumbnails are added.

### Paste Pose

1. Select the pose you wish to paste from the list of saved thumbnails.
2. The selected pose is applied to the current scene.

### Function when right-clicking on a thumbnail

- `Replace` : Overwrites the selected thumbnail.
- `Symmetry` : This is an sRig-only feature.  
A symmetrical pose of the thumbnail pose is created and added to the thumbnail.  
- `Rename` : You can rename saved poses.
- `Delete` : Saved poses can be deleted.

## precautions

- Rig controllers are sorted in hierarchical order to some extent, but in case of abnormalities in pasting, please select in hierarchical order from parent to child.
- If the destination folder for the pose data and the image folder do not exist, they will be created automatically.
