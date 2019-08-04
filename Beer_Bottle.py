for i in range(99, 0, -1):
    if i == 1:
        print("{} bottle of beer on the wall,take one down, pass it around, "
              "{} bottle of beer on the wall".format(i, i - 1))
    elif i == 2:
        print("{} bottle of beer on the wall,take one down, pass it around, "
              "{} bottle of beer on the wall".format(i, i - 1))
    elif i == 0:
        print("{} bottle of beer on the wall,".format(i))
    else:
        print("{} bottles of beer on the wall,take one down, pass it around, "
              "{} bottles of beer on the wall".format(i, i - 1))
