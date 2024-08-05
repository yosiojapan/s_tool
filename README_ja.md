# S_TOOL

[README](./README.md)

## 概要

- 独学で作成していたMayaツールです。
- バグもあるかと思います。各ツールは使用前に保存してから実行してください。
- このスクリプトの使用によって生じたいかなる損害や問題についても、作者は一切の責任を負いませんので、承知の上でご利用ください。
- Mayaバージョンは2020です。BoneDynamics_uiのみ2025動作確認済みです。
- 他の製作者のMELやプラグインを使用し、さらに効率アップするツールもあります。
- 他の製作者のMELは各自ダウンロードしてください。
- 古いMELもあります。Mayaのデフォルト機能で既に存在している場合もあります。

## インストール方法

- 好きな場所にフォルダを配置
- StartMaya2025_sTool.batなどインストールされたMayaのバージョン名実行する。
- バッチを起動するとメニューにS_TOOLが表示されます。

## 使用言語

- MEL
- python(勉強中)

## 構成

各フォルダにツールが入っています。

- `anim_scripts` : アニメーション関連(sRig用も含む)
- `clip_scripts` : クリップ関連(不要なはずなのでバッチでは除外フォルダ)
- `common_scripts` : 雑多MELです
- `DL_scripts` : DLしたMELを入れておく場所
- `file_scripts` : ファイル関連のMELです。
- `joint_scripts` : ジョイント関連
- `material_scripts` : マテリアル関連
- `modeling_scripts` : モデリング関連
- `module_scripts` : 複数のMELが使用するMELです。直接使うことはありません。
- `plug-ins` : 巨匠たちのプラグインを入れておく場所
  - `boneDynamicsNode.mll` `rotationDriver.py` `weightDriver.mll` など各自入れてみてください。
- `projects_scripts` : 自作のMELを入れる場所
- `py_scripts` : pythonのツールを置いておくところ。
  - `dwpicker` や `expcol` を入れています。
- `rig_module_scripts` : リグ用のMELです。直接使うことはありません。
- `rig_scripts` : 自作リグ関連sRig
- `weight_scripts` : ウエイト関連

## フォルダについて

> 不要であれば削除、またはフォルダの名前を変更すると必要なMELだけ読み込めます。  
ただし `module_scripts` と `py_scripts` のフォルダは削除しないでください。

`rig_scripts` を使用する場合は `rig_module_scripts` こちらも使用します。

## 機能説明

### Modeling

- `Mirror` : オブジェクトミラー・フェースのミラーができる
- `VertexSymmetryMove` : 頂点シンメトリ [Readme](./modeling_scripts/yjp_VertexSymmetryMove_ja.md)
- ~~`UVSymmetryMove` : UV頂点のミラー~~
- `VertexSnap` : 初めに選択したオブジェに次の選択したオブジェクトの頂点を近似値でスナップ。  頂点選択でもOK [Readme](./modeling_scripts/yjp_VertexSnap_ja.md)
- ~~`VertexSnapPlus` : ２つのメッシュの頂点を選択しスナップする。法線やウエイトも同調させる。[Readme](./modeling_scripts/yjp_VertexSnapPlus_ja.md)~~
- `SepalateMaterial` : 選択したオブジェクトのフェースをマテリアル単位でセパレートする
- `Construction` : バインドされたメッシュの中間オブジェクトを編集するビューを開きます [Readme](./modeling_scripts/yjp_Construction_ja.md)
- `WorldCenterPivot` : ピボットをワールドセンターにする
- `FreezeChannel` : 指定した座標を保持したままフリーズトランスフォームさせる  Readme
- `OutLineObjectCreate`指定したオブジェクトの輪郭メッシュを作る
- `curve_cv_select` : カーブのCVを選択する
- `RefreshVertexOfFBX` : FBXのモデルデータの一部のバグを修正する
- `VertexNormalCTRL` : VertexNormalCopyとVertexNormalPasteのUI
- `VertexNormalCopy` : 法線のコピー
- `VertexNormalPaste` : 法線のペースト
- `ModelCheck` : モデルシーン内のデータをチェックする [Readme](./modeling_scripts/yjp_ModelCheck_ja.md)

---

- `mCombine` : リンク不明 [**movie**](https://vimeo.com/47843888)

### Texture

- `ChangeTexPathtolocal` : テクスチャパスをローカルパスに変更する
- `UpdateTexturesAuto` : テクスチャーの更新をMayaに反映するMELだが、今はもういらないかも。
~~- UVpattern~~

### Joint

- `RelocationJoint` : スケール調整したジョイントをスケール1で作り直す。
- `yjp_preferredAngleZero` : preferredAngleを0にします。

---

- `templateSkeletonLE` : ジョイントチェーンを作成とチェーンのリビルド。  
Maya6.0の時代のMELで、DLできる場所が不明なので、こちらに置いておきます。
- `cometJointOrient` : ジョイントオリエントを編集するMEL  
こちらももうリンクがない。  
- LMrigger : cometJointOrient の上位版 [こちらでDL](https://luismiherrera.gumroad.com/l/LMrigger?layout=profile)

> [cometJointOrientとLMriggerの解説サイト](https://inopoa.com/maya-rigging-joint-orient/#index_id6)

### Weight

- `PaintSikinWeightButton` : ウエイトブラシのui。ウエイト量をボタンで切り替えるだけ。
- `WeightEdit` : 1頂点単位でウエイトをスライドバーで調整 [**Readme**](./weight_scripts/yjp_WeightEdit_ja.md)
- `ShellWeight` : バグあり。複数頂点と１つのジョイントを選択して実行。繋がったポリゴンが選択されウエイト１でジョイントとバインドされる
- `VUW_Symmetry` : ウエイトシンメトリー [**Readme**](./weight_scripts/yjp_VUW_Symmetry_ja.md)
- `yjp_BindPoseCoordinateCheck` : バインドポーズをするとずれるかチェック
- `yjp_SeparateMeshWeight` : スキンクラスタがあればウエイトもコピー
- `yjp_ShellWeight` : 複数頂点と１つのジョイントを選択して実行すると繋がったポリゴンが選択されウエイト１でジョイントとバインドされる
- `DoraSkinWeightImpExp` : ウエイトをセーブロードできるMEL[こちらでDL](http://dorayuki.com/doramaya/doraskinweightimpexp.html)  
`DL_scripts` フォルダに `DoraSkinWeightImpExp.mel` を置いてください  
DoraSkinWeightImpExpを使用したほかのMELが以下になります。
  - `DuplicateMeshSkin` : 複製してウエイトを維持する
  - `CombineMeshSkin` : 選択した２このオブジェクトをマージしてウエイトもマージする
  - `SeparateMeshSkin` : 選択したフェースをセパレートしてウエイトを維持する
  - `QuickDoraSkinWeightExport` : オブジェクト名でウエイトをwds形式で保存します
  - `QuickDoraSkinWeightImport` : オブジェクト名のウエイトを探してIDでウエイト読み込みします
  - `DetachBindShelf` : バインド情報を保存してデタッチします。オブジェ名シェルフで再バインド
  - `ReBind` : ヒストリーを消して再バインド
  - `RebindShelf` : ヒストリーを消しシェルフに保存後、再バインド
  - `ImitateBind` : 初めに選択したオブジェのバインド情報で次に選択したオブジェにバインド。
  - `DoraVertexWeightPaste` : 選択した頂点にウエイトをペーストします
  - `DoraVertexWeightCopy` : 選択した頂点のウエイトをコピーします

### sRig

- `sRig` : リグの作成 [**Readme**](./rig_scripts/yjp_sRig_ja.md)
- `sRig CTRL Edit` : リグコントローラのカーブを編集する [**Readme**](./rig_scripts/yjp_sRg_CTRL_Edit_ja.md)
- `Loads file and Replace sRigCTRL` : ファイルを読み込んでリグコントローラを置き換える
~~- `CTRL List` : リグコントローラのリスト。コントローラー選択ツール~~
- `sRig Checker` : sRigにエラーがないかチェックする [**Readme**](./rig_scripts/yjp_sRig_rigchecker_ja.md)
- `sRig PoseMirror` : sRigコントローラーのポーズをX反転する [**Readme**](./rig_scripts/yjp_poseMirror_ja.md)
- `sRig CTRL AllSelect` : キャラクターコントローラ全てが選択される
- `FK to IK` : FKctrlをIKctrlに変換
- `FK to IK AllFrame` : タイムスライダー範囲すべての FKctrl を IKctrl に変換
- `IK_to_FK` : IKctrl を FKctrl に変換
- `IK to FK AllFrame` : タイムスライダー範囲すべての IKctrl を FKctrl に変換
- `IK Length Limit 0.0` : 伸びきったIKをジョイントの長さにコントローラーを合わせる
- `IK Length Limit 1.0` : 伸びきったIKをジョイントの長さにコントローラーを合わせ少し曲げる
- `Constraint Table Edit` : csvファイルを作って複数のペアレントコンストレインをするツール [**Readme**](./rig_scripts/yjp_ConstraintTableEdit_ja.md)
- `sRig_ConstraintSwitch` : 複数コントローラーを選択後タイムスライダ範囲選択で親を切り替える
  - 各ナンバーでリグで設定した親に切り替わる
- `sRig Motion Check` : sRigで作成したモーションでエラーを検索します。[Readme作成中](./rig_scripts/yjp_MotionCheck.mel_ja.md)

### Animation

- `Pose Copy Paste` : 選択したノードのポーズコピーペースト [**Readme**](./anim_scripts/yjp_PoseCopyPaste_ja.md)
- `TRS Copy Paste` : オブジェクトがオブジェクトを追従するようにベイク [**Readme**](./anim_scripts/yjp_TRS_CopyPaste_ja.md)
- `Every Frame MEL` : 毎フレーム記述したMELを実行する [**Readme**](./anim_scripts/yjp_EveryFrameMEL_ja.md)
- `Time Offset 0` : シーンの全キーを0フレームに寄せる
- `Time Offset UI` : シーンの全キーをずらす
- `FBX Animation Convert` : 実行するとシーン内のアルファアニメUVアニメビジビリティアニメを別ノードチャンネルに渡します。値は100倍にしてます [**Readme**](./anim_scripts/yjp_FBXAnimationConvert_ja.md)
- `Add Const Node` : 選択したノードをコンストレインするロケーターを追加する
- `anim cutOut Of Range` : タイムスライダー選択した範囲外のキーを削除
- `Smooth Curve` : カーブのキーを選択してキースムーズにする
- `Loop Curve` : ループモーションを作るためカーブの最初のフレームと最後のフレームを調整
- `Animation Work Tool` : アニメーション関連ツールセット
- `MotionCopy` : 主にsRigにモーションを移植する [**Readme**](./anim_scripts/yjp_MotionCopy_ja.md)
- `FPS 30` : FPSを30にする
- `sRig_GlobalFollow` : Groundコントローラが動かされて足と地面の滑りをなくします [**Readme**](./anim_scripts/yjp_GlobalFollow_ja.md)

---

- `oaSmoothKeys` : [highend3](https://www.highend3d.com/maya/script/oasmoothkeys-for-maya) 選択したキーをスムーズにする
- `DWpicker` : リグピッカー [Dreamwall PickerはこちらからDL](https://github.com/DreamWall-Animation/dwpicker)
- `BoneDynamics_ui` : 揺れものを自動化する`boneDynamicsNode`を使って簡単に追加、編集、ベイク、セーブ、ロードができるツールです。 [**Readme**](./py_scripts/bdn/yjp_boneDynamicsNode_ui_ja.md)  
[boneDynamicsNode はこちらからDL](https://github.com/akasaki1211/boneDynamicsNode)  
plug-ins フォルダに `boneDynamicsNode.mll` を置きます。  
[maya_expressionCollision はこちらからDL](https://github.com/akasaki1211/maya_expressionCollision)  
py_scripts フォルダに expcol も置きます。

### File

- `Open project folder` : プロジェクトフォルダを開く
- `Run MEL to MB` : 複数のシーンで任意のMELを順次実行
- `Scene Search` : 複数のシーンで任意のMELを順次実行し調査する
- `MB To MA` : フォルダ内のmbをmaで保存
- `FBX To MB` : フォルダ内のfbxをmbで保存
- `MA to MB` :フォルダ内のmbをmbで保存
- `MB To FBX` : フォルダ内のmb,maをfbxで保存
- `ATOM Export` : ATOM Export

### Etc

- `MEL_LanguageEdit` : ツールの説明文を英語と日本語を切り替えます
- `Cameras follow` : 選択したノードに追従するビューを作ります
- `All Back ground Color` : シーン内全てのカメラBGカラーを変更する
- `Replaces Word` : シーン内すべてのノード名を置換する。左に検索単語、右に置き換え単語を入力
- `同名ノードチェック` : シェイプも含めた同名ノードを検索して選択する
- `全ての同名ノードをリネーム` : シーン内の同名ノードすべてを自動リネーム

---

- `View Capture` : ViewCapture
- `Box Capture` : 6方向からのキャプチャー
- `View To Shelf` : ビューの表示状態をシェルフに保存
- `View Show Custom` : ビュー編集ウインドウ
- `Show all layers` : すべてのレイヤーを表示する

---

- `ALL Import Reference` : シーン内のリファレンスを全てインポートする
- `Reference SetAttr Remove` : リファレンスが編集された情報を削除する

---

- `Unknown Plugin Delete` : 使用しないプラグインをシーンから削除します
- `Window Delete` : ほとんどのウインドウを閉じる

- `Hide Remove Reference` : アンロードのリファレンスを全て削除する
- `Delete Reference` : トランスフォームノードをリファレンスか調べて孤立したリファレンスノードを削除します
- `Render Layer Delete` : レンダーレイヤーを削除
- `ReLoadMenu` : STOOLのメニューリロード
- `CleanUp Scene Model` : リファレンス、不要プラグイン、unknownノードなどを削除してから最適化
- `Node UnLock` : 複数のノード選択して実行するとすべてアンロックする

### DLscript

- `AriSceneOpener` : ファイルを開く便利なMEL [DLはこちらから](http://cgjishu.net/blog-entry-261.html)

## MELを追加する場合

プロシージャー名とmelファイル名を同じにします。  
`projects_scripts`フォルダに置きます。  
するとDL_scriptsメニューに追加されます。  
引数があるMELを追加したい場合は `module_scripts` フォルダに置いてください。

## ライセンス

- Licenseファイルをご覧ください。

## サポート

基本的にサポートはできません。

2024/7/12 Mayaから離れてしまうので、次回修正日は未定です。
