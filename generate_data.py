'''
注: これはファイルdata.txtを作成するための
プログラムです。課題とは直接関係ありません。
'''
# %%
import numpy as np
rng = np.random.default_rng(123)
x = rng.normal(4,2,100)
e = rng.normal(0,2,100)
y = 12 - 0.8 * x + e
lines = [str(y[i].round(5)) + ' ' + str(x[i].round(5)) + '\n' for i in range(100)]
lines = ['Y-values X-values\n'] + lines
with open('./data.txt','w') as file:
    file.writelines(lines)
