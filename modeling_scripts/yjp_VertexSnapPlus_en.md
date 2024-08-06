# VertexSnapPlus MEL Script

## 概要

`VertexSnapPlus`は、選択した頂点やオブジェクトをスナップするためのMELスクリプトです。  
このスクリプトは、法線やウエイトの調整もサポートしています。


## UIの構成

- **チェックボックス**:
  - 法線の一致 (`vspNormalMatcheCheck`)
  - スナップの平均 (`vspAverageCheck`)
  - ボーダーエッジのみ (`vspBoEdgeCheck`)
  - 法線の調整 (`vspNormalTuningCheck`)
  - ウエイトの調整 (`vspWeightTuningCheck`)

- **ボタン**:
  - `Apply`ボタン: `do_VertexSnapPlus`を実行。
  - `Close`ボタン: ウィンドウを閉じる。

## 使用方法

1. `VertexSnapPlus`を実行してUIを表示。
2. 必要なオプションを設定し、`Apply`ボタンをクリックしてスナップを実行。

## 注意点

- スクリプトは選択されたオブジェクトや頂点に対してのみ動作します。
- 選択が2つ未満の場合、スクリプトは警告を表示して終了します。
