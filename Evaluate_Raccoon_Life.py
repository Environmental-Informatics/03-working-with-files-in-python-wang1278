# -*- coding: utf-8 -*-
"""
Date of Creation: 02/07/2020
Name of Creator: Linji Wang
Description of Program:
    Assignment 03 - Using Files and Simple Data Structures with Python
    This scrpt reads data from text file '2008Male00006.txt', 
    calculates several variables and store data in a re-orgnized, 
    tab-delimited format inside a new text file 'Georges_life.txt'.
"""
import math
# sum_lst is a function defined for calculating sum of a list.
def sum_lst(lst):
    x=0
    for i in range(len(lst)):
       x=x+float(lst[i])
    return x
# mean_lst is a function defined for calculating sum of a list.
def mean_lst(lst):
    x=sum_lst(lst)/len(lst)
    return x
# dist_lst is a function defined for calculating the distance between two points given as lists.
def dist_lst(lst1,lst2):
    lst=[0]*len(lst1)
    # the following argument are to change the given data type into float for computations.
    for i in range(1,len(lst1)):
        lst1[i]=float(lst1[i])
        lst1[i-1]=float(lst1[i-1])
        lst2[i]=float(lst2[i])
        lst2[i-1]=float(lst2[i-1])
        # Distance calculation is as follow
        lst[i]=math.sqrt((lst1[i]-lst1[i-1])**2+(lst2[i]-lst2[i-1])**2)
    return lst

# Import the data file as a list.
dm=open('2008Male00006.txt','r')
lst=dm.readlines()
dm.close()
# Creat a list and stor headers, contents in it.
header=lst[0].strip().split(',')
df=[]
l=len(lst)
for i in lst[1:l]:
    if i.find(',') !=-1:
        df.append([l for l in i.strip().split(',')])
    # Identify the different lines and store differenly.
    else:
        stat=i.strip()
# Create a disctionary and first store headers and values.
dic_hv={}
for i in range(len(header)):
    dic_hv[header[i].strip()]=[row[i] for row in df]
# Create another dictionary to store distances.
dic_dis={}
dic_dis['Distance']=dist_lst(dic_hv['X'],dic_hv['Y'])
# Combine the two dictionary
dic_rac=dict(dic_hv,**dic_dis)

# Create an text output file "Georges_life.txt" with proper header block.
gl=open('Georges_life.txt','w')
name=header[3]+dic_rac[header[3]][0]
x_ave=str(mean_lst(dic_rac['X']))
y_ave=str(mean_lst(dic_rac['Y']))
sum_dist=str(sum_lst(dic_rac['Distance']))
ave_energy=str(mean_lst(dic_rac['Energy Level']))
gl_hb=['Raccoon name: '+name+'\n'+'Average location: '+x_ave+', '+y_ave+'\n'+'Distance traveled: '+sum_dist+'\n'+'Average energy level: '+ave_energy+'\n'+'Raccoon end state: '+stat+'\n']
gl.writelines(gl_hb)
# Write headers and data in a tab delimited format.
gl_header=['Date\tTime\tX\tY\tAsleep Flag\tBehavior Mode\tDistance Traveled\n']
gl.writelines(gl_header)
gl_data=[]
for i in range(len(df)):
    gl_data.append(str(dic_rac['Day'][i])+'\t'+str(dic_rac['Time'][i])+'\t'+str(dic_rac['X'][i])+'\t'+str(dic_rac['Y'][i])+'\t'+dic_rac['Asleep'][i]+'\t'+dic_rac['Behavior Mode'][i]+'\t'+str(dic_rac['Distance'][i])+'\n')
gl.writelines(gl_data)
# Close the file to apply changes.
gl.close()
