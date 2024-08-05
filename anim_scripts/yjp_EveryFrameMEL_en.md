# yjp_EveryFrameMEL manual

The following text is a machine translation.

## summary

`yjp_anm_EveryFrameMEL` is a tool for executing a MEL script every frame within a specified frame range. This tool is useful when you need to run a script at every specific frame of an animation.

## usage rules

### Window Operations

1. `S_TOOL` > `Animation` > `EveryFrameMEL` Run and display window

### Frame range setting

1. `startF` : Click the button to set the start frame.
2. `endF` : Click the button to set the end frame.
3. `Interval` : Set the execution interval in the field (default is 0).

### Enter Script

1. `EveryFrameMELtextField` Enter the MEL script you wish to run

### execution

click the `RunMEL` button to execute the script within the specified frame range.

### Other Functions

- Click the `getRange` button to get the current playback range and set it to the start and end frames.
- Click the `Rename` button to save the log file under a different name.
- Select a log file from the `Log` drop-down menu to load the script.

## precautions

- A progress window will appear while the script is running, allowing you to check its progress.
- To interrupt execution, click the Cancel button in the progress window.

## Example

Below is an example of a simple script that selects objects in each frame.

```mel
select -r pSphere1;
```

Enter this script in `EveryFrameMELtextField` and click the `RunMEL` button to select every frame `pSphere1` within the specified frame range.
