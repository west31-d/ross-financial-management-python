#Future value calculator
def fv(pv, r, n):
    fv = pv*(1+r) ** n
    return fv

#Present value calculator
def pv(fv, r, n):
    pv = fv/((1+r)**n)
    return pv

#Determining the Discount Rate
def r(pv, fv, t):
    r = (fv/pv) ** (1/t) - 1
    return r

#Finding the Number of Periods
def t(pv, fv, r):
    t = np.log(fv/pv) / np.log(1+r)
    return t
