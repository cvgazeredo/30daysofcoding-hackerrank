from typing import List

# https://leetcode.com/problems/boats-to-save-people/description/


class Solution:

    def numRescueBoats(self, people: List[int], limit: int) -> int:

        print(people)

        boats = []
        num_boats = 0

        # Remove person with same limit boat weight or heigher
        for i in range(len(people)):
            print(people[i])
            if people[i] >= limit:
                num_boats = + 1
                boats.append([people[i]])
                people.pop(i)

        # Re arrange list in order to be acendent
        people.sort(reverse=True)
        print(people)

        # Combine pairs with max weight with min weight.
        for j in people:
            for k in people:
                # While person1 + person2 grater than limit
                if people[j] + people[j + k] > limit and k <= len(people):
                    # Increment index
                    k + 1

                    # Check again
                    if people[j] + people[k] <= limit:
                        num_boats = + 1
                        boats.append([people[j], people[k]])
                        people.pop(j)
                        people.pop(k)

                    elif people[j] + people[k] > limit:
                        num_boats = + 1
                        boats.append([people[j]])
                        people.pop(j)
                    else:
                        pass


people = list(map(int, input().split()))
limit = int(input())
s = Solution()
s.numRescueBoats(people, limit)
