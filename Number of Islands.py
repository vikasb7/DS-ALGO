'''

Vikas Bhat
Number of Islands
Type: Graph
Time Complexity: O(n)
Space Complexity: O(1)

'''

class main:

    def numIslands(self,grid):

        m = len(grid)
        n = len(grid[0])
        self.ans = 0

        def isIsland(x, y):

            if (x >= m or y >= n or x < 0 or y < 0 or grid[x][y] == "0"):
                return 0

            grid[x][y] = '0'
            isIsland(x + 1, y)
            isIsland(x - 1, y)
            isIsland(x, y + 1)
            isIsland(x, y - 1)

            return 1

        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    self.ans += isIsland(i, j)

        return self.ans



if __name__=="__main__":

    v=main()
    print(v.numIslands([
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]))
    print(v.numIslands([
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]))