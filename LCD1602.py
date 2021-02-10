import serial
import time
import jaconv
import MeCab
mecab = MeCab.Tagger ("-Oyomi")
def convmap(string):
    string = str(string
        .replace ( '？','0x3F' )
        .replace ( '￥','0x5C' )
        .replace ( '！','0x21' )
        .replace ( '→','0x7E' )
        .replace ( '←','0x7F' )
        .replace ( '。','0xA1' )
        .replace ( '「','0xA2' )
        .replace ( '」','0xA3' )
        .replace ( '、','0xA4' )
        .replace ( '｡','0xA1' )
        .replace ( '｢','0xA2' )
        .replace ( '｣','0xA3' )
        .replace ( '【','0xA2' )
        .replace ( '】','0xA3' )
        .replace ( '､','0xA4' )
        .replace ( '･','0xA5' )
        .replace ( '・','0xA5' )
        .replace ( 'ｱ','0xB1' )
        .replace ( 'ｲ','0xB2' )
        .replace ( 'ｳ','0xB3' )
        .replace ( 'ｴ','0xB4' )
        .replace ( 'ｵ','0xB5' )
        .replace ( 'ｶ','0xB6' )
        .replace ( 'ｷ','0xB7' )
        .replace ( 'ｸ','0xB8' )
        .replace ( 'ｹ','0xB9' )
        .replace ( 'ｺ','0xBA' )
        .replace ( 'ｻ','0xBB' )
        .replace ( 'ｼ','0xBC' )
        .replace ( 'ｽ','0xBD' )
        .replace ( 'ｾ','0xBE' )
        .replace ( 'ｿ','0xBF' )
        .replace ( 'ﾀ','0xC0' )
        .replace ( 'ﾁ','0xC1' )
        .replace ( 'ﾂ','0xC2' )
        .replace ( 'ﾃ','0xC3' )
        .replace ( 'ﾄ','0xC4' )
        .replace ( 'ﾅ','0xC5' )
        .replace ( 'ﾆ','0xC6' )
        .replace ( 'ﾇ','0xC7' )
        .replace ( 'ﾈ','0xC8' )
        .replace ( 'ﾉ','0xC9' )
        .replace ( 'ﾊ','0xCA' )
        .replace ( 'ﾋ','0xCB' )
        .replace ( 'ﾌ','0xCC' )
        .replace ( 'ﾍ','0xCD' )
        .replace ( 'ﾎ','0xCE' )
        .replace ( 'ﾏ','0xCF' )
        .replace ( 'ﾐ','0xD0' )
        .replace ( 'ﾑ','0xD1' )
        .replace ( 'ﾒ','0xD2' )
        .replace ( 'ﾓ','0xD3' )
        .replace ( 'ﾔ','0xD4' )
        .replace ( 'ﾕ','0xD5' )
        .replace ( 'ﾖ','0xD6' )
        .replace ( 'ﾗ','0xD7' )
        .replace ( 'ﾘ','0xD8' )
        .replace ( 'ﾙ','0xD9' )
        .replace ( 'ﾚ','0xDA' )
        .replace ( 'ﾛ','0xDB' )
        .replace ( 'ﾜ','0xDC' )
        .replace ( 'ｦ','0xA6' )
        .replace ( 'ﾝ','0xDD' )
        .replace ( 'ﾞ','0xDE' )
        .replace ( 'ﾟ','0xDF' )
        .replace ( 'ｧ','0xA7' )    
        .replace ( 'ｨ','0xA8' )
        .replace ( 'ｩ','0xA9' )
        .replace ( 'ｪ','0xAA' )
        .replace ( 'ｫ','0xAB' )
        .replace ( 'ｬ','0xAC' )
        .replace ( 'ｭ','0xAD' )
        .replace ( 'ｮ','0xAE' )
        .replace ( 'ｯ','0xAF' )
        .replace ( 'ｰ','0xB0' )
        .replace ( 'ー','0xB0' )
        .replace ( 'α','0xE0' )
        .replace ( 'ä','0xE1' )
        .replace ( 'β','0xE2' )
        .replace ( 'ε','0xE3' )
        .replace ( 'μ','0xE4' )
        .replace ( 'σ','0xE5' )
        .replace ( 'ρ','0xE6' )
        .replace ( 'φ','0xEC' )
        .replace ( 'θ','0xF2' )
        .replace ( '∞','0xF3' )
        .replace ( 'Ω','0xF4' )
        .replace ( 'ü','0xF5' )
        .replace ( '∑','0xF6' )
        .replace ( '仟','0xFA' )     #using special kanji to avoid mecab convert
        .replace ( '贎','0xFB' )
        .replace ( '閆','0xFC' )
        .replace ( '÷','0xFD' )
        .replace ( '■','0xFF' )
               )
    return string
    
    
def kataconv(content):
    try:                      #Disable mecab by commenting the following 3 lines
        kanji = input("Convert kanji?: ") 
        if kanji == "Y"or kanji == "y" or kanji == "ｙ" or kanji == "Ｙ":
            content = mecab.parse(content) 
        content = content.replace("\n","")
        content = content.replace("‖"," "*32)#act as enter, change num here to fit
        content = jaconv.normalize(content)
        content = jaconv.z2h(content)
        content = jaconv.hira2hkata(content)
        print("Output content: "+content)
        return content
    except Exception as error:
        print(error)

def binconv(string):
    lst = list(string)
    data = []
    digi = []
    for item in lst:
        item = jaconv.hira2hkata(item)
        item = jaconv.z2h(item)
        item = convmap(item)
        data.append(item)
    for stri in data:
        try:
            if len(stri) == 1 and ord(stri)<= 128:
                digi.append(int(ord(stri)))
            else:
                digi.append(int(stri,16))
        except:
            digi.append(int(255))
    return digi

exit = ""

try:
    ser = serial.Serial('COM10', 9600) #change port here
    time.sleep(3)          #initialize port
except Exception as error:
    print(error)
    exit = input("Input anything to Exit: ")
    
while exit  == "":
    try:
        content = str(input("Input content: "))
        ser.write(bytearray(binconv(kataconv(content))))
        exit = input("Input anything to Exit: ")
    except Exception as error:
        print(error)
        exit = input("Input anything to Exit: ")
#ser.write(b"\xB1"+b"\xB2"+b"\xD7")

try:
    ser.close()
except:
    print("Port not found.")

