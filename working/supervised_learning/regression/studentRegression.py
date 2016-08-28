from sklearn import linear_model

def studentReg(ages_train, net_worths_train):
    reg = linear_model.LinearRegression()
    reg.fit (ages_train, net_worths_train)


    return reg
