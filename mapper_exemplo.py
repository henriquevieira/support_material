def mapper():
    reader = csv.reader(sys.stdin, delimiter='\t')
    writer = csv.writer(sys.stdout, delimiter='\t', quotechar='"', quoting=csv.QUOTE_ALL)

    for line in reader:

        one, two, three, four, five, six = line
        c = [pos for pos, char in enumerate(five) if char == '!' or char == '?' or char == '.']
        if(len(c) > 1):
            continue
        
        if(c):
            if( len(five)-1 != c[0]):
                continue
        
        writer.writerow(line)
