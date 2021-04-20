import pandas as pd
import csv
import os
import time
from first_improvement import *
from best_improvment import *

Algoritm = ['FTR', 'FER', 'FIR', 'FTRZ', 'FERZ', 'FIRZ', 'BTR', 'BER', 'BIR', 'BTRZ', 'BERZ', 'BIRZ']


def RPD(bs, mbs):
    c = 100 * ((float(mbs) - float(bs)) / float(bs))
    return c


def creat_experement_csv_file(Algo):
    for i in range(len(Algo)):
        header = ['file', 'sct', 'bs', 'mbs', 'RPD', 'TK']
        with open('experement/' + Algo[i] + '.csv', 'w') as f:
            dw = csv.DictWriter(f, delimiter=',', fieldnames=header)
            dw.writeheader()
        f.close()


#creat_experement_csv_file(Algoritm)


def get_file_names(path):
    l = os.listdir(path)
    li = [x.split('.')[0] for x in l]
    li = li[1:-1]
    return li





# print(File_name)

def add_in_all_file(file, w, column):
    for i in range(len(file)):
        df = pd.read_csv('experement/' + file[i] + '.csv')
        df[str(column)] = w
        df.to_csv('experement/' + file[i] + '.csv')
        # df.close()


def add_in_one_file(file, w, column):
    df = pd.read_csv('experement/' + file + '.csv')
    df[str(column)] = w
    df.to_csv('experement/' + file + '.csv', index=False)
    # df.close()


# add_in_all_file(Algoritm,File_name,'file')

def get_best_solution():
    with open('instances/instances/bestSolutions.txt') as f:
        A = []
        for i in range(61):
            line = f.readline()
            line = line.strip()
            L = line.split(',')
            l = L[1]
            A.append(l)
        A.remove(A[0])
        return A
    f.close




# print(bestsolution)
# print(bestsolution[0])
# print(len(bestsolution))
# add_in_all_file(Algoritm,bestsolution,'bs')


# ----------------------------------- best improvment-----------------------------------------
# -------- 01
def get_experement_BER_result(file_name, bestsolut):
    mbs = []
    sct = []
    RDp = []
    Tk = []
    bs = []

    for i in range(len(file_name)):
        if i <= 29:
            start = time.time()
            sct1, mbs1 = best_improvement_Exchange_Random_permutation(file_name[i], 100, 20)
            end = time.time()
            bss = bestsolut[i]
            print(i)
            print(sct1, mbs1)
            RDp.append(RPD(bss, mbs1))
            mbs.append(mbs1)
            sct.append(sct1)
            Tk.append(end-start)
            bs.append(bss)
        else:
            start = time.time()
            sct1, mbs1 = best_improvement_Exchange_Random_permutation(file_name[i], 50, 20)
            end = time.time()
            bss = bestsolut[i]
            print(i)
            print(sct1, mbs1)
            RDp.append(RPD(bss, mbs1))
            mbs.append(mbs1)
            sct.append(sct1)
            Tk.append(end-start)
            bs.append(bss)


    print(mbs, sct)
    add_in_one_file('BER', mbs, 'mbs')
    add_in_one_file('BER', sct, 'sct')
    add_in_one_file('BER', RDp, 'RPD')
    add_in_one_file('BER', file_name, 'file')
    add_in_one_file('BER', bs, 'bs')
    add_in_one_file('BER', Tk, 'Tk')
    print("the experement BER is done!")




# -------- 02

def get_experement_BERZ_result(file_name, bestsolut):
    mbs = []
    sct = []
    RDp = []
    Tk = []
    bs = []
    for i in range(len(file_name)):
        if i <= 29:
            start = time.time()
            sct1, mbs1 = best_improvement_Exchange_Simplified_RZ_heuristic(file_name[i], 20)
            end = time.time()
            bss= bestsolut[i]
            print(i)
            print(sct1, mbs1)
            RDp.append(RPD(bss, mbs1))
            mbs.append(mbs1)
            sct.append(sct1)
            Tk.append(end-start)
            bs.append(bss)
        else:
            start = time.time()
            sct1, mbs1 = best_improvement_Exchange_Simplified_RZ_heuristic(file_name[i], 20)
            end = time.time()
            bss = bestsolut[i]
            print(i)
            print(sct1, mbs1)
            RDp.append(RPD(bss, mbs1))
            mbs.append(mbs1)
            sct.append(sct1)
            Tk.append(end-start)
            bs.append(bss)
    print(mbs, sct)
    add_in_one_file('BERZ', mbs, 'mbs')
    add_in_one_file('BERZ', sct, 'sct')
    add_in_one_file('BERZ', RDp, 'RPD')
    add_in_one_file('BERZ', file_name, 'file')
    add_in_one_file('BERZ', bs, 'bs')
    add_in_one_file('BERZ', Tk, 'TK')
    print("the experement BERZ is done!")




# -------- 03
def get_experement_BIR_result(file_name, bestsolut):
    mbs = []
    sct = []
    RDp = []
    Tk = []
    bs = []
    for i in range(len(file_name)):
        if i <= 29:
            start = time.time()
            sct1, mbs1 = best_improvement_Insert_Random_permutation(file_name[i], 100, 20)
            end = time.time()
            bss = bestsolut[i]
            print(i)
            print(sct1, mbs1)
            RDp.append(RPD(bss, mbs1))
            mbs.append(mbs1)
            sct.append(sct1)
            Tk.append(end-start)
            bs.append(bss)
        else:
            start = time.time()
            sct1, mbs1 = best_improvement_Insert_Random_permutation(file_name[i], 50, 20)
            end = time.time()
            bss = bestsolut[i]
            print(i)
            print(sct1, mbs1)
            RDp.append(RPD(bss, mbs1))
            mbs.append(mbs1)
            sct.append(sct1)
            Tk.append(end-start)
            bs.append(bss)
    print(mbs, sct)
    add_in_one_file('BIR', mbs, 'mbs')
    add_in_one_file('BIR', sct, 'sct')
    add_in_one_file('BIR', RDp, 'RPD')
    add_in_one_file('BIR', file_name, 'file')
    add_in_one_file('BIR', bs, 'bs')
    add_in_one_file('BIR', Tk, 'TK')
    print("the experement BIR is done!")


# -------- 04

def get_experement_BIRZ_result(file_name, bestsolut):
    mbs = []
    sct = []
    RDp = []
    Tk = []
    bs = []
    for i in range(len(file_name)):
        if i <= 29:
            start = time.time()
            sct1, mbs1 = best_improvement_Insert_Simplified_RZ_heuristic(file_name[i], 20)
            end = time.time()
            bss = bestsolut[i]
            print(i)
            print(sct1, mbs1)
            RDp.append(RPD(bss, mbs1))
            mbs.append(mbs1)
            sct.append(sct1)
            Tk.append(end-start)
            bs.append(bss)
        else:
            start = time.time()
            sct1, mbs1 = best_improvement_Insert_Simplified_RZ_heuristic(file_name[i], 20)
            end = time.time()
            bss = bestsolut[i]
            print(i)
            print(sct1, mbs1)
            RDp.append(RPD(bss, mbs1))
            mbs.append(mbs1)
            sct.append(sct1)
            Tk.append(end-start)
            bs.append(bss)
    print(mbs, sct)
    add_in_one_file('BIRZ', mbs, 'mbs')
    add_in_one_file('BIRZ', sct, 'sct')
    add_in_one_file('BIRZ', RDp, 'RPD')
    add_in_one_file('BIRZ', file_name, 'file')
    add_in_one_file('BIRZ', bs, 'bs')
    add_in_one_file('BIRZ', Tk, 'TK')
    print("the experement BIRZ is done!")



# -------- 05
def get_experement_BTR_result(file_name, bestsolut):
    mbs = []
    sct = []
    RDp = []
    Tk = []
    bs = []
    for i in range(len(file_name)):
        if i <= 29:
            start = time.time()
            sct1, mbs1 = best_improvement_Transpose_Random_permutation(file_name[i], 100, 20)
            end = time.time()
            bss = bestsolut[i]
            print(i)
            print(sct1, mbs1)
            RDp.append(RPD(bss, mbs1))
            mbs.append(mbs1)
            sct.append(sct1)
            Tk.append(end-start)
            bs.append(bss)
        else:
            start = time.time()
            sct1, mbs1 = best_improvement_Transpose_Random_permutation(file_name[i], 50, 20)
            end = time.time()
            bss = bestsolut[i]
            print(i)
            print(sct1, mbs1)
            RDp.append(RPD(bss, mbs1))
            mbs.append(mbs1)
            sct.append(sct1)
            Tk.append(end-start)
            bs.append(bss)
    print(mbs, sct)
    add_in_one_file('BTR', mbs, 'mbs')
    add_in_one_file('BTR', sct, 'sct')
    add_in_one_file('BTR', RDp, 'RPD')
    add_in_one_file('BTR', file_name, 'file')
    add_in_one_file('BTR', bs, 'bs')
    add_in_one_file('BTR', Tk, 'TK')
    print("the experement BTR is done!")



# -------- 06

def get_experement_BTRZ_result(file_name, bestsolut):
    mbs = []
    sct = []
    RDp = []
    Tk = []
    bs = []
    for i in range(len(file_name)):
        if i <= 29:
            start = time.time()
            sct1, mbs1 = best_improvement_Transpose_Simplified_RZ_heuristic(file_name[i], 20)
            end = time.time()
            bss = bestsolut[i]
            print(i)
            print(sct1, mbs1)
            RDp.append(RPD(bss, mbs1))
            mbs.append(mbs1)
            sct.append(sct1)
            Tk.append(end-start)
            bs.append(bss)
        else:
            start = time.time()
            sct1, mbs1 = best_improvement_Transpose_Simplified_RZ_heuristic(file_name[i], 20)
            end = time.time()
            bss = bestsolut[i]
            print(i)
            print(sct1, mbs1)
            RDp.append(RPD(bss, mbs1))
            mbs.append(mbs1)
            sct.append(sct1)
            Tk.append(end-start)
            bs.append(bss)
    print(mbs, sct)
    add_in_one_file('BTRZ', mbs, 'mbs')
    add_in_one_file('BTRZ', sct, 'sct')
    add_in_one_file('BTRZ', RDp, 'RPD')
    add_in_one_file('BTRZ', file_name, 'file')
    add_in_one_file('BTRZ', bs, 'bs')
    add_in_one_file('BTRZ', Tk, 'TK')
    print("the experement BTRZ is done!")



#####
# ----------------------------------- FIRST improvment-----------------------------------------
# -------- 01
def get_experement_FER_result(file_name, bestsolut):
    mbs = []
    sct = []
    RDp = []
    Tk = []
    bs = []
    for i in range(len(file_name)):
        if i <= 29:
            start = time.time()
            sct1, mbs1 = first_improvement_Exchange_Random_permutation(file_name[i], 100, 20)
            end = time.time()
            bss = bestsolut[i]
            print(i)
            print(sct1, mbs1)
            RDp.append(RPD(bss, mbs1))
            mbs.append(mbs1)
            sct.append(sct1)
            Tk.append(end-start)
            bs.append(bss)
        else:
            start = time.time()
            sct1, mbs1 = first_improvement_Exchange_Random_permutation(file_name[i], 50, 20)
            end = time.time()
            bss = bestsolut[i]
            print(i)
            print(sct1, mbs1)
            RDp.append(RPD(bss, mbs1))
            mbs.append(mbs1)
            sct.append(sct1)
            Tk.append(end-start)
            bs.append(bss)
    print(mbs, sct)
    add_in_one_file('FER', mbs, 'mbs')
    add_in_one_file('FER', sct, 'sct')
    add_in_one_file('FER', RDp, 'RPD')
    add_in_one_file('FER', file_name, 'file')
    add_in_one_file('FER', bs, 'bs')
    add_in_one_file('FER', Tk, 'TK')
    print("the experement FER is done!")



# -------- 02

def get_experement_FERZ_result(file_name, bestsolut):
    mbs = []
    sct = []
    RDp = []
    Tk = []
    bs = []
    for i in range(len(file_name)):
        if i <= 29:
            start = time.time()
            sct1, mbs1 = first_improvement_Exchange_Simplified_RZ_heuristic(file_name[i], 20)
            end = time.time()
            bss = bestsolut[i]
            print(i)
            print(sct1, mbs1)
            RDp.append(RPD(bss, mbs1))
            mbs.append(mbs1)
            sct.append(sct1)
            Tk.append(end-start)
            bs.append(bss)
        else:
            start = time.time()
            sct1, mbs1 = first_improvement_Exchange_Simplified_RZ_heuristic(file_name[i], 20)
            end = time.time()
            bss = bestsolut[i]
            print(i)
            print(sct1, mbs1)
            RDp.append(RPD(bss, mbs1))
            mbs.append(mbs1)
            sct.append(sct1)
            Tk.append(end-start)
            bs.append(bss)
    print(mbs, sct)
    add_in_one_file('FERZ', mbs, 'mbs')
    add_in_one_file('FERZ', sct, 'sct')
    add_in_one_file('FERZ', RDp, 'RPD')
    add_in_one_file('FERZ', file_name, 'file')
    add_in_one_file('FERZ', bs, 'bs')
    add_in_one_file('FERZ', Tk, 'TK')
    print("the experement FERZ is done!")




# -------- 03
def get_experement_FIR_result(file_name, bestsolut):
    mbs = []
    sct = []
    RDp = []
    Tk = []
    bs = []
    for i in range(len(file_name)):
        if i <= 29:
            start = time.time()
            sct1, mbs1 = first_improvement_Insert_Random_permutation(file_name[i], 100, 20)
            end = time.time()
            bss = bestsolut[i]
            print(i)
            print(sct1, mbs1)
            RDp.append(RPD(bss, mbs1))
            mbs.append(mbs1)
            sct.append(sct1)
            Tk.append(end-start)
            bs.append(bss)
        else:
            start = time.time()
            sct1, mbs1 = first_improvement_Insert_Random_permutation(file_name[i], 50, 20)
            end = time.time()
            bss = bestsolut[i]
            print(i)
            print(sct1, mbs1)
            RDp.append(RPD(bss, mbs1))
            mbs.append(mbs1)
            sct.append(sct1)
            Tk.append(end-start)
            bs.append(bss)
    print(mbs, sct)
    add_in_one_file('FIR', mbs, 'mbs')
    add_in_one_file('FIR', sct, 'sct')
    add_in_one_file('FIR', RDp, 'RPD')
    add_in_one_file('FIR', file_name, 'file')
    add_in_one_file('FIR', bs, 'bs')
    add_in_one_file('FIR', Tk, 'TK')
    print("the experement FIR is done!")



# -------- 04

def get_experement_FIRZ_result(file_name, bestsolut):
    mbs = []
    sct = []
    RDp = []
    Tk = []
    bs = []
    for i in range(len(file_name)):
        if i <= 29:
            start = time.time()
            sct1, mbs1 = first_improvement_Insert_Simplified_RZ_heuristic(file_name[i], 20)
            end = time.time()
            bss= bestsolut[i]
            print(i)
            print(sct1, mbs1)
            RDp.append(RPD(bss, mbs1))
            mbs.append(mbs1)
            sct.append(sct1)
            Tk.append(end-start)
            bs.append(bss)
        else:
            start = time.time()
            sct1, mbs1 = first_improvement_Insert_Simplified_RZ_heuristic(file_name[i], 20)
            end = time.time()
            bss = bestsolut[i]
            print(i)
            print(sct1, mbs1)
            RDp.append(RPD(bss, mbs1))
            mbs.append(mbs1)
            sct.append(sct1)
            Tk.append(end-start)
            bs.append(bss)
    print(mbs, sct)
    add_in_one_file('FIRZ', mbs, 'mbs')
    add_in_one_file('FIRZ', sct, 'sct')
    add_in_one_file('FIRZ', RDp, 'RPD')
    add_in_one_file('FIRZ', file_name, 'file')
    add_in_one_file('FIRZ', bs, 'bs')
    add_in_one_file('FIRZ', Tk, 'TK')
    print("the experement FIRZ is done!")



# -------- 05
def get_experement_FTR_result(file_name, bestsolut):
    mbs = []
    sct = []
    RDp = []
    Tk = []
    bs = []
    for i in range(len(file_name)):
        if i <= 29:
            start = time.time()
            sct1, mbs1 = first_improvement_Transpose_Random_permutation(file_name[i], 100, 20)
            end = time.time()
            bss = bestsolut[i]
            print(i)
            print(sct1, mbs1)
            RDp.append(RPD(bss, mbs1))
            mbs.append(mbs1)
            sct.append(sct1)
            Tk.append(end-start)
            bs.append(bss)
        else:
            start = time.time()
            sct1, mbs1 = first_improvement_Transpose_Random_permutation(file_name[i], 50, 20)
            end = time.time()
            bss = bestsolut[i]
            print(i)
            print(sct1, mbs1)
            RDp.append(RPD(bss, mbs1))
            mbs.append(mbs1)
            sct.append(sct1)
            Tk.append(end-start)
            bs.append(bss)
    print(mbs, sct)
    add_in_one_file('FTR', mbs, 'mbs')
    add_in_one_file('FTR', sct, 'sct')
    add_in_one_file('FTR', RDp, 'RPD')
    add_in_one_file('FTR', file_name, 'file')
    add_in_one_file('FTR', bs, 'bs')
    add_in_one_file('FTR', Tk, 'TK')
    print("the experement FTR is done!")



# -------- 06

def get_experement_FTRZ_result(file_name, bestsolut):
    mbs = []
    sct = []
    RDp = []
    Tk = []
    bs = []
    for i in range(len(file_name)):
        if i <= 29:
            start = time.time()
            sct1, mbs1 = first_improvement_Transpose_Simplified_RZ_heuristic(file_name[i], 20)
            end = time.time()
            bss = bestsolut[i]
            print(i)
            print(sct1, mbs1)
            RDp.append(RPD(bss, mbs1))
            mbs.append(mbs1)
            sct.append(sct1)
            Tk.append(end-start)
            bs.append(bss)
        else:
            start = time.time()
            sct1, mbs1 = first_improvement_Transpose_Simplified_RZ_heuristic(file_name[i], 20)
            end = time.time()
            bss = bestsolut[i]
            print(i)
            print(sct1, mbs1)
            RDp.append(RPD(bss, mbs1))
            mbs.append(mbs1)
            sct.append(sct1)
            Tk.append(end-start)
            bs.append(bss)
    print(mbs, sct)
    add_in_one_file('FTRZ', mbs, 'mbs')
    add_in_one_file('FTRZ', sct, 'sct')
    add_in_one_file('FTRZ', RDp, 'RPD')
    add_in_one_file('FTRZ', file_name, 'file')
    add_in_one_file('FTRZ', bs, 'bs')
    add_in_one_file('FTRZ', Tk, 'TK')
    print("the experement FTRZ is done!")

import sys
def loud_bs_filename():
    File_name = get_file_names('instances/instances')
    bestsolution = get_best_solution()
    return File_name,bestsolution
process_arg=sys.argv[1]
if process_arg=='BER':
    print('Starting the ' + process_arg + '...')
    get_experement_BER_result(*loud_bs_filename())
    print(process_arg + 'is donne!')
if process_arg=='FTRZ':
    print('Starting the ' + process_arg + '...')
    get_experement_FTRZ_result(*loud_bs_filename())
    print(process_arg + 'is donne!')
if process_arg=='FTR':
    print('Starting the ' + process_arg + '...')
    get_experement_FTR_result(*loud_bs_filename())
    print(process_arg + 'is donne!')
if process_arg=='FIRZ':
    print('Starting the ' + process_arg + '...')
    get_experement_FIRZ_result(*loud_bs_filename())
    print(process_arg + 'is donne!')
if process_arg=='FIR':
    print('Starting the ' + process_arg + '...')
    get_experement_FIR_result(*loud_bs_filename())
if process_arg=='FERZ':
    print('Starting the ' + process_arg + '...')
    get_experement_FERZ_result(*loud_bs_filename())
    print(process_arg + 'is donne!')
if process_arg=='FER':
    print('Starting the ' + process_arg + '...')
    get_experement_FER_result(*loud_bs_filename())
    print(process_arg + 'is donne!')
if process_arg=='BTRZ':
    print('Starting the ' + process_arg + '...')
    get_experement_BTRZ_result(*loud_bs_filename())
    print(process_arg + 'is donne!')
if process_arg=='BTR':
    print('Starting the ' + process_arg + '...')
    get_experement_BTR_result(*loud_bs_filename())
    print(process_arg + 'is donne!')
if process_arg=='BIRZ':
    print('Starting the ' + process_arg + '...')
    get_experement_BIRZ_result(*loud_bs_filename())
    print(process_arg + 'is donne!')
if process_arg=='BIR':
    print('Starting the ' + process_arg + '...')
    get_experement_BIR_result(*loud_bs_filename())
    print(process_arg + 'is donne!')
if process_arg=='BERZ':
    print('Starting the ' + process_arg + '...')
    get_experement_BERZ_result(*loud_bs_filename())
    print(process_arg + 'is donne!')

