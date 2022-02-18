import numpy as np
import matplotlib.pyplot as plt
import csv

def read_csv_file(filename):
    data = []
    with open(filename) as f:
        
        #remove first 9 lines
        lines = f.readlines()[10:]
        
        for index in range(len(lines)):
            
            if index == 0:
                
                headers = []
                for i in range(len(lines[index].split(",")[:10])):
                    attr = lines[index].split(",")[i]
                    if lines[index+1].split(",")[i] not in lines[index].split(",")[i]:
                       attr = ' '.join([lines[index].split(",")[i].strip(), lines[index+1].split(",")[i].strip()])
                    headers.append(attr)
                
                continue
                
            if index == 1: continue
            
            line = {}
            for i in range(len(headers)):
                
                if headers[i] == 'alpha':
                    line[headers[i]] = int(float(lines[index].split(",")[i]))
                else:
                    line[headers[i]] = float(lines[index].split(",")[i])
            
            data.append(line)
    return data
            

# Problem 1 Code
def problem1(problem1_data):
    pass

# Problem 2 Code        
def problem2(filename1,filename2,filename3):
    pass

# Problem 3 Code
def problem3(filename1):
    pass
    
    
# run all problems
def main():
    problem1_data = read_csv_file('homeworks/homework3/george/data/NACA0012.csv')
    print(problem1_data)
if __name__ == "__main__":
    main()
    