def find_max(array,k,min_array):
    pointer = -1

    if(len(array)<k):
        return min_array
    minimum = array[pointer + 1]
    for i in range(0,k):
        if (array[i] < minimum):
            minimum = array[i]
        pointer+=1
    min_array.append(minimum)
    if (pointer <= len(array) - 1):
        min_array=find_max(array[k-pointer:len(array)],k,min_array)
    return min_array


def min_k_size_window(array,k):

    min_array=[]
    if(len(array)==k):
        minimum=array[0]
        for i in range(1,len(array)):
            if(array[i]<minimum):
                minimum=array[i]
        print(minimum)
        min_array.append(minimum)
        return min_array
    else:
        return find_max(array,k,min_array)

if __name__ == "__main__":

    output=min_k_size_window([6,5,4,3,2,1],1)
    print(output)
    print(max(output))