def value(roman):
    if(roman=='I'):
        return 1
    elif(roman=='IV'):
        return 4
    elif(roman=='V'):
        return 5
    elif(roman=='IX'):
        return 9
    elif(roman=='X'):
        return 10
    elif(roman=='XL'):
        return 40
    elif(roman=='L'):
        return 50
    elif(roman=='XC'):
        return 90
    elif(roman=='C'):
        return 100
    elif(roman=='CD'):
        return 400
    elif(roman=='D'):
        return 500
    elif(roman=='CM'):
        return 900
    elif(roman=='M'):
        return 1000
    else:
        return -1


def romanToDecimal(roman):
    answer = 0
    i = 0
    while i<len(roman):
        letter1 = roman[i]
        if(i+1<len(roman)):
            letter2 = roman[i+1]
            combined = letter1+letter2
            if(value(combined) != -1):
                answer+=value(combined)
                i+=2
            else:
                answer+=value(letter1)
                i+=1
        else:
            answer+=value(roman[i])
            i+=1
    return answer
    
roman = input().upper()
print(romanToDecimal(roman))