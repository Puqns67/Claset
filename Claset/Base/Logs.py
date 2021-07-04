#VERSION=2
#
#Claset/Base/Logs.py
#日志记录
#

from time import localtime, strftime

from Claset.Base.Loadfile import loadfile
from Claset.Base.Path import path as pathmd


class Logs():
    def __init__(self, LogPath="$EXEC/Log.log", Configs=None):
        if Configs == None:
            self.Configs = loadfile("$EXEC/Configs/Logs.json", "json")
        else:
            self.Configs = Configs

        if "$" in LogPath:
            LogPath = pathmd(LogPath)

        if self.Configs["ProgressiveWrite"] == True:
            self.LogPath = LogPath
            with open(self.LogPath, mode="w+") as File:
                pass
        else:
            self.LogFile = open(LogPath, mode="w+")



    def GenLog(self, Perfixs=[], Value=".", SaveToFile=True):
        Perfix = ""

        #Perfixs
        if len(Perfixs) != 0:
            for Name in Perfixs:
                Perfix += self.Configs["Format"]["Perfix"].replace(r"{Name}", str(Name))
        
        #Value
        Value.replace(r"{Value}", Value)

        #Time
        Time = strftime(self.Configs["Format"]["Time"], localtime())

        FullLog = self.Configs["Format"]["FullLog"].replace(r"{Time}", Time).replace(r"{Perfixs}", Perfix).replace(r"{Value}", Value) + "\n"

        if SaveToFile == True:
            if self.Configs["ProgressiveWrite"] == True:
                with open(self.LogPath, mode="a") as File:
                    File.write(FullLog)
            else:
                self.LogFile.write(FullLog)

        print(FullLog, end="")
