# myled
robosys2019_kadai1

# 概要
*　5つのLEDを左から順番に点灯させるプログラム

## 
* 2回実行
* Ctrl+Cでストップ
* [ demo - YouTube](https)

## 環境
* Raspberry Pi 3 Model B
* ubuntu 18.04
* LED 5つ 
* 接続ピン - GPIO16,20,21,25,26 GND
* 抵抗 - 330[Ω]
* 実行方法
```
$ git clone https://github.com/yurinishio1139/myled.git
$ cd myled
$ make 
$ sudo insmod myled.ko 
$ sudo chmod 666 /dev/myled0 
$ chmod +x spin.py 
$ python spin.py

```
## 回路図
![回路図](https://user-images.githubusercontent.com/58972086/71590667-c03e6b80-2b6c-11ea-9650-4bd7a2052478.PNG)

## 参考文献


