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

## Present Value and Future Value of Multiple Cash Flows
#in present value
def multi_pv(pmt, r, n, fv, pv):
    pv_1 = 0
    n_1 = np.arange(1,n)
    for i in n_1:
        pv += pmt/(1+r)**i
    fv = fv/(1+r)**n
    pv = pv+fv+pv_1
    return pv

#in future value
def multi_fv(pmt, r, n, pv, fv):
    fv_1 = 0
    n_1 = np.arange(1,n)
    for i in n_1:
        fv_1 += pmt*(1+r)**i
    pv = pv*(1+r)**n
    fv = pv+fv+fv_1
    return fv

# Present Value of a Growing Annuity
def GApv(c, g, r):
    pv = c*(1-(1+g/1+r)**t)/(r-g)
    return pv


# Present Value of a Growing Perpetuity
def GPpv(c, g, r):
    pv = c/(r-g)
    return pv