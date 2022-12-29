def euclidian(a,b):
        if a == 0:
                return b
        elif b == 0:
                return a
        else:
                while a > 0 or b > 0:
                        if b == 0:
                                break
                        else:
                                r = a % b
                                a = b
                                b = r
                return a

print(euclidian(66528,52920))
