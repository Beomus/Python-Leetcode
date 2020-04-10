def prefix(arr):
    ref = arr[0]
    res = [""]
    for i in range(len(ref)):
        common = ref[0:i+1]
        for j in range(1, len(arr)):
            if common in arr[j] and common not in res:
                res.append(common)
            elif common not in arr[j]:
                return res[-1]
        
    return res[-1]


print(prefix(["grace", "graceful", "disgraceful", "gracefully"]))
print(prefix(['flower', 'flow', "flight"]))
print(prefix(["cat", "meow", "nyan"]))
    