# 020_extractor_data
![](https://img.shields.io/badge/type-python3-brightgreen)  ![](https://img.shields.io/badge/windows%20build-passing-brightgreen) ![](https://img.shields.io/badge/license-MIT-brightgreen) 

## DEMO
**Output Data  <-**  
<img src="https://user-images.githubusercontent.com/44888139/105790143-14fa2300-5fc7-11eb-821f-5e803d164bfe.png" width="400px">  
**INPUT Data  ->**   
<img src="https://user-images.githubusercontent.com/44888139/105966797-7655eb00-60c8-11eb-997c-9ea81346d853.png" width="300px"> 
<img src="https://user-images.githubusercontent.com/44888139/105789589-0fe8a400-5fc6-11eb-83bb-00fda47ff499.png" width="600px">  
  
## Features
You can create graphs and result's csv files from original csv files.

### specification
- You get the separated data by 2 columns from the ranges which you want between high and low.
- You can change the settings by setting file.
### original csv files
- You should assume files which output from a logger.
- The files must contain data1, data2.
- The data must have stable data for a certain period.
### output data
- You can get the results which are csv files and graphs.

## Requirement 
Python 3
 - I ran this program with the following execution environment.
   - Python 3.8
   - Windows 10

Python Library
  - pandas
  - matplotlib
  - glob
  - json

## Usage
1. You place the csv files in the same folder as this program.
1. Run this program.
1. Display graphs plotting the median.
1. And then generate result's csv files.  
   Note:It is not generated if results already exists.
## Note
Nothing in particular

## License
This program is under MIT license.
# 【日本語】


## 機能
元のcsvファイルからグラフとcsvファイルを作成します。
- 仕様
  - 一定の値を取る部分から中央値を取得します
  - 元のcsvファイルに記載されているロガー型式で設定を変更できます
- 元のcsvファイル
  - ロガーから出力されたファイルを想定しています
  - フォーマットは日付、データ1、データ2がある必要があります
  - 一定期間の安定した領域があるデータであることを想定しています
- 出力する内容
  - 中央値をまとめてcsvファイルに出力（画像、csvファイル）します

## 必要なもの
Python 3
- このプログラムは、Python 3.8とWindows10で動作確認しています。

## 使い方
1. 本プログラムと同じフォルダにcsvファイル（複数可能）を置きます
1. 本プログラムを実行します
1. 中央値をプロットしたグラフが表示されます
1. 同時に、result_が先頭に付いたcsvファイルが生成されます  
   但し、すでにファイルがあれば生成されません


## 備考
特にありません

## ライセンス
本プログラムは、MITライセンスです
