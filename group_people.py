import collections


def groupThePeople(groupSizes):
    ids = {}
    ans = []
    # put same w/ same groupSize into same bucket
    for id, size in enumerate(groupSizes):
        ids.setdefault(size, []).append(id)
    # seperate them into small groups based on size
    for k, v in ids.items():
        for i in range(0, len(v), k):
            ans.append(v[i:i+k])

    return ans


groupSizes = [3, 3, 3, 3, 3, 1, 3]
print(groupThePeople(groupSizes))
