import pandas as pd
import csv
import os
import time
from VND_Algo import *


Algoritm = ['VND01', 'VND02']
def RPD(bs,mbs):

    c=100*((float(mbs)-float(bs))/float(bs))
    return c

def creat_experement_csv_file(Algo):
    for i in range(len(Algo)):
        header = ['file', 'sct', 'bs', 'mbs', 'RPD','Tk']
        with open('experement2/' + Algo[i] + '.csv', 'w') as f:
            dw = csv.DictWriter(f, delimiter=',', fieldnames=header)
            dw.writeheader()
        f.close()
#creat_experement_csv_file(Algoritm)

def get_file_names(path):
    l = os.listdir(path)
    li = [x.split('.')[0] for x in l]
    li = li[1:-1]
    return li



def add_in_all_file(file, w, column):
    for i in range(len(file)):
        df = pd.read_csv('experement2/' + file[i] + '.csv')
        df[str(column)] = w
        df.to_csv('experement2/' + file[i] + '.csv')
        #df.close()

def add_in_one_file(file,w, column):
        df = pd.read_csv('experement2/' + file + '.csv')
        df[str(column)] = w
        df.to_csv('experement2/' + file + '.csv',index=False)
        #df.close()

def get_best_solution():
    with open('instances/instances/bestSolutions.txt') as f:
        A = []
        for i in range(61):
            line = f.readline()
            line = line.strip()
            L = line.split(',')
            l=L[1]
            A.append(l)
        A.remove(A[0])
        return A
    f.close


#_______________________________fist order___________________
def get_experement_VND01_result(file_name,bestsolut):
    mbs=[]
    sct=[]
    RDp=[]
    Tk=[]
    bs=[]
    for i in range(len(file_name)):
        start = time.time()
        sct1, mbs1 =VND_first_order(file_name[i], 20)
        end = time.time()
        bss = bestsolut[i]
        print(i)
        print(sct1, mbs1)
        RDp.append(RPD(bss, mbs1))
        mbs.append(mbs1)
        sct.append(sct1)
        bs.append(bss)
        Tk.append(end-start)

    print(mbs,sct)
    add_in_one_file('VND01', mbs, 'mbs')
    add_in_one_file('VND01', sct, 'sct')
    add_in_one_file('VND01', RDp, 'RPD')
    add_in_one_file('VND01', file_name, 'file')
    add_in_one_file('VND01', bs, 'bs')
    add_in_one_file('VND01', Tk, 'TK')
    print("the experement VND01 is done!")
#
#______________________________________second order_______________________

def get_experement_VND02_result(file_name,bestsolut):
    mbs=[]
    sct=[]
    RDp=[]
    Tk = []
    bs=[]
    for i in range(len(file_name)):
        start = time.time()
        sct1, mbs1 =VND_second_order(file_name[i], 20)
        end = time.time()
        bss = bestsolut[i]
        print(i)
        print(sct1, mbs1)
        RDp.append(RPD(bss, mbs1))
        mbs.append(mbs1)
        sct.append(sct1)
        bs.append(bss)
        Tk.append(end - start)
    print(mbs,sct)
    add_in_one_file('VND02', mbs, 'mbs')
    add_in_one_file('VND02', sct, 'sct')
    add_in_one_file('VND02', RDp, 'RPD')
    add_in_one_file('VND02', file_name, 'file')
    add_in_one_file('VND02', bs, 'bs')
    add_in_one_file('VND02', Tk, 'TK')
    print("the experement VND02 is done!")

import sys
def loud_bs_filename():
    File_name = get_file_names('instances/instances')
    bestsolution = get_best_solution()
    return File_name,bestsolution
process_arg=sys.argv[1]
if process_arg=='VNDFO':
    print('Starting the ' + process_arg + '...')
    get_experement_VND02_result(*loud_bs_filename())
    print(process_arg + 'is donne!')
if process_arg=='VNDSO':
    print('Starting the ' + process_arg + '...')
    get_experement_VND01_result(*loud_bs_filename())
    print(process_arg + 'is donne!')
