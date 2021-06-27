# HW2(維吉尼亞密碼原理及Python實現)
。
## 算法
* 將位移量從單一數字變成一連串的位移，也就是讓金鑰變成金鑰陣列時， 加密方法就從「凱撒密碼」進化成了「維吉尼亞密碼」

* 加密過程:明文字母p對應的列和秘鑰字母k對應的行的交叉點就 是加密字母后的密文字母
* 解密過程:在密鑰字母k對應的行找到對應密文字母，則該密 文  字母對應的列的字母就是明文字母

 
## [程式碼](https://github.com/ukarara/ai109b/blob/main/homework/w4/Vigenere.py)
參考自
```
# -*- coding: utf-8 -*-
# Author:0verWatch

import string


"""
确保大小写正确转换，用了两个列表
"""
letter_list = string.ascii_uppercase
letter_list2 = string.ascii_lowercase


def get_real_key():
    """
    获取列需要加的秘钥
    """
    print("输入你的秘钥")
    key = input()      #得确保都是英文
    tmp = []
    flag = 0
    for i in key:
        if i.isalpha():
            pass
        else:
            flag = 1
    if flag == 0:
        for i in key:
            tmp.append(ord(i.upper()) - 65)
        return tmp
    else:
        print("请输入英文秘钥")


def get_info():
    """
    获取信息
    """
    print("input your message: ")
    message = input()
    return  message


def Encrypt(message,key):
    ciphertext = ""
    flag = 0
    key_list = key
    for plain in message:
        if flag % len(key_list) == 0:
            flag = 0
        if plain.isalpha(): #判断是否为英文
            if plain.isupper():
                ciphertext += letter_list[(ord(plain) - 65 + key_list[flag]) % 26] #行偏移加上列偏移
                flag += 1
            if plain.islower():
                ciphertext += letter_list2[(ord(plain) - 97 + key_list[flag]) % 26]
                flag += 1
        else:#不是英文不加密
            ciphertext += plain

    return ciphertext


def Decrypt(message,key):
    plaintext = ""
    flag = 0
    key_list = key
    for cipher in message:
        if flag % len(key_list) == 0:
            flag  = 0
        if cipher.isalpha():
            if cipher.isupper():
                plaintext += letter_list[(ord(cipher) - 65 - key_list[flag]) %26]
                flag += 1
            if cipher.islower():
                plaintext += letter_list2[(ord(cipher) - 97 - key_list[flag]) % 26]
                flag += 1
        else:
            plaintext += cipher
    return plaintext


if __name__ == '__main__':
    while True:
        print("请选择加密或解密模式")
        print("1. Encrypt")
        print("2. Decrypt")
        choice = input("Your choice")
        if choice == '1':
            message = get_info()
            key = get_real_key()
            print(Encrypt(message, key))
        if choice == '2':
            message = get_info()
            key = get_real_key()
            print(Decrypt(message, key))
```    

### 測試
以輸入”hello”為例，然後進行加解密，能夠正確完成
### 結果
``` PS
PS C:\Users\User\Desktop\109-2school\ai109b\homework\w4> python Vigenere.py
请选择加密或解密模式
1. Encrypt
2. Decrypt
Your choice1                #進行加密
input your message: 
hello                       #輸入hello
输入你的秘钥
kara                        #輸入密鑰kara
recly                       #獲得加密訊息
请选择加密或解密模式
1. Encrypt
2. Decrypt
Your choice2                #選擇解密
input your message: 
recly                       #加密訊息
输入你的秘钥
kara                        #填入密鑰
hello                       #獲得解密訊息
``` 


