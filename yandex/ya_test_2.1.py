def checkTree(root) -> bool:
    return True if int(root[0]) == int(root[1]) + int(root[2]) else False


print(checkTree([10, 4, 6]))

