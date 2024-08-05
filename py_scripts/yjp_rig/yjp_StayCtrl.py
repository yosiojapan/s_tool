# -*- coding: utf-8 -*-undChoice
from maya import cmds

def yjp_StayCtrl(ROOT='world_ctl|global_C0_root', SDK='global_C0_ik_cns', CTRL='global_C0_ctl'):
    if(cmds.objExists(ROOT)) and (cmds.objExists(SDK)) and (cmds.objExists(CTRL)):
        cmds.select(CTRL)

        cmds.addAttr( longName='Stay', attributeType='bool', k=1, defaultValue=0, minValue=0, maxValue=1 )

        Inverse = cmds.createNode( 'inverseMatrix', n='Inverse' )
        Choice = cmds.createNode( 'choice', n='Choice' )
        Decompos = cmds.createNode( 'decomposeMatrix', n='Decompos' )

        cmds.connectAttr("{}.matrix".format(CTRL),"{}.inputMatrix".format(Inverse))

        cmds.connectAttr("{}.matrix".format(ROOT),"{}.input[0]".format(Choice))
        cmds.connectAttr("{}.outputMatrix".format(Inverse),"{}.input[1]".format(Choice))
        cmds.connectAttr("{}.Stay".format(CTRL),"{}.selector".format(Choice))
        cmds.connectAttr("{}.output".format(Choice),"{}.inputMatrix".format(Decompos))

        cmds.connectAttr("{}.outputTranslate".format(Decompos),"{}.translate".format(SDK))
        cmds.connectAttr("{}.outputRotate".format(Decompos),"{}.rotate".format(SDK))
        cmds.connectAttr("{}.outputScale".format(Decompos),"{}.scale".format(SDK))
        cmds.connectAttr("{}.outputShear".format(Decompos),"{}.shear".format(SDK))
        if(cmds.objExists('guide|' + ROOT)):
            cmds.setAttr('guide|' + ROOT + '.scale', 1, 1, 1)
        cmds.select(CTRL)
    else:
        print('NO node '+ROOT+' '+SDK+' '+CTRL)