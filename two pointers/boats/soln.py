class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
    # numBoats: 1
    # limit 5
    # [3,5,3,4]
    # [3 3 4 5]
    # []
    #. l r
      boats = 0
      people = sorted(people)
      l, r = 0, len(people) - 1
      while(r >= 0 and people[r] == limit):
          boats += 1
          r -= 1
      
      while(l <= r):
          totalWeight = people[l] + people[r]
          if (totalWeight > limit):
              boats += 1
              r -= 1
          else:
              boats += 1
              l += 1
              r -= 1
      return boats
