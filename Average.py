import pandas as pd
import os


def add_in_one_file(file, w, column):
    df = pd.read_csv(file )
    df[str(column)] = w
    df.to_csv( file , index=False)
    # df.close()
def get_file_names(path):
    l = os.listdir(path)
    print(l)
    li = [x.split('.')[0] for x in l]
    return li
File_name_Experement01= get_file_names('experement')
File_name_Experement02=get_file_names('experement2')
print(File_name_Experement02)
Savepath01='Average/Experement1/Avrage1.csv'
savepath02='Average/Experement2/Avrage2.csv'

def get_Avrage_RPD_and_Tk(Filepath,file_name,savepath):
    aRPD100=[]
    aRPD50=[]
    aTK100=[]
    aTK50=[]
    for i in range (len(file_name)):
        df = pd.read_csv(Filepath+'/'+file_name[i]+'.csv')
        shape0 = df.shape[0]
        s = int(shape0 / 2)
        ARPD100 = df['RPD'][0:s].mean()
        ARDP50 = df['RPD'][s:].mean()
        ATK100 = df['TK'][0:s].mean()
        ATk50 = df['TK'][s:].mean()
        aRPD100.append(ARPD100)
        aRPD50.append(ARDP50)
        aTK100.append(ATK100)
        aTK50.append(ATK100)
    add_in_one_file(savepath,file_name,'experement')
    add_in_one_file(savepath,aRPD100,'ARPD100')
    add_in_one_file(savepath,aRPD50,'ARPD50')
    add_in_one_file(savepath,aTK100,'ATK100')
    add_in_one_file(savepath,aTK50,'ATK50')

#get_Avrage_RPD_and_Tk('experement',File_name_Experement01,Savepath01)

get_Avrage_RPD_and_Tk('experement2',File_name_Experement02,savepath02)