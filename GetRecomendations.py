import pearsonCorealation as PC
#this is a Dictionary of movie critics

critics={'Lisa Rose': {'Lady in the Water': 2.5, 'Snakes on a Plane': 3.5,
 'Just My Luck': 3.0, 'Superman Returns': 3.5, 'You, Me and Dupree': 2.5,
 'The Night Listener': 3.0},
'Gene Seymour': {'Lady in the Water': 3.0, 'Snakes on a Plane': 3.5,
 'Just My Luck': 1.5, 'Superman Returns': 5.0, 'The Night Listener': 3.0,
 'You, Me and Dupree': 3.5},
'Michael Phillips': {'Lady in the Water': 2.5, 'Snakes on a Plane': 3.0,
 'Superman Returns': 3.5, 'The Night Listener': 4.0},
'Claudia Puig': {'Snakes on a Plane': 3.5, 'Just My Luck': 3.0,
 'The Night Listener': 4.5, 'Superman Returns': 4.0,
 'You, Me and Dupree': 2.5},
'Mick LaSalle': {'Lady in the Water': 3.0, 'Snakes on a Plane': 4.0,
 'Just My Luck': 2.0, 'Superman Returns': 3.0, 'The Night Listener': 3.0,
 'You, Me and Dupree': 2.0},
'Jack Matthews': {'Lady in the Water': 3.0, 'Snakes on a Plane': 4.0,
 'The Night Listener': 3.0, 'Superman Returns': 5.0, 'You, Me and Dupree': 3.5},
'Toby': {'Snakes on a Plane':4.5,'You, Me and Dupree':1.0,'Superman Returns':4.0}}

def Reccomend(prefs,p1,similarity=PC.pearson):
    total={}
    simSum={}
    for other in prefs:
        #not comparing the same person to himself
        if other == p1:
            continue
        sim = similarity(prefs,p1,other)

        #scores below zero are ignored
        if sim<0:
            continue
        
        for item in prefs[other]:
            if item not in prefs[p1] or prefs[p1][item]==0:
                total.setdefault(item,0)
                total[item]=total[item]+prefs[other][item]*sim
                simSum.setdefault(item,0)
                simSum[item]= simSum[item]+sim

        ranking = [(total/simSum[item],item) for item,total in total.items()]

        ranking.sort()
        ranking.reverse()
        return ranking

