class Solution:
    def minProcessingTime(self, processorTime: List[int], tasks: List[int]) -> int:
        tasks.sort(reverse=True)

        processorTime.sort()

        max_time = 0

        n = len(processorTime)

        for i in range(n):
            max_time = max(max_time, processorTime[i] + tasks[i*4])

        return max_time
