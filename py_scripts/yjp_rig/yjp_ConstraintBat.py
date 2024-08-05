# -*- coding: utf-8 -*-
import maya.cmds as cmds
import codecs
import os

def yjp_ConstraintBat(path):
    is_file = os.path.isfile(path)
    if not is_file:
        print('exit No path')
        exit()
    f_in  = codecs.open(path, 'r','Shift_JIS')
    lines = f_in.readlines()
    nodeT = []
    nodeR = []
    nodeS = []
    Log = ''

    for line in lines:
        mofset = 0
        buffer = line.split(',')
        buffer[3] = buffer[3].replace('\n', '')
        print(buffer[3])
        if buffer[3]=='1':
            mofset = 1
            print(buffer[3])
        if(cmds.objExists(buffer[0])) and (cmds.objExists(buffer[1])):
            nodeT = cmds.listConnections( (buffer[1]+'.tx'), d=False, s=True )
            nodeR = cmds.listConnections( (buffer[1]+'.rx'), d=False, s=True )
            nodeS = cmds.listConnections( (buffer[1]+'.sx'), d=False, s=True )
            if buffer[2]=='Point' :
                if not nodeT :
                    cmds.pointConstraint( buffer[0], buffer[1], mo=buffer[3] )
                else:
                    Log += (buffer[1] + ' is connected to '+nodeT[0]+'\n')
            elif buffer[2]=='Parent' :
                if not nodeT :
                    cmds.parentConstraint( buffer[0], buffer[1], mo=mofset )
                else:
                    Log += (buffer[1] + ' is connected to '+nodeT[0]+'\n')
            elif buffer[2]=='Orient' :
                if not nodeR :
                    cmds.orientConstraint( buffer[0], buffer[1], mo=mofset )
                else:
                    Log += (buffer[1] + ' is connected to '+nodeR[0]+'\n')
            elif buffer[2]=='Scale' :
                if not nodeS :
                    cmds.scaleConstraint( buffer[0], buffer[1], mo=mofset )
                else:
                    Log += (buffer[1] + ' is connected to '+nodeS[0]+'\n')
    print (Log)