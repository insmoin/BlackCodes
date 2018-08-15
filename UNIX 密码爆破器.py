# !/usr/bin/env python3

# __author: "insmoin"
# date: "2017/5/28 16:10"


"""
暴力破解UNIX的密码，需要输入字典文件和UNIX的密码文件
但是现代的×NIX 系统将密码存储在/etc/shadow 文件中，提供了个更安全的
哈希散列算法 SHA-512 算法，Python 的标准库中 hashlib 模块提供了此算法，
我们可以更新我们的脚本，破解 SHA-512 哈希散列加密算法的密码。
"""
import crypt
def testPass(cryptPass):
    salt = cryptPass[0:2]
    dictfile = open('dictionary.txt', 'r') #打开字典文件
    for word in dictfile.readlines():
        word = word.strip('\n') #保留原始的字符，不去空格
        cryptWord = crypt.crypt(word, salt)
        if cryptPass == cryptWord:
            print('Found passed : ', word)
            return
        print('没找到密码 !')
        return
    
def main():
    passfile = open('passwords.txt', 'r') #读取密码文件
    for line in passfile.readlines():
        user = line.split(':')[0]
        cryptPass = line.split(':')[1].strip('')
        print("破解到密码 For :", user)
        testPass(cryptPass)
        
if __name__ == '__main__':
    main()