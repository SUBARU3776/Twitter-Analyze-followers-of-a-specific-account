# Twitter-Analyze-followers-of-a-specific-account
### このスクリプトはTwitter APIを使用して特定のTwitterアカウントのフォロワーの情報を取得し、フォロワーのデータを可視化するためのものです。
### 偽フォロワーの分析に役立ちます。

##### 具体的には、以下のような処理を行っています。
###### Obtain follower information for a specific account v1.0.py 
- 指定されたTwitterアカウントのフォロワーのIDを取得し、IDを使用してフォロワーの情報を取得します。
- 取得した情報はrowsリストに格納され、取得できるフォロワーの数に応じて複数回のAPI呼び出しを行っています。
- rowsリストをデータフレームに変換しCSVファイルに書き出しています。

###### Visualize follower information v1.0.py
- colors変数には、「いいね」したことがあるかどうかによって、色を分けるための情報が設定されています。
- DataFrameオブジェクトを加工してから、Bokehを使ってグラフを作成します。<br>
*******************************************************************************************************************************************************
### This script uses the Twitter API to retrieve information about followers of a specific Twitter account and visualize the follower data.
### It is useful for analyzing fake followers.

##### Specifically, the following process is used
###### Obtain follower information for a specific account v1.0.py 
- Obtains follower IDs for a specific Twitter account and uses the IDs to obtain follower information.
- The acquired information is stored in arows list and multiple API calls are made depending on the number of followers that can be acquired.
- The rows list is converted to a data frame and exported to a CSV file.

###### Visualize follower information v1.0.py
- The colors variable is set to the information used to divide the colors according to whether or not the user has ever "liked" the site.
- After processing the DataFrame object, a graph is created using Bokeh.
