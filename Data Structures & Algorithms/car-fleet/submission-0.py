class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        pair = [[p,s] for p,s in zip(position, speed)]
        time = []
        for i in sorted(pair)[::-1]:
            t = (target - i[0])/i[1]
            time.append(t)
        stack = []
        stack.append(time[0])
        print(time)
        for t in time:
            fl = stack[-1]
            print(t,fl)
            if t <= fl:
                continue
            stack.append(t)
        return len(stack)