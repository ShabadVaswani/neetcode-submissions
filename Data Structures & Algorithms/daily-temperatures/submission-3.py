class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        temperatures = temperatures[::-1]
        st = []
        sol = []
        for i, n in enumerate(temperatures):
            while len(st)>0 and n >= st[-1][0]:
                st.pop()

            if len(st) == 0:
                sol.append(0)
            else:
                sol.append(i-st[-1][1])
            st.append((n,i))

        return sol[::-1]