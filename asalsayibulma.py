def asalsayibulma(y):

    if y > 1:
        for i in range(2,y):
            if (y % i) == 0:
                return True
    else:
        return False

