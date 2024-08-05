# -*- coding: utf-8 -*-
#yjp_AddKeyToAnimCurveUU
def main(animCurve,start,end):
    from maya.api import OpenMaya as om
    from maya.api import OpenMayaAnim as oma
    node = om.MGlobal.getSelectionListByName(animCurve)
    anim = oma.MFnAnimCurve(node.getDependNode(0))
    # (Time, Value)
    anim.addKey(start, end)