def list_zuoye():

    lai_list=[3,'五',2,1,4]
    print(lai_list[2])
    print(lai_list[1:5])
    lai_list.pop(3)
    print(lai_list)
    lai_list.append(6)
    lai_list.append('七')
    print(lai_list)
    c=[8,9]
    lai_list.extend(c)
    print(lai_list)
    lai_list[0]='5'
    print(lai_list)
    print(len(lai_list))
if __name__ == '__main__':
    list_zuoye()
