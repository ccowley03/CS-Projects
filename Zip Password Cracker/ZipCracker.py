from tqdm import tqdm


import zipfile

import sys

import requests

import multiprocessing as mp

from multiprocessing import Process


numthread = 5



def ZipCracker():
    


    wordlist = sys.argv[2]

    myzip = sys.argv[1]

    myzip = zipfile.ZipFile(myzip)

    numword = len(list(open(wordlist,"rb")))

    print("Total number of passwords to test:", numword)

    with open(wordlist,"rb") as wordlist:
        for word in tqdm(wordlist,total=numword,unit= "word"):
            try:
                myzip.extractall(pwd=word.strip())

            except:
                continue

            else:
                print("[!] Password Found!:",word.decode().strip())
                queue1.task_done()

    print("[!] Password not found, try other list")
        
        


if __name__ == '__main__':
    p = Process(target=ZipCracker)
    p.start()
    p.join()
    
   
    

   
 
   
