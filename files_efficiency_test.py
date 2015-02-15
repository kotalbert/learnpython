#This is to test the python efficiency in reading large files
import random


def create_data_file(size):
    with open('C:/Users/lenovo/Desktop/sample_file.txt', 'w') as f:
        for i in range(0,size):
            rg = random.gauss(0,1)
            ru = random.uniform(0,1)
            line = "%i,%f,%f\n" %(i,rg,ru)
            f.write(line)
        f.close()
    print 'file created'

big_num =  2*10**6
small_num = 10**3       
#create_data_file(big_num)
        
#Reading file and some simple manipulation
import csv
import datetime
def manipulate_file():
    start_time = datetime.datetime.now()
    with open('C:/Users/lenovo/Desktop/sample_file.txt', 'r') as f:
        file_rows = csv.reader(f)
       
        for r in file_rows:
            id = int(r[0])
            g = float(r[1])
            u = float(r[2])
            g = g*1000+random.uniform(0,1)
            u = u*5000+random.gauss(0,1)
    f.close()
    end_time = datetime.datetime.now()
    print end_time - start_time
    
manipulate_file()