from fractions import Fraction
def make_score(s):
    score = Fraction()
    rotated_init = False
    for i in s:
        if i == 'S':
            if rotated_init:
                pass
            else:
                score +=1
        if i == 'R':
            if score == Fraction():
                rotated_init = not rotated_init               
            else:
                score = Fraction (-score.denominator, score.numerator)
    return score

def untangle(score):
    
    q = []
    q.append(['', score])
    
    if score == 0:
        return "untangled"
    
    while q:
        new_ele = q.pop(0)
        if new_ele[1] + 1 == Fraction():
            return new_ele[0]+'S'
        else:
            q.append([new_ele[0] + 'S', new_ele[1] + 1])
            q.append([new_ele[0] + 'R', Fraction( -new_ele[1].denominator, new_ele[1].numerator)])


#run this

untangle(make_score('SRSRRSSRSRSSRSSRRSSRSSSSSRSSRSSRSRSSRSSRSSSSSSSSRSSRSSSSSRSSRSSRRSSRSSSSSRSSRSSRSSSSSSSSSSSSSSSSSRSSRSSRS'))