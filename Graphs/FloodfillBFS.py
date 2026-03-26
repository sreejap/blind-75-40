from collections import deque # this has to be lower case collections
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        if not image:
            return image # null case

        start_color = image [sr][sc]
        if start_color == color:
            return image 

        queue = deque ([(sr,sc)])

        rows = len (image)
        cols = len (image[0])
        dirs = [(0,1),(1,0),(-1,0),(0,-1)]
        while len(queue) > 0:
            level = len(queue)

            for _ in range (level):
                cell = queue.popleft()
                cell_x, cell_y = cell # exapnd the tuple
                image [cell_x] [cell_y] = color
                for d in dirs:
                    neighbor_x = cell_x + d[0]
                    neighbor_y = cell_y + d[1]

                    if neighbor_x >=0 and neighbor_x < rows and neighbor_y >=0 and neighbor_y < cols and image [neighbor_x][neighbor_y] == start_color:
                        image [neighbor_x][neighbor_y] = color
                        queue.append ((neighbor_x,neighbor_y))
        return image
