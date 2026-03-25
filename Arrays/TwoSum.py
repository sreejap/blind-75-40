def two_sum(arr: list[int], target: int) -> list[int]:
    mapping = {}
    for i in range(len(arr)):
        rem = target - arr[i]
        if rem in mapping: # key exists
            pair = mapping[rem] # get the index
            return [pair,i]
        else:
           mapping[arr[i]] = i  # 2 -0
    
    return []
