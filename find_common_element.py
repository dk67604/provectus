def find_common_element(input_a,input_b):
    """
    Find common element between two sorted array in O(n) runtime
    :param input_a:
    :param input_b:
    :return:
    """
    index=0
    flag=False
    for i in range (0,len(input_a)):
        if input_a[i]>=input_b[index]:
            for j in range(index,len(input_b)):
                if(input_a[i]==input_b[j]):
                    print(input_a[i])
                    flag=True
                    index+=1
                    break
                if (input_a[i]<input_b[j]):
                    index+=1
                    break

        else:
            continue
    if not flag:
        print("No common element")

if __name__ == '__main__':
    a=[13,17,35,40,49,55,59]
    b=[13,35,39,40,55,58,60]
    find_common_element(a,b)

