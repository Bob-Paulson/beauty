
string = input()
count = 1

if len(string) == 1:
    print(string+str(1))

else:
    for i in range(len(string) - 1):
        if string[i] == string[i+1]:                             # if current symbol eq next symbol
            count += 1
        elif i == len(string) - 1 or string[i] != string[i+1]:   # if current symbol last or current symbol!=next symbol
                print(string[i]+str(count), end='')
                count = 1

    print(string[i+1]+str(count), end='')                        # output last symbol + count





