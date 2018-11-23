'''
Given a list of words and two words word1 and word2, return the shortest distance between these two words in the list.

word1 and word2 may be the same and they represent two individual words in the list.

Example:
Assume that words = ["practice", "makes", "perfect", "coding", "makes"].

Input: word1 = “makes”, word2 = “coding”
Output: 1
Input: word1 = "makes", word2 = "makes"
Output: 3
Note:
You may assume word1 and word2 are both in the list.
'''

class Solution:
    def shortestWordDistance(self, words, word1, word2):
        index1=set([i for i in range(len(words)) if words[i]==word1])
        index2=set([i for i in range(len(words)) if words[i]==word2])
        i=0
        ret_min=float('inf')
        return min([abs(x-y) for x in index1 for y in index2 if x!=y])
