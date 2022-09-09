def main():

    infile = open('clients.txt', 'r')
    
    i = 1
    for line in infile:
        print(i, '. ', line.rstrip('\n'), sep='')
        i += 1

    infile.close

main()

