class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        sor_pos = sorted(enumerate(position), reverse=True, key=lambda x:x[1])
        stack = [(target - sor_pos[0][1]) / speed[sor_pos[0][0]]]
        del sor_pos[0]

        for pos in sor_pos:
            time = (target - pos[1]) / speed[pos[0]]
            if time > stack[-1]:
                stack.append(time)
        
        return len(stack)