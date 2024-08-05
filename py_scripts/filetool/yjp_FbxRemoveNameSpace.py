# -*- coding: utf-8 -*-

import os
import maya.cmds as cmds

def FbxRemoveNameSpace():
    print('yjp_FbxRemoveNameSpace')
    file_name=''
    ID=''
    filePathName = cmds.workspace(q=True,fn=True)
    fbxPath = filePathName + '/data'
    fbxfile = cmds.getFileList(folder=fbxPath,filespec='*.fbx')
    for n in range(len(fbxfile)):
        if '_' in fbxfile[n]:
            file_name = str(fbxPath+ '/' +fbxfile[n])
            array=fbxfile[n].split('_')
            ID = array[0]+'00:'
            with open(file_name,'r') as f:
                data_lines = f.read()

            data_lines = data_lines.replace(ID, '')

            with open(file_name, 'w') as f:
                f.write(data_lines)
            print(file_name)
    print('yjp_FbxRemoveNameSpace END')