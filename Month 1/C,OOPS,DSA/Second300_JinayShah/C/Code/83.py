def addOperators(num, target):
    def backtrack(index, path, value, prev_operand):
        if index == len(num):
            if value == target:
                result.append(path)
            return

        for i in range(index, len(num)):
            curr_str = num[index:i+1]
            curr_num = int(curr_str)

            if index == 0:
                backtrack(i + 1, curr_str, curr_num, curr_num)
            else:
                
                backtrack(i + 1, path + '+' + curr_str, value + curr_num, curr_num)

                
                backtrack(i + 1, path + '-' + curr_str, value - curr_num, -curr_num)

                
                backtrack(i + 1, path + '*' + curr_str, value - prev_operand + prev_operand * curr_num, prev_operand * curr_num)

            if curr_num == 0:
                break  

    result = []
    if num:
        backtrack(0, '', 0, 0)

    return result


num = "123"
target = 6
result = addOperators(num, target)
print("Expression Add Operators Result:", result)
