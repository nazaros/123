#!/usr/bin/env python
#Simple actions, just a practice

def file_stat():
    import os
    os.system("ls -l filename.txt")

def delimiter():
    print "===================================================================="

def read_file():
    try:
        with open("filename.txt","r") as f:
            read_data = f.read().replace('\n', '')
        print read_data
    except IOError:
        print 'oops!'

def nazaros_max(l):
    max=l[0]
    for i in l:
        if i>max:
            max=i
    print max

def nazaros_min(l):
    min=l[0]
    for i in l:
        if i<min:
            min=i
    print min
 
if __name__ == '__main__':
    file_stat()
    delimiter()
    read_file()
