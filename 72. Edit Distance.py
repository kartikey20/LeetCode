def solve(word1, word2):
    delete_var = [0]
    insert_var = [0]
    replace_var = [0]

    def dfs(word1, word2, delete, replace, insert):
        if word1 and word2:
            if word1[0] == word2[0]:
                dfs(word1[1:], word2[1:], delete, replace, insert)
            else:
                dfs(word1[1:], word2, delete + 1, insert, replace)  # delete
                dfs(word1, word2[1:], delete, insert + 1, replace)  # insert
                dfs(word1[1:], word2[1:], delete,
                    insert, replace + 1)  # replace
        delete_var[0] = delete
        insert_var[0] = insert
        replace_var[0] = replace
    dfs(word1, word2, 0, 0, 0)
    print(delete_var[0], insert_var[0], replace_var[0])


print(solve("horse", "ros"))
