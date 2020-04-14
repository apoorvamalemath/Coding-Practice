def next(ptr):
    if ptr is None:
        return None
    else:
        return ptr.next
    
def ahit(d, key):
    if key is None:
        return 0
    elif key in d:
        return 1
    else:
        d[key] = 1
        return 0
    
def findMergeNode(headA, headB):
    result = None
    d = {}
    while True:
        if headA is None and headB is None:
            break
        if ahit(d, headA):
            result = headA.data
            break
        if ahit(d, headB):
            result = headB.data
            break
        else:
            headA = next(headA)
            headB = next(headB)
  
    return result
