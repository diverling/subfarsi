with open('JNS.srt') as jns:
    alllets = []
    for line in jns:
        for let in list(line):
            if let not in alllets:
                alllets.append(let)
    print(alllets)