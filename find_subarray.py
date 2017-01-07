def find_subarray(input_list):
    lowindex=-1 #Stores lowindex of unsorted sub-array
    highindex=-1 #Stores highindex of unsorted sub-array
    min_value=input_list[0]
    sub_list=[]
    max_value=input_list[len(input_list)-1]
    for i in range(1,len(input_list)):
        if min_value<=input_list[i]:
            min_value=input_list[i]
            continue
        else:
            lowindex=i
            break
    for j in range(len(input_list)-2,-1,-1) :
        if max_value >= input_list[j]:
            max_value=input_list[j]
            continue
        else:
            highindex=j
            break
    #If value is unchanged from initialised value,means array is already sorted
    if (lowindex==highindex):
        return 0
    if(lowindex>highindex):
        sub_list=input_list[highindex:lowindex+1]
    else:
        sub_list=input_list[lowindex:highindex+1]

    min_sub_list=min(sub_list)
    max_sub_list = max(sub_list)
    #Find the position of minimum element in unsorted sub-list lie in left-side
    # and the postion of maximum element in unsorted sub-list lie in right-side
    for i in range(0,len(input_list)):
        if min_sub_list>input_list[i]:
            continue
        else:
            lowindex=i
            break
    for j in range(len(input_list)-1,-1,-1):
        if max_sub_list<input_list[j]:
            continue
        else:
            highindex=j
            break

    print("Subarray which requires sorting start from %d" %lowindex,"and ends at %d"%highindex)
    return (highindex-lowindex)+1


if __name__ == '__main__':
    input_list=[1,2,0,0,0,7,8]
    value=find_subarray(input_list)
    print(value)
