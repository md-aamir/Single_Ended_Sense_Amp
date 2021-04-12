
import csv
filename = "sample.txt"
    
step=0.005
vi=0.8

ti=0.0000000025
tad1=0.0000000001
tad2=0.000000002

v=1.06
t=ti
t2=0
Data=[['#time','V'],[0,v]]
for i in range(20):
        Data.append([t,v])
        v=v+step
        t2=t+tad1
        Data.append([t2,v])
        t=t+tad2
v=1.045	
for i in range(10):
         Data.append([t,v])
         v=v-step
         t2=t+tad1
         Data.append([t2,v])
         t=t+tad2



# writing to csv file  
with open(filename, 'w') as csvfile:  
    # creating a csv writer object  
    csvwriter = csv.writer(csvfile)  
        
    # writing the data rows  
    csvwriter.writerows(Data)
