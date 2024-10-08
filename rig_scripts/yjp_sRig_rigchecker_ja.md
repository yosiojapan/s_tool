# rigchecker 説明書

## 概要

`rigchecker` は、Mayaのリグをチェックするためのスクリプトです。  
このスクリプトは、リグの位置や回転の誤差、コントローラーの存在、接続の有無などを検証し、エラーログを生成します。

指定されたリグIDに対してリグチェックを行い、エラーログを返します。

## 使用方法

1. `rigchecker` コマンドを実行して、リグチェッカーのUIを表示します。
2. `Check` ボタンをクリックして、リグチェックを開始します。
3. エラーログがUIに表示されます。

## 詳細な処理内容

### リグの位置と回転のチェック

リグのコントローラーやジョイントのワールド座標を取得し、保存されたログと比較します。誤差が一定値を超える場合、エラーログに記録します。

### コントローラーの存在チェック

特定のコントローラーが存在するかどうかを確認し、存在しない場合はエラーログに記録します。

### 接続のチェック

コントローラーやメッシュの接続が正しく行われているかを確認し、接続がない場合はエラーログに記録します。

### その他のチェック

- リグのスケールが正しいかどうか
- 特定の属性が存在するかどうか
- IKハンドルのアップベクトルが正しいかどうか
- アニメーションレイヤーの存在チェック。あればエラー
- コントローラーのサイズチェック

## エラーログの保存

エラーログは、リグのSetupディレクトリに `rigerrorlog.txt` として保存されます。

## 注意事項

- スクリプトはsRig専用で動作することを前提としています。
