

def generateList(num):
    divisors = []
    i = 1
    while( i < num):
        value = 0
        # print("i {}: ".format(i))
        sumlist = []
        n = (i*2) + 1
        for k in range(i, n ):
            value = (2 ** k)
            # print("values {}".format(value))
            sumlist.append(value)
        divisors.append(sumlist)
        print(isPerfect(sum(sumlist)))
        i += 1

def isPerfect(num):
    divisors = [1]
    limit = num + 1
    iter = 2
    print("perfect check: {}".format(num))
    while(iter < limit):
        if((num % iter) == 0):
            divisors.append(iter)
            limit = num / iter
            divisors.append(limit)
        iter += 1

    total = sum(divisors)
    #print("Sum:{}".format(sum))
    return (total == num)

input = int(input("Enter Number:\n"))
generateList(input)

