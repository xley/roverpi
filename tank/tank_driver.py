#import Throttle
from . import throttle # OK when key_drive
#from throttle import Throttle # NG when key_drive
#from .throttle import Throttle # OK when key_drive

class TankDriver:
    # DualWheelPwmDriver dualWheel
    # Throttle leftThrottle
    # Throttle rightThrottle

    @property
    def powerText(self):
        return "{0}:{1}".format( self.leftThrottle.level, self.rightThrottle.level)
        
    @property
    def isFore(self):
        return (self.leftThrottle.level + self.rightThrottle.level) > 0

    @property
    def isBack(self):
        return (self.leftThrottle.level + self.rightThrottle.level) < 0


    @property
    def isLeft(self):
        return (self.leftThrottle.level < self.rightThrottle.level);

    @property
    def isRight(self):
        return (self.leftThrottle.level > self.rightThrottle.level)
    
    @property
    def throttleAverage(self):
        # need kiriage
        return int((self.leftThrottle.level + self.rightThrottle.level) / 2.0)

    '''
    def __init__( self, leftWheel, rightWheel ):
        self.leftWheel = leftWheel
        self.rightWheel = rightWheel
        self.leftThrottle = throttle.Throttle()
        self.rightThrottle = throttle.Throttle()
    '''

    def __init__( self, on_accel, on_brake ):
        #self.leftWheel = leftWheel
        #self.rightWheel = rightWheel
        self.leftThrottle = throttle.Throttle()
        self.rightThrottle = throttle.Throttle()
        self.on_accel = on_accel
        self.on_brake = on_brake
        

    def ApplyAccel(self, left_rate, right_rate):
        #self.leftWheel.Accel(left_rate)
        #self.rightWheel.Accel(right_rate)
        self.on_accel(left_rate, right_rate)

    def Brake(self):
        self.leftThrottle.Reset ()
        self.rightThrottle.Reset ()
        #self.leftWheel.Free()
        #self.rightWheel.Free()
        self.on_brake()

    def Fore(self):
        if (self.isBack) :
            self.Brake ()
            return
    
        self.leftThrottle.StepUp ()
        self.rightThrottle.StepUp ()
        self.ApplyAccel(self.leftThrottle.rate, self.rightThrottle.rate)
        


    def Back(self):
        if (self.isFore) :
            self.Brake ()
            return

        self.leftThrottle.StepDown ()
        self.rightThrottle.StepDown ()
        self.ApplyAccel(self.leftThrottle.rate, self.rightThrottle.rate)

    def TurnLeft(self):
        if (self.isRight) :
            self.leftThrottle.level = self.throttleAverage
            self.rightThrottle.level = self.throttleAverage
        else :
            self.leftThrottle.StepDown ();
            self.rightThrottle.StepUp ();

        self.ApplyAccel(self.leftThrottle.rate, self.rightThrottle.rate)

    def TurnRight(self):
        if (self.isLeft):
            self.leftThrottle.level = self.throttleAverage
            self.rightThrottle.level = self.throttleAverage
        else :
            self.leftThrottle.StepUp ()
            self.rightThrottle.StepDown ()

        self.ApplyAccel(self.leftThrottle.rate, self.rightThrottle.rate)

    def __Log(self):
        left = self.leftThrottle.level
        right = self.rightThrottle.level

        print ("{0} / {1}", left.ToString (), right.ToString ());

if __name__ == "__main__":
    print('test')

