# Twitter-Analyze-followers-of-a-specific-account
### このスクリプトは、Twitter APIを使用して、特定のTwitterアカウントのフォロワーの情報を取得し、フォロワーのデータを可視化するためのものです。
### 偽フォロワーの分析に役立ちます。

##### 具体的には、以下のような処理を行っています。
###### Obtain follower information for a specific account v1.0.py 
- 指定されたTwitterアカウントのフォロワーのIDを取得し、IDを使用してフォロワーの情報を取得します。
- 取得した情報はrowsリストに格納され、取得できるフォロワーの数に応じて複数回のAPI呼び出しを行っています。
- rowsリストをデータフレームに変換しCSVファイルに書き出しています。

###### Visualize follower information v1.0.py
- DataFrameオブジェクトを加工してから、Bokehを使ってグラフを作成します。
- colors変数には、「いいね」したことがあるかどうかによって、色を分けるための情報が設定されています。
- 作成したグラフを表示します。
