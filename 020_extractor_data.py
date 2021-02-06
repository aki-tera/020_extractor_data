import glob

import json

import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.pyplot import figure




class DataExtractor:
    def __init__(self, filename, dict):
        # ファイル名
        self.DEFilename = filename
        # 各種設定を定義
        self.DECol1 = list(dict.keys())[0]
        self.DECol2 = list(dict.keys())[1]
        self.DECol3 = list(dict.keys())[2]

        self.DEHigh1 = dict[self.DECol1]["high"]
        self.DELow1 = dict[self.DECol1]["low"]

        self.DEHigh2 = dict[self.DECol2]["high"]
        self.DELow2 = dict[self.DECol2]["low"]

        self.DEFirst = dict[self.DECol3]["first"]


    def create_dataframe(self):
        # ファイルの読み出し
        self.df = pd.read_csv(self.DEFilename, encoding="SHIFT-JIS", engine='python')
        # 差分を追加
        if self.DEFirst == self.DECol1:
            self.df[self.DECol3] = self.df[self.DECol1] - self.df[self.DECol2]
        else:
            self.df[self.DECol3] = self.df[self.DECol2] - self.df[self.DECol1]

    def separate_dataframe(self):
        # 該当のINDEXを抽出
        #list = self.df.query("({0} < OUT1 | {0} < OUT2) & (OUT1 < {1} | OUT2 < {1})".format(SD_low,SD_high)).index
        query_eva1 = "({1} < {0} & {0} < {2})".format(self.DECol1,self.DELow1,self.DEHigh1)
        query_eva2 = "({1} < {0} & {0} < {2})".format(self.DECol2,self.DELow2,self.DEHigh2)
        list = self.df.query(query_eva1+" | "+query_eva2).index
        # INDEXの塊をリストに切り分け
        self.result = []
        val_pre = 0
        for i, val in enumerate(list):
            if i == 0:
                temp = [val]
            elif val - val_pre < 2:
                temp.append(val)
            else:
                self.result.append(temp)
                temp = [val]
            val_pre = val
        # 各列ごとにファイルにまとめる
        # 各列ごとのデータフレームの初期化
        self.df1 = pd.DataFrame(index=range(100))
        self.df2 = pd.DataFrame(index=range(100))
        self.df3 = pd.DataFrame(index=range(100))
        # 各データフレームに値を入れていく
        for i, temp in enumerate(self.result):
            label = "{0:03}".format(i)
            self.df1["1" + label] = pd.DataFrame(self.df[temp[0]:temp[-1]][self.DECol1]
                                    .reset_index().loc[:, [self.DECol1]])
            self.df2["2" + label] = pd.DataFrame(self.df[temp[0]:temp[-1]][self.DECol2]
                                    .reset_index().loc[:, [self.DECol2]])
            self.df3["3" + label] = pd.DataFrame(self.df[temp[0]:temp[-1]][self.DECol3]
                                    .reset_index().loc[:, [self.DECol3]])

    def save_dataframe(self):
        # ファイルに書き込み
        # excelで開きたいのでshift-jisを指定する
        self.df1.to_csv(self.DEFilename[:-4] + "-out1.csv", encoding="shift_jis")
        self.df2.to_csv(self.DEFilename[:-4] + "-out2.csv", encoding="shift_jis")
        self.df3.to_csv(self.DEFilename[:-4] + "-diff.csv", encoding="shift_jis")

    def plot_dataframe(self):
        # 参考までに表示
        fig = figure(figsize=(10, 8))
        for i in range(9):
            num = i

            # 表示場所を指定
            ax = fig.add_subplot(3, 3, i + 1)
            # 折れ線グラフ
            self.df[self.result[num][0]:self.result[num][-1]].plot(ax=ax)
            # 縦軸の値を指定
            ax.set_ylim(bottom=-5, top=5)
            # グリッド表示
            ax.grid(True)


def main():
    # パラメータの取り出し
    setting = open("setting.json", "r", encoding="utf-8")
    dict = json.load(setting)

    # ファイル読み込み
    filename = glob.glob("*.csv")
    for row in filename:
        if row[-9:] not in ["-out1.csv", "-out2.csv", "-diff.csv"]:
            d = DataExtractor(row, dict)
            d.create_dataframe()
            d.separate_dataframe()
            d.save_dataframe()
            d.plot_dataframe()
    plt.show()

if __name__=="__main__":
    main()
