# -*- coding: utf-8 -*-
"""
Created on Fri Dec  8 09:06:11 2017

@author: backesj
"""

latinList = ['.txt','.sas', '.docx']    
    
def findText(inList, fileType, searchTerm):
    """
    This function takes a directory or a list of directories and searches all folders
    for a type of file using set of text that the user defines
    """
    inListTemp = list(inList)
    fileTypeTemp = list(fileType)
    searchTermTemp = list(searchTerm)
    latinList = ['.txt','.sas', '.docx']    

    import os
        
    from os import listdir
    from os.path import isfile, join
    outList = []
    for i in inListTemp:
        print(i)
        for root, dirs, files in os.walk(i):
            for file in files:
                for fType in fileTypeTemp:
                    if file.endswith(fType):
                        if any(item == fType for item in latinList):
                        #if any( [fileType == '.sas', fileType == '.txt'] ):
                            with open(os.path.join(root, file),'r', encoding = 'latin1') as text:
                                data = text.read()
                                if and(term in data for temrm in searchTermTemp):
                                    outList.append(os.path.join(root, file))
                                    text.close()
                                else:
                                    text.close()
                        else:
                            with open(os.path.join(root, file),'r') as text:
                                data = text.read()
                                if and(term in data for temrm in searchTermTemp):
                                    outList.append(os.path.join(root, file))
                                    text.close()
                                else:
                                    text.close()
        return outList
fileList = findText( ["C:/Users/backesj", "H:/", "S:/DA_work_files" ],
                    ".py", 
                    "S:\DA_work_files\DA_Work_Python\phantomjs-2.1.1-windows\bin\phantomjs.exe") 
                    
                   