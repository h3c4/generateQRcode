#!/usr/bin/python3
import pyqrcode
import png
from pyqrcode import QRCode
import os,sys
import time

#Autor: H3C4

def error():
    if len(sys.argv)!=3:
        print("\n[!] Use: python3 " + sys.argv[0] + " < url > " + "<directory to save>")
        sys.exit(1)
        

if __name__ == '__main__' :
    
    try :
        QRstring = str(sys.argv[1])
        directory = str(sys.argv[2])+'qr.png'
        genereate = pyqrcode.create(QRstring)       
        save = genereate.png(directory,scale = 8)
        save
        print ("\n[!]Creating QR code for: ",QRstring)
        time.sleep(2)
        print("\n\t[*]Succes, QR code created")
        time.sleep(1)
        print("\n[!]Show in ",directory)
    except:
        error()    
