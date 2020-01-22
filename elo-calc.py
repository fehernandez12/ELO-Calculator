import math
import sys

k = 25
exit_var = False
export_string = ''

def main_func():
    global k
    name1 = input('Insert Player1\'s name: ')
    name2 = input('Insert Player2\'s name: ')
    rating1 = int(input('Insert player 1\'s rating: '))
    rating2 = int(input('Insert player 2\'s rating: '))
    ratings = [rating1, rating2]
    prob1 = 1/(1 + math.exp(-(rating1 - rating2) / ((k**2) / math.log(k/2))))
    prob2 = 1/(1 + math.exp(-(rating2 - rating1) / ((k**2) / math.log(k/2))))
    print('The win probability for player 1 is {}'.format(str(prob1)))
    print('The win probability for player 2 is {}'.format(str(prob2)))
    prev_k = k
    k = k_digester(k, rating1, rating2)

    probabilities = prob_calc(rating1, rating2, prev_k)

    scores = score_calc()
    scores = scores_digester(scores)

    ratings = rating_calc(probabilities, ratings, scores)
    ratings = ratings_digester(ratings)

    match_string = (name1 + ' vs. ' + name2 + ':\nScore: ' + str(scores[0]) + '-' + str(scores[1]) + 
        '\nNew rating for ' + name1 + ': ' + str(ratings[0]) + '\nNew rating for ' + name2 + ': ' + 
        str(ratings[1]) + '\n' + '------------------------------------------------------\n')

    string_append(match_string)

def prob_calc(rating1, rating2, prev_k):
    global k
    if rating1 > rating2:
        prob1 = 1/(1 + math.exp(-(rating1 - rating2) / ((k**2) / math.log(k/2))))
        prob2 = 1/(1 + math.exp(-(rating2 - rating1) / ((prev_k**2) / math.log(prev_k/2))))
    elif rating2 > rating1:
        prob1 = 1/(1 + math.exp(-(rating1 - rating2) / ((prev_k**2) / math.log(prev_k/2))))
        prob2 = 1/(1 + math.exp(-(rating2 - rating1) / ((k**2) / math.log(k/2))))
    else:
        prob1 = 1/(1 + math.exp(-(rating1 - rating2) / ((k**2) / math.log(k/2))))
        prob2 = 1/(1 + math.exp(-(rating2 - rating1) / ((k**2) / math.log(k/2))))
    return [prob1, prob2]

def k_digester(_k, rating1, rating2):
    global k
    if abs(rating1 - rating2) > 2000:
        k = 50
    elif abs(rating1 - rating2) > 1000:
        k += 25
    elif abs(rating1 - rating2) > 800:
        k += 20
    elif abs(rating1 - rating2) > 600:
        k += 15
    elif abs(rating1 - rating2) > 400:
        k += 10
    elif abs(rating1 - rating2) > 200:
        k += 5    
    else:
        continue
    return k

def string_append(string_to_append):
    global export_string
    export_string += string_to_append

def ratings_digester(ratings):
    for rating in ratings:
        rating = float("{0:.2f}".format(rating))
    return ratings

def scores_digester(scores):
    if scores[0] < scores[1] and scores[0] != 0:
        scores[0] = 1
        scores[1] = 2
    elif scores[0] == 0:
        scores[0] = 0
        scores[1] = 2
    elif scores[1] < scores[0] and scores[1] != 0:
        scores[0] = 2
        scores[1] = 1
    elif scores[1] == 0:
        scores[0] = 2
        scores[1] = 0
    else:
        scores[0] = 1
        scores[1] = 1
    return scores

def export():
    global export_string
    text_file = open('Ratings export.txt', 'w')
    text_file.write(export_string)
    text_file.close()
    print('Matches successfully exported to Ratings export.txt!')

def score_calc():
    score1 = int(input('Insert player 1\'s score in the match: '))
    score2 = int(input('Insert player 2\'s score in the match: '))
    score1 = (1 / (score1 + score2)) * score1
    score2 = (1 / (score1 + score2)) * score2
    scores = [score1, score2]
    return scores

def rating_calc(probabilities, ratings, scores):
    global k
    if len(probabilities) == 0:
        print('Error! You haven\'t calculated the probabilities!')
    else:
        new_rating1 = ratings[0] + k * (scores[0] - probabilities[0])
        new_rating2 = ratings[1] + k * (scores[1] - probabilities[1])
        print('Player 1\'s new rating is {}'.format(str(new_rating1)))
        print('Player 2\'s new rating is {}'.format(str(new_rating2)))

    return [new_rating1, new_rating2]

def menu():
    print('Select an option:')
    print('[C]alculate a new match')
    print('[E]xport calculated matches')
    print('E[x]it')
    option = input()
    option = option.upper()
    if option == 'C':
        main_func()
    elif option == 'E':
        export()
    elif option == 'X':
        sys.exit()
    else:
        print('Incorrect option.')

if __name__ == '__main__':
    while True:
        menu()
