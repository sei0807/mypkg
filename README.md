# 現在位置推定シュミレータ
![test](https://github.com/sei0807/mypkg/actions/workflows/test.yml/badge.svg)

ランダムな速度データを積分して、ロボットの現在位置を推定するシミュレータです。

## 使用方法
このパッケージには、速度指令を送る `talker` と、それを受信して位置を計算する `listener` が含まれています。

### 実行手順
ローンチファイルを使用して、2つのノードを同時に起動します。
```bash
$ ros2 launch mypkg talk_listen.launch.py
```

実行結果の例
端末には以下のように、現在の速度（Velocity）と計算された位置（Current Position）が表示されます。
```
[INFO] [listener]: Velocity: 0, Current Position: 0
[INFO] [listener]: Velocity: 1, Current Position: 1
[INFO] [listener]: Velocity: 1, Current Position: 2
[INFO] [listener]: Velocity: 0, Current Position: 2
[INFO] [listener]: Velocity: -1, Current Position:1
```
## 必要なソフトウェア
-ROS 2 Humble Hawksbill
- Python 3.10

## テスト環境
- Ubuntu 22.04 LTS

## ライセンス
- このソフトウェアパッケージは、3条項BSDライセンスの下、再頒布および使用が許可されます。
- © 2025 Seiya Ohata

## 謝辞
このパッケージのコードは、下記のスライド（CC-BY-SA 4.0 by Ryuichi Ueda）のものを、参考にしています。
[ryuichiueda/slides_marp/robosys2025](https://github.com/ryuichiueda/slides_marp/tree/master/robosys2025)
