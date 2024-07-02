import sys

# stack -> pilha - Last in, First out
# = pilha de pratos para lavar

# queueu -> fila First in, First out
# = fila de banco


class Solution:
    def __init__(self):
        self.stack = []
        self.queue = []

    # Push a character onto a stack - void
    def pushCharacter(self, stack):
        self.stack.append(stack)

    # Enqueue a character in queue variable - void
    def enqueueCharacter(self, queue):
        self.queue.append(queue)

    # Pops and returns char at top of stack variable - return char
    def popCharacter(self):
        stack = self.stack.pop(len(self.stack) - 1)
        return stack

    # Dequeue and return first char in queue variable - return char
    def dequeueCharacter(self):
        if self.queue is not None:
            queue = self.queue.pop(0)
            return queue


# Read the string s
s = input()

# Create the Solution class object
obj = Solution()

l = len(s)

# Push/enqueue all the characters of string s to stack
for i in range(l):
    obj.pushCharacter(s[i])
    obj.enqueueCharacter(s[i])

isPalindrome = True
'''
pop the top character from stack
dequeue the first character from queue
compare both the characters
'''
for i in range(l // 2):
    if obj.popCharacter() != obj.dequeueCharacter():
        isPalindrome = False
        break

# Finally print whether string s is palindrome or not.
if isPalindrome:
    print("The word, "+s+", is a palindrome.")
else:
    print("The word, "+s+", is not a palindrome.")
