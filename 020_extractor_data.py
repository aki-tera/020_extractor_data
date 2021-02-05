import glob

import json

import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.pyplot import figure




class DataExtractor:
    def __init__(self, filename):
        # ファイル名
        self.filename = filename
        # パラメータの取り出し
        DESetting = open("setting.json", "r")
        DEDict = json.load(DESetting)
        # 辞書から取り出したパラメータをセットする
        self.DEHigh = DEDict["high"]
        self.DELow = DEDict["low"]

    def create_dataframe():
        # ファイルの読み出し
        self.df = pd.read_csv(self.finename, encoding="SHIFT-JIS", engine='python')
        # 差分を追加
        self.df["diff"] = self.df["OUT1"] - self.df["OUT2"]

    def separate_dataframe():
        # 該当のINDEXを抽出
        list = self.df.query("OUT1 < {0} | OUT2 < {0} | {1} < OUT1 | {1} < out2".format(self.DEHigh,self.DELow)).index
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
        self.df1 = pd.DataFrame(index=range(1000))
        self.df2 = pd.DataFrame(index=range(1000))
        self.df3 = pd.DataFrame(index=range(1000))
        # 各データフレームに値を入れていく
        for i, temp in enumerate(self.result):
            label = "{0:03}".format(i)
            self.df1["1" + label] = pd.DataFrame(self.df[temp[0]:temp[-1]]["OUT1"]
                                    .reset_index().loc[:, ["OUT1"]])
            self.df2["2" + label] = pd.DataFrame(self.df[temp[0]:temp[-1]]["OUT2"]
                                    .reset_index().loc[:, ["OUT2"]])
            self.df3["3" + label] = pd.DataFrame(self.df[temp[0]:temp[-1]]["diff"]
                                    .reset_index().loc[:, ["diff"]])

    def save_dataframe():
        # ファイルに書き込み
        # excelで開きたいのでshift-jisを指定する
        self.df1.to_csv(self.filename[:-4] + "-out1.csv", encoding="shift_jis")
        self.df2.to_csv(self.filename[:-4] + "-out2.csv", encoding="shift_jis")
        self.df3.to_csv(self.filename[:-4] + "-diff.csv", encoding="shift_jis")

    def plot_dataframe():
        # 参考までに表示
        fig = figure(figsize=(20, 10))
        for i in range(9):
            num = i * 10
            # 表示場所を指定
            ax = fig.add_subplot(3, 3, i + 1)
            # 折れ線グラフ
            self.df[self.result[num][0]:self.result[num][-1]].plot(ax=ax)
            # 縦軸の値を指定
            ax.set_ylim(bottom=-0.1, top=0.1)
            # グリッド表示
            ax.grid(True)


def main():
    filename = glob.glob("*.csv")
    for row in filename:
        if row[-9:] not in ["-out1.csv", "-out1.csv", "-out1.csv"]:
            d = DataExtractor(row)
            d.create_dataframe()
            d.separate_dataframe()
            d.save_dataframe()
            d.plot_dataframe()
    plot.show()

if __name__=="__main__":
    main()
