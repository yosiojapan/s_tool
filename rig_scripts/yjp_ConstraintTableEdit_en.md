# ConstraintTableEdit

## Overview

`Constraint Table Edit` is a MEL script designed to simplify the process of setting up multiple constraints.  
 It provides a tool for editing the constraint table and efficiently setting up constraints.

## Key Features

- **Row Addition**: Adds the selected node to the table.
- **Row Insertion**: Inserts a new row at a specified index.
- **Row Selection Addition**: Adds the selected node to the table.
- **Table Import/Export**: Imports the table from a CSV file and exports the table to a CSV file.
- **Text Search**: Searches for text within the table and highlights the corresponding field.
- **Run**: Sets up constraints in bulk based on a CSV file.

## Usage

Running `S_TOOL` > `Rig` > `Constraint Table Edit` displays a window.  
This window includes the following elements.

### Path Settings

- **Path Field**: Specifies the path of the CSV file.
- **Folder Open**: Opens the folder specified by the path.

### Buttons

- **Import Button**: Imports the table from the specified CSV file.
- **Export Button**: Exports the table to a CSV file.
- **Run Button**: Sets up constraints based on the specified CSV file.

### Table Operations

- **Row Addition**: Adds a new row to the table.
- **Row Insertion with Selected Follower**: Adds a new row with the selected node as a follower.
- **Row Addition for All Levels**: Adds all levels of nodes to the table.
- **Row Clear**: Clears the rows of the table.

### Text Search

- **Text Search Field**: Searches for text within the table and highlights the corresponding field.

### Functions Available by Right-Clicking on a Row Field

- **Get**: Enters the selected node into the field.
- **Select**: Selects the node named in the row.
- **Delete**: Deletes the content written in the row.
