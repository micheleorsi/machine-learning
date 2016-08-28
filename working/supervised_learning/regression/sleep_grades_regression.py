#
#
# Regression and Classification programming exercises
#
#


#
#	In this exercise we will be taking a small data set and computing a linear function
#	that fits it, by hand.
#

#	the data set

import numpy as np

sleep = [5,6,7,8,10]
scores = [65,51,75,75,86]

def compute_regression(sleep,scores):

    #	First, compute the average amount of each list
    print sleep
    print scores

    avg_sleep = reduce(lambda x, y: x + y, sleep) / (len(sleep)*1.0)
    print "avg_sleep: "+str(avg_sleep)
    avg_scores = reduce(lambda x, y: x + y, scores) / (len(scores)*1.0)
    print "avg_scores: "+str(avg_scores)

    #	Then normalize the lists by subtracting the mean value from each entry

    normalized_sleep = map(lambda x,y:x-y, sleep, [avg_sleep]*len(sleep))
    # print normalized_sleep

    normalized_scores = map(lambda x,y:x-y, scores, [avg_scores]*len(scores))
    # print normalized_scores

    #	Compute the slope of the line by taking the sum over each student
    #	of the product of their normalized sleep times their normalized test score.
    #	Then divide this by the sum of squares of the normalized sleep times.

    product_sleep_times_scores = map(lambda x,y:x*y, normalized_sleep, normalized_scores)
    # print product_sleep_times_scores

    sum_products = reduce(lambda x, y: x + y, product_sleep_times_scores)
    # print sum_products

    squares_sleep = map(lambda x: x*x, normalized_sleep)
    # print squares_sleep

    sum_squares_sleep = reduce(lambda x, y: x + y, squares_sleep)
    # print sum_squares_sleep

    slope = sum_products / (sum_squares_sleep*1.0)
    # print slope

    #	Finally, We have a linear function of the form
    #	y - avg_y = slope * ( x - avg_x )
    #	Rewrite this function in the form
    #	y = m * x + b
    #	Then return the values m, b

    m=slope
    b=avg_scores - (slope*avg_sleep)
    return m,b


if __name__=="__main__":
    m,b = compute_regression(sleep,scores)
    print "Your linear model is y={}*x+{}".format(m,b)
