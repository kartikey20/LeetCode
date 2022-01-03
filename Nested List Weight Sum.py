def depthSum(nestedList):
    s = [0]

    def dfs(nestedList, level):
        for elem in nestedList:
            if elem.isInterger():
                s[0] += level * elem.getInterger()
            else:
                s[0] += dfs(elem.getList(), level+1)

    dfs(nestedList, 1)


# if type([1, 1]) == list:
#     print('working')
