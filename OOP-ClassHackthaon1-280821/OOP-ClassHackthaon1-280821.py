import os
name=[]
branch=[]
bloodgrp=[]
date=[]
status=[]
def donate(name,branch,date,bloodgrp,status,data):
    name.append(input("Enter your name please :"))
    branch.append(input("Enter your branch name:"))
    bloodgrp.append(input("Enter your blood group :"))
    date.append(input("Enter date :"))
    data.write("\n ********************* \n "+"Name :"+str(name[len(name)-1])+"\n Branch Name :"+str(branch[len(name)-1])+"\n Blood Group :"+str(bloodgrp[len(name)-1])+"\n Date : "+str(date[len(name)-1])+"\nStatus : Blood Donated\n")
    status.append(1)
def request(name,branch,date,bloodgrp,status,data):
    name.append(input("Enter your name please :"))
    branch.append(input("Enter your branch name :"))
    bloodgrp.append(input("Enter requested blood group :"))
    date.append(input("Enter date :"))
    data.write("\n ********************* \n "+"Name :"+"\n Branch Name :"+str(branch[len(name)-1])+"\n Blood Group :"+str(bloodgrp[len(name)-1])+"\n Date : "+str(date[len(name)-1])+"\nStatus : Blood requested \n")
    status.append(2)
def bloodinfo(name,branch,date,bloodgrp,status):
    for i in range(len(name)):
        print("\n ********************* \n "+"Name :"+str(name[i])+"\n Branch Name :"+str(branch[i])+"\n Blood Group :"+str(bloodgrp[i])+"\n Date : "+str(date[len(name)-1]))
        if(status[i]==1):
            print(" Status : Blood Donated")
        else:
            print(" Status : Blood Requested")
print("------- Welcome to Blood Bank ------- ")
os.chdir("C:\\Users\\LENOVO\\OneDrive\\Desktop\\OOP\\OOP-ClassHackthaon1-280821")
data=open("BloodBankData.txt",'a+')
while(1):
    print("\n 1) Donate Blood\n 2) Request Blood \n 3) Blood Bank's Data \n 4) Enteries with rare blood group \n 5) Enteries in a particular branch \n 6)Search by date \n 7) Search person by name \n 8) Exit")
    n=int(input())
    if(n==1):
        donate(name,branch,date,bloodgrp,status,data)
    elif(n==2):
        request(name,branch,date,bloodgrp,status,data)
    elif(n==3):
        bloodinfo(name,branch,date,bloodgrp,status)
    elif(n==4):
        for i in range(len(name)):
            if(bloodgrp[i]=="O-"):
                print("\n ********************* \n "+"Name :"+str(name[i])+"\n Branch Name :"+str(branch[i])+"\n Blood Group :"+str(bloodgrp[i]))
                if(status[i]==1):
                    print(" Status : Blood Donated")
                else:
                    print(" Status : Blood Requested") 
    elif(n==5):
        br=input("Enter the name of branch :")
        for i in range(len(name)):
            if(branch[i]==br):
                print("\n ********************* \n "+"Name :"+str(name[i])+"\n Branch Name :"+str(branch[i])+"\n Blood Group :"+str(bloodgrp[i]))
                if(status[i]==1):
                    print(" Status : Blood Donated")
                else:
                    print(" Status : Blood Requested")  
    elif(n==6):
        d=input("Enter date :")
        for i in range(len(name)):
            if(date[i]==d):
                print("\n ********************* \n "+"Name :"+str(name[i])+"\n Branch Name :"+str(branch[i])+"\n Blood Group :"+str(bloodgrp[i]))
                if(status[i]==1):
                    print(" Status : Blood Donated")
                else:
                    print(" Status : Blood Requested")                
    elif(n==7):
        ind=input("Enter name :")
        for i in range(len(name)):
            if(name[i]==ind):
                print("Name :"+str(name[i])+"\n Branch Name :"+str(branch[i])+"\n Blood Group :"+str(bloodgrp[i]))
                if(status[i]==1):
                    print(" Status : Blood Donated")
                else:
                    print(" Status : Blood Requested")
    else:
        break