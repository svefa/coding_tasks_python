# """
# This is the robot's control interface.
# You should not implement it, or speculate about its implementation
# """
#class Robot:
#    def move(self):
#        """
#        Returns true if the cell in front is open and robot moves into the cell.
#        Returns false if the cell in front is blocked and robot stays in the current cell.
#        :rtype bool
#        """
#
#    def turnLeft(self):
#        """
#        Robot will stay in the same cell after calling turnLeft/turnRight.
#        Each turn will be 90 degrees.
#        :rtype void
#        """
#
#    def turnRight(self):
#        """
#        Robot will stay in the same cell after calling turnLeft/turnRight.
#        Each turn will be 90 degrees.
#        :rtype void
#        """
#
#    def clean(self):
#        """
#        Clean the current cell.
#        :rtype void
#        """

class Solution:
    def cleanRoom(self, robot):
        i,j=0,0
        seen = set()
        def bt(i,j, seen):
            robot.clean()
            seen.add((i,j))

            if (i, j + 1) not in seen:
                #j = j+1
                if robot.move():
                    bt(i, j+1,seen)
                    robot.turnLeft()
                    robot.turnLeft()
                    robot.move()
                    robot.turnLeft()
                    robot.turnLeft()
                #j = j-1
            if (i, j - 1) not in seen:
                #j = j-1
                robot.turnLeft()
                robot.turnLeft()
                if robot.move():
                    robot.turnLeft()
                    robot.turnLeft()
                    bt(i, j-1,seen)
                    robot.move()
                else:
                    robot.turnLeft()
                    robot.turnLeft()
                    
                #j = j+1
            if (i+ 1, j ) not in seen:
                #i = i+1
                robot.turnRight()
                if robot.move():
                    robot.turnLeft()
                    bt(i+1, j,seen)
                    robot.turnLeft()
                    robot.move()
                    robot.turnRight()
                else:
                    robot.turnLeft()
                #i = i-1
            if (i- 1, j ) not in seen:
                #i = i-1
                robot.turnLeft()
                if robot.move():
                    robot.turnRight()
                    bt(i-1, j,seen)
                    robot.turnRight()
                    robot.move()
                    robot.turnLeft()
                else:
                    robot.turnRight()
                #i = i+1
        bt(0,0, seen)
        print(seen)
            
            
         