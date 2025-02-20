# https://www.hellointerview.com/learn/code/sliding-window/maximum-points-you-can-obtain-from-cards

# key: The key to this problem is recognizing that each valid arrangement of cards we can choose is 
# equivalent to removing n - k cards from the middle of the array, where n is the length of the array.

def maxScore(cards, k):
    total = sum(cards)
    if k >= len(cards):
        return total

    state = 0
    max_points = 0
    start = 0

    for end in range(len(cards)):
        state += cards[end]
    
    if end - start + 1 == len(cards) - k:
        max_points = max(total - state, max_points)
        state -= cards[start]
        start += 1
  
    return max_points
