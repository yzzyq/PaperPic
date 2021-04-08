



if __name__ == '__main__':
    all_result = []
    with open('C:/Users/yzzyq/Desktop/结果/19411/19411-precise-recall.txt', 'r') as f:
        one_sn_result = []
        for line_index, one_line in enumerate(f.readlines()):
            one_line = one_line.strip('')
            many_result = one_line.split(', ')
            one_result = []
            for index in range(3):
                num = float(many_result[index].split(':')[1])
                one_result.append(num)
            one_sn_result.append(one_result)
            if (line_index + 1) % 20 == 0:
                print(one_sn_result)
                all_result.append(one_sn_result)
                one_sn_result = []
    # print(all_result)
            
            
        