# @before-stub-for-debug-begin
# @before-stub-for-debug-end

#
# @lc app=leetcode id=488 lang=python3
#
# [488] Zuma Game
#

# @lc code=start


class Solution:
    def findMinStep(self, board: str, hand: str) -> int:
        def remove_consecutives(index, s):
            if index < 0:
                return s

            left = right = index

            while left > 0 and s[left-1] == s[index]:
                left -= 1

            while right < len(s) - 1 and s[index] == s[right+1]:
                right += 1

            length = right - left + 1
            if length >= 3:
                new_s = s[:left] + s[right + 1:]
                return remove_consecutives(left-1, new_s)
            else:
                return s

        def bfs(start):
            board, hand, step = start
            queue = [start]
            visited = set([(board, hand)])

            for x in queue:
                curr_board, curr_hand, step = x

                for i in range(len(curr_board)):
                    for j in range(len(curr_hand)):

                        new_board = remove_consecutives(i, curr_board[:i] + curr_hand[j] + curr_board[i:])
                        new_hand = curr_hand[:j] + curr_hand[j+1:]
                        if not new_board:
                            return step + 1
                        if (new_board, new_hand) not in visited:
                            queue.append([new_board, new_hand, step+1])
                            visited.add((new_board, new_hand))
        hand = "".join(sorted(hand))
        val = bfs([board, hand, 0])
        return val if val is not None else -1

# @lc code=end
