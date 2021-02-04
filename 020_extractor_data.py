import glob

import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.pyplot import figure

# データ読み出し
file = glob.glob("*.csv")[0]
df = pd.read_csv(file, encoding="SHIFT-JIS", engine='python')

# 差分を追加
df = df.assign(diff=df["OUT1"] - df["OUT2"])

# 該当のINDEXを抽出
list = df.query("OUT1 < 3 | OUT2 < 3").index

# INDEXの塊をリストに切り分け
result = []
val_pre = 0

for i, val in enumerate(list):
    if i == 0:
        temp = [val]
    elif val - val_pre < 2:
        temp.append(val)
    else:
        result.append(temp)
        temp = [val]
    val_pre = val


# 抽出した内容をファイルに出力
for i, temp in enumerate(result):
    df[result[i][0]:result[i][-1]
       ].to_csv(file[:-4] + "_{0:03}.csv".format(i), encoding="shift_jis")


# 参考までに表示
fig = figure(figsize=(20, 10))
for i in range(9):
    num = i * 10
    # 表示場所を指定
    ax = fig.add_subplot(3, 3, i + 1)
    # 折れ線グラフ
    df[result[num][0]:result[num][-1]].plot(ax=ax)
    # 縦軸の値を指定
    ax.set_ylim(bottom=-0.1, top=0.1)
    # グリッド表示
    ax.grid(True)

plt.show()
