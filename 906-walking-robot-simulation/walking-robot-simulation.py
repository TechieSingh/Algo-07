class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:

        current = [0, 0]
        directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]  
        direction_index = 0  
        result = 0

        obstacle_set = set(map(tuple, obstacles))

        for command in commands:
            if command == -1:  
                direction_index = (direction_index + 1) % 4
            elif command == -2:  
                direction_index = (direction_index - 1) % 4
            else:
                for _ in range(command):
                    # Calculate next position
                    next_pos = [current[0] + directions[direction_index][0], current[1] + directions[direction_index][1]]
                    if tuple(next_pos) not in obstacle_set:  # Check if next position is an obstacle
                        current = next_pos  # Update current position
                        result = max(result, current[0] ** 2 + current[1] ** 2)  # Update result with max distance squared

        return result
