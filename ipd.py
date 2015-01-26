# payoffs
sucker = -3
defect = -1
coop = 1
suckee  = 3

# quaternary() setup
ones = 0
fours = 0

# <WIP>
# all previous outcomes and results
history = []

# first-level nested lists
outcomes = 0
payoffs = 1

# second-level nested lists (payoffs)
allC = 0
allD = 1
fiftyfifty = 2
titfortat = 3
# </WIP>

round = 1

def outcome(choiceA, choiceB): # the definition of prisoner's dilemma
    if A == 0:
        if B == 0:
            return [defect, defect]
        if B == 1:
            return [suckee, sucker]
    if A == 1:
        if B == 0:
            return [sucker, suckee]
        if B == 0:
            return [coop, coop]

def allC(): # all cooperate
    return 1

def allD(): # all defect
    return 0

def fiftyfifty(): # random with p = 0.5
    return choose(0, 1)

def titfortat(): # cooperates the first round and returns what the opponent played the previous round every round after
    if round == 1:
        return 1
    elif playerA == "titfortat":
        return history[outcomes][titfortat][len(titfortat-1)][1] # WIP
    else:
        return history[outcomes][titfortat][len(titfortat-1)][0] # WIP

# <WIP>
def quaternary(): # chooses matchups
    ones++
    if ones == 4):
        ones = 0
        fours++
    if ones + fours == 6:
        ones, fours = 0
# </WIP>