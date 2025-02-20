# https://www.hellointerview.com/learn/code/intervals/insert-interval

# 

def insertIntervals(intervals, newInterval):
  merged = []
  i = 0
  n = len(intervals)

  while i < n and intervals[i][1] < newInterval[0]:
    merged.append(intervals[i])
    i += 1

  while i < n and intervals[i][0] <= newInterval[1]:
    newInterval[0] = min(intervals[i][0], newInterval[0])
    newInterval[1] = max(intervals[i][1], newInterval[1])
    i += 1

  merged.append(newInterval)
  for j in range(i, n):
    merged.append(intervals[j])

  return merged
