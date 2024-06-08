

def portfolio_cost(name):
    fp = open("../{}".format(name), 'r')

    alt = fp.readlines()
    sum = 0

    for n in alt:
        n = n.split()
        try:
            sum += int(n[1]) * float(n[2])
        except ValueError as e:
            print("Couldn't parse: ", n)
            print("Reason: ", e)
    
    return sum

if __name__ == '__main__':
    print(portfolio_cost('Data/portfolio.dat'))