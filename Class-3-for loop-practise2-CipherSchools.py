# practise for loop
# ask user name and count each character
# "POCHIMIREDDY HARIKA"
# P : 
# O : 
# C : 
# H :
# I :
# M :
# R :
# E :
# D :
# Y :
# A :
# K :
name = input("enter your name : ")
temp = ""
for i in range(0,len(name)):
    if name[i] not in temp:
        print(f"{name[i]}: {name.count(name[i])}")
        temp += name[i]