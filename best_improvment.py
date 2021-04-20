from Methods import *
from Simplified_RZ_heuristic import Simplified_RZ_heuristic


def best_improvement_Transpose_Random_permutation(csv, job, machine):#give it the csv file with n° machine and jobs return sct and wct

    s = getDataframe('instances/instance2/' + csv + '.csv', machine)
    jobs = list(range(0, job))
    jp = Random_permutation(jobs)
    list_of_nieborhod = transpose_neighbourhood(jp)
    msct1,min1 = WTC(new_matrix_step(s, list_of_nieborhod[0]))
    for i in range(len(list_of_nieborhod)):
        m = new_matrix_step(s, list_of_nieborhod[i])
        sct,wtc = WTC(m)
        if i == 0:
            min = min1
            min1 = 0
            msct= msct1
        else:
            if min > wtc:
                min = wtc
                new_list = list_of_nieborhod[i]
                msct=sct
    return msct,min

def best_improvement_Exchange_Random_permutation(csv, job, machine):#give it the csv file with n° machine and jobs return sct and wct
    s = getDataframe('instances/instance2/' + str(csv) + '.csv', machine)
    jobs = list(range(0, job))
    jp = Random_permutation(jobs)
    list_of_nieborhod = exchange_neighbourhood(jp)
    msct1, min1 = WTC(new_matrix_step(s, list_of_nieborhod[0]))
    for i in range(len(list_of_nieborhod)):
        m = new_matrix_step(s, list_of_nieborhod[i])
        sct, wtc = WTC(m)
        if i == 0:
            min = min1
            min1 = 0
            msct = msct1
        else:
            if min > wtc:
                min = wtc
                new_list = list_of_nieborhod[i]
                msct = sct
    return msct, min

def best_improvement_Insert_Random_permutation(csv, job, machine):#give it the csv file with n° machine and jobs return sct and wct
    s = getDataframe('instances/instance2/' + csv + '.csv', machine)
    jobs = list(range(0, job))
    jp = Random_permutation(jobs)
    list_of_nieborhod = insert_neighbourhood(jp)
    msct1, min1 = WTC(new_matrix_step(s, list_of_nieborhod[0]))
    for i in range(len(list_of_nieborhod)):
        m = new_matrix_step(s, list_of_nieborhod[i])
        sct, wtc = WTC(m)
        if i == 0:
            min = min1
            min1 = 0
            msct = msct1
            msct1=0
        else:
            if min > wtc:
                min = wtc
                new_list = list_of_nieborhod[i]
                msct = sct
    return msct, min

#print(best_improvement_Transpose_Random_permutation('100_20_01',100,20))
#print(best_improvement_Exchange_Random_permutation('50_20_01',50,20))
#print(best_improvement_Insert_Random_permutation('50_20_01',50,20))

def best_improvement_Transpose_Simplified_RZ_heuristic(csv, machine):#give it the csv file with n° machine return sct and wct
    s = getDataframe('instances/instance2/' + csv + '.csv', machine)
    jp = Simplified_RZ_heuristic(csv, machine)

    list_of_nieborhod = transpose_neighbourhood(jp)

    msct1, min1 = WTC(new_matrix_step(s, list_of_nieborhod[0]))
    for i in range(len(list_of_nieborhod)):
        m = new_matrix_step(s, list_of_nieborhod[i])
        sct, wtc = WTC(m)
        if i == 0:
            min = min1
            min1 = 0
            msct = msct1
        else:
            if min > wtc:
                min = wtc
                new_list = list_of_nieborhod[i]
                msct = sct
    return msct, min

def best_improvement_Exchange_Simplified_RZ_heuristic(csv, machine):#give it the csv file with n° machine return sct and wct
    s = getDataframe('instances/instance2/' + csv + '.csv', machine)
    jp = Simplified_RZ_heuristic(csv, machine)

    list_of_nieborhod = exchange_neighbourhood(jp)

    msct1, min1 = WTC(new_matrix_step(s, list_of_nieborhod[0]))
    for i in range(len(list_of_nieborhod)):
        m = new_matrix_step(s, list_of_nieborhod[i])
        sct, wtc = WTC(m)
        if i == 0:
            min = min1
            min1 = 0
            msct = msct1
        else:
            if min > wtc:
                min = wtc
                new_list = list_of_nieborhod[i]
                msct = sct
    return msct, min

def best_improvement_Insert_Simplified_RZ_heuristic(csv, machine):#give it the csv file with n° machine return sct and wct
    s = getDataframe('instances/instance2/' + csv + '.csv', machine)
    jp = Simplified_RZ_heuristic(csv, machine)

    list_of_nieborhod = insert_neighbourhood(jp)

    msct1, min1 = WTC(new_matrix_step(s, list_of_nieborhod[0]))
    for i in range(len(list_of_nieborhod)):
        m = new_matrix_step(s, list_of_nieborhod[i])
        sct, wtc = WTC(m)
        if i == 0:
            min = min1
            min1 = 0
            msct = msct1
        else:
            if min > wtc:
                min = wtc
                new_list = list_of_nieborhod[i]
                msct = sct
    return msct, min

#print(best_improvement_Transpose_Simplified_RZ_heuristic('50_20_11',20))
#print(best_improvement_Exchange_Simplified_RZ_heuristic('50_20_01',20))
#print(best_improvement_Insert_Simplified_RZ_heuristic('50_20_19',20))

#print(best_improvement_Transpose_Random_permutation('100_20_01',100,20))
#print(best_improvement_Exchange_Random_permutation('50_20_01',50,20))
#print(best_improvement_Insert_Random_permutation('50_20_01',50,20))


import sys
process_arg1=sys.argv[1]
process_arg2=sys.argv[2]
process_arg3=sys.argv[3]
process_arg4=sys.argv[4]
if process_arg1=='BTR':
    print('Starting the ' + process_arg1 + '...')
    print(best_improvement_Transpose_Random_permutation(process_arg2,int(process_arg3),int(process_arg4)))
    print(process_arg1 + 'is donne!')
if process_arg1=='BER':
    print('Starting the ' + process_arg1 + '...')
    print(best_improvement_Exchange_Random_permutation(process_arg2,int(process_arg3),int(process_arg4)))
    print(process_arg1 + 'is donne!')
if process_arg1=='BIR':
    print('Starting the ' + process_arg1 + '...')
    print(best_improvement_Insert_Random_permutation(process_arg2,int(process_arg3),int(process_arg4)))
    print(process_arg1 + 'is donne!')
if process_arg1=='BTRZ':
    print('Starting the ' + process_arg1 + '...')
    print(best_improvement_Transpose_Simplified_RZ_heuristic(process_arg2,int(process_arg3)))
    print(process_arg1 + 'is donne!')
if process_arg1=='BIRZ':
    print('Starting the ' + process_arg1 + '...')
    print(best_improvement_Insert_Simplified_RZ_heuristic(process_arg2,int(process_arg3)))
    print(process_arg1 + 'is donne!')
if process_arg1=='BERZ':
    print('Starting the ' + process_arg1 + '...')
    print(best_improvement_Exchange_Simplified_RZ_heuristic(process_arg2,int(process_arg3)))
    print(process_arg1 + 'is donne!')

