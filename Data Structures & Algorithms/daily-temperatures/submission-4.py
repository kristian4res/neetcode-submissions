class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        result = [0] * n
        stack = []  # indices of days waiting for a warmer temperature

        for i, temperature in enumerate(temperatures):
            # Resolve previous days that are colder than today
            while stack and temperature > temperatures[stack[-1]]:
                previous_day = stack.pop()
                result[previous_day] = i - previous_day

            # Today still needs a warmer future day
            stack.append(i)

        return result