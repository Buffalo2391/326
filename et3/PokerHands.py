''' Cosc326 Levi Faid 3894507 Python 3.6.2 '''

from sys import stdin
import re

ranks = ('2','3','4','5','6','7','8','9','10','J','Q','K','A')
suits = ('C','D','H','S')
AllCards = []
DeckInPlay = []
for rank in ranks:
    for suit in suits:
        AllCards.append("%s%s" % (rank, suit))
        DeckInPlay.append("%s%s" % (rank, suit))
        DeckInPlay.append("%s%s" % (rank, suit))
def Hcard(hand):
    return AllCards.index(hand[4]) 
    
def THcard(hand):
    return AllCards.index(hand[3])
def Ccard(hand):
    return AllCards.index(hand[2])


def Dcard(hand):
    for i in range(len(hand)):
        REstring = "%s[CDHS] %s[CDHS]" % (hand[i][:len(hand[i])-1], hand[i][:len(hand[i])-1])
        if re.search(REstring, " ".join(hand), flags=0):
            return AllCards.index(hand[i])
            

def PrintPowerRankings(AllHands):
    remainingHands = sorted(list(AllHands), key=Hcard)
    rankNo = 1
    rankings = []
    #Royal Flush
    for suit in ['C', 'D', 'H', 'S']:
        for hand in AllHands:            
            if hand[0]==('10%s'%(suit)):
                if hand[1]==('J%s'%(suit)):
                    if hand[2]==('Q%s'%(suit)):
                        if hand[3]==('K%s'%(suit)):
                            if hand[4]==('A%s'%(suit)):
                                rankings.append("#%d %s Royal Flush"%(rankNo, " ".join(hand)))
                                rankNo+=1
                                remainingHands.remove(hand)
    #Straight Flush
    Aranks = ('A','2','3','4','5','6','7','8','9','10','J','Q','K','A')                            
    cardStorage = []
    for suit in ['C', 'D', 'H', 'S']:
        for hand in reversed(remainingHands):
            i = Aranks.index(hand[0][:len(hand[0])-1])
            if i<len(Aranks)-4:
                ACEstring = "2{0} 3{0} 4{0} 5{0} A{0}".format(suit)
                REstring = "{1}{0} {2}{0} {3}{0} {4}{0} {5}{0}".format(suit, Aranks[i], Aranks[i+1], Aranks[i+2], Aranks[i+3],Aranks[i+4])
                if re.search(REstring, " ".join(hand), flags=0) or re.search(ACEstring, " ".join(hand), flags=0):
                   cardStorage.append(hand)
    for hand in reversed(cardStorage):
        rankings.append("#%d %s Straight Flush"%(rankNo, " ".join(hand)))
        rankNo += 1
        remainingHands.remove(hand)
        
    #4 of a kind
    cardStorage = []
    for hand in reversed(remainingHands):
        x = hand[3][:len(hand[0])-1]
        REstring = "%s[CDHS] %s[CDHS] %s[CDHS] %s[CDHS]" % (x, x, x, x)
        if re.search(REstring, " ".join(hand), flags=0):
           cardStorage.append(hand)
    cardStorage = sorted(cardStorage, key=Ccard)
    for hand in reversed(cardStorage):
        rankings.append("#%d %s Four of a Kind with %s's"%(rankNo, " ".join(hand), hand[3][:len(hand[0])-1]))
        rankNo += 1
        remainingHands.remove(hand)
    
    #Full House
    for hand in reversed(remainingHands):
        REstring = "%s[CDHS] %s[CDHS] %s[CDHS]" % (hand[4][:len(hand[0])-1], hand[4][:len(hand[0])-1], hand[4][:len(hand[0])-1])
        WEstring = "%s[CDHS] %s[CDHS]" % (hand[0][:len(hand[0])-1], hand[0][:len(hand[0])-1])
        if re.search(REstring, " ".join(hand), flags=0) and re.search(WEstring, " ".join(hand), flags=0):
            cardStorage.append(hand)
        REstring = "%s[CDHS] %s[CDHS] %s[CDHS]" % (hand[0][:len(hand[0])-1], hand[0][:len(hand[0])-1], hand[4][:len(hand[0])-1])
        WEstring = "%s[CDHS] %s[CDHS]" % (hand[4][:len(hand[0])-1], hand[4][:len(hand[0])-1])
        if re.search(REstring, " ".join(hand), flags=0) and re.search(WEstring, " ".join(hand), flags=0):
            cardStorage.append(hand)
    cardStorage = sorted(cardStorage, key=Ccard)

    for hand in reversed(cardStorage):
        if hand in remainingHands:
            remainingHands.remove(hand)
            rankings.append("#%d %s Full House"%(rankNo, " ".join(hand)))
            rankNo += 1

    #Flush
    cardStorage = []
    for hand in reversed(remainingHands):
        for suit in ['C', 'D', 'H', 'S']:
            REstring = "(([1-9ATJQK]|1[0-3])%s ){4}([1-9ATJQK]|1[0-3])%s" % (suit, suit)
            if re.search(REstring, " ".join(hand), flags=0):
                rankings.append("#%d %s Flush"%(rankNo, " ".join(hand)))
                rankNo += 1
                cardStorage.append(hand)
    for hand in cardStorage:
        remainingHands.remove(hand)
 
    #Straight
    cardStorage = []
    for hand in reversed(remainingHands):
        i = Aranks.index(hand[0][:len(hand[0])-1])
        ACEstring = "2{0} 3{0} 4{0} 5{0} A{0}".format("[CDHS]")
        if i<len(Aranks)-4:
            REstring = "{1}{0} {2}{0} {3}{0} {4}{0} {5}{0}".format("[CDHS]", Aranks[i], Aranks[i+1], Aranks[i+2], Aranks[i+3],Aranks[i+4])
            if re.search(REstring, " ".join(hand), flags=0):
               cardStorage.append(hand)   
    for hand in reversed(cardStorage):
        rankings.append("#%d %s Straight"%(rankNo, " ".join(hand)))
        rankNo += 1
        remainingHands.remove(hand)

    #Three of a Kind
    cardStorage = []
    for hand in reversed(remainingHands):
        x = hand[2][:len(hand[0])-1]
        REstring = "%s[CDHS] %s[CDHS] %s[CDHS]" % (x, x, x)
        
        if re.search(REstring, " ".join(hand), flags=0):
           cardStorage.append(hand)
    cardStorage = sorted(cardStorage, key=Ccard)
    for hand in reversed(cardStorage):
        rankings.append("#%d %s Three of a Kind with %s's "%(rankNo, " ".join(hand), hand[2][:len(hand[0])-1]))
        rankNo += 1
        remainingHands.remove(hand)




    #Two Pair
    cardStorage = []
    for hand in reversed(remainingHands):
        REstring = "%s[CDHS] %s[CDHS]" % (hand[3][:len(hand[3])-1], hand[3][:len(hand[3])-1])
        WEstring = "%s[CDHS] %s[CDHS]" % (hand[1][:len(hand[1])-1], hand[1][:len(hand[1])-1])
        if re.search(REstring, " ".join(hand), flags=0) and re.search(WEstring, " ".join(hand), flags=0):
            cardStorage.append(hand)
    cardStorage = sorted(cardStorage, key=THcard)
    for hand in reversed(cardStorage):
        rankings.append("#%d %s Two Pair"%(rankNo, " ".join(hand)))
        rankNo += 1
        remainingHands.remove(hand)



    #Pair
    cardStorage = []
    for hand in reversed(remainingHands):
        for i in range(len(hand)):
            REstring = "%s[CDHS] %s[CDHS]" % (hand[i][:len(hand[i])-1], hand[i][:len(hand[i])-1])
            if re.search(REstring, " ".join(hand), flags=0):
                if not hand in cardStorage:
                    cardStorage.append(hand)
    cardStorage = sorted(cardStorage, key=Dcard)
    for hand in reversed(cardStorage):
        value = AllCards[Dcard(hand)]
        rankings.append("#%d %s Pair of %s's"%(rankNo, " ".join(hand), value[:len(value)-1]))
        rankNo += 1
        remainingHands.remove(hand)
    
    #High Card       
    for hand in reversed(remainingHands):
        rankings.append("#%d %s High card"%(rankNo, " ".join(hand)))
        rankNo+=1
    for hand in rankings:
        print(hand)

#This function checks a hand, if it is valid it prints it and returns false if not it returns true
def IsHandCheck(hand):
    for item in (' ','-','/'):
        exp = '(([1-9ATJQK]|1[0-3])[CDHS][%s]){4}([1-9ATJQK]|1[0-3])[CDHS]' % (item)
        if re.fullmatch(exp, hand, flags=0):
            hand = re.sub('T','10',hand)
            hand = re.sub('11','J',hand)
            hand = re.sub('12','Q',hand)
            hand = re.sub('13','K',hand)
            hand = re.sub('1([CDHS])', 'A\\1',hand)
            cards = re.split(item, hand, flags=0)
            for card in cards:
                if card in DeckInPlay:
                    DeckInPlay.remove(card)
                else:
                    print("SOMEONE'S CHEATING")
                    return None
            if len(cards)==len(set(cards)):
                cards = sorted(cards,key=AllCards.index)            
                return cards
    return None



#take in the input and check each line 
lines = stdin.readlines()
allHands = []
for line in lines:
    hands = IsHandCheck(line.upper().rstrip('\n'))
    if hands is None:
         print('Invalid: %s' % (line.rstrip('\n')))
    else:
        allHands.append(hands)
if len(allHands)>0:
    PrintPowerRankings(allHands)




