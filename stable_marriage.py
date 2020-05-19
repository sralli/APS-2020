def StableMarriage(Proposers, Proposed):
    Matched = ()

    Unmatched = list(Proposers.keys())
    Unmatchedcopy = Unmatched

    Matched = dict(zip(Unmatched, [0]*len(Proposers)))

    while(len(Unmatchedcopy)>0):
        for u in Unmatchedcopy:
            partner = Proposers[u][Matched[u]]

            if partner in Matched:
                if Proposed[partner].index(u) < Proposed[partner].index(Matched[partner]):
                    Unmatched.append(Matched(partner))
                    Unmatched.remove(u)
                    Matched[partner] = U

            else:
                Matched[partner] = u
                Unmatched.remove(u)

            
            #Updating:

            Matched[u] = Matched[u]+1
            Unmatchedcopy = Unmatched
    return Matched


mens = []
women = []
men_dic = {}
women_dic = {}
free_men = [i for i in range(1,num+1)]
free_women = [i for i in range(1,num+1)]

for i in range(num):
    mens.append(list(map(int, input().split(' '))))
for i in range(num):
    women.append(list(map(int, input().split(' '))))
    
for i in range(num):
    men_dic[free_men[i]] = mens[i]
    
for i in range(num):
    women_dic[free_women[i]] = women[i]

