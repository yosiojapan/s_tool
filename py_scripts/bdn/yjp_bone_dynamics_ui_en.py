import maya.cmds as cmds
from functools import partial
import maya.mel as mel
import json
import glob
import os
import subprocess
from expcol import collider

# maya_expressionCollision

cmds.loadPlugin("boneDynamicsNode.mll", qt=True)

def boneDynamics_create(jointlist=[], addjoint=False, usetarget=False, usetargetCTRL=False):
    if not(jointlist):
        return None
    bindJoint=''
    length = 10
    
    #global bone_dynamics_data
    #bone_dynamics_data['source_joint'][jointlist[0]] = jointlist
    
    root = cmds.listRelatives(jointlist[0], p=True) or []
    if(root):
        pc = cmds.listRelatives(root[0], type='parentConstraint') or []
        if (pc):
            root = cmds.listConnections((pc[0]+'.target[0].targetTranslate'))
        cmds.select(root[0])
    else:
        cmds.select(cl=True)

    driven =[]
    atr=['tx','ty','tz','rx','ry','rz']
    for bindJoint in jointlist:
        drivenJoint = cmds.joint(p=(0, 0, 0),n=(bindJoint + '_driven'))
        driven.append(drivenJoint)
        cmds.matchTransform(drivenJoint,bindJoint)
        length = cmds.getAttr(bindJoint + '.tx')
        r = cmds.getAttr(bindJoint + '.rotate')
        jo = cmds.getAttr(bindJoint + '.jointOrient')
        cmds.setAttr((drivenJoint + '.rotate'), r[0][0], r[0][1], r[0][2],type="double3")
        cmds.setAttr((drivenJoint + '.jointOrient'), jo[0][0], jo[0][1], jo[0][2],type="double3")
        
        tempNode = cmds.createNode("network")
        cmds.addAttr(tempNode, longName='rx', attributeType='float' )
        cmds.addAttr(tempNode, longName='ry', attributeType='float' )
        cmds.addAttr(tempNode, longName='rz', attributeType='float')
        cmds.addAttr(tempNode, longName='tx', attributeType='float')
        cmds.addAttr(tempNode, longName='ty', attributeType='float' )
        cmds.addAttr(tempNode, longName='tz', attributeType='float' )
        cmds.addAttr(tempNode, longName='bd', hidden=1, attributeType='message')

        if not (cmds.attributeQuery( 'bd', node=bindJoint, ex=True )):
            cmds.addAttr(bindJoint, longName='bd', hidden=1, attributeType='message')

        cmds.connectAttr( tempNode+'.bd', bindJoint + '.bd', force=True)

        for at in atr:
            constNode = cmds.listConnections( (bindJoint + '.' + at), p=True, s=True )
            if constNode:
                if cmds.isConnected(constNode[0],(bindJoint + '.' + at) ):
                    cmds.disconnectAttr(constNode[0],(bindJoint + '.' + at) )
                cmds.connectAttr(constNode[0] , (tempNode + '.'+ at), force=True)
        cmds.parentConstraint(drivenJoint,bindJoint)
        cmds.select(drivenJoint)

    if(addjoint):
        addJoint = cmds.joint(p=(0, 0, 0),n=(bindJoint + '_lastadd'))
        driven.append(addJoint)
        cmds.matchTransform(addJoint,bindJoint)
        cmds.setAttr((addJoint + '.t'), length, 0, 0)

    cmds.select(driven[0])
    cmds.addAttr( longName='driven', dt='string')
    cmds.setAttr(driven[0] + '.driven', 'root', type="string")
    #bone_dynamics_data['driven_list'][jointlist[0]]=driven

    bDN=[]
    for bone, end in zip(driven[:-1], driven[1:]):
        boneDynamicsNode = cmds.createNode('boneDynamicsNode')
        bDN.append(boneDynamicsNode)
        cmds.connectAttr('time1.outTime', boneDynamicsNode + '.time', force=True)
        cmds.connectAttr(bone + '.translate', boneDynamicsNode + '.boneTranslate', f=True)
        cmds.connectAttr(bone + '.parentMatrix[0]', boneDynamicsNode + '.boneParentMatrix', f=True)
        cmds.connectAttr(bone + '.parentInverseMatrix[0]', boneDynamicsNode + '.boneParentInverseMatrix', f=True)
        cmds.connectAttr(bone + '.jointOrient', boneDynamicsNode + '.boneJointOrient', f=True)
        cmds.connectAttr(end + '.translate', boneDynamicsNode + '.endTranslate', f=True)

        cmds.connectAttr(boneDynamicsNode + '.outputRotate', bone + '.rotate', f=True)

        cmds.setAttr (boneDynamicsNode + ".radius",3)
        fps = mel.eval('currentTimeUnitToFPS') 
        cmds.setAttr (boneDynamicsNode + ".fps",fps)
        current = cmds.currentTime(q=True)
        cmds.setAttr (boneDynamicsNode + ".resetTime",current)
        cmds.setAttr (boneDynamicsNode + ".elasticity",30)
        cmds.setAttr (boneDynamicsNode + ".gravityMultiply",1)
        cmds.setAttr (boneDynamicsNode + ".enableAngleLimit",1)
        cmds.setAttr (boneDynamicsNode + ".angleLimit",90)
        cmds.setAttr (boneDynamicsNode + ".radius",4)
        cmds.setAttr (boneDynamicsNode + ".enableGroundCol",1)

        boneDynamics_cone_root = cmds.createNode('transform', n = bone + "_cone_root")
        boneDynamics_cone_ro = cmds.createNode('transform', n = bone + "_cone_ro")
        implicitConeShape = cmds.createNode("implicitCone")
        implicitCone = cmds.listRelatives(implicitConeShape, p=True)
        implicitSphereShape = cmds.createNode("implicitSphere")
        implicitSphere = cmds.listRelatives(implicitSphereShape, p=True)
        
        cmds.setAttr((implicitCone[0] + '.ry'),-90)

        parentNode = cmds.listRelatives (bone, p=True)
        if parentNode:
            cmds.parent( boneDynamics_cone_root, parentNode[0] )
        cmds.parent( boneDynamics_cone_ro, boneDynamics_cone_root )
        cmds.parent( implicitCone[0], boneDynamics_cone_ro )
        cmds.parent( implicitSphere[0], end ,relative=True)

        cmds.connectAttr(boneDynamicsNode +'.enableAngleLimit', boneDynamics_cone_root + '.visibility', force=True)
        cmds.connectAttr(boneDynamicsNode +'.boneTranslate', boneDynamics_cone_root + '.translate', force=True)
        cmds.connectAttr(boneDynamicsNode +'.boneJointOrient', boneDynamics_cone_root + '.rotate', force=True)

        cmds.connectAttr(boneDynamicsNode +'.rotationOffset', boneDynamics_cone_ro + '.rotate', force=True)

        cmds.connectAttr(boneDynamicsNode +'.angleLimit', implicitConeShape + '.coneAngle', force=True)
        cmds.connectAttr(boneDynamicsNode +'.radius', implicitSphereShape + '.radius', force=True)
    
        set_name = "boneDynamicsNodeSet"
        if not cmds.objExists(set_name):
            cmds.select(cl=True)
            cmds.sets(name=set_name)
        
        cmds.sets(boneDynamicsNode, addElement=set_name)


    target_list=[]
    if(usetarget):
        roottarget=''
        for bindJoint,bd in zip(driven,bDN):
            targetname = bindJoint.replace('_driven', '_target')
            cmds.duplicate(bindJoint, po=1, n=targetname)  
            target_list.append(targetname)
            if(roottarget):
                cmds.parent(targetname, roottarget)
                cmds.matchTransform(targetname,bindJoint)
            cmds.setAttr((targetname + '.rotate'), 0, 0, 0,type="double3")
            radiussize = cmds.getAttr(bindJoint+'.radius')
            cmds.setAttr((targetname + '.radius'), (radiussize+2))
            roottarget= targetname
            cmds.connectAttr(targetname +'.rotate', bd + '.rotationOffset', force=True)

    #bone_dynamics_data['target_list'][jointlist[0]]=target_list

    if(usetargetCTRL):
        ctrllist=[]
        for bindJoint in jointlist:
            meta = cmds.listConnections(bindJoint,t='network')
            if(meta):
                ctrl = cmds.listConnections((meta[0]+'.FKctrl'))
                ctrllist.append(ctrl[0])
        
        dict_target_list = dict(zip(target_list, ctrllist))
        # boneDynamics_targetCtrl(target_list)
        for bindJoint,ctrl, in dict_target_list.items():
            cmds.parentConstraint(ctrl,bindJoint)
    # boneDynamics_datadict()


def boneDynamics_chainRefresh(node):
    global bone_dynamics_data
    chainList = list(bone_dynamics_data['source_joint'].keys())
    cmds.textScrollList('Bdynamics_chainList', edit=True, ra=True)
    cmds.textScrollList('Bdynamics_chainList', edit=True, a=chainList)
    if cmds.objExists(node):
        cmds.textScrollList('Bdynamics_chainList', edit=True, si=node)

    # boneDynamics_BDRefresh()


def boneDynamics_datadict(*args):
    #Maya boneDynamics > dict
    global bone_dynamics_dat
    #scene boneDynamicsNode data
    boneDynamics = cmds.ls(type= 'boneDynamicsNode')
    for bdn in boneDynamics:
        driven = cmds.listConnections((bdn + '.outputRotate'), type='joint')
        if(cmds.attributeQuery ('driven', node=driven[0], ex=True)):
            if(cmds.getAttr((driven[0]+'.driven'))=='root'):
                drivenjoint = cmds.listRelatives(driven[0],type ='joint',ad=True)
                drivenjoint.reverse()
                drivenjoint.insert(0, driven[0])
                string = ",".join(drivenjoint)
                string_new = string.replace('_driven', '')
                sourcejoint =  string_new.split(",")
                add = [s for s in drivenjoint if '_lastadd' in s]
                if(add):
                    drivenjoint = list(set(drivenjoint) - set(add))
                    valx = cmds.getAttr(add[0]+'.tx')
                    valy = cmds.getAttr(add[0]+'.ty')
                    valz = cmds.getAttr(add[0]+'.tz')
                    sourcejoint = sourcejoint[:-1]
                    bone_dynamics_data['add_joint'][sourcejoint[-1]]=[valx,valy,valz]

                bone_dynamics_data['source_joint'][sourcejoint[0]]=sourcejoint

                bone_dynamics_data['driven_list'][sourcejoint[0]]=drivenjoint
                
                targetjoint = [s + '_target' for s in sourcejoint]
                if not (add):
                    targetjoint = targetjoint[:-1]
                if(targetjoint):
                    bone_dynamics_data['target_list'][sourcejoint[0]]=targetjoint
                    ctrllist=[]
                    for trg in targetjoint:
                        pc = cmds.listConnections((trg + '.rx'), type='parentConstraint')
                        if(pc):
                            ctrl = cmds.listConnections((pc[0] + '.target[0].targetTranslate'))
                            ctrllist.append(ctrl[0])
                    if(ctrllist):
                        bone_dynamics_data['ctrl_list'][sourcejoint[0]]=ctrllist
        joint = driven[0].replace('_driven', '')
        bdatr = boneDynamics_getAttr(bdn)
        bone_dynamics_data['dynamics_attr'][joint]=bdatr

    collider_node = cmds.ls(type='transform')
    #collider_nodeにcolliderTypeアトリビュートが無ければcollider_nodeから削除
    
    collider_node = [j for j in collider_node if cmds.attributeQuery('colliderType', node=j, ex=True)==True]
    if(collider_node):
        cmds.textScrollList('colliderList', edit=True, ra=True)
    for coll in collider_node:
        cmds.textScrollList('colliderList', edit=True, a=coll)
        coltype = cmds.getAttr(coll + '.colliderType')
        if not ('collider_list' in bone_dynamics_data):
            bone_dynamics_data['collider_list'] ={}
        bone_dynamics_data['collider_list'][coll]={}
        bone_dynamics_data['collider_list'][coll]['coltype'] = coltype
        tra = cmds.getAttr(coll + '.t')
        bone_dynamics_data['collider_list'][coll]['translate'] = [tra[0][0], tra[0][1], tra[0][2]]
        rot = cmds.getAttr(coll + '.r')
        bone_dynamics_data['collider_list'][coll]['rotate'] = [rot[0][0], rot[0][1], rot[0][2]]
        
        pnode = cmds.listRelatives(coll,p=True) or []
        if(pnode):
            pcnode = cmds.listConnections((pnode[0] + '.rx'), type='parentConstraint') or []
            pnode = cmds.listConnections((pcnode[0] + '.target[0].targetParentMatrix')) or []
            bone_dynamics_data['collider_list'][coll]['parent'] = pnode[0]

        if(coltype == 'sphere'):
            rad = cmds.getAttr(coll + '.radius')
            bone_dynamics_data['collider_list'][coll]['radius'] = rad

        elif(coltype == 'capsule'):
            rad = cmds.getAttr(coll + '.radius')
            hei = cmds.getAttr(coll + '.height')
            bone_dynamics_data['collider_list'][coll]['radius'] = rad
            bone_dynamics_data['collider_list'][coll]['height'] = hei

        elif(coltype == 'capsule2'):
            radA = cmds.getAttr(coll + '.radiusA')
            radB = cmds.getAttr(coll + '.radiusB')
            hei = cmds.getAttr(coll + '.height')
            bone_dynamics_data['collider_list'][coll]['radiusA'] = radA
            bone_dynamics_data['collider_list'][coll]['radiusB'] = radB
            bone_dynamics_data['collider_list'][coll]['height'] = hei
        bdn = cmds.listConnections(coll,d=True,t='boneDynamicsNode') or [] #or[]でNnonではなく[]になる
        
        bdn = set(bdn)#リスト内重複削除
        col_connect=[]
        for bd in bdn:
            driven = cmds.listConnections((bd + '.outputRotate'), type='joint')
            joint = driven[0].replace('_driven', '')
            col_connect.append(joint)
        bone_dynamics_data['collider_list'][coll]['connect'] =col_connect

    boneDynamics_chainRefresh('None')


def boneDynamics_BDRefresh():
    #boneDynamics_joint UIRefresh
    global bone_dynamics_data

    chains = cmds.textScrollList('Bdynamics_chainList', q=True, si=True)
    if not (chains):
        return
    
    cmds.textScrollList('Bdynamics_jointList', e=True, deselectAll=True)
    cmds.textScrollList('Bdynamics_jointList', e=True, removeAll=True)
    cmds.textScrollList('Bdynamics_targetList', e=True, deselectAll=True)
    cmds.textScrollList('Bdynamics_targetList', e=True, removeAll=True)
    cmds.textScrollList('Bdynamics_ctrlList', e=True, deselectAll=True)
    cmds.textScrollList('Bdynamics_ctrlList', e=True, removeAll=True)

    for chain in chains:
        joints = bone_dynamics_data['source_joint'][chain]
        ctrl=[]
        use=[]
        for joint in joints:
            if(cmds.objExists(joint + '_driven')==True):
                if(cmds.listConnections( (joint + '_driven.rotate'), d=False, s=True,type='boneDynamicsNode')!=None):
                    use.append(joint)
        #joint.pop(-1)
        cmds.textScrollList('Bdynamics_jointList', edit=True, a=use)
        
        targetJoint = bone_dynamics_data['target_list'][chain]
        targetJoint = [j for j in targetJoint if cmds.objExists(j)==True]

        if(targetJoint):
            cmds.textScrollList('Bdynamics_targetList', e=True, a=targetJoint)

        if(chain in bone_dynamics_data['ctrl_list']):
            ctrl = bone_dynamics_data['ctrl_list'][chain]
            ctrl = [c for c in ctrl if cmds.objExists(c)==True]

        if(ctrl):
            cmds.textScrollList('Bdynamics_ctrlList', e=True, a=ctrl)
            cmds.textScrollList('Bdynamics_targetList', e=True, en =False)
    cmds.textScrollList('Bdynamics_jointList', e=True, deselectAll=True)
    # cmds.textScrollList('Bdynamics_jointList', edit=True, sii=1)
        
    boneDynamics_dataRefresh


def connect_target_ctrl(*args):
    global bone_dynamics_data

    if(args[0]):
        jointRoot = args[0]
        target = bone_dynamics_data['target_list'][jointRoot]
        ctrl = bone_dynamics_data['ctrl_list'][jointRoot]
    else:
        if not ('ctrl_list' in bone_dynamics_data):
            bone_dynamics_data['ctrl_list']={}
        target = cmds.textScrollList('Bdynamics_targetList', q=True, ai=True)
        if not target:
            return
        ctrl = cmds.textScrollList('Bdynamics_ctrlList', q=True, ai=True)
        if not ctrl:
            return
        chain = cmds.textScrollList('Bdynamics_chainList', q=True, si=True)
        bone_dynamics_data['ctrl_list'][chain[0]] = ctrl

    for tag, ctl in zip(target, ctrl):
        cmds.parentConstraint(ctl, tag)

def selected_get_ctrl():
    ctrl = cmds.ls(sl=True)
    if len(ctrl) == 0:
        return
    cmds.textScrollList('Bdynamics_ctrlList', edit=True, removeAll=True)
    cmds.textScrollList('Bdynamics_ctrlList', edit=True, append=ctrl)
    cmds.select(cl=True)


def do_boneDynamics_create(*args):
    global bone_dynamics_data
    joint = cmds.ls(sl=True)
    AddEnd = cmds.checkBox('bone_dynamics_addEndcheck',q=True,v=True)
    Target = cmds.checkBox('bone_dynamics_targetcheck',q=True,v=True)

    if (args[0]=='json'):
        chainList = cmds.textScrollList('Bdynamics_chainList', q=True, si=True)
        if not(chainList):
            return
        for chainRoot in chainList:
            AddJoint = False
            jsonTarget = False
            AddEnd = False
            Target = False
            jointchain = bone_dynamics_data['source_joint'][chainRoot]
            if not (jointchain):
                print('Joints do not exist')
                continue

            drivenjoint = bone_dynamics_data['driven_list'][chainRoot]
            if(cmds.objExists(drivenjoint[0])):
                print('bone_dynamics exists')
                continue

            cmds.select(jointchain)
            if 'add_joint' in bone_dynamics_data :
                if jointchain[-1] in bone_dynamics_data['add_joint'].keys():
                    AddJoint = True
            if 'target_list' in bone_dynamics_data :
                if chainRoot in bone_dynamics_data['target_list'].keys():
                    jsonTarget = True

            if(AddJoint):
                AddEnd = True
            if(jsonTarget):
                Target = True
            
            boneDynamics_create(jointchain, addjoint=AddEnd, usetarget=Target)

            # boneDynamics_chainRefresh(jointchain[0])
            if 'ctrl_list' in bone_dynamics_data :
                if chainRoot in bone_dynamics_data['ctrl_list'].keys() :
                    # target_list = bone_dynamics_data['target_list'][jointchain[0]]
                    connect_target_ctrl(chainRoot)
            #bone_dynamics_datareplace(joint[0])
        
            for joint in jointchain:
                bdn = cmds.listConnections((joint + '_driven.rotate'), type='boneDynamicsNode')
                if joint in bone_dynamics_data['dynamics_attr'].keys():
                    dynamics_attrdict = bone_dynamics_data['dynamics_attr'][joint]
                    for attr,val in dynamics_attrdict.items():
                        cmds.setAttr(bdn[0] +'.'+attr, val)
    else:
        boneDynamics_create(joint,addjoint=AddEnd, usetarget=Target)
        boneDynamics_datadict()
        #boneDynamics_chainRefresh(joint[0])

def boneDynamics_getAttr(bdn):
    if cmds.objExists(bdn):
        bdnattr={'resetTime':0,'damping':0,'elasticity':0,'stiffness':0,
                'mass':0,'gravityX':0,'gravityY':0,'gravityZ':0,
                'gravityMultiply':0,'enableAngleLimit':True,'angleLimit':0,'radius':0,
                'iterations':0,'enableGroundCol':False,'groundHeight':0
                }
        for attr in bdnattr:
            bdnattr[attr] = cmds.getAttr(bdn +'.'+attr)
        return bdnattr


def boneDynamics_dataRefresh():
    cmds.intFieldGrp('BDNresetTime', en=False, e=True)
    cmds.floatSliderGrp('BDNdamping', en=False, e=True)
    cmds.floatSliderGrp('BDNelasticity', en=False, e=True)
    cmds.floatSliderGrp('BDNstiffness', en=False, e=True)
    cmds.floatSliderGrp('BDNmass', en=False, e=True)
    cmds.floatSliderGrp('BDNgravityX', en=False, e=True)
    cmds.floatSliderGrp('BDNgravityY', en=False, e=True)
    cmds.floatSliderGrp('BDNgravityZ', en=False, e=True)
    cmds.floatSliderGrp('BDNgravityMultiply', en=False, e=True)
    cmds.checkBoxGrp('BDNenableAngleLimit', en=False, e=True)
    cmds.floatSliderGrp('BDNangleLimit', en=False, e=True)
    cmds.floatSliderGrp('BDNradius', en=False, e=True)
    cmds.intFieldGrp('BDNiterations', en=False, e=True)
    cmds.checkBoxGrp('BDNenableGroundCol', en=False, e=True)
    cmds.floatSliderGrp('BDNgroundHeight', en=False, e=True)

    joint = cmds.textScrollList('Bdynamics_jointList', q=True, si=True)
    if not cmds.objExists(joint[0]):
        return
    if not cmds.objExists(joint[0]+ '_driven'):
        return
    bdn = cmds.listConnections((joint[0] + '_driven.rotate'), type='boneDynamicsNode')
    if (bdn):
        bdnatr={'resetTime':0,'damping':0,'elasticity':0,'stiffness':0,
                'mass':0,'gravityX':0,'gravityY':0,'gravityZ':0,
                'gravityMultiply':0,'enableAngleLimit':0,'angleLimit':0,'radius':0,
                'iterations':0,'enableGroundCol':0,'groundHeight':0
                }
        for attr in bdnatr:
            bdnatr[attr] = cmds.getAttr(bdn[0] +'.'+attr)

        cmds.intFieldGrp('BDNresetTime', en=True, e=True, v1 = bdnatr['resetTime'])
        cmds.floatSliderGrp('BDNdamping', en=True, e=True, v= bdnatr['damping'] )
        cmds.floatSliderGrp('BDNelasticity', en=True, e=True, v= bdnatr['elasticity'] )
        cmds.floatSliderGrp('BDNstiffness', en=True, e=True, v= bdnatr['stiffness'] )
        cmds.floatSliderGrp('BDNmass', en=True, e=True, v=bdnatr['mass'] )
        cmds.floatSliderGrp('BDNgravityX', en=True, e=True, v=bdnatr['gravityX'] )
        cmds.floatSliderGrp('BDNgravityY', en=True, e=True, v=bdnatr['gravityY'] )
        cmds.floatSliderGrp('BDNgravityZ', en=True, e=True, v=bdnatr['gravityZ'] )
        cmds.floatSliderGrp('BDNgravityMultiply', en=True, e=True, v=bdnatr['gravityMultiply'] )
        cmds.checkBoxGrp('BDNenableAngleLimit', en=True, e=True, v1=bdnatr['enableAngleLimit'] )
        cmds.floatSliderGrp('BDNangleLimit', en=True, e=True, v=bdnatr['angleLimit'] )
        cmds.floatSliderGrp('BDNradius', en=True, e=True, v=bdnatr['radius'] )
        cmds.intFieldGrp('BDNiterations', en=True, e=True, v1=bdnatr['iterations'] )
        cmds.checkBoxGrp('BDNenableGroundCol', en=True, e=True, v1=bdnatr['enableGroundCol'] )
        cmds.floatSliderGrp('BDNgroundHeight', en=True, e=True, v=bdnatr['groundHeight'] )
    return


def boneDynamics_dataEdit(*args):
    attr = args[0]
    jointlist = cmds.textScrollList('Bdynamics_jointList', q=True, si=True)
    for joint in jointlist:
        bdn = cmds.listConnections((joint + '_driven.rotate'), type='boneDynamicsNode')
        if(bdn[0]):
            Val=0
            if(attr == 'resetTime' or attr == 'iterations' ):
                Val = cmds.intFieldGrp(('BDN'+attr), q=True, value1 = True)
            elif(attr == 'enableAngleLimit' or attr == 'enableGroundCol'):
                Val = cmds.checkBoxGrp(('BDN'+attr), q=True, v1=True)
            else:
                Val = cmds.floatSliderGrp(('BDN'+attr), q=True, v=True )
            cmds.setAttr ((bdn[0] + '.'+ attr),Val)


def bd_targetselect():

    joint = cmds.textScrollList('Bdynamics_targetList', q=True, si=True)
    if not cmds.objExists(joint[0]):
        return
    cmds.select(joint)


def bd_ctrlselect():

    joint = cmds.textScrollList('Bdynamics_ctrlList', q=True, si=True)
    if not cmds.objExists(joint[0]):
        return
    cmds.select(joint)


def bone_dynamics_bake(*args):
    global bone_dynamics_data
    strat = cmds.playbackOptions(q=1, minTime=1 )
    end = cmds.playbackOptions(q=1, maxTime=1 )

    chainlist = cmds.textScrollList('Bdynamics_chainList', q=True, si=True)
    
    for chain in chainlist:
        drivenjoint = bone_dynamics_data['driven_list'][chain]
        if not (cmds.objExists(drivenjoint[0])):
            continue
        jointlist = bone_dynamics_data['source_joint'][chain]
        ctrllist=[]
        pclist=[]
        drivenGrp=[]
        targetGrp=[]
        bakelist=[]
        for joint in jointlist:
            drivenGrp.append(joint+'_driven')
            if(cmds.objExists(joint+'_target')):
                targetGrp.append(joint+'_target')
                #ctrlがあれば_drivenなければソースジョイントそのもの
                pc = cmds.listConnections((joint+'_target'), s=True, type='parentConstraint') or []
                pc = (list(set(pc)))
                if(pc):
                    pclist.append(pc[0])
                    ctrl = cmds.listConnections(pc[0]+'.target[0].targetTranslate')
                    ctrllist.append(ctrl[0])

        cmds.bakeSimulation( drivenGrp, t=(strat,end), sb=1, at=['tx','ty','tz','rx','ry','rz'], hi='none', mr=True )
        bone_dynamics_delete(*jointlist)

        if(ctrllist):
            bakelist = ctrllist
        else:
            bakelist = jointlist

        bakepc=[]
        for node,driv in (zip(bakelist,drivenGrp)):
            bpc=cmds.parentConstraint(driv,node)
            bakepc.append(bpc[0])
        cmds.bakeSimulation( bakelist, t=(strat,end), sb=1, at=['tx','ty','tz','rx','ry','rz'], hi='none',pok=True, mr=True )
        cmds.delete(bakepc)
        
        cmds.delete(drivenGrp,targetGrp)
        cone = jointlist[0] + '_driven_cone_root'
        if(cmds.objExists(cone)):
            cmds.delete(cone)

    print('bake END')


def bone_dynamics_delete(*args):
    jointlist = args

    for joint in jointlist:
        if(cmds.objExists(joint+'_driven')):
            bdn = cmds.listConnections((joint+'_driven.rotate'), type='boneDynamicsNode') or []
            if (bdn):
                cmds.delete(bdn)

    atr = ['tx','ty','tz','rx','ry','rz',]
    for joint in jointlist:
        if cmds.attributeQuery('bd', node=joint, exists=True):
            network = cmds.listConnections((joint+'.bd'), type='network')
            if(network):
                bdpc = cmds.listConnections((joint+'.tx'), s=True, type='parentConstraint')
                for at in atr:
                    originalNode = cmds.listConnections((network[0] + '.' + at),p=True, d=False, s=True, scn=True)
                    if(originalNode):
                        cmds.connectAttr(originalNode[0], (joint + '.' + at), force=True)
                cmds.delete(network,bdpc)
                cmds.deleteAttr( joint, at='bd' )
    boneDynamics_BDRefresh

def bone_dynamics_remove(*args):
    chainlist = cmds.textScrollList('Bdynamics_chainList', q=True, si=True)
    drivenGrp=[]
    targetGrp=[]
    for chain in chainlist:
        jointlist = bone_dynamics_data['source_joint'][chain]
        bone_dynamics_delete(*jointlist)
        for joint in jointlist:
            drivenGrp.append(joint+'_driven')
            if(cmds.objExists(joint+'_target')):
                targetGrp.append(joint+'_target')
        cone = jointlist[0] + '_driven_cone_root'
        if(cmds.objExists(cone)):
            cmds.delete(cone)
    grp = (drivenGrp + targetGrp)
    for j in grp:
        if(cmds.objExists(j)):
            cmds.delete(j)
    boneDynamics_BDRefresh()

def bone_dynamics_save(*args):
    global bone_dynamics_data
    boneDynamics_datadict()
    json_path = cmds.workspace( q=True, rd=True )
    json_path= os.path.dirname(json_path)
    name= os.path.basename(json_path)
    jsonname =cmds.textScrollList('Bdynamics_jsonList', q=True, si=True)
    if(jsonname):
        name = jsonname[0].replace('.json', '')
    json_path = cmds.text('bdjson_path',q=True, l=True)

    result = cmds.promptDialog(
		title='saveName',
		message='Enter Name:',
        text = name,
		button=['OK', 'Cancel'],
		defaultButton='OK',
		cancelButton='Cancel',
		dismissString='Cancel')

    if result == 'OK':
        json_path = json_path + '/'+(cmds.promptDialog(query=True, text=True)) + '.json'

        with open(json_path, 'wt', encoding='utf-8' ) as file:
            json.dump(bone_dynamics_data,file,indent=2)
        bone_dynamics_preset_reload()
    else:
        return


def bone_dynamics_load(*args):
    # json形式をpython形式に変換
    global bone_dynamics_data
    load_bonedynamics_fromscene

    path = cmds.text('bdjson_path', q=True, l=True)
    jsonfile = cmds.textScrollList('Bdynamics_jsonList', q=True, si=True)
    if not jsonfile:
        return
    with open(path + '/' + jsonfile[0]) as f:
        jsontxt = json.load(f)
    bone_dynamics_data = jsontxt

    jointlist = list(bone_dynamics_data['source_joint'].keys())
    cmds.textScrollList('Bdynamics_chainList', edit=True, ra=True)
    cmds.textScrollList('Bdynamics_chainList', edit=True, a=jointlist)
    
    if('collider_list' in bone_dynamics_data):
        collist = list(bone_dynamics_data['collider_list'].keys())
        cmds.textScrollList('colliderList', edit=True, ra=True)
        cmds.textScrollList('colliderList', edit=True, a=collist)


def load_bonedynamics_fromscene(*args):
    global bone_dynamics_data
    bone_dynamics_data={}
    bone_dynamics_data['source_joint']={}
    bone_dynamics_data['driven_list']={}
    bone_dynamics_data['add_joint']={}
    bone_dynamics_data['target_list']={}
    bone_dynamics_data['ctrl_list']={}
    bone_dynamics_data['dynamics_attr']={}
    bone_dynamics_data['collider_list']={}
    
    boneDynamics_datadict()
    jsontxt = json.dumps(bone_dynamics_data, indent=4)
    #print('dict/////////////////////////////////////')
    #print(jsontxt)
    #print('/////////////////////////////////////////')


def bone_dynamics_preset_reload():
    global bone_dynamics_data

    path=cmds.text('bdjson_path', q=True, l=True)
    file_list = glob.glob(path+"/*.json")
    files = [os.path.basename(file) for file in file_list]
    cmds.textScrollList('Bdynamics_jsonList', edit=True, ra=True)
    cmds.textScrollList('Bdynamics_jsonList', edit=True, a=files)

def bone_dynamics_jsonopen(*args):
    path = cmds.text('bdjson_path', l=True, q=True)
    json = cmds.textScrollList('Bdynamics_jsonList', q=True, si=True)
    subprocess.Popen(["start", "", (path+'/'+json[0])], shell=True)


def collider_create(*args):
    '''
    collider.iplane()   # 無限平面
    collider.sphere()   # 球
    collider.capsule()  # カプセル
    collider.capsule2() # 半径を個別に変えられるカプセル
    '''
    node = cmds.ls(sl=True,type='transform')
    colname = ''
    if(args[0] =='sphere'):
        colname = collider.sphere()
        cmds.setAttr(colname + '.radius', 5)
    elif(args[0] =='capsule'):
        colname = collider.capsule()
        cmds.setAttr(colname + '.radius', 5)
        cmds.setAttr(colname + '.height', 10)
    elif(args[0] =='capsule2'):
        colname = collider.capsule2()
        cmds.setAttr(colname + '.radiusA', 5)
        cmds.setAttr(colname + '.radiusB', 5)
        cmds.setAttr(colname + '.height', 10)
    elif(args[0] =='iplane'):
        colname = collider.iplane()
    cmds.textScrollList('colliderList', edit=True, a=colname)
    
    if(node):
        if(cmds.objExists(node[0])):
            grp = node[0]+'_collgrp'
            if not(cmds.objExists(grp)):
                cmds.group(w=True, em=True, n=grp)
                cmds.parentConstraint(node[0], grp)
            cmds.setAttr((colname+'.rz'),90)
            cmds.parent(colname, grp, r=True)


def bd_colliderselect():
    
    colist = cmds.textScrollList('colliderList', q=True, si=True)

    if(colist):
        colist = [co for co in colist if cmds.objExists(co)==True]
        cmds.select(colist)
        
    if(colist):
        bdnlist = cmds.ls(type='boneDynamicsNode')
        #cmds.textScrollList('Bdynamics_jointList', edit=True, ra=True)
        txtlist = cmds.textScrollList('Bdynamics_jointList', q=True, ai=True) or []
        for bdn in bdnlist:
            driven = cmds.listConnections((bdn+'.outputRotate'), type='joint')
            joint = driven[0].replace('_driven', '')
            if not(joint in txtlist):
                cmds.textScrollList('Bdynamics_jointList', edit=True, a=joint)

        bdnlist = cmds.listConnections(colist[0],d=True,type= 'boneDynamicsNode') or[]
        bdnlist = set(bdnlist)
        cmds.textScrollList('Bdynamics_jointList', e=True, da=True)
        if(bdnlist):
            bdnlist = set(bdnlist)
            for bdn in bdnlist:
                driven = cmds.listConnections((bdn+'.outputRotate'), type='joint')
                joint = driven[0].replace('_driven', '')
                cmds.textScrollList('Bdynamics_jointList', e=True, si=joint)


def collider_connect(collider=None,connectlist=[]):
    colliders = []
    jointlist = []
    connectCount = 0
    colliders.insert(0, collider)
    jointlist = list(connectlist)
    if not(collider):
        colliders = cmds.textScrollList('colliderList', q=True, si=True)
    if not(connectlist):
        jointlist = cmds.textScrollList('Bdynamics_jointList', q=True, si=True)
    if not(jointlist):
        return
    
    for coll in colliders:
        for joint in jointlist:
            if not (cmds.objExists(joint + '_driven') ):
                continue
            ind = 0
            connectCount += 1
            bdn = cmds.listConnections((joint + '_driven.rotate'), type='boneDynamicsNode')
            bdnc = cmds.listConnections(coll,type='boneDynamicsNode') or []
            if not (bdn[0] in bdnc):
                colltype = cmds.getAttr((coll+'.colliderType'))
                if(colltype == 'sphere'):
                    while True:
                        cc = cmds.listConnections((bdn[0] + '.sphereCollider['+str(ind)+'].sphereColMatrix'))
                        if(cc==None):
                            break
                        ind += 1
                    cmds.connectAttr((coll+'.worldMatrix[0]'), (bdn[0] + '.sphereCollider['+str(ind)+'].sphereColMatrix'), force=True)
                    cmds.connectAttr((coll+'.radius'), (bdn[0] + '.sphereCollider['+str(ind)+'].sphereColRadius'), force=True)
                
                elif(colltype == 'capsule' or colltype == 'capsule2'):
                    nubs = cmds.listRelatives(coll,ad=True,type='transform')
                    nubs = [s for s in nubs if 'Sphere' in s]
                    radiusA = '.radius'
                    radiusB = '.radius'
                    if(colltype == 'capsule2'):
                        radiusA = '.radiusA'
                        radiusB = '.radiusB'
                    while True:
                        cc = cmds.listConnections((bdn[0] + '.capsuleCollider['+str(ind)+'].capsuleColMatrixA'))
                        if(cc==None):
                            break
                        ind += 1
                    cmds.connectAttr((nubs[0]+'.worldMatrix[0]'), (bdn[0] + '.capsuleCollider['+str(ind)+'].capsuleColMatrixA'), force=True)
                    cmds.connectAttr((nubs[1]+'.worldMatrix[0]'), (bdn[0] + '.capsuleCollider['+str(ind)+'].capsuleColMatrixB'), force=True)
                    
                    cmds.connectAttr((coll + radiusA), (bdn[0] + '.capsuleCollider['+str(ind)+'].capsuleColRadiusA'), force=True)
                    cmds.connectAttr((coll + radiusB), (bdn[0] + '.capsuleCollider['+str(ind)+'].capsuleColRadiusB'), force=True)

                elif(colltype == 'infinitePlane'):
                    while True:
                        cc = cmds.listConnections((bdn[0] + '.infinitePlaneCollider['+str(ind)+'].infinitePlaneColMatrix'))
                        if(cc==None):
                            break
                        ind += 1
                    cmds.connectAttr((coll+'.worldMatrix[0]'), (bdn[0] + '.infinitePlaneCollider['+str(ind)+'].infinitePlaneColMatrix'), force=True)
    return connectCount

def collider_disconnect(self):
    colliders = cmds.textScrollList('colliderList', q=True, si=True)
    jointlist = cmds.textScrollList('Bdynamics_jointList', q=True, si=True)
    if not(jointlist):
        return    
    for coll in colliders:
        bdnc = cmds.listConnections(coll,type='boneDynamicsNode') or []
        if not(bdnc):
            break
        for joint in jointlist:
            colconnect = cmds.listConnections(coll,p=True)
            coltype = cmds.getAttr(coll + '.colliderType')
            if('capsule' == coltype or 'capsule2' == coltype):
                nurb = cmds.listRelatives(coll)
                nurb = [s for s in nurb if 'Sphere' in s]
                for n in nurb:
                    nu = cmds.listConnections(n,p=True)
                    colconnect = colconnect + nu
            bdn = cmds.listConnections((joint + '_driven.rotate'), type='boneDynamicsNode')
            attlist = [s for s in colconnect if bdn[0] in s]
            attlist = set(attlist)
            for att in attlist:
                col = cmds.listConnections(att,s=True,p=True)
                cmds.disconnectAttr(col[0],att)


def collider_build(*args):
    global bone_dynamics_data
    
    colliders = cmds.textScrollList('colliderList', q=True, si=True)
    for coll in colliders:
        colltype = bone_dynamics_data['collider_list'][coll]['coltype']
        jointlist = list(bone_dynamics_data['collider_list'][coll]['connect'])
        if(colltype =='sphere'):
            colname = collider.sphere()
            radiusVal = bone_dynamics_data['collider_list'][coll]['radius']
            cmds.setAttr((colname + '.radius'), radiusVal)

        elif(colltype =='capsule'):
            colname = collider.capsule()
            heightVal = bone_dynamics_data['collider_list'][coll]['height']
            cmds.setAttr((colname + '.height'), heightVal)
            radiusVal = bone_dynamics_data['collider_list'][coll]['radius']
            cmds.setAttr((colname + '.radius'), radiusVal)

        elif(colltype =='capsule2'):
            colname = collider.capsule2()
            heightVal = bone_dynamics_data['collider_list'][coll]['height']
            cmds.setAttr((colname + '.height'), heightVal)
            radiusVal = bone_dynamics_data['collider_list'][coll]['radiusA']
            cmds.setAttr((colname + '.radiusA'), radiusVal)
            radiusVal = bone_dynamics_data['collider_list'][coll]['radiusB']
            cmds.setAttr((colname + '.radiusB'), radiusVal)

        elif(colltype =='infinitePlane'):
            colname = collider.iplane()
        connectCount = collider_connect(collider=coll ,connectlist=jointlist)
        if(connectCount==0):
            cmds.delete (colname)
            print('boneDynamics does not exist')
            continue
        parentNode=''
        if('parent' in bone_dynamics_data['collider_list'][coll]):
            parentNode = bone_dynamics_data['collider_list'][coll]['parent']
        if(parentNode):
            if(cmds.objExists(parentNode)):
                grp = parentNode+'_collgrp'
                if not(cmds.objExists(grp)):
                    cmds.group(w=True, em=True, n=grp)
                    cmds.parentConstraint(parentNode, grp)
                cmds.parent(colname, grp, r=True)

        tra = bone_dynamics_data['collider_list'][coll]['translate']
        cmds.setAttr((colname + '.t'), *tra)

        rot = bone_dynamics_data['collider_list'][coll]['rotate']
        cmds.setAttr((colname + '.r'), *rot)


def collider_visibility(self):
    colliders = cmds.textScrollList('colliderList', q=True, si=True)
    for collider in colliders:
        if(cmds.objExists (collider)):
            condition = cmds.getAttr((collider + '.v'))
            if(condition):
                cmds.setAttr((collider + '.v'), 0) 
            else:
                cmds.setAttr((collider + '.v'), 1) 


def collider_delete(self):
    colliders = cmds.textScrollList('colliderList', q=True, si=True)
    for col in colliders:
        colgrp = cmds.listRelatives(col,p=True)
        if(cmds.objExists (colgrp[0])):
            cmds.delete(colgrp)
        elif(cmds.objExists (col)):
            cmds.delete(col)
            
    cmds.textScrollList('colliderList', e=True, ri=colliders)

    
def Remove_dict_data():
    global bone_dynamics_data
    chainlist = cmds.textScrollList('Bdynamics_chainList', q=True, si=True)
    bone_dynamics_remove
    for joint in chainlist:
        if joint in bone_dynamics_data['source_joint']:
            jointList = bone_dynamics_data['source_joint'][joint]
            bone_dynamics_data['source_joint'].pop(joint)
        if joint in bone_dynamics_data['driven_list']:
            bone_dynamics_data['driven_list'].pop(joint)
        if joint in bone_dynamics_data['add_joint']:
            bone_dynamics_data['add_joint'].pop(joint)
        if joint in bone_dynamics_data['target_list']:
            bone_dynamics_data['target_list'].pop(joint)
        if joint in bone_dynamics_data['ctrl_list']:
            bone_dynamics_data['ctrl_list'].pop(joint)
        if joint in bone_dynamics_data['dynamics_attr']:
            for jit in jointList:
                if bone_dynamics_data.get('dynamics_attr',{}).get(jit):
                    bone_dynamics_data['dynamics_attr'].pop(jit)
            cmds.textScrollList('Bdynamics_chainList', edit=True, removeItem=joint)

def bone_dynamics_ui():

    if (cmds.window('bone_dynamics_editwindow',q=1,ex=1)):
        cmds.deleteUI('bone_dynamics_editwindow')
    window = cmds.window('bone_dynamics_editwindow', title='bone_dynamics_edit', widthHeight=(400, 500) )
    cmds.about(q=1, v=1), cmds.about(q=1, cd=1), cmds.about(q=1, ct=1), cmds.file(q=1, sn=1)
    wval=300
    wb=140
    cmds.scrollLayout(bv=True,cr=True,mcw=340 ,horizontalScrollBarThickness=16,verticalScrollBarThickness=16)
    
    #form = cmds.formLayout()
    # このパイソンのパスを取得するコード
    script_path = os.path.abspath(__file__)
    script_path= os.path.dirname(script_path)
    mdpath = script_path +'\yjp_boneDynamicsNode_ui_en.md'
    cmds.button(label='Help', h=20, command=lambda *args: os.system('start ' + mdpath))
    ###############################################################################
    preset = cmds.frameLayout( label='preset', cll=True )
    # set library : jsonのパス

    json_path = cmds.workspace( q=True, rd=True )
    json_path =(json_path+'bdn')
    if not(os.path.isdir(json_path)):
        cmds.sysFile( json_path, makeDir=True )
    cmds.text('bdjson_path', l=json_path)
    #cmds.textField(w=400)
    
    cmds.paneLayout( configuration='vertical2' )

    # json list 
    cmds.textScrollList('Bdynamics_jsonList', numberOfRows=6, allowMultiSelection=True)
    cmds.popupMenu()
    cmds.menuItem(label='Open',c=bone_dynamics_jsonopen)
    
    cmds.columnLayout( adjustableColumn=False )
    #preset save : プリセットセーブ
    cmds.button( label='Preset Save',w=wb, c=bone_dynamics_save)
    #preset save : プリセットセーブ
    #cmds.button( label='preset newsave',w=150, c=bone_dynamics_save(['new']))

    #preset load : プリセットパス変更
    cmds.button( label='Preset Load',w=wb, c=bone_dynamics_load)
    #cmds.button( label='dict reload',w=150, c=boneDynamics_datadict)

    cmds.setParent( '..' )

    cmds.setParent( '..' )

    cmds.setParent( '..' )
    ###############################################################################
    #bdui = cmds.scrollLayout(horizontalScrollBarThickness=16,verticalScrollBarThickness=16)
    
    buttong = cmds.frameLayout( label='Manual Build', cll=True )
    cmds.rowColumnLayout( numberOfColumns=3, columnWidth=[(1,160), (2,90), (3,90)],
                        columnAttach=[(1, 'both', 5), (2, 'both', 5), (3, 'both', 5)] )

    #Joint selection and build : ジョイント選択後押すボタンcommand=do_boneDynamics_create
    cmds.button('Jointbuild', w=wb, label='Build selected joints',command=partial(do_boneDynamics_create,'none') )

    #Target Use checkbox : ターゲット使用チェックボックス
    cmds.checkBox('bone_dynamics_targetcheck', label='Use Target' ,v=True)

    #Add end checkbox : 末端追加チェックボックス
    cmds.checkBox('bone_dynamics_addEndcheck', label='Add child' )

    cmds.setParent( '..' )
    
    #cmds.columnLayout( adjustableColumn=True )
    cmds.setParent( '..' )
    cmds.frameLayout( label='Build and Bake', cll=True )
    
    cmds.paneLayout(w=340,configuration='vertical2')
    #cmds.rowColumnLayout( numberOfColumns=3, columnWidth=[(1, 130), (2, 130), (3, 130)],columnAttach=[(1, 'both', 5), (2, 'both', 5), (3, 'both', 5)] )
    cmds.columnLayout( adjustableColumn=True )
    
    cmds.text('Chain Root List',w=wb)
    #chain: チェーンリスト
    cmds.textScrollList('Bdynamics_chainList',w=wb, numberOfRows=8, allowMultiSelection=True,sc=boneDynamics_BDRefresh)
    #cmds.popupMenu()
    #cmds.menuItem()
    #cmds.menuItem()
    #cmds.menuItem()
    #Delete Select dynamics : デリートセレクトジョイント
    #cmds.button( label='Delete Select dynamics',w=125, c=bone_dynamics_delete)
    
    cmds.setParent( '..' )   

    cmds.columnLayout(adjustableColumn=False )

    cmds.button('ChainBuildbutton', label='Chain Build',w=wb,c=partial(do_boneDynamics_create,'json'))

    #bake select joint : ベイクチェーンcommand=defaultButtonPush
    cmds.button('ChainBakedbutton', label='Chain Bake',w=wb,c=bone_dynamics_bake)
    
    cmds.button('ChainRemovebutton', label='Dynamics Remove',w=wb, c=bone_dynamics_remove)

    cmds.button( label='Chain Delete',w=wb, c=lambda *args: Remove_dict_data())

    cmds.setParent( '..' )
    cmds.setParent( '..' )
    cmds.setParent( '..' )
    cmds.setParent( '..' )

    #cmds.rowColumnLayout( numberOfColumns=3, columnWidth=[(1, 175), (2, 175), (3, 175)],columnAttach=[(1, 'both', 5), (2, 'both', 5)] )
    
    cmds.setParent( '..' )
    ###############################################################################
    bdnlist = cmds.frameLayout( label='target list', cll=True )
    cmds.paneLayout(w=340, st=5,configuration='vertical2')

    cmds.columnLayout( adjustableColumn=True )
    
    cmds.text('Target List',w=120)
    
    #Controller scroll list to manipulate target: ターゲットを動かす既存コントローラ指定スクロールリスト
    cmds.textScrollList('Bdynamics_targetList',w=100, numberOfRows=8, allowMultiSelection=True,sc=bd_targetselect)
    
    cmds.button( label='Connect Target Ctrl',w=120,c=partial(connect_target_ctrl))    
    
    cmds.setParent( '..' )

    cmds.columnLayout(adjustableColumn=True)
    cmds.text('Ctrl List',w=120)

    #FK: FKリスト
    cmds.textScrollList('Bdynamics_ctrlList',w=100, numberOfRows=8, allowMultiSelection=True,sc=bd_ctrlselect)

    cmds.button( label='Selected Get Ctrl',w=120,c=lambda *args: selected_get_ctrl())
    
    cmds.setParent( '..' )
    cmds.setParent( '..' )
    cmds.setParent( '..' )
    cmds.setParent( '..' )
    ###############################################################################
    #Dynamics Parameters : ダイナミクスパラメーター
    bdnattr = cmds.frameLayout( label='boneDynamics_attr', cll=True)
    
    #cmds.scrollLayout(horizontalScrollBarThickness=16,verticalScrollBarThickness=16)
    ########################
    cmds.paneLayout(configuration='vertical2')
            
    #Joint: ジョイントリスト
    ########################
    cmds.columnLayout( adjustableColumn=True )

    cmds.text('Joint List')

    cmds.textScrollList('Bdynamics_jointList',w=120, numberOfRows=20, allowMultiSelection=True,sc=boneDynamics_dataRefresh)

    cmds.setParent( '..' )

    ########################
    cmds.columnLayout( adjustableColumn=True )

    cmds.intFieldGrp('BDNresetTime', l='resetTime', en=False, cw2=[92,40], v1=0, cc=partial(boneDynamics_dataEdit,'resetTime'))
    cmds.floatSliderGrp('BDNdamping', l='damping', en=False, adj=3, cw3=[92,40,100], f=True, min=0.1, max=1.0, fmn=0.01, fmx=1.0, v=0.01, cc=partial(boneDynamics_dataEdit,'damping'))
    cmds.floatSliderGrp('BDNelasticity', l='elasticity', en=False, adj=3, cw3=[92,40,100], f=True, min=0.0, max=100.0, fmn=0.0, fmx=100.0, v=30, cc=partial(boneDynamics_dataEdit,'elasticity') )
    cmds.floatSliderGrp('BDNstiffness', l='stiffness', en=False, adj=3, cw3=[92,40,100], f=True, min=0.0, max=10.0, fmn=0.0, fmx=10.0, v=0, cc=partial(boneDynamics_dataEdit,'stiffness') )
    cmds.floatSliderGrp('BDNmass', l='mass', en=False, adj=3, cw3=[92,40,100], f=True, min=0.0, max=5.0, fmn=0.0, fmx=5.0, v=1, cc=partial(boneDynamics_dataEdit,'mass') )
    cmds.floatSliderGrp('BDNgravityX', l='gravityX', en=False, adj=3, cw3=[92,40,100], f=True, min=-1000.0, max=1000.0, fmn=-1000.0, fmx=1000.0, v=0, cc=partial(boneDynamics_dataEdit,'gravityX') )
    cmds.floatSliderGrp('BDNgravityY', l='gravityY', en=False, adj=3, cw3=[92,40,100], f=True, min=-1000.0, max=1000.0, fmn=-1000.0, fmx=1000.0, v=-980, cc=partial(boneDynamics_dataEdit,'gravityY') )
    cmds.floatSliderGrp('BDNgravityZ', l='gravityZ', en=False, adj=3, cw3=[92,40,100], f=True, min=-1000.0, max=1000.0, fmn=-1000.0, fmx=1000.0, v=0, cc=partial(boneDynamics_dataEdit,'gravityZ') )
    cmds.floatSliderGrp('BDNgravityMultiply', l='gravityMultiply', en=False, adj=3, cw3=[92,40,100], f=True, min=0.0, max=1, fmn=0.0, fmx=1.0, v=1.0, cc=partial(boneDynamics_dataEdit,'gravityMultiply') )
    
    cmds.checkBoxGrp('BDNenableAngleLimit', l='enableAngleLimit', cw2=[92,40], v1=0, cc=partial(boneDynamics_dataEdit,'enableAngleLimit'))
    
    cmds.floatSliderGrp('BDNangleLimit', l='angleLimit', en=False, adj=3, cw3=[92,40,100], f=True, min=0, max=180, fmn=0, fmx=180.0, v=90, cc=partial(boneDynamics_dataEdit,'angleLimit') )
    cmds.floatSliderGrp('BDNradius', l='radius', en=False, adj=3, cw3=[92,40,100], f=True, min=0, max=20.0, fmn=0, fmx=20, v=4, cc=partial(boneDynamics_dataEdit,'radius') )

    cmds.intFieldGrp('BDNiterations', l='iterations', en=False, cw2=[92,40], v1=5, cc=partial(boneDynamics_dataEdit,'iterations') )
    
    cmds.checkBoxGrp('BDNenableGroundCol', l='enableGroundCol', cw2=[92,40], v1=0, cc=partial(boneDynamics_dataEdit,'enableGroundCol') ) 

    cmds.floatSliderGrp('BDNgroundHeight', l='groundHeight', en=False, adj=3, cw3=[92,40,100],f=True, min=-10.0, max=10.0, fmn=-100.0, fmx=100.0, v=0, cc=partial(boneDynamics_dataEdit,'groundHeight') )
    
    cmds.setParent( '..' )
    ########################
    cmds.setParent( '..' )
    cmds.setParent( '..' )
    ########################
    cmds.frameLayout( label='collider_create', cll=True)
    ########################
    cmds.rowColumnLayout( numberOfColumns=4, columnWidth=[(1,90), (2,90), (3,90), (4,90)],
                                columnAttach=[(1, 'both', 5), (2, 'both', 5), (3, 'both', 5), (4, 'both', 5)] ) 
    cmds.button( label='sphere',w=80,c=partial(collider_create,'sphere'))
    cmds.button( label='capsule',w=80,c=partial(collider_create,'capsule'))
    cmds.button( label='capsule2',w=80,c=partial(collider_create,'capsule2'))
    cmds.button( label='iplane',w=80,c=partial(collider_create,'iplane'))
    cmds.setParent( '..' )
    cmds.setParent( '..' )
    ########################
    cmds.frameLayout( label='collider', cll=True)
    ########################
    cmds.paneLayout(configuration='vertical2')

    cmds.textScrollList('colliderList',w=wb, numberOfRows=8, allowMultiSelection=True,sc=bd_colliderselect)

    cmds.columnLayout( adjustableColumn=True )


    cmds.button( label='collider_Connect',w=120,c=collider_connect)

    cmds.button( label='collider_Disconnect',w=120,c=collider_disconnect)

    cmds.button( label='collider_Build',w=120,c=collider_build)
    
    cmds.button( label='collider_Visibility',w=120,c=collider_visibility)

    cmds.button( label='collider_Delete',w=120,c=collider_delete)

    cmds.setParent( '..' )

    cmds.setParent( '..' )
    cmds.setParent( '..' )
    #cmds.setParent( '..' )

    ###############################################################################
    #cmds.setParent( '..' )
    #preset buttong bdnlist bdnattr
    cmds.showWindow(window)

    cmds.window('bone_dynamics_editwindow',e=True,widthHeight=(400, 400) )
    
    bone_dynamics_preset_reload()

    load_bonedynamics_fromscene()