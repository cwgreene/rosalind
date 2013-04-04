from rosalind import readfile, numbers

def prob_children(AA, Aa, aa, BB, Bb, bb):
    return [AA*.50+Aa*.25,
            AA*.50+Aa*.50+aa*.50,
            aa*.50+Aa*.25,
            BB*.50+Bb*.25,
            BB*.50+Bb*.50+bb*.50,
            bb*.50+Bb*.25]
def prob_gen_k(probs, k):
    if k == 0:
        return probs
    return prob_gen_k(prob_children(*probs), k-1)

def prob_child_balanced(probs):
    return probs[1]*probs[-2]

def fac(n):
    p = 1
    for i in range(1,n+1):
        p*=i
    return p

def choose(n, k):
    return fac(n)/(fac(k)*fac(n-k))

def prob_k_children_balanced(probs, k, total):
    prob = prob_child_balanced(probs)
    p = 0
    for i in range(k, total+1): 
        p += (choose(total, i))*prob**i*(1-prob)**(total-i)
    return p

k, n = numbers(readfile()[0])
print prob_k_children_balanced(prob_gen_k([0,1,0,0,1,0], 1), n, 2**k)
