#!/usr/bin/python
import cgitb, cgi
cgitb.enable()
form = cgi.FieldStorage()
val1 = form.getvalue('message')
print("Content-Type: text/html\n\n")
print('<!DOCTYPE html><head><link href="https://fonts.googleapis.com/css?family=Dosis" rel="stylesheet"><link href="https://fonts.googleapis.com/css?family=Quicksand" rel="stylesheet"><script src="https://ajax.googleapis.com/ajax/libs/jquery/3.1.1/jquery.min.js"></script><link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css"><meta charset="UTF-8"></head><body style="background-color: #ff30cb"><div style="padding: 30px 30px 30px 30px; text-align: center;"><div class="thing"><div id="heart" class="heart" style=" background-color: none; margin:auto; text-align: center"><div style="z-index: 100; width: 100%; position: absolute; padding-top: 100px; margin: auto; transform: rotate(45deg); left: 15%"><h style="font-size: 40px; color:white">Enter Message</h><form id="selectForm" method="POST" action="index.py"><input style="font-family: Lovely; font-size: 30px; border-style: none; border-radius: 10%: color" type="text" name="message"><input class="gobutton" style="font-family: Lovely; background-color: transparent; border-style: none; color: white; font-size: 30px" type="submit" value="Go"></form></div></div></div></div><link href="nicky.css" rel="stylesheet"></body>')
if(val1 != ""):
        try:
            myfile = open("message.txt", "w")
            myfile.write(val1)
            myfile.close()
        except:
            print()

