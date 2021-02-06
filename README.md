# LCD1602-Python-Serial-Interface-With-Japanese-Support
A simple python program allows you to control an LCD1602 display via serial port (tested with Arduino) using MeCab for Japanese Katakana support
## How to use this program
* install MeCab and jaconv for Japanese support
* Config your Arduino with a 1602 LCD to receive the serial data as characters to display
* Config the COM port in the program
* The character ‖ act as enter, config the space number to fit your own project
```
[evaluate LCD1602.py]
Input content: test
Convert kanji?: n
test
Input to Exit: 
Input content: Shiro   ‖    7940
Convert kanji?: n
Shiro                                       7940
Input to Exit: 
Input content: アイラ
Convert kanji?: n
ｱｲﾗ
Input to Exit: 
Input content: 煙 草
Convert kanji?: y
ｹﾑﾘ ｸｻ
Input to Exit: 
Input content: 合縁奇縁 ‖一期一会
Convert kanji?: y
ｱｲｴﾝｷｴﾝ                                 ｲﾁｺﾞｲﾁｴ
Input to Exit: exit
```
If the configuration is correct on both end, you should see characters appear on the LCD display
