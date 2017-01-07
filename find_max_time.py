import time
def get_max_time(a,b,c,d):
    max_time="" #store maximum time
    input_list=[]
    input_list.append(a)
    input_list.append(b)
    input_list.append(c)
    input_list.append(d)
    result=calculate_max_time(input_list,max_time)
    print(result)

def calculate_max_time(input_list,max_time):
    pos=-1
    flag_time=False
    flag_min=False
    temp=input_list[0]
    #Find a value in the range 0-2 for first position of HH format
    for i in range(0,len(input_list)):
        if(0<=input_list[i]<=2):
            if(temp>2):
                temp=input_list[i]
                pos=i
            if (temp<=input_list[i]):
                temp=input_list[i]
                pos=i
    max_time+=str(input_list[pos])
    #Check if there is valid range for hours is present or not
    flag_hr,input_list,max_time=check_valid_hour_format(input_list,max_time,pos)
    if (flag_hr):
        #Check if there is valid range for minute is present or not
        flag_min,input_list,max_time=check_valid_minute_format(input_list,max_time)
        if (flag_min):
            max_time+=str(input_list[0])
            flag_time=True
        else:
            #If Valid Hour and Minute is not found then check again for the next combination
            flag_hr=False
            # Restore the numbers in list
            input_list.append(int(max_time[0]))
            input_list.append(int(max_time[1]))
            max_time=""
    if((not flag_hr) and (not flag_min)):
        for i in range(0, len(input_list)):
            if (0 <= input_list[i] <= 2):
                if (temp > 2):
                    temp = input_list[i]
                if (temp <= input_list[i]):
                    temp = input_list[i]
                pos = i
        max_time += str(input_list[pos])
        flag_hr, input_list, max_time = check_valid_hour_format(input_list, max_time, pos)
        if (flag_hr):
            flag_min, input_list, max_time = check_valid_minute_format(input_list, max_time)
            if (flag_min):
                max_time += str(input_list[0])
                flag_time = True
    if (flag_time):
        return max_time
    else:
        return "NOT POSSIBLE"

#Function validate the hour format, if it is valid than return True
# else return False
def check_valid_hour_format(input_list,max_time,pos):
    flag=False
    if(int(max_time[0])==2):
        input_list.pop(pos)
        temp_index=-1
        temp_val=input_list[0]
        for i in range (0,len(input_list)):
            if(0<=input_list[i]<=3):
                if(temp_val>3):
                    temp_val=input_list[i]
                    temp_index = i
                if(input_list[i]>=temp_val):
                    temp_val=input_list[i]
                    temp_index = i
                flag=True
        if(flag):
            max_time+=str(temp_val)
            input_list.pop(temp_index)
    if (0<=int(max_time[0])<2):
        input_list.remove(input_list[pos])
        temp_index = -1
        temp_val = input_list[0]
        for i in range(0,len(input_list)):
            if(temp_val<=input_list[i]):
                temp_val=input_list[i]
                temp_index=i
                flag=True
        if(flag):
            max_time += str(temp_val)
            input_list.pop(temp_index)
    return flag,input_list,max_time

#Function validate the minute format, if it is valid than return True
# else return False
def check_valid_minute_format(input_list,max_time):
    flag=False
    temp_val=input_list[0]
    pos=-1
    for j in range (0,len(input_list)):
        if(0<=input_list[j]<=5):
            if(temp_val>5):
                temp_val=input_list[j]
                pos = j
            if(temp_val<=input_list[j]):
                temp_val=input_list[j]
                pos = j
            flag=True
    if(flag):
        max_time+=":"+str(temp_val)
        input_list.pop(pos)
    return flag,input_list,max_time

if __name__ == '__main__':
    start_time = time.time()
    get_max_time(2,9,0,0)
