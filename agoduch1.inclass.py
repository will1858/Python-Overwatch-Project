import json
import requests
import time
with open('items.json', 'r') as fd:
    storage=json.load(fd)
url="https://ow-api.com/v1/stats/pc/us/"
#bt = "Mezie#1897" #test only
url_2="/complete"

c=input("Enter (1) to examine stats for a specific battletag, (2) for a list of known battletags, (3) to examine stats for all known battletags, or nothing to stop: ").lower()
print()
while c != '':

    if c in "123":
        if c == "1":
            bt = input("Enter BattleTag: ")   #UNDO WHEN DONE TESTING
            if bt in storage:
                response=storage[bt]
            else:
                bt=bt.replace("#","-")
                response = requests.get(url+bt+url_2).json()
                #print(response)
                bt=bt.replace("-","#")
                while "error"  in response:
                    print("ERROR : Player not found")
                    bt = input("Enter BattleTag: ")        #UNDO WHEN DONE TESTING
                    bt=bt.replace("#","-")
                    response = requests.get(url+bt+url_2).json()
                    #print(response)
                    bt=bt.replace("-","#")
            mode= input("Select [c]ompetitive, [q]uickplay, or [r]eturn: ").lower()
            print()
            while mode != "r":
                if mode in "cq":
                    if mode =="c":
                        comp_stat=input("Select [g]ame stats, [a]verage stats, [h]ero specific stats, or [r]eturn: ").lower()
                        print()
                        while comp_stat != "r":
                            if comp_stat in "gahr":
                                if comp_stat == "g":
                                    game_data_g = response['competitiveStats']['careerStats']['allHeroes']['game']
                                    for x in game_data_g:
                                        print(x.upper()," : ",game_data_g[x])
                                if comp_stat == "a":
                                    game_data_a = response['competitiveStats']['careerStats']['allHeroes']['average']
                                    for x in game_data_a:
                                        print(x," : ",game_data_a[x])
                                if comp_stat == "h":
                                    hero = int(input('''
Select a hero:
[1]. Ana
[2]. Ashe
[3]. Brigitte
[4]. D.Va
[5]. Doomfist
[6]. Genji
[7]. Hanzo
[8]. Junkrat
[9]. Lucio
[10]. McCree
[11]. Mei
[12]. Mercy
[13]. Moira
[14]. Orisa
[15]. Pharah
[16]. Reaper
[17]. Reinhardt
[18]. Roadhog
[19]. Solidier:76
[20]. Sombra
[21]. Symmetra
[22]. Torbjorn
[23]. Tracer
[24]. Widowmaker
[25]. Winston
[26]. Wrecking Ball
[27]. Zarya
[28]. Zenyatta
    
'''))
                                    if 1<=hero<=28:
                                        hero_data = response['competitiveStats']['topHeroes']
                                        hero_lis=list(hero_data.keys())
                                        print(hero_lis[hero-1].upper())
                                        for x in hero_data[hero_lis[hero-1]]:
                                            print(x.upper()," : ",hero_data[hero_lis[hero-1]][x])

                            print()
                            comp_stat=input("Select [g]ame stats, [a]verage stats, [h]ero specific stats, or [r]eturn: ").lower()
                            print()
                        mode= input("Select [c]ompetitive, [q]uickplay, or [r]eturn: ").lower()
                        print()
                else:
                     mode= input("Select [c]ompetitive, [q]uickplay, or [r]eturn: ").lower()
                if mode =="q":
                    comp_stat=input("Select [g]ame stats, [a]verage stats, [h]ero specific stats, or [r]eturn: ").lower()
                    print()
                    while comp_stat != "r":
                        if comp_stat in "gahr":
                            if comp_stat == "g":
                                game_data_g = response['quickPlayStats']['careerStats']['allHeroes']['game']
                                for x in game_data_g:
                                    print(x.upper()," : ",game_data_g[x])
                            if comp_stat == "a":
                                game_data_a = response['quickPlayStats']['careerStats']['allHeroes']['average']
                                for x in game_data_a:
                                    print(x," : ",game_data_a[x])
                            if comp_stat == "h":
                                hero = int(input('''
Select a hero:
[1]. Ana
[2]. Ashe
[3]. Brigitte
[4]. D.Va
[5]. Doomfist
[6]. Genji
[7]. Hanzo
[8]. Junkrat
[9]. Lucio
[10]. McCree
[11]. Mei
[12]. Mercy
[13]. Moira
[14]. Orisa
[15]. Pharah
[16]. Reaper
[17]. Reinhardt
[18]. Roadhog
[19]. Solidier:76
[20]. Sombra
[21]. Symmetra
[22]. Torbjorn
[23]. Tracer
[24]. Widowmaker
[25]. Winston
[26]. Wrecking Ball
[27]. Zarya
[28]. Zenyatta

'''))
                                if 1<=hero<=28:
                                    hero_data = response['quickPlayStats']['topHeroes']
                                    hero_lis=list(hero_data.keys())
                                    print(hero_lis[hero-1].upper())
                                    for x in hero_data[hero_lis[hero-1]]:
                                        print(x.upper()," : ",hero_data[hero_lis[hero-1]][x])
                        else:
                            comp_stat=input("Select [g]ame stats, [a]verage stats, [h]ero specific stats, or [r]eturn: ").lower()
                        print()
                        comp_stat=input("Select [g]ame stats, [a]verage stats, [h]ero specific stats, or [r]eturn: ").lower()
                        print()
                    mode= input("Select [c]ompetitive, [q]uickplay, or [r]eturn: ").lower()
                    print()
            with open('items.json', 'r') as fd:
                storage=json.load(fd)
            open("items.json", "w").close()
            storage[bt] = response
            with open("items.json", mode='r+', encoding='utf-8') as fp:
                if len(fp.read()) == 0:
                    fp.write(json.dumps(storage))
                else:
                    fp.write(',\n' + json.dumps(storage))

            c=input("Enter (1) to examine stats for a specific battletag, (2) for a list of known battletags, (3) to examine stats for all known battletags, or nothing to stop: ").lower()
            print()
        if c =="2":
            with open('items.json', 'r') as fd:
                data = json.load(fd)
                names = list(data.keys())
                for x in names:
                    print(x)

            print()
            c=input("Enter (1) to examine stats for a specific battletag, (2) for a list of known battletags, (3) to examine stats for all known battletags, or nothing to stop: ").lower()
            print()
        if c == "3":
            mode= input("Select [c]ompetitive, [q]uickplay, or [r]eturn: ").lower()
            print()

            while mode != "r":
                if mode in "cq":
                    if mode =="c":
                        statdict={}
                        stat = input('''Select a statistic to examine.  One of: 
[1]eliminations, [2]damage, [3]deaths, [4]finalblows, [5]healing, 
[6]objectivekills, [7]objectivetime, [8]solokills, [9]games_played, [10]games_won , [r]eturn

''').lower()
                        with open('items.json', 'r') as fd:
                            data = json.load(fd)
                            names = list(data.keys())
                            num = str(len(names))
                        display = int(input("How many of " + num +" to display [1 - "+num+"]?"))
                        print()
                        while stat != "r":
                            if stat == "1":
                                for x in names:
                                    val = storage[x]['competitiveStats']['careerStats']['allHeroes']['combat']['eliminations']
                                    if len(statdict)!=display:
                                        statdict[val]=x
                                sortedict=dict(sorted(statdict.items(), reverse=True))
                                for x in sortedict:
                                    print(sortedict[x]+" .... "+str(x))
                                statdict={}
                            if stat == "2":
                                for x in names:
                                    val = storage[x]['competitiveStats']['careerStats']['allHeroes']['combat']['damageDone']
                                    if len(statdict)!=display:
                                        statdict[val]=x
                                sortedict=dict(sorted(statdict.items(), reverse=True))
                                for x in sortedict:
                                    print(sortedict[x]+" .... "+str(x))
                                statdict={}
                            if stat =="3":
                                for x in names:
                                    val = storage[x]['competitiveStats']['careerStats']['allHeroes']['combat']['deaths']
                                    if len(statdict)!=display:
                                        statdict[val]=x
                                sortedict=dict(sorted(statdict.items(), reverse=True))
                                for x in sortedict:
                                    print(sortedict[x]+" .... "+str(x))
                                statdict={}
                            if stat =="4":
                                for x in names:
                                    val = storage[x]['competitiveStats']['careerStats']['allHeroes']['combat']['finalBlows']
                                    if len(statdict)!=display:
                                        statdict[val]=x
                                sortedict=dict(sorted(statdict.items(), reverse=True))
                                for x in sortedict:
                                    print(sortedict[x]+" .... "+str(x))
                                statdict={}
                            if stat =="5":
                                for x in names:
                                    val = storage[x]['competitiveStats']['careerStats']['allHeroes']['best']['healingDoneMostInGame']
                                    if len(statdict)!=display:
                                        statdict[val]=x
                                sortedict=dict(sorted(statdict.items(), reverse=True))
                                for x in sortedict:
                                    print(sortedict[x]+" .... "+str(x))
                                statdict={}
                            if stat =="6":
                                for x in names:
                                    val = storage[x]['competitiveStats']['careerStats']['allHeroes']['combat']['objectiveKills']
                                    if len(statdict)!=display:
                                        statdict[val]=x
                                sortedict=dict(sorted(statdict.items(), reverse=True))
                                for x in sortedict:
                                    print(sortedict[x]+" .... "+str(x))
                                statdict={}
                            if stat =="7":
                                for x in names:
                                    val = storage[x]['competitiveStats']['careerStats']['allHeroes']['combat']['objectiveTime']
                                    if len(statdict)!=display:
                                        statdict[val]=x
                                sortedict=dict(sorted(statdict.items(), reverse=True))
                                for x in sortedict:
                                    print(sortedict[x]+" .... "+str(x))
                                statdict={}
                            if stat =="8":
                                for x in names:
                                    val = storage[x]['competitiveStats']['careerStats']['allHeroes']['combat']['soloKills']
                                    if len(statdict)!=display:
                                        statdict[val]=x
                                sortedict=dict(sorted(statdict.items(), reverse=True))
                                for x in sortedict:
                                    print(sortedict[x]+" .... "+str(x))
                                statdict={}
                            if stat =="9":
                                for x in names:
                                    val = storage[x]['competitiveStats']['careerStats']['allHeroes']['game']['gamesPlayed']
                                    if len(statdict)!=display:
                                        statdict[val]=x
                                sortedict=dict(sorted(statdict.items(), reverse=True))
                                for x in sortedict:
                                    print(sortedict[x]+" .... "+str(x))
                                statdict={}
                            if stat =="10":
                                for x in names:
                                    val = storage[x]['competitiveStats']['careerStats']['allHeroes']['game']['gamesWon']
                                    if len(statdict)!=display:
                                        statdict[val]=x
                                sortedict=dict(sorted(statdict.items(), reverse=True))
                                for x in sortedict:
                                    print(sortedict[x]+" .... "+str(x))
                                statdict={}
                            print()
                            stat = input('''Select a statistic to examine.  One of:
[1]eliminations, [2]damage, [3]deaths, [4]finalblows, [5]healing,
[6]objectivekills, [7]objectivetime, [8]solokills, [9]games_played, [10]games_won , [r]eturn

''').lower()
                        mode= input("Select [c]ompetitive, [q]uickplay, or [r]eturn: ").lower()
                        print()
                    if mode == "q":
                        statdict={}
                        stat = input('''Select a statistic to examine.  One of: 
[1]eliminations, [2]damage, [3]deaths, [4]finalblows, [5]healing, 
[6]objectivekills, [7]objectivetime, [8]solokills, [9]games_played, [10]games_won , [r]eturn

''').lower()
                        with open('items.json', 'r') as fd:
                            data = json.load(fd)
                            names = list(data.keys())
                            num = str(len(names))
                        display = int(input("How many of " + num +" to display [1 - "+num+"]?"))
                        print()
                        while stat != "r":
                            if stat == "1":
                                for x in names:
                                    val = storage[x]['quickPlayStats']['careerStats']['allHeroes']['combat']['eliminations']
                                    if len(statdict)!=display:
                                        statdict[val]=x
                                sortedict=dict(sorted(statdict.items(), reverse=True))
                                for x in sortedict:
                                    print(sortedict[x]+" .... "+str(x))
                                statdict={}
                            if stat == "2":
                                for x in names:
                                    val = storage[x]['quickPlayStats']['careerStats']['allHeroes']['combat']['damageDone']
                                    if len(statdict)!=display:
                                        statdict[val]=x
                                sortedict=dict(sorted(statdict.items(), reverse=True))
                                for x in sortedict:
                                    print(sortedict[x]+" .... "+str(x))
                                statdict={}
                            if stat =="3":
                                for x in names:
                                    val = storage[x]['quickPlayStats']['careerStats']['allHeroes']['combat']['deaths']
                                    if len(statdict)!=display:
                                        statdict[val]=x
                                sortedict=dict(sorted(statdict.items(), reverse=True))
                                for x in sortedict:
                                    print(sortedict[x]+" .... "+str(x))
                                statdict={}
                            if stat =="4":
                                for x in names:
                                    val = storage[x]['quickPlayStats']['careerStats']['allHeroes']['combat']['finalBlows']
                                    if len(statdict)!=display:
                                        statdict[val]=x
                                sortedict=dict(sorted(statdict.items(), reverse=True))
                                for x in sortedict:
                                    print(sortedict[x]+" .... "+str(x))
                                statdict={}
                            if stat =="5":
                                for x in names:
                                    val = storage[x]['quickPlayStats']['careerStats']['allHeroes']['best']['healingDoneMostInGame']
                                    if len(statdict)!=display:
                                        statdict[val]=x
                                sortedict=dict(sorted(statdict.items(), reverse=True))
                                for x in sortedict:
                                    print(sortedict[x]+" .... "+str(x))
                                statdict={}
                            if stat =="6":
                                for x in names:
                                    val = storage[x]['quickPlayStats']['careerStats']['allHeroes']['combat']['objectiveKills']
                                    if len(statdict)!=display:
                                        statdict[val]=x
                                sortedict=dict(sorted(statdict.items(), reverse=True))
                                for x in sortedict:
                                    print(sortedict[x]+" .... "+str(x))
                                statdict={}
                            if stat =="7":
                                for x in names:
                                    val = storage[x]['quickPlayStats']['careerStats']['allHeroes']['combat']['objectiveTime']
                                    if len(statdict)!=display:
                                        statdict[val]=x
                                sortedict=dict(sorted(statdict.items(), reverse=True))
                                for x in sortedict:
                                    print(sortedict[x]+" .... "+str(x))
                                statdict={}
                            if stat =="8":
                                for x in names:
                                    val = storage[x]['quickPlayStats']['careerStats']['allHeroes']['combat']['soloKills']
                                    if len(statdict)!=display:
                                        statdict[val]=x
                                sortedict=dict(sorted(statdict.items(), reverse=True))
                                for x in sortedict:
                                    print(sortedict[x]+" .... "+str(x))
                                statdict={}
                            if stat =="9":
                                for x in names:
                                    val = storage[x]['quickPlayStats']['careerStats']['allHeroes']['game']['gamesPlayed']
                                    if len(statdict)!=display:
                                        statdict[val]=x
                                sortedict=dict(sorted(statdict.items(), reverse=True))
                                for x in sortedict:
                                    print(sortedict[x]+" .... "+str(x))
                                statdict={}
                            if stat =="10":
                                for x in names:
                                    val = storage[x]['quickPlayStats']['careerStats']['allHeroes']['game']['gamesWon']
                                    if len(statdict)!=display:
                                        statdict[val]=x
                                sortedict=dict(sorted(statdict.items(), reverse=True))
                                for x in sortedict:
                                    print(sortedict[x]+" .... "+str(x))
                                statdict={}
                            print()
                            stat = input('''Select a statistic to examine.  One of: 
[1]eliminations, [2]damage, [3]deaths, [4]finalblows, [5]healing, 
[6]objectivekills, [7]objectivetime, [8]solokills, [9]games_played, [10]games_won , [r]eturn

''').lower()
                        mode= input("Select [c]ompetitive, [q]uickplay, or [r]eturn: ").lower()
                        print()
            c=input("Enter (1) to examine stats for a specific battletag, (2) for a list of known battletags, (3) to examine stats for all known battletags, or nothing to stop: ").lower()
            print()
