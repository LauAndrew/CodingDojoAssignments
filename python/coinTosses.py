import random

def toss(coin):
    coin_attempt = 1
    heads = 0
    tails = 0
    results = ""
    result_string_complete = ""

    for x in range(1, coin):
        new_toss = random.randint(0,1)
        if new_toss == 1:
            heads += 1
            results = "head"
            print "Attempt #", coin_attempt, ": Throwing a coin... It's a ", results, "! Got ", heads, "head(s) so far and", tails, "tail(s) so far"
        else:
            tails += 1
            results = "tails"
            print "Attempt #", coin_attempt, ": Throwing a coin... It's a ", results, "! Got ", heads, "head(s) so far and", tails, "tail(s) so far"
            coin_attempt += 1

toss(5001)
