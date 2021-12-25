# @before-stub-for-debug-begin
# @before-stub-for-debug-end

#
# @lc app=leetcode id=126 lang=python3
#
# [126] Word Ladder II
#

# @lc code=start
from typing import Sequence, Tuple


class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        def diff(word1, word2):
            count = 0
            for i in range(len(word1)):
                if not word1[i] == word2[i]:
                    count += 1
            if count == 1:
                return True
            return False

        wordList.insert(0, beginWord)
        sequences = []
        visited = [False for _ in range(len(wordList))]

        def dfs(word, index, path, visited):
            visited[index] = True
            path.append(word)
            for i in range(len(wordList)):
                if not visited[i] and diff(word, wordList[i]):
                    dfs(wordList[i], i, path[:], visited[:])
            if word == endWord:
                sequences.append(path)
        dfs(beginWord, 0,  [], visited)
        return sequences


# @lc code=end
