'''

Vikas Bhat
Word Search
Type: 2d Array/List
Time Complexity: O(n^2)
Space Complexity: O(1)

'''


class main:

    def exist(self,board,word):

        m=len(board)
        n=len(board[0])

        def check_path(x,y,index):

            if index==len(word):
                return True

            elif x<0 or x>=m or y<0 or y>=n or board[x][y]!=word[index]:
                return False

            temp=board[x][y]
            board[x][y]="#"
            res=check_path(x+1,y,index+1) or check_path(x-1,y,index+1) or check_path(x,y-1,index+1) or check_path(x,y+1,index+1)
            board[x][y]=temp
            return res




        for i in range(m):
            for j in range(n):
                if board[i][j]==word[0]:
                    if(check_path(i,j,0)):
                        return True

        return False




if __name__=="__main__":
    v=main()
    print(v.exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]],"ABCCED"))
    print(v.exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]],"SEE"))
    print(v.exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "ABCD"))

