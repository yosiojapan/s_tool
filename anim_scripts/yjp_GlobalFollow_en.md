# GlobalFollow

## Overview

`GlobalFollow` is a MEL script used to prevent slipping between the feet and the ground when creating animations in Maya.  
It is used for rigs created with sRig. It adjusts the positional relationship between the selected foot controller and ground controller and sets keys within the specified frame range.

## Usage

1. Select the **foot controller**.
2. Next, select the **ground controller**.
3. Run the script and open the window.
4. Set the start and end frames.
5. Optionally, select the translation axes (tX, tY, tZ).
6. Click the `Follow` button to run the script.

## Interface

- **start**: Sets the current frame as the start frame.
- **end**: Sets the current frame as the end frame.
- **Interval**: Sets the interval of keyframes.
- **tX, tY, tZ**: Selects the translation axes.
- **Follow**: Runs the script and sets keys.

## Precautions

- Please ensure that the foot controller and ground controller are correctly selected before running the script.
- Keys are set within the selected frame range, so please check the range.
