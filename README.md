# 課題4

## 4-1

線形回帰分析を行う課題です。ファイル[data.txt](./data.txt)には、pythonスクリプト[generate_data.py](./generate_data.py)によって生成された擬似的なデータが格納されています。1列目は従属変数Yの値、2列目は独立変数Xの値です。

[data.txt](./data.txt)を読み込んで線形回帰分析を行い、

1. 傾きの推定値
2. 傾きのP値
3. 切片の推定値
4. 相関係数

を画面に出力するスクリプトregression.pyを作成しなさい。**出力の内容がoutput_sample.txtの内容と同じになるように**スクリプト[regression.py](./regression.py)を作成しなさい。P値以外の数値は小数点5位で丸めてください。注; 回帰分析の結果はサンプルと完全に一致するとは限りません。ちなみに傾きと切片の真の値はそれぞれ-0.8と12です。

## 4-2

線形回帰分析から得られた傾きと切片の推定値を用いて、各データ点についてXの値からYの予測値を計算しなさい。またYの実測値からYの予測値を引いたもの(残差)を計算しなさい。これらYの予測値と残差を、Yの実測値およびX値とともにファイルprediction.txtに出力するコードを、課題4-1のコードに続けてスクリプト[regression.py](./regression.py)内に記述しなさい。prediction.txtのサンプルをprediction_sample.txtとして添付しておきますので、出力ファイルがこれと同じになるようにスクリプトを作成してください。1列目がXの値、2列目がYの実測値、3列目がYの予測値、4列目が残差です。数値は全て小数点5位で丸めてください。注; 予測値や残差はサンプルと完全に一致するとは限りません。
