def areFollowingPatterns(strings, patterns):
    wordPattern = {}
    commandPattern = {}
    checkOrderArray = []
    avaibleWordsString = []
    for word in strings:
        if word not in wordPattern:
             avaibleWordsString.append(word);
             wordPattern[word] = 1;
        else:
            wordPattern[word] += 1;
    iterateCheck = 0        
    for command in patterns:
        
        
        if command not in commandPattern:  
                # checkOrderArray.append(avaibleWordsString[iterateCheck])
                commandPattern[command] = 1;
                # iterateCheck += 1;
                # if iterateCheck > len(wordPattern):
                #     print(iterateCheck, len(wordPattern))  
                #     print("returned false")
                #     return(False);
                 
        else:
            # checkOrderArray.append(avaibleWordsString[iterateCheck])
            commandPattern[command] += 1;
      
        

    if len(wordPattern) != len(commandPattern):
        print(checkOrderArray)
        print(iterateCheck, len(wordPattern))  
        return(False);
    else:
        comparison = {}
        for s, p in zip(strings, patterns):
            if s in comparison and comparison[s] != p:
                return False
            comparison[s] = p
        # return len(d) == len(set(d.values()))
        
        print(checkOrderArray)
        print(iterateCheck, len(wordPattern))  
        return(True);
    
