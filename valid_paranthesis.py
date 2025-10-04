class Solution:
    def isValid(self, s: str) -> bool:
        h = {')' : '(', '}' : '{', ']' : '['}
        stk = [] # ( [ {
        # pts: paranthesis
        # ([  ])
        # h = { ) : (, ], [  }
        # stk1 = (
        # stk2 = ( [
        # popped1 = [ and it is in h
        # popped2 = ( and it is in h
        # stk is empty: not (FALSE) = TRUE
        for pts in s:
            if pts not in h: # it is an opening pts
                stk.append(pts)
            else:
                if not stk:
                    return False
                else:
                    popped = stk.pop()
                    if popped != h[pts]:
                        return False
        return not stk
