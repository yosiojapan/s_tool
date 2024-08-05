# TRS_CopyPaste

## summary

`TRS_CopyPaste` is a MEL script that copies the position, rotation, and scale (TRS) of selected nodes to other nodes.  
This script is useful for copying TRS data within a specific frame range of an animation.

## usage rules

After executing the script, the following window will appear

### Window Configuration

- **getRange button**: retrieve the start and end frames of the playback range.
- **startFrame button**: set the start frame.
- **endFrame button**: sets the end frame.
- **Interval slider**: set the frame interval.
- **source button**: selects the source node.
- **target button**: selects the destination node.
- **Maintainoffset checkbox**: set whether or not the offset is maintained.
- **translate checkbox**: Sets whether the position is copied or not.
- **rotate checkbox**: Sets whether the rotation is copied.
- **scale checkbox**: Sets whether to copy scale.
- **RangeCopy button**: Copies TRS data in the specified range.

## Notes

- Save the file before executing.
- Before executing the script, be sure to select the correct source and destination nodes.
- Set the frame range and frame spacing appropriately.
