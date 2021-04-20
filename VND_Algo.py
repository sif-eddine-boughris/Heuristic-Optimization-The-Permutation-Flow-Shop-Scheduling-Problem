from Methods import *
from Simplified_RZ_heuristic import Simplified_RZ_heuristic

def first_improvement_Insert(csv,machine,init_list):#give it the file name ,n° of machine and the intial sequance return wtc and new list of nighborhod
    s = getDataframe('instances/instance2/' + csv + '.csv', machine)
    list_of_nieborhod =insert_neighbourhood(init_list)

    msct1, min1 = WTC(new_matrix_step(s, list_of_nieborhod[0]))
    new_list=list_of_nieborhod[0]
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
                break


    return msct,min,new_list


def first_improvement_exchange(csv,machine,init_list):#give it the file name ,n° of machine and the intial sequance return wtc and new list of nighborhod
    s = getDataframe('instances/instance2/' + csv + '.csv', machine)
    list_of_nieborhod =exchange_neighbourhood(init_list)

    msct1, min1 = WTC(new_matrix_step(s, list_of_nieborhod[0]))
    new_list=list_of_nieborhod[0]
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
                break


    return msct,min,new_list

def first_improvement_transpose(csv,machine,init_list):#give it the file name ,n° of machine and the intial sequance return wtc and new list of nighborhod
    s = getDataframe('instances/instance2/' + csv + '.csv', machine)
    list_of_nieborhod =transpose_neighbourhood(init_list)

    msct1, min1 = WTC(new_matrix_step(s, list_of_nieborhod[0]))
    new_list=list_of_nieborhod[0]
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
                break


    return msct,min,new_list


def VND_first_order(csv,machine):
    s = getDataframe('instances/instance2/' + csv + '.csv', machine)
    jp = Simplified_RZ_heuristic(csv, machine)
    msct1,min1,list1=first_improvement_transpose(csv,machine,jp)
    msct2, min2, list2=first_improvement_exchange(csv,machine,list1)
    msct3, min3, list3=first_improvement_Insert(csv,machine,list2)
    return msct3,min3



def VND_second_order(csv,machine):
    s = getDataframe('instances/instance2/' + csv + '.csv', machine)
    jp = Simplified_RZ_heuristic(csv, machine)
    msct1,min1,list1=first_improvement_transpose(csv,machine,jp)
    msct2, min2, list2=first_improvement_Insert(csv,machine,list1)
    msct3, min3, list3=first_improvement_exchange(csv,machine,list2)
    return msct3,min3


import sys
process_arg1=sys.argv[1]
process_arg2=sys.argv[2]
process_arg3=sys.argv[3]
if process_arg1=='VNDFO':
    print('Starting the ' + process_arg1 + '...')
    print(VND_first_order(process_arg2,int(process_arg3)))
    print(process_arg1 + 'is donne!')
if process_arg1=='VNDSO':
    print('Starting the ' + process_arg1 + '...')
    print(VND_first_order(process_arg2,int(process_arg3)))
    print(process_arg1 + 'is donne!')
