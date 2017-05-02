import collections as c

class Node:
    def __init__(self):
        self.children = c.defaultdict(lambda: None)
        self.isWord = False

class Trie:

    def __init__(self):
        self.root = Node()

    def add(self, word):
        currentNode = self.root
        for index in range(len(word)):
            letter = word[index]
            if currentNode.children[letter] is None:
                currentNode.children[letter] = Node()

            currentNode = currentNode.children[letter]
            if index == len(word) - 1:
                currentNode.isWord = True

    def find(self, word):
        currentNode = self.root
        for index, letter in enumerate(word):
            if currentNode.children[letter] is None:
                return 0
            currentNode = currentNode.children[letter]

        #now to count the remaining words
        return self.count(currentNode, 0)

    def count(self, start, currentSum):
        if start.isWord:
            currentSum += 1
        for letter in start.children.keys():
            currentSum += self.count(start.children[letter], 0)
        return currentSum


# class Trie:
#     def __init__(self):
#         self.freqs = c.defaultdict(lambda: 0)

#     def add(self,word):
#         for index in range(len(word)):
#             key = word[:index+1]
#             self.freqs[key] += 1

#     def find(self,word):
#         return self.freqs[word]


myTrie = Trie()
myTrie.add("adam")
myTrie.add("adany")
print myTrie.find("adanyggf")


# myTrie = Trie()
# n = int(raw_input().strip())
# for a0 in xrange(n):
#     op, contact = raw_input().strip().split(' ')
#     if op == "add":
#         myTrie.add(contact)
#     if op == "find":
#         print myTrie.find(contact)
