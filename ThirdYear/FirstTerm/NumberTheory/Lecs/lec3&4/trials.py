
# the compact version of the ecludies algo is here
# this is fast because the remainder of a % b is always < a/2 so we remove half of the result
# each iteration so we can get the results very fast so the
# complexity here is O(lg(2)(a) + lg(2)(b))
def recersiveEcludieAlgo(a, b):
    if(b <= 0):
        return a

    return recersiveEcludieAlgo(b, a % b)


print(recersiveEcludieAlgo(28, 14))
