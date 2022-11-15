# 第8章 Turtleで遊ぶ
# 参照：turtle --- タートルグラフィックス

# Turtleを使用したデモを起動すことができます。

# py -m turtledemo



# 5か所クリックした後に、タートルが5か所を移動するプログラムを作成してください。

# "p8-4.py"より

# from turtle import *

# list_xx_yy = []

# count =0
# count_max =5

# def come(x, y):
#     (xx, yy) = pos()
#     newxy = ((xx+x)/2, (yy+y)/2)
#     print(x, y)

#     # goto(newxy)
#     list_xx_yy.append(newxy)
#     goto_XX_YY()

# def goto_XX_YY():
#     global count # これを忘れる
#     count +=1
#     if count_max <= count:
#         for xx_yy in list_xx_yy:
#             goto(xx_yy)
#         initialize()
        

# def initialize():
#     global count # これを忘れる
#     global list_xx_yy # これを忘れる
#     count =0
#     list_xx_yy =[]


# onscreenclick(come)
# done()





# 🥴マウスにタートルがついてくるプログラムを作成してください。 ヒント：マニュアル参照

# from turtle import *


# def come(x, y):
    
#     # (xx, yy) = pos()
    
#     # newxy = ((xx+x)/2, (yy+y)/2)
#     newxy = (x, y)

#     print(x, y)

#     goto(newxy)
#     # setpos(newxy) #変わらない？
#     # setposition(newxy) #変わらない？

# penup() #p123より
# onscreenclick(come)
# done()






# 演習問題
# 概要
# PythonのTurtleクラスを使用して、ランダムな位置に円を描画します。座標、半径と色はランダムな値を使用します。

# 設計
# アプリケーションの仕様が決まったら、それを実現する機能（詳細設計）を行う必要があります。Python言語やTurtleでサポートされている機能を調査します。

# 座標はウィンドウのサイズ以内とします。ウィンドウのサイズはturtle.screensize()メソッドで取得します。
# 円はturtle.circle()メソッドで描きます。半径は10～100の範囲とします。
# 描く時間間隔はtime.sleep()メソッドを使用します。
# 色は赤、緑、青、黒からランダムな色を選択します。Turtle Colors
# 塗りつぶしの色はturtle.color()メソッドを使用します。
# 任意の位置をクリックすると円を消去します。turtle.clear()メソッドを使用します。
# 初めて使用するモジュール、クラスやメソッドはテストして動作を確認します。Tuttleのメソッドの使い方はturtle --- タートルグラフィックスを参照してください。




# 機能テスト
# ランダムな整数を取得する方法を確認します。Pythonのrandomモジュールのrandint()関数を使用して、10から100の値を生成します。

# import random
# num = random.randint(0, 10)
# print(num)

# {note}
# Python Shellでタートルを実行するとdone()関数で終了できません。




# Turtleのスクリーンサイズを取得してコンソールに表示します。

# import turtle
# turtle.home() # とりあえずTurtle用スクリーンを表示
# size = turtle.screensize() # スクリーンサイズを取得
# turtle.done() # 終了




# 円を描画します。

# import turtle
# turtle.color('black') # 線の色を黒に設定
# speed = turtle.speed('fastest') # 描画スピードを最速に設定
# turtle.circle(100) # 半径100の円を描画
# turtle.speed(speed) # 描画スピードを元に戻す
# turtle.done()




# 赤色で塗りつぶされた円を描画します。

# import turtle

# turtle.color('black', 'black') # 線の色と塗りつぶしの色を黒に設定
# speed = turtle.speed('fastest')
# turtle.begin_fill() # 塗りつぶしを開始
# turtle.circle(100)
# turtle.end_fill() # 塗りつぶしを終了
# turtle.speed(speed)
# turtle.done()




# クリックしたら、クリックされたことをコンソールに表示します。

# import turtle

# def hello(x, y):
#     """マウスクリックで呼び出される関数（イベントハンドラ）"""
#     print(f'座標({x},{y})でクリックされました。')

# turtle.home()
# turtle.onscreenclick(hello) # スクリーンをクリックしたときに呼び出される関数を設定
# turtle.done()



# クリックしたら描画を消去します。

# import turtle

# def screen_clear(x, y):
#     turtle.clear() # スクリーンをクリア

# turtle.speed('fastest')
# turtle.color('blue', 'blue')
# turtle.begin_fill()
# turtle.circle(100)
# turtle.end_fill()
# turtle.speed('normal')
# turtle.onscreenclick(screen_clear) # スクリーンをクリックしたときに呼び出される関数を設定
# turtle.done()



# 実装
# これまでのテスト結果を元に、仕様を満たすアプリケーションを作成してください。
# PythonのTurtleクラスを使用して、ランダムな位置に円を描画します。座標、半径と色はランダムな値を使用します。
# 描く時間間隔はtime.sleep()メソッドを使用します。

import time
import turtle
import random

# 色は赤、緑、青、黒からランダムな色を選択します。Turtle Colors
turtle_colors = ('red', 'green', 'blue', 'black')

list_turtles = []

# 任意の位置をクリックすると円を消去します。turtle.clear()メソッドを使用します。
def screen_clear(x, y, turtle=turtle):
    turtle.clear() # スクリーンをクリア,現状こっちは要らないかも

    for t in list_turtles:t.clear()
    list_turtles.clear() #これだと微妙におかしい


def drawCircle():

#    global turtles #無くても動く

   turtle_new = turtle.Turtle()

   list_turtles.append(turtle_new)

   turtle_new.penup()
   turtle_new.hideturtle() # 11:23 11-Oct-22 小澤さんより

   # 座標はウィンドウのサイズ以内とします。ウィンドウのサイズはturtle.screensize()メソッドで取得します。
   # Turtleのスクリーンサイズを取得してコンソールに表示します。
   turtle_new.home() # とりあえずTurtle用スクリーンを表示
   size = turtle.screensize() # スクリーンサイズを取得
#    print(size) #検証用

   turtle_new.setpos(random.randint(-size[0], size[0]), random.randint(-size[1], size[1]))

   turtle_new.speed('fastest')
   # 塗りつぶしの色はturtle.color()メソッドを使用します。
   turtle_new.color(turtle_colors[random.randint(0, len(turtle_colors))-1], turtle_colors[random.randint(0, len(turtle_colors))-1])
   turtle_new.begin_fill()
   # 円はturtle.circle()メソッドで描きます。半径は10～100の範囲とします。
   turtle_new.circle(random.randint(10, 100))
   turtle_new.end_fill()
   turtle_new.speed('normal')
   # 任意の位置をクリックすると円を消去します。turtle.clear()メソッドを使用します。

# 乱数を使うので random モジュールもインポート
# 実行を停止するための変数（フラッグ）
stop_flag = False
# マウスがクリックされたときの関数, 引数 x, y をとるように
# しないといけないが, 使わない
# 実行停止フラグを True にする

#"p130_8-5 random_turtle.py"より
def clicked(x, y):
    global stop_flag
    stop_flag = True
    # time.sleep(5) #意味なさそう
    screen_clear(x, y)
    stop_flag = False

#"p130_8-5 random_turtle.py"より
# マウスがクリックされたときの動作を指定, clicked 関数を
# 呼び出す
#

turtle.hideturtle() # 11:23 11-Oct-22 小澤さんより

turtle.onscreenclick(clicked)

while (not stop_flag): drawCircle()
    
turtle.done()