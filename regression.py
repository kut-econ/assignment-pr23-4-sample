# 課題4-1のプログラム
# %%
# 必要なモジュールの読み込み
import numpy as np
from scipy import stats

# ファイルからデータの読み込み
with open('./data.txt','r') as file:
    lines = file.readlines()

# Y値のリストを変数Yに、X値のリストを変数X
# に代入する
Y = [float(line.split(' ')[0]) for line in lines[1:]]
X = [float(line.split(' ')[1]) for line in lines[1:]]

# %%
# ここに適切なコードを書き、課題4-1のプログラムを完成
# させてください。下記の説明に従ってください。
# 
# 上記のセルを実行すると、変数YにはY(従属変数)の値の
# リストが、変数XにはX(独立変数)の値のリストが代入さ
# れた状態になります。これらのリストを配列に変換して
# 回帰分析を実行し、
#
# (1) 傾きの推定値(小数点第5位で丸め)
# (2) 傾きのP値
# (3) 切片の推定値(小数点第5位で丸め)
# (4) 相関係数(小数点第5位で丸め)
#
# を画面に出力するコードを書いてください。出力の形式はファ
# イルoutput_sample.txtと同じになるようにしてくださ
# い(計算誤差により、各数値はoutput_sample.txtの数値
# からごくわずかにずれる可能性があります)。

# Numpy配列への変換
X = np.array(X)
Y = np.array(Y)
# 回帰分析
res = stats.linregress(X,Y)
# 画面への出力
print("Slope = ",res.slope.round(5))
print("P-Value = ",res.pvalue)
print("Intercept = ",res.intercept.round(5))
print("R-Value = ",res.rvalue.round(5))
# %%
# 課題4-2のプログラム
#
# ここに課題4-2のコードを書いてください。
# 課題4-1の結果を積極的に利用してください。
#
# ヒント: 4-1で計算したY切片の推定値、傾きの推定値、
# Xの配列からYの予測値の配列を作ってください。残差は
# 次の式
#
# 残差  = Yの実測値 - Yの予測値
#
# から計算してください。あとは
# 
# X値、Y実測値、Y予測値、残差
# 
# を小数点第5位で丸め、prediction.txtに出力して終わり
# です。with構文を使って出力してください。

# 予測値
Y_pred = (res.intercept + res.slope * X).round(5)
# 残差
residual = (Y - Y_pred).round(5)

# ファイル出力
with open('prediction.txt','w') as file:
    file.write('X値 Y値 Y予測値 残差\n')
    for i in range(len(X)):
        file.write(f'{X[i]} {Y[i]} {Y_pred[i]} {residual[i]}\n')
