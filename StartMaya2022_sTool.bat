echo ---- Start Maya 2022 S_TOOL script ----

set MOL=module_scripts;
set COM=common_scripts;
set MOD=modeling_scripts;
set MAT=material_scripts;
set JNT=joint_scripts;
set WGT=weight_scripts;
set RIGM=rig_module_scripts;
set RIG=rig_scripts;
set ANI=anim_scripts;
set FIL=file_scripts;
set DL=DL_scripts;
set PRO=projects_scripts;

set CLP=clip_scripts;

set PYT=py_scripts;
set plug=plug-ins;

set MAYA_SCRIPT_PATH=%~dp0%MOL%^
%~dp0%COM%^
%~dp0%MOD%^
%~dp0%MAT%^
%~dp0%JNT%^
%~dp0%WGT%^
%~dp0%RIGM%^
%~dp0%RIG%^
%~dp0%ANI%^
%~dp0%FIL%^
%~dp0%DL%^
%~dp0%PRO%
REM %~dp0%CLP%
set MAYA_PLUG_IN_PATH=%~dp0%plug%
set PYTHONPATH=%~dp0%PYT%

SET MAYA_UI_LANGUAGE=en_US
REM SET MAYA_UI_LANGUAGE=ja_JP
start "" "C:\Program Files\Autodesk\Maya2022\bin\maya.exe" -hideConsole
REM start "" "C:\Program Files\Autodesk\Maya2022\bin\maya.exe" -hideConsole -noAutoloadPlugins