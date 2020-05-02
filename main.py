import sys
import os
from lib.tools import *

class program():
    def __init__(self,args):
        self.tool = tools(args)
        self.setup(args)

    def setup(self,args):
        if self.tool.argHasValue("-sf"):#the folder for source files
          val=self.tool.argValue("-sf")
          self.folderPathSource=val.replace("\\","/")
          #print("folderPathSource",self.folderPathSource)
        else:
          self.stop("Error, -sf (source fold) is missing !")

        if self.tool.argHasValue("-of"):#the folder for source files
          val=self.tool.argValue("-of")
          self.folderPathOutput=val.replace("\\","/")
          try:
            os.mkdir(self.folderPathOutput,0o777)
          except:1
          #print("folderPathOutput",self.folderPathOutput)
        else:
          self.stop("Error, -of (output folder) is missing !")

    def run(self):
        for root, dirs, files in os.walk(self.folderPathSource):
            for filename in files:
                try:
                    self.move(root,filename)
                except:1
    def move(self,rootPath,file):
        year=file[:4]
        month=file[4:6]

        if "2000"<= year and year<="2030" and "01"<=month and month<="12":
            print("OK",file)
            previousPath=rootPath + "/" + file

            newFolderPath=self.folderPathOutput + "/" + year
            try:
                os.mkdir(newFolderPath,0o777)
            except:1

            newFolderPath += "/" + month + "/" 
            try:
                os.mkdir(newFolderPath,0o777)
            except:1

            newPath=newFolderPath + file

            os.rename(previousPath, newPath)
        else:
            print("NO",file)


    def stop(self,msg):
        print(msg)
        exit(0)


if __name__ == '__main__':
    prog=program(sys.argv)
    prog.run()