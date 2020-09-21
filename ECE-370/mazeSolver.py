from robot_control_class import RobotControl

rc = RobotControl()

class mazeSolver:
    def distRead(self):                 #check distance to walls
        return [rc.get_laser(0),rc.get_laser(360),rc.get_laser(719)]

    def mazeMove(self):
        foo = float('inf')
        print("Moving Forwards")
        #self.aligner()
        while True:
            dm = rc.get_laser(360)      #check distance to next wall
            if dm < 0.9:
                rc.stop_robot()
                self.mazeTurn()         #turning when close to wall
            elif dm == foo:
                self.finTest()          #test for exiting the maze if exit is found
            else:
                rc.move_straight()
            print("Distance = %0.2f m" % dm)

    def mazeTurn(self):
        self.aligner()
        l = self.distRead()
        if l[0] < l[2]:                 #if the right side is blocked then turn left
            print("Turning Left")
            rc.rotate(90)
            self.finTest()              #testing to see if exit found after each turn
        else:                           #if the right side is open then turn right
            print("Turning Right")
            rc.rotate(-90)
            self.finTest()              #testing to see if exit found after each turn

    def aligner(self):                  #aligning the bot to face the wall straight-on
        da = rc.get_laser_full()
        di = da[240:480]
        i = di.index(min(di))
        i = (i-120)/4                   #making laser(0)=-90degrees and laser(719)=90degrees
        print("Rotating", i,"degrees to align")
        rc.rotate(i)

    def startSolver(self):
        self.mazeMove()
    
    def finTest(self):
        foo = float('inf')
        while True:
            l=self.distRead()
            if l[1] == foo:             #if the bot sees the end of the maze
                print("Exit Found")
                while True:
                    df = [rc.get_laser(0),rc.get_laser(719)]
                    if (df[0] != foo) and (df[1] != foo):
                        rc.move_straight()
                    else:               #if the bot has exited the maze
                        rc.stop_robot()
                        print("Maze Solved")
            else:
                self.mazeMove()


rc.stop_robot()
mBot = mazeSolver()
mBot.startSolver()
