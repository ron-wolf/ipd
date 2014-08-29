int payoff  = [-3, -1, 1, 3]

int defect  = 0
int sucker  = 1
int coop = 2
int suckee  = 3

int ones = 0
int fours = 0

int choiceA
int choiceB

tit = 1

round = 0

def outcome(choiceA, choiceB)
    if(A == 0)
        if(B == 0)
            return [ payoff[defect], payoff[defect] ]
        if(B == 1)
            return [ payoff[suckee], payoff[sucker] ]
    if(A == 1)
        if(B == 0)
            return [ payoff[sucker], payoff[suckee] ]
        if(B == 0)
            return [ payoff[coop], payoff[coop] ]

def allC()
    return 1

def allD()
    return 0

def fiftyfifty()
    return choose(0, 1)

def titfortat(tit)
    int tat = tit
    return tat

def quaternary
    ones++
    if(ones == 4)
        ones = 0
        fours++
    if(ones + fours == 6)
        ones, fours = 0

def matchup(playerA, playerB)
    print(playerA + " vs. " + playerB + ": ", end = "")
    if(playerA == "allC")
       choiceA =   allC()
    if(playerA == "allD")
       choiceA =   allD()
    if(playerA == "fiftyfifty")
       choiceA =   fiftyfifty()
    if(playerB == "allC")
       choiceB =   allC()
    if(playerB == "allD")
       choiceB =   allD()
    if(playerB == "fiftyfifty")
       choiceB =   fiftyfifty()
    if(playerA == "titfortat")
        if(round == 0 || playerB == "allC" || playerB == "titfortat")
            return titfortat( 1 )
        if(round == 1 && playerB == "allD")
            return titfortat( allD() )