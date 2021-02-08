import glob

import json

import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.pyplot import figure

# 日本語フォント
jp_font = "Yu Gothic"


class DataExtractor:
    """Extract the values from csv files and save them to csv files.
    """

    def __init__(self, filename, dict):
        """Set variables.

        Args:
            filename (str): file name of csv
            dict (dict): parameters of setting
        """
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

        self.DEPlotsize = {
            "small": (9, 5),
            "large": (13, 10),
            "zero": (1, 1)
        }[dict["graph"]["size"]]

    def create_dataframe(self):
        """Convert from csv to DataFrame.

        Returns:
            bool: True is processable, False isn't.

        """
        if self.DEFilename[-8:] not in [self.DECol1 + ".csv",
                                        self.DECol2 + ".csv",
                                        self.DECol3 + ".csv"]:
            # ファイルの読み出し
            self.df = pd.read_csv(
                self.DEFilename,
                encoding="SHIFT-JIS",
                engine='python')
            # 差分を追加
            try:
                if self.DEFirst == self.DECol1:
                    self.df[self.DECol3] = self.df[self.DECol1] - \
                        self.df[self.DECol2]
                else:
                    self.df[self.DECol3] = self.df[self.DECol2] - \
                        self.df[self.DECol1]
                print("処理実施：" + self.DEFilename)
                return(True)
            except BaseException as e:
                print("処理不可：{0}  -->{1}が存在しません".format(self.DEFilename, str(e)))
        else:
            print("処理不要：" + self.DEFilename)
        return(False)

    def separate_dataframe(self):
        """Split the data which extract in range into each DataFrames.
        """
        # 該当のINDEXを抽出
        query_eva1 = "({1} < {0} & {0} < {2})".format(
            self.DECol1, self.DELow1, self.DEHigh1)
        query_eva2 = "({1} < {0} & {0} < {2})".format(
            self.DECol2, self.DELow2, self.DEHigh2)
        list = self.df.query(query_eva1 + " | " + query_eva2).index

        # INDEXの塊をリストに切り分け
        self.result = []
        val_pre = 0
        index_max = 0
        for i, val in enumerate(list):
            if i == 0:
                temp = [val]
            elif val - val_pre < 2:
                temp.append(val)
            else:
                self.result.append(temp)
                # 最も大きいindexを調査
                if len(temp) > index_max:
                    index_max = len(temp)
                temp = [val]
            val_pre = val

        # 各列ごとにファイルにまとめる
        # 各列ごとのデータフレームの初期化
        self.df1 = pd.DataFrame(index=range(index_max - 1))
        self.df2 = pd.DataFrame(index=range(index_max - 1))
        self.df3 = pd.DataFrame(index=range(index_max - 1))

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
        """Save each DataFrames.
        """
        # ファイルに書き込み
        # excelで開きたいのでshift-jisを指定する
        self.df1.to_csv(
            self.DEFilename[:-4] + "-" + self.DECol1 + ".csv", encoding="shift_jis")
        self.df2.to_csv(
            self.DEFilename[:-4] + "-" + self.DECol2 + ".csv", encoding="shift_jis")
        self.df3.to_csv(
            self.DEFilename[:-4] + "-" + self.DECol3 + ".csv", encoding="shift_jis")

    def plot_dataframe(self):
        """Display some data in a graph.

        Returns:
            int: If one,  graph is displayed by plt.show().

        """

        if self.DEPlotsize == (1, 1):
            return(0)

        # 参考までにグラフを表示する

        # プロットするグラフの飛び数
        num_plot_add = 1
        # プロットするグラフの最大の数
        num_plot_max = len(self.result)
        if num_plot_max > 9:
            num_plot_add = int(num_plot_max / 9)
            num_plot_max = 9

        fig = figure(figsize=self.DEPlotsize)

        # 描画タイトルを表示
        fig.suptitle(self.DEFilename, fontname=jp_font)

        for i in range(num_plot_max):
            num = i * num_plot_add

            # 表示場所を指定
            ax = fig.add_subplot(3, 3, i + 1)
            if self.DEPlotsize[0] > 10:
                display_legend = True
                # 描画タイトルを表示
                ax.set_title("No.{0}".format(num))
            else:
                display_legend = False

            # 折れ線グラフ
            self.df[self.result[num][0]:self.result[num][-1]].plot(
                legend=display_legend,
                ax=ax)
            # 縦軸の値を指定
            ax.set_ylim(bottom=-1, top=1)
            # グリッド表示
            ax.grid(True)

        return(1)


def main():
    # パラメータの取り出し
    setting = open("setting.json", "r", encoding="utf-8")
    dict = json.load(setting)

    # ファイル読み込み
    filename = glob.glob("*.csv")
    plot_counter = 0
    for row in filename:
        d = DataExtractor(row, dict)
        if d.create_dataframe():
            d.separate_dataframe()
            d.save_dataframe()
            plot_counter = d.plot_dataframe()
    if plot_counter != 0:
        plt.show()


if __name__ == "__main__":
    main()
