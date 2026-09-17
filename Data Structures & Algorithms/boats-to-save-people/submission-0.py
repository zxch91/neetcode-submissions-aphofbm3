class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:

        people.sort()

        lightest = 0
        heaviest = len(people) - 1
        boats = 0

        while lightest <= heaviest:
            if people[lightest] + people[heaviest] <= limit:
                lightest += 1

            heaviest -= 1
            boats += 1

        return boats
            
        