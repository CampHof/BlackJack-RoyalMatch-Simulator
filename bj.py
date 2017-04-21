#import card deck library
import pydealer

#initialize deck
deck = pydealer.Deck()

#shuffle deck
deck.shuffle()

#deal a hand
hand = deck.deal(2)

f = open("results.txt", "w")

#def card value extractor
#will return a specific card's (cardNumber)
#rank or suit (value) given the hand
def getCardValues(hand, value, cardNumber):
    cardNumber -= 1
    if value == "suit":
        suit = hand[cardNumber]
        suit = str(suit).split(" ")
        return(suit[2])
    elif value == "rank":
        rank = hand[cardNumber]
        rank = str(rank).split(" ")
        return(rank[0])
    else:
        card = hand[cardNumber]
        return(card)

#determine if hand is a Match, Royal Match, or neither
def findMatch():
    if getCardValues(hand, "suit", 1) == getCardValues(hand, "suit", 2):
        if getCardValues(hand, "rank", 1) == "King" and getCardValues(hand, "rank", 2) == "Queen":
            status = "RMATCH"
            return(status)
        elif getCardValues(hand, "rank", 2) == "King" and getCardValues(hand, "rank", 1) == "Queen":
            status = "RMATCH"
            return(status)
        else:
            status = "MATCH"
            return(status)
    else:
        status = "UNMATCH"
        return(status)

#Config trials
handCount = 1
trials = 1000
mCount = 0
rCount = 0
uCount = 0
bank = 0

#loop through number of trials tallying instances of M, R, or U
while handCount <= trials:
    if findMatch() == "MATCH":
        status = "M"
        mCount += 1
        bank += 3
    elif findMatch() == "RMATCH":
        status = "R"
        rCount += 1
        bank += 10
    else:
        status = "U"
        uCount += 1
        bank -= 1
    roi = float(bank) / float(trials)
    trialResult = (str(handCount) + "|" + status + "|" + str(roi) + "|" + str(rCount) + " R, " + str(mCount) + " M, " + str(uCount) + " U" + "|" + str(hand[0]) + " & " + str(hand[1]))
    f.write(trialResult)
    f.write("\n")

    #increase handCount, replace cards, shuffle, redeal hand
    handCount += 1
    deck += hand
    deck.shuffle()
    hand = deck.deal(2)