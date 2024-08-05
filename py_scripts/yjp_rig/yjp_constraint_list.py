# -*- coding: utf-8 -*-

"""!
Maya Constraint Table

2024/3/12 edit
"""

import maya.cmds as cmds
import maya.mel as mel
import os
import csv
import os.path
import sys

def edit_cell(row, column, value):
    return 1

def add_row(*args):
    last_row_num = cmds.scriptTable('table', query=True, rows=True)
    cmds.scriptTable('table', edit=True,insertRow=last_row_num)

def delete_row(*args):
    last_row_num = cmds.scriptTable('table', query=True, rows=True)
    cmds.scriptTable('table', edit=True,deleteRow=last_row_num - 1)

def insert_add_row(*args):
    try:
        selected_row = cmds.scriptTable('table', query=True, selectedRows=True)[0]
        if selected_row == None:
            print ('Select Row to Insert')
        else:
            cmds.scriptTable('table', edit=True,insertRow=selected_row)
    except:
        print ('Select Row to Insert')

def delete_sel_row(*args):
    try:
        selected_row = cmds.scriptTable('table', query=True, selectedRows=True)[0]
        if selected_row == None:
            print ('Select Row to Delete')
        else:
            cmds.scriptTable('table', edit=True,deleteRow=selected_row)
    except:
        print ('Select Row to Delete')
        
def set_sel1(*args):
    if not cmds.ls( selection=True ):
        print ('Select Object to List')
    else:
        selected_obj = cmds.ls( sl=True )[0]
        selected_row = cmds.scriptTable('table', query=True, selectedRows=True)
        if selected_row == None:
            print ('Select Row to List')
        else:
            selected_row = cmds.scriptTable('table', query=True, selectedRows=True)[0]
            cmds.scriptTable('table', edit=True, selectedCells=[selected_row,1])
            cmds.scriptTable('table', cellIndex=(selected_row,1), edit=True, cellValue=selected_obj)
            cmds.scriptTable('table', edit=True, selectedRows=selected_row)

def set_sel2(*args):
    if not cmds.ls( selection=True ):
        print ('Select Object to List')
    else:
        selected_obj = cmds.ls( sl=True )[0]
        selected_row = cmds.scriptTable('table', query=True, selectedRows=True)
        if selected_row == None:
            print ('Select Row to List')
        else:
            selected_row = cmds.scriptTable('table', query=True, selectedRows=True)[0]
            cmds.scriptTable('table', edit=True, selectedCells=[selected_row,2])
            cmds.scriptTable('table', cellIndex=(selected_row,2), edit=True, cellValue=selected_obj)
            cmds.scriptTable('table', edit=True, selectedRows=selected_row)

def set_sel3a(*args):
    selected_row = cmds.scriptTable('table', query=True, selectedRows=True)
    if selected_row == None:
        print ('Select Row to List')
    else:
        constaint_mode = 'Point'
        selected_row = cmds.scriptTable('table', query=True, selectedRows=True)[0]
        cmds.scriptTable('table', edit=True, selectedCells=[selected_row,3])
        cmds.scriptTable('table', cellIndex=(selected_row,3), edit=True, cellValue=constaint_mode)
        cmds.scriptTable('table', edit=True, selectedRows=selected_row)

def set_sel3b(*args):
    selected_row = cmds.scriptTable('table', query=True, selectedRows=True)
    if selected_row == None:
        print ('Select Row to List')
    else:
        constaint_mode = 'Parent'
        selected_row = cmds.scriptTable('table', query=True, selectedRows=True)[0]
        cmds.scriptTable('table', edit=True, selectedCells=[selected_row,3])
        cmds.scriptTable('table', cellIndex=(selected_row,3), edit=True, cellValue=constaint_mode)
        cmds.scriptTable('table', edit=True, selectedRows=selected_row)

def set_sel3c(*args):
    selected_row = cmds.scriptTable('table', query=True, selectedRows=True)
    if selected_row == None:
        print ('Select Row to List')
    else:
        constaint_mode = 'Orient'
        selected_row = cmds.scriptTable('table', query=True, selectedRows=True)[0]
        cmds.scriptTable('table', edit=True, selectedCells=[selected_row,3])
        cmds.scriptTable('table', cellIndex=(selected_row,3), edit=True, cellValue=constaint_mode)
        cmds.scriptTable('table', edit=True, selectedRows=selected_row)

def set_sel3d(*args):
    selected_row = cmds.scriptTable('table', query=True, selectedRows=True)
    if selected_row == None:
        print ('Select Row to List')
    else:
        constaint_mode = 'Scale'
        selected_row = cmds.scriptTable('table', query=True, selectedRows=True)[0]
        cmds.scriptTable('table', edit=True, selectedCells=[selected_row,3])
        cmds.scriptTable('table', cellIndex=(selected_row,3), edit=True, cellValue=constaint_mode)
        cmds.scriptTable('table', edit=True, selectedRows=selected_row)

def set_sel4a(*args):
    selected_row = cmds.scriptTable('table', query=True, selectedRows=True)
    if selected_row == None:
        print ('Select Row to List')
    else:
        offset_mode = '0'
        selected_row = cmds.scriptTable('table', query=True, selectedRows=True)[0]
        cmds.scriptTable('table', edit=True, selectedCells=[selected_row,4])
        cmds.scriptTable('table', cellIndex=(selected_row,4), edit=True, cellValue=offset_mode)
        cmds.scriptTable('table', edit=True, selectedRows=selected_row)

def set_sel4b(*args):
    selected_row = cmds.scriptTable('table', query=True, selectedRows=True)
    if selected_row == None:
        print ('Select Row to List')
    else:
        offset_mode = '1'
        selected_row = cmds.scriptTable('table', query=True, selectedRows=True)[0]
        cmds.scriptTable('table', edit=True, selectedCells=[selected_row,4])
        cmds.scriptTable('table', cellIndex=(selected_row,4), edit=True, cellValue=offset_mode)
        cmds.scriptTable('table', edit=True, selectedRows=selected_row)

def load_csv(*args):

    tmp_csv_filename = cmds.workspace( q=True, rd=True )

    multipleFilters = "All Files (*.*)"
    import_filename = cmds.fileDialog2(fileMode=1,fileFilter=multipleFilters,
        dialogStyle=2,startingDirectory=tmp_csv_filename,caption=' CSV file')

    if import_filename:
        cmds.textFieldButtonGrp('load_csv', edit=True, text=import_filename[0])

        o_file = open(import_filename[0], 'r')
        reader = csv.reader(o_file)
        header = next(reader)

        row_no = 1
        for row in reader:
            if row_no > 3:
                cmds.scriptTable('table', edit=True,insertRow=row_no)

            cmds.scriptTable('table', cellIndex=(row_no,1), edit=True, cellValue=row[0])
            cmds.scriptTable('table', cellIndex=(row_no,2), edit=True, cellValue=row[1])
            cmds.scriptTable('table', cellIndex=(row_no,3), edit=True, cellValue=row[2])
            cmds.scriptTable('table', cellIndex=(row_no,4), edit=True, cellValue=row[3])
            cmds.scriptTable('table', cellIndex=(row_no,5), edit=True, cellValue=row[4])
            cmds.scriptTable('table', cellIndex=(row_no,6), edit=True, cellValue=row[5])
            cmds.scriptTable('table', cellIndex=(row_no,7), edit=True, cellValue=row[6])
            row_no = 1 + row_no

        o_file.close()

def output_to_cvs(*args):
    o_namespace = cmds.textField('c_namespace',q=True,text=True)
    
    n_namespace = ""
    if o_namespace != "":
        n_namespace = o_namespace + ':'

    s_namespace = cmds.textField('d_namespace',q=True,text=True)
    m_namespace = ""
    if s_namespace != "":
        m_namespace = s_namespace + ':'

    csv_file = cmds.textFieldButtonGrp('load_csv',q=True,text=True)

    if not (cmds.file(csv_file,query=True, exists=True)):
        tmp_csv_file = open(csv_file, 'w' ,os.O_CREAT)
    else:
        tmp_csv_file = open(csv_file, 'w')
    writer = csv.writer(tmp_csv_file, lineterminator='\n')

    all_rows = cmds.scriptTable('table', query=True, rows=True)
    for o_r in range(all_rows):
        
        all_colums = cmds.scriptTable('table', query=True, columns=True)
        data_list = []
        for o_c in range( all_colums - 1):
            if o_r == 0:
                data_list = ["SourceNodeName", "DestinationNodeName", "Constrain","MaintainOffset"]
            else:
                cell_list = cmds.scriptTable('table', cellIndex=(o_r,o_c + 1), query=True, cellValue=True)
                if o_c == 0:
                    if type(cell_list) == list:
                        cell_text = n_namespace + "".join(cell_list)
                        print (cell_text)
                    elif cell_list == None:
                        cell_text = u''
                    else:
                        cell_text = cell_list
                    data_list.append(cell_text)
                elif o_c == 1:
                    if type(cell_list) == list:
                        cell_text = m_namespace + "".join(cell_list)
                    elif cell_list == None:
                        cell_text = u''
                    else:
                        cell_text = cell_list
                    data_list.append(cell_text)
                else:
                    if type(cell_list) == list:
                        cell_text = "".join(cell_list)
                    elif cell_list == None:
                        cell_text = u''
                    else:
                        cell_text = cell_list
                    data_list.append(cell_text)
        writer.writerow(data_list)

    tmp_csv_file.close()


def do_constraint(*args):

    try:
        o_namespace = cmds.textField('c_namespace',q=True,text=True)
        n_namespace = ""
        if o_namespace != "":
            n_namespace = o_namespace + ':'

        s_namespace = cmds.textField('d_namespace',q=True,text=True)
        m_namespace = ""
        if s_namespace != "":
            m_namespace = s_namespace + ':'

        last_row_num = cmds.scriptTable('table', query=True, rows=True)
        row_no = 1
        for row in range( last_row_num - 1):
            o_sname = cmds.scriptTable('table', cellIndex=(row_no,1), q=True, cellValue=True)[0]
            o_dname = cmds.scriptTable('table', cellIndex=(row_no,2), q=True, cellValue=True)[0]
            o_conmodel = cmds.scriptTable('table', cellIndex=(row_no,3), q=True, cellValue=True)[0]
            o_offmodel = cmds.scriptTable('table', cellIndex=(row_no,4), q=True, cellValue=True)[0]

            if o_sname == "" or o_dname == "" or o_conmodel == "" or o_offmodel == "":
                cmds.confirmDialog( title='ERROR', message='No Node Name to Set !_! ')
                break
            else:
                if o_conmodel == 'Point':
                    o_conmodel_t = 'pointConstraint'
                elif o_conmodel == 'Orient':
                    o_conmodel_t = 'orientConstraint'
                elif o_conmodel == 'Parent':
                    o_conmodel_t = 'parentConstraint'
                elif o_conmodel == 'Scale':
                    o_conmodel_t = 'scaleConstraint'

                if o_offmodel == '0':
                    o_offmodel_t = 'False'
                    if o_conmodel == 'Parent':
                        if cmds.pointConstraint(m_namespace + o_dname,q=True) != None:
                            cmds.pointConstraint(n_namespace + o_sname,m_namespace + o_dname,edit=True,remove=True)
                        if cmds.orientConstraint(m_namespace + o_dname,q=True) != None:
                            cmds.orientConstraint(n_namespace + o_sname,m_namespace + o_dname,edit=True,remove=True)

                        do_const = "cmds." + o_conmodel_t + "('"+ n_namespace + o_sname +"','" + m_namespace + o_dname + "',maintainOffset=False)"
                        exec (do_const)

                    elif o_conmodel == 'Point':
                        if cmds.orientConstraint(m_namespace + o_dname,q=True) != None:
                            cmds.orientConstraint(n_namespace + o_sname,m_namespace + o_dname,edit=True,remove=True)
                        if cmds.parentConstraint(m_namespace + o_dname,q=True) != None:
                            cmds.parentConstraint(n_namespace + o_sname,m_namespace + o_dname,edit=True,remove=True)

                        o_off_x = cmds.scriptTable('table', cellIndex=(row_no,5), q=True, cellValue=True)[0]
                        if o_off_x == '':
                            o_off_x_t = '0.0000'
                        else:
                            o_off_x_t = str(o_off_x)

                        o_off_y = cmds.scriptTable('table', cellIndex=(row_no,6), q=True, cellValue=True)[0]
                        if o_off_y == '':
                            o_off_y_t = '0.0000'
                        else:
                            o_off_y_t = str(o_off_y)

                        o_off_z = cmds.scriptTable('table', cellIndex=(row_no,7), q=True, cellValue=True)[0]
                        if o_off_z == '':
                            o_off_z_t = '0.0000'
                        else:
                            o_off_z_t = str(o_off_z)

                        do_const = "cmds." + o_conmodel_t + "('" + n_namespace + o_sname +"','" + m_namespace + o_dname + "',maintainOffset=False,offset=[" + o_off_x_t + "," + o_off_y_t + "," +  o_off_z_t + "])"
                        exec (do_const)

                    elif o_conmodel == 'Orient':
                        if cmds.pointConstraint(m_namespace + o_dname,q=True) != None:
                            cmds.pointConstraint(n_namespace + o_sname,m_namespace + o_dname,edit=True,remove=True)
                        if cmds.parentConstraint(m_namespace + o_dname,q=True) != None:
                            cmds.parentConstraint(n_namespace + o_sname,m_namespace + o_dname,edit=True,remove=True)

                        o_off_x = cmds.scriptTable('table', cellIndex=(row_no,5), q=True, cellValue=True)[0]
                        if o_off_x == '':
                            o_off_x_t = '0.0000'
                        else:
                            o_off_x_t = str(o_off_x)

                        o_off_y = cmds.scriptTable('table', cellIndex=(row_no,6), q=True, cellValue=True)[0]
                        if o_off_y == '':
                            o_off_y_t = '0.0000'
                        else:
                            o_off_y_t = str(o_off_y)

                        o_off_z = cmds.scriptTable('table', cellIndex=(row_no,7), q=True, cellValue=True)[0]
                        if o_off_z == '':
                            o_off_z_t = '0.0000'
                        else:
                            o_off_z_t = str(o_off_z)

                        do_const = "cmds." + o_conmodel_t + "('" + n_namespace + o_sname +"','" + m_namespace + o_dname + "',maintainOffset=False,offset=[" + o_off_x_t + "," + o_off_y_t + "," +  o_off_z_t + "])"
                        exec (do_const)

                    elif o_conmodel == 'Scale':
                        if cmds.orientConstraint(m_namespace + o_dname,q=True) != None:
                            cmds.orientConstraint(n_namespace + o_sname,m_namespace + o_dname,edit=True,remove=True)
                        if cmds.parentConstraint(m_namespace + o_dname,q=True) != None:
                            cmds.parentConstraint(n_namespace + o_sname,m_namespace + o_dname,edit=True,remove=True)

                        o_off_x = cmds.scriptTable('table', cellIndex=(row_no,5), q=True, cellValue=True)[0]
                        if o_off_x == '':
                            o_off_x_t = '1.0000'
                        else:
                            o_off_x_t = str(o_off_x)

                        o_off_y = cmds.scriptTable('table', cellIndex=(row_no,6), q=True, cellValue=True)[0]
                        if o_off_y == '':
                            o_off_y_t = '1.0000'
                        else:
                            o_off_y_t = str(o_off_y)

                        o_off_z = cmds.scriptTable('table', cellIndex=(row_no,7), q=True, cellValue=True)[0]
                        if o_off_z == '':
                            o_off_z_t = '1.0000'
                        else:
                            o_off_z_t = str(o_off_z)

                        do_const = "cmds." + o_conmodel_t + "('" + n_namespace + o_sname +"','" + m_namespace + o_dname + "',maintainOffset=False,offset=[" + o_off_x_t + "," + o_off_y_t + "," +  o_off_z_t + "])"
                        exec (do_const)

                else:
                    o_offmodel_t = 'True'
                    if o_conmodel == 'Parent':
                        if cmds.pointConstraint(m_namespace + o_dname,q=True) != None:
                            cmds.pointConstraint(n_namespace + o_sname,m_namespace + o_dname,edit=True,remove=True)
                        if cmds.orientConstraint(m_namespace + o_dname,q=True) != None:
                            cmds.orientConstraint(n_namespace + o_sname,m_namespace + o_dname,edit=True,remove=True)
                    elif o_conmodel == 'Point':
                        if cmds.orientConstraint(m_namespace + o_dname,q=True) != None:
                            cmds.orientConstraint(n_namespace + o_sname,m_namespace + o_dname,edit=True,remove=True)
                        if cmds.parentConstraint(m_namespace + o_dname,q=True) != None:
                            cmds.parentConstraint(n_namespace + o_sname,m_namespace + o_dname,edit=True,remove=True)
                    elif o_conmodel == 'Orient':
                        if cmds.pointConstraint(m_namespace + o_dname,q=True) != None:
                            cmds.pointConstraint(n_namespace + o_sname,m_namespace + o_dname,edit=True,remove=True)
                        if cmds.parentConstraint(m_namespace + o_dname,q=True) != None:
                            cmds.parentConstraint(n_namespace + o_sname,m_namespace + o_dname,edit=True,remove=True)

                    do_const = "cmds." + o_conmodel_t + "('" + n_namespace + o_sname +"','" + m_namespace + o_dname + "',maintainOffset=True)"
                    exec (do_const)

            row_no += 1

    except:
        cmds.confirmDialog( title='Name ERROR', message=' No Node Name to Constraint !! ')

def constraint_list_menu(*args):
    if cmds.window('ConstraintTable', exists=True):
        cmds.deleteUI('ConstraintTable')

    workspace_dir = cmds.workspace( q=True, rd=True )
    
    Pro_dir = os.path.basename(workspace_dir)

    tmp_csv_file = workspace_dir + Pro_dir + '_constraint_table.csv'

    window = cmds.window('ConstraintTable', title='Constraint Table',sizeable=True, topLeftCorner=[300, 50], widthHeight=(540, 600))
    form = cmds.formLayout(numberOfDivisions=100)

    table1 = cmds.scriptTable('table',rows=3, columns=7,columnWidth=([1,135],[2,145],[3,70],[4,45],[5,40],[6,40],[7,40]),
        label=[(1,"SourceNodeName"), (2,"DestinationNodeName"), (3,"Constrain"), (4,"Offset"), (5,"X"), (6,"Y"), (7,"Z")],
        cellChangedCmd=edit_cell)

    addButton = cmds.button(label="Add Row",command=add_row)
    deleteButton = cmds.button(label="Delete Row",command=delete_row)
    insertAddRowButton = cmds.button(label="Insert to Selected Row",command=insert_add_row)
    deleteSelRowButton = cmds.button(label="Delete Selected Row",command=delete_sel_row)

    column = cmds.columnLayout()
    cmds.textFieldButtonGrp('load_csv',label='Select csv File ',text=tmp_csv_file, buttonLabel='LoadCSV',
        columnWidth3=[80,500,30],buttonCommand=load_csv)

    cmds.separator(height=10)
    cmds.text(label='Select Row to Input',width=420,bgc=[0.2,0.2,0.2],align='center' )
    cmds.rowLayout(numberOfColumns=2)
    cmds.button('set_bot1',label='Select SourceNodeName',width=210,bgc=[0.6,0.5,0.5],command=set_sel1)
    cmds.button('set_bot2',label='Select DestinationNodeName',width=210,bgc=[0.5,0.5,0.6],command=set_sel2)
    cmds.setParent('..')
    cmds.separator(height=3)
    cmds.text(label='Select Constaint Type                    Select Offset Mode ',width=420,align='center' )
    cmds.rowLayout(numberOfColumns=6)
    cmds.button('set_bot3',label='Point',width=50,bgc=[0.6,0.5,0.5],command=set_sel3a)
    cmds.button('set_bot5',label='Orient',width=50,bgc=[0.65,0.5,0.5],command=set_sel3c)
    cmds.button('set_bot4',label='Parent',width=53,bgc=[0.7,0.5,0.5],command=set_sel3b)
    cmds.button('set_bot8',label='Scale',width=50,bgc=[0.7,0.5,0.5],command=set_sel3d)
    cmds.button('set_bot6',label='Offset OFF',width=105,bgc=[0.5,0.5,0.6],command=set_sel4a)
    cmds.button('set_bot7',label='Offset ON',width=103,bgc=[0.5,0.5,0.65],command=set_sel4b)
    cmds.setParent('..')
    cmds.separator(height=15)
    cmds.rowLayout(numberOfColumns=2)
    cmds.text( label='       ' )
    cmds.button('output_bot1',label='SAVE  LIST  to .CSV',width=350,height=20,bgc=[0.6,0.6,0.5],align='center',command=output_to_cvs)
    cmds.setParent('..')
    cmds.separator(height=15)

    cmds.rowLayout(numberOfColumns=4)
    cmds.text( label='    ' )
    cmds.columnLayout()
    cmds.text(label='SourceNamespace' )
    cmds.textField('c_namespace',text='',bgc=[0.15,0.0,0.0],width=135)
    cmds.text(label='DestinationNamespace' )
    cmds.textField('d_namespace',text='',bgc=[0.15,0.0,0.0],width=135)
    cmds.setParent('..')
    cmds.text( label='    ' )
    cmds.button('do_bot',label='Do All Constraint ',height=40,width=200,bgc=[0.8,0.5,0.5],command=do_constraint)

    cmds.setParent('..')
    cmds.formLayout( form, edit=True,
         attachForm=[
              (table1, 'left', 5), (table1, 'top', 0), (table1, 'right', 5), (table1, 'bottom', 10),
              (column, 'top', 5), (column, 'left', 5),

              (addButton, 'left', 0), (addButton, 'bottom', 0),
              (deleteButton, 'bottom', 0), (deleteButton, 'right',0),
              (insertAddRowButton, 'bottom', 0), (insertAddRowButton, 'right', 0),
              (deleteSelRowButton, 'bottom', 0), (deleteSelRowButton, 'right', 0)
              ],
         attachControl=[(table1, 'top', 10,column ),(table1, 'bottom', 0, addButton)],
         attachPosition=[(column, 'right', 0, 100),
              (addButton, 'right', 0, 25),(deleteButton, 'left', 0, 25),(deleteButton, 'right', 0, 50),
              (insertAddRowButton, 'left', 0,50),(insertAddRowButton, 'right', 0, 75),(deleteSelRowButton, 'left', 0,75)],
         attachNone=[(addButton, 'top'),(deleteButton, 'top'),(insertAddRowButton, 'top'),(deleteSelRowButton, 'top')])

    cmds.showWindow( window )