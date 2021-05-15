 def  calcscore(bricks, majongg = false):
 
    for group in bricks:
        if group.len == 4:
            if isCong(group) != -1:
                #cong
        if group.len == 3:
            if isChao(group) != -1:
                #chao
            elif isPong(group) != -1:
                #pong
        elif group.len == 2:
            if majongg:
                if isPair(group) != -1:
                    #pair für mahjongg
            else:
                if group[0].typ == dragon:
                    #drachenpaar
        elif group.len == 1:
            if group[0].typ == season:
                #jahreszeit
                

 def isPong(group):

    if group[0].typ == group[1].typ && group[1].typ == group[2].typ:
        if group[0].typ == wind:
            return 8
        elif group[0].typ == dragon:
            return 8
        elif group[0].typ != season:
            if group[0].num == group[1].num && group[1].num == group[2].num:
                if group[0].num == 1 || group[0].num == 9:
                    return 8
                else
                    return 4
    
    return -1
    
    
 def isChao(group):

    if group[0].typ == group[1].typ && group[1].typ == group[2].typ:
        if group[0].typ != season && group[0].typ != wind && group[0].typ != dragon:
            if group[0].num == group[1].num - 1 && group[1].num == group[2].num - 1:
                return 0
    return -1
    
 def isCong(group):

    if group[0].typ == group[1].typ && group[1].typ == group[2].typ && group[2].typ == group[3].typ:
        if group[0].typ == wind:
            return 32
        elif group[0].typ == dragon:
            return 32
        elif group[0].typ != season:
            if group[0].num == group[1].num && group[1].num == group[2].num:
                if group[0].num == 1 || group[0].num == 9:
                    return 32
                else
                    return 16
    
    return -1
    
    
 def isPair(group):

    if group[0].typ == group[1].typ:
        if group[0].typ == wind:
            return 0
        elif group[0].typ == dragon:
            return 2
        elif group[0].typ != season:
            if group[0].num == group[1].num && group[1].num == group[2].num:
                if group[0].num == 1 || group[0].num == 9:
                    return 0
                else
                    return 0
    
    return -1
    
    
    
    