# -*- coding: utf-8 -*-
import os

def yjp_get_file_recursive(search_dir, file):
    result = ''
    print (search_dir)
    for dirPath, dirList, fileList in os.walk(search_dir):
        for fileName in fileList:
            #print (fileName)
            if fileName == file:
                result = (dirPath + '/' + fileName)
                result = result.replace('\\','/')
                print(result)
                break
    return result