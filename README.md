# Heuristic-Optimization-The-Permutation-Flow-Shop-Scheduling-Problem




#### Sif Eddine Boughris

#### Dr.T.Stutzle

#### Federico Pagnozzi

##### 2020





## 1 Reforming the data

```
In the class DAtafix, I took the txt file and reformed it into a csv file such that :
```
1. first column is Job.
2. from second column until 20Th is the machines.
3. the last column is the weight w




## 2 The Permutation Flow Shop Scheduling Problem

```
In the class Methods I create a function for :
```
1. Calculate the Computing completion times
2. Calculate the Make-span
3. Calculate Sum of completion times
4. Calculate Weighted sum of completion times
5. give a Random permeation
6. get all the possible transpose neighbourhood
7. get all the possible exchange neighbourhood
8. get all the possible insert neighbourhood
In the class Simplified RZ heuristic :
1. get the Initial solution
to try a file with this function call :
directory>python SRZH File_name n°machine
example :
PycharmProjects\Implimentation_01>python Simplified_RZ_heuristic.py SRZH 50_20_01 20




Exercise 1.

### 3.1 first-improvement

#### 3.1.1 code

in class First improvement i create 6 function take csv file name and number of machine return
Sum of completion times and Weighted sum of completion times :

1. first improvement Transpose Random permutation (FTR)
2. first improvement Exchange Random permutation (FER)
3. first improvement Insert Random permutation (FIR)
4. first improvement Transpose Simplified RZ heuristic (FTRZ)
5. first improvement Exchange Simplified RZ heuristic (FERZ)
6. first improvement Insert Simplified RZ heuristic (FIRZ)
to try one of the code on a file run :
for Random prmutation you need to give it the filename and the job n° and machine n° :
directory>python first_improvment.py function File_name n°job n°machine
for Simplified RZ heuristic you need to give it the file name and the machine n° :
directory>python first_improvment.py function File_name n°machine
example :
python first_improvment.py FTR 50_20_01 20

#### 3.1.2 experiment

in class Experiment-ex01 i create 6 function that take A list Of file Name and list of best sulution
return a scv file of the experement with :




1. file : the file name
2. sct : the Sum of completion times
3. bs : the given best solution
4. mbs : my best solution
5. RPD : Relative percentage deviation
6. TK : Computation time
function :
1. get experement FER result
2. get experement FERZ result
3. get experement FIR result
4. get experement FIRZ result
5. get experement FTR result
6. get experement FTRZ result
to lunch the experiment on terminal i did it this way do i can do multiples experiments in the same
time :
give it the Function abbreviation :directory>python function
example :
Implimentation_01>python experement_ex1.py FTR

### 3.2 best-improvement

#### 3.2.1 code

in class First improvement i create 6 function take csv file name and number of machine return
Sum of completion times and Weighted sum of completion times :

1. best improvement Transpose Random permutation (BTR)
2. best improvement Exchange Random permutation (BER)
3. best improvement Insert Random permutation (BIR)
4. best improvement Transpose Simplified RZ heuristic (BTRZ)
5. best improvement Exchange Simplified RZ heuristic (BERZ)
6. best improvement Insert Simplified RZ heuristic (BIRZ)


to try one of the code on a file run :
for Random prmutation you need to give it the filename and the job n° and machine n° :
directory>python best_improvment.py function File_name n°job n°machine
for Simplified RZ heuristic you need to give it the file name and the machine n° :
directory>python best_improvment.py function File_name n°machine
example :
>python best_improvment.py BTR 50_20_01 20

#### 3.2.2 experiment

in class Experiment-ex01 i create 6 function that take A list Of file Name and list of best sulution
return a scv file of the experement with :

1. file : the file name
2. sct : the Sum of completion times
3. bs : the given best solution
4. mbs : my best solution
5. RPD : Relative percentage deviation
6. TK : Computation time
function :
1. get experement BER result
2. get experement BERZ result
3. get experement BIR result
4. get experement BIRZ result
5. get experement BTR result
6. get experement BTRZ result
to lunch the experiment on terminal i did it this way do i can do multiples experiments in the same
time :
give it the Function abbreviation :directory>python experement_ex1.py function
example :
Implimentation_01>python experement_ex1.py BTR



### 3.3 Average

in the class Average I create a function that take a list of CSV file of the experiment and for
each file calculate the Average relative percentage deviation and the Average computation time,
and return a csv file with :

1. experiment : name of the experiment
2. ARPD100 : Average relative percentage deviation of 100 jobs
3. ARPD50 :Average relative percentage deviation of 50 jobs
4. ATK100 :Average computation time of 100 jobs
5. ATK50 : Average computation time of 50 jobs

### 3.4 statistically significant difference

```
Between t-test Wilcoxon test
FER and FERZ 2.008025e-47 1.671329e-
FIR and FIRZ 4.888526e-47 1.671329e-
FTR and FTRZ 3.755509e-46 1.671e-
BER and BERZ 1.433584e-44 1.671329e-
BIR and BIRZ 9.19861e-45 1.671329e-
BIR and BIRZ 9.236752e-50 1.671329e-
```

## From the result we got we can say that the BIRZ is the best between All of them

### 3.3 Average
```
    experement ARPD100 ARPD50 ATK100 ATK
    BER 44.19015517709465 33.822018411697876 55.2666533390681 55.
    BERZ 4.567794178615989 3.7168858649276495 116.00498882134757 116.
    BIR 45.99690863889201 36.13293355226444 158.00781416893003 158.
    BIRZ 4.454317815029091 3.432013268964613 275.64490847587587 275.
    BTR 47.970525713775366 38.527317990105374 1.0243775844573977 1.
    BTRZ 4.695859047305018 3.803821206730712 47.33931296666463 47.
    FER 50.06445478128428 40.00482636778615 1.3007618506749472 1.
    FERZ 4.717295373426015 3.7782950845415537 59.46191665331523 59.
    FIR 48.872748346412585 39.78089831320312 26.8381044626236 26.
    FIRZ 4.712243120796617 3.7240231971564057 166.7576253414154 166.
    FTR 49.37680088285586 39.96281042588668 0.1699773708979289 0.
    FTRZ 4.728584881391611 3.822780238218405 45.3091076374054 45.
```



Exercise 2.

In the class VND i create a 3 function that take csv file name ,the number of machine and the
Initial solution/sequence,return Weighted sum of completion times and the new Initial solution :

1. first improvement Insert
2. first improvement exchange
3. first improvement transpose

### 4.1 First order

transpose, exchange, insert VNDFO
I create a function that take the 3 function above in the order given and return the Weighted sum
of completion times, Sum of completion times

### 4.2 second order

transpose, insert, exchange VNDSO
I creat a function that take the 3 function above in the order given and return the Weighted sum of
completion times, Sum of completion times
To run one of the orders on a file do :directory>python experement_ex1.py order
example :
\Implimentation_01>python experement_ex1.py VNDFO|

### 4.3 Experiment

in class Experiment-ex01 i create 2 function that take A list Of file Name and list of best sulution
return a csv file of the experement with :





1. file : the file name
2. sct : the Sum of completion times
3. bs : the given best solution
4. mbs : my best solution
5. RPD : Relative percentage deviation
6. TK : Computation time
function :
1. get experement VND01 result
2. get experement VND01 result
to run the experement do :directory>python VND_Algo.py order file_name n°machine
example :
Implimentation_01>python VND_Algo.py VNDFO 50_20_02 20

### 4.4 Average

in the class Average I create a function that take a list of CSV file of the experiment and for
each file calculate the Average relative percentage deviation and the Average computation time,
and return a csv file with :

1. experiment : name of the experiment
2. ARPD100 : Average relative percentage deviation of 100 jobs
3. ARPD50 :Average relative percentage deviation of 50 jobs
4. ATK100 :Average computation time of 100 jobs
5. ATK50 : Average computation time of 50 jobs

### 4.5 statistically significant difference

```
Between t-test Wilcoxon test
VND1 and VND2 0.4312 0.
```
for the first order :
the Average relative percentage deviation of 100 job is equal to 4.56 and for 50 jobs is equal to
3.55 , the Average computation time of 100 jobs is equal to 148.64 and also for 50 job with a small




difference
for the second order :
the Average relative percentage deviation of 100 job is equal to 4.55 and for 50 jobs is equal to
3.52 , the Average computation time of 100 jobs is equal to 148.34 and also for 50 job with a small
difference
so the first order is better then the second one

### 4.6 NOTE

in the beginning of development i thought that the machine number is changeable this is why
you find me give it as a input, for future development i will take that into account


