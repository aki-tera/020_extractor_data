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
- The files must contain data1, data2.
- The data needs to be stable data outside the range for a certain period of time.
### output data
- You can get three results (split data 1 and data 2, difference between data 1 and 2).
- Each results are csv files and graphs

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
1. A few graphs is displayed for confirmation.
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
  - ある範囲の２列のデータを分割しながら、まとめて取得します。
  - 設定で列の名称や範囲を変更できます。
- 元のcsvファイル
  - データ1、データ2がある必要があります。
  - 一定期間の範囲外があるデータが必要です。
- 出力する内容
  - データ１，データ２とその差分をそれぞれまとめて出力します。
  - 結果はファイルに出力（画像、csvファイル）します。

## 必要なもの
Python 3
- このプログラムは、Python 3.8とWindows10で動作確認しています。

## 使い方
1. 本プログラムと同じフォルダにcsvファイル（複数可能）を置きます
1. 本プログラムを実行します
1. 確認用にいくつかピックアップしたグラフが表示されます
1. 同時に、末尾に列の名称が付いたcsvファイルが生成されます  
   但し、すでにファイルがあれば生成されません


## 備考
特にありません

## ライセンス
本プログラムは、MITライセンスです
