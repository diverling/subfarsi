import re
with open('JNS.srt') as jns, open('all_lets', 'w') as alts, open('keeplets') as klts:
    count = 0
    keeplets = []
    uwords = []
    for let in klts:
        keeplets.append(let[0])
    #print(keeplets)
    for line in jns:
        wordlist = re.split(" ", line)
        #print(wordlist)
        for word in wordlist:
            cleanword = []
            letlist = list(word)
            for let in letlist:
                if let in keeplets:
                    cleanword.append(let)
            clnwrd = "".join(cleanword)
            if clnwrd not in uwords:
                uwords.append(clnwrd)
                count += 1
                print(clnwrd)
    print(count)
