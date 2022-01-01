# @before-stub-for-debug-begin
# @before-stub-for-debug-end

#
# @lc app=leetcode id=126 lang=python3
#
# [126] Word Ladder II
#

# @lc code=start

class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        def diff(word1, word2):
            if len(word1) == len(word2):
                count = 0
                for i in range(len(word1)):
                    if not word1[i] == word2[i]:
                        count += 1
                        if count > 1:
                            return False
                return count == 1
            else:
                return False

        wordList.insert(0, beginWord)
        n = len(wordList)
        visited = [False for _ in range(n)]
        res = []

        def dfs(index, visited, n, path):
            path.append(wordList[index])
            visited[index] = True
            for i in range(n):
                if not visited[i]:
                    if diff(wordList[index], wordList[i]):
                        dfs(i, visited[:], n, path[:])

            if wordList[index] == endWord:
                res.append(path)

        dfs(0, visited, n, [])
        return res

        # @lc code=end
