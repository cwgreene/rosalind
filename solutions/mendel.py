def prob_dominant(k, m, n):
    total = float(k+m+n)
    return (k*(k-1)+
            2*k*m+
            2*m*n*.5+
            2*k*n+
            m*(m-1)*.75) / (total*(total-1))
print prob_dominant(19,24,30)
