import csv
import os
from itertools import islice
import pandas as pd

def get_file_names(path):  ## get the name of the file in instance with out the type
    l = os.listdir(path)
    li = [x.split('.')[0] for x in l]
    li = li[1:-1]
    return li


File_name = get_file_names('instances/instances')


def creat_csv(csv_name):  ## creat a csv file with the list of th file names
    for i in csv_name:
        import pandas as pd
        df = pd.DataFrame()
        df.to_csv('instances/instance2/' + str(i) + '.csv', header=False, index=False)


# creat_csv(File_name)

def CSV_file(filename): #write in the csv file the data frome the txt file coresspond
    with open('instances/instances/' + filename + '.txt') as f:
        first_line = f.readline()
        jobs = first_line.split(' ')[0]
        machine = first_line.split(' ')[1]
        #print(machine)
        header = ['job']
        w = 'w'

        for i in range(int(machine)):
            M = 'M' + str(i + 1)
            header.append(M)
        header.append(w)
        #print(header)
        with open('instances/instance2/' + filename + '.csv', 'w') as file:
            dw = csv.DictWriter(file, delimiter=',', fieldnames=header)
            dw.writeheader()
        for i in range(int(jobs)):
            line = f.readline()
            line = line.strip()
            L = line.split(' ')
            L2 = []
            for Z in range(len(L) + 1):
                if Z % 2 != 0:
                    L1 = L[Z]
                    L2.append(L1)
            LLL = [str(i + 1)]
            LLL = LLL + L2
            with open('instances/instance2/' + filename + '.csv', 'a') as fd:
                writer = csv.writer(fd)
                writer.writerow(LLL)
            #fd.close()
        file.close()
for i in range(len(File_name)):
    CSV_file(File_name[i])
    print('file '+File_name[i]+' done!')

def get_wieght_from_txt(file_name): #get the weight from the txt file and return in into a list of list
    with open('instances/instances/'+file_name+'.txt') as f:
        first_line = f.readline()
        jobs = first_line.split(' ')[0]
        w = int(jobs) + 1
        w1 = int(jobs) * 2
        # f.seek(5527,0)
        # F= [jobs,w]
        A = []
        for line in islice(f, w, w1+1):
            line=line[:-1]
            l = line[11:14]
            A.append(l)
        return A

def add_wieght(file,w):
    df = pd.read_csv('instances/instance2/'+file+'.csv')
    df['w'] = w
    df.to_csv('instances/instance2/'+file+'.csv')

for i in range(len(File_name)):
    w=get_wieght_from_txt(File_name[i])
    add_wieght(File_name[i],w)
    print('file'+File_name[i]+'is done!')