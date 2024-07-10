from direct.showbase.ShowBase import ShowBase
from panda3d.core import *
from direct.task import Task

class Universe(ShowBase):

    def __init__(self, loader:Loader, modelPath:str, parentNode:NodePath, nodeName:str, texPath:str, posVec:Vec3, scaleVec:float):

        self.modelNode = loader.loadModel(modelPath)
        self.modelNode.reparentTo(parentNode)
        self.modelNode.setPos(posVec)
        self.modelNode.setScale(scaleVec)

        self.modelNode.setName(nodeName)
        tex = loader.loadTexture(texPath)
        self.modelNode.setTexture(tex,1)

class Planet(ShowBase):

    def __init__(self, loader:Loader, modelPath:str, parentNode:NodePath, nodeName:str, texPath:str, posVec:Vec3, scaleVec:float):

        self.modelNode = loader.loadModel(modelPath)
        self.modelNode.reparentTo(parentNode)
        self.modelNode.setPos(posVec)
        self.modelNode.setScale(scaleVec)

        self.modelNode.setName(nodeName)
        tex = loader.loadTexture(texPath)
        self.modelNode.setTexture(tex,1)

class Dumbledore(ShowBase):

    def __init__(self, loader:Loader, modelPath:str, parentNode:NodePath, nodeName:str, texPath:str, posVec:Vec3, scaleVec:float):

        self.modelNode = loader.loadModel(modelPath)
        self.modelNode.reparentTo(parentNode)
        self.modelNode.setPos(posVec)
        self.modelNode.setScale(scaleVec)

        self.modelNode.setName(nodeName)
        tex = loader.loadTexture(texPath)
        self.modelNode.setTexture(tex,1)

        self.SetKeyBindings()
        
    def Thrust(self, keyDown):

        if keyDown:
            base.taskMgr.add(self.ApplyThrust, 'forward-thrust')
            
        else:
            base.taskMgr.remove('forward-thrust')

    def ApplyThrust(self, task):

        rate = 5
        trajectory = base.render.getRelativeVector(self.modelNode, Vec3.forward())
        trajectory.normalize()

        self.modelNode.setFluidPos(self.modelNode.getPos() + trajectory * rate)

        return Task.cont

    def LeftTurn(self, keyDown):

        if keyDown:
            base.taskMgr.add(self.ApplyLeftTurn, 'left-turn')

        else:
            base.taskMgr.remove('left-turn')

    def ApplyLeftTurn(self, task):

        rate = -0.5
        self.modelNode.setH(self.modelNode.getH() + rate)
        return Task.cont
    
    def RightTurn(self, keyDown):

        if keyDown:
            base.taskMgr.add(self.ApplyRightTurn, 'right-turn')

        else:
            base.taskMgr.remove('right-turn')

    def ApplyRightTurn(self, task):

        rate = 0.5
        self.modelNode.setH(self.modelNode.getH() + rate)
        return Task.cont
    
    def Climb(self, keyDown):

        if keyDown:
            base.taskMgr.add(self.ApplyClimb, 'climb')

        else:
            base.taskMgr.remove('climb')

    def ApplyClimb(self, task):

        rate = 0.5
        self.modelNode.setP(self.modelNode.getP() + rate)
        return Task.cont
    
    def Dive(self, keyDown):

        if keyDown:
            base.taskMgr.add(self.ApplyDive, 'dive')

        else:
            base.taskMgr.remove('dive')
    
    def ApplyDive(self, task):

        rate = -0.5
        self.modelNode.setP(self.modelNode.getP() + rate)
        return Task.cont
    
    def LeftRoll(self, keyDown):

        if keyDown:
            base.taskMgr.add(self.ApplyLeftRoll, 'left-roll')

        else:
            base.taskMgr.remove('left-roll')

    def ApplyLeftRoll(self, task):

        rate = -0.5
        self.modelNode.setR(self.modelNode.getR() + rate)
        return Task.cont
    
    def RightRoll(self, keyDown):

        if keyDown:
            base.taskMgr.add(self.ApplyRightRoll, 'right-roll')

        else:
            base.taskMgr.remove('right-roll')

    def ApplyRightRoll(self, task):

        rate = 0.5
        self.modelNode.setR(self.modelNode.getR() + rate)
        return Task.cont
           
    def SetKeyBindings(self):

        self.accept("space", self.Thrust, [1])
        self.accept("space-up", self.Thrust, [0])
        self.accept("d", self.LeftTurn, [1])
        self.accept("d-up", self.LeftTurn, [0])
        self.accept("a", self.RightTurn, [1])
        self.accept("a-up", self.RightTurn, [0])
        self.accept("w", self.Climb, [1])
        self.accept("w-up", self.Climb, [0])
        self.accept("s", self.Dive, [1])
        self.accept("s-up", self.Dive, [0])
        self.accept("q", self.LeftRoll, [1])
        self.accept("q-up", self.LeftRoll, [0])
        self.accept("e", self.RightRoll, [1])
        self.accept("e-up", self.RightRoll, [0])


class SpaceStation(ShowBase):

    def __init__(self, loader:Loader, modelPath:str, parentNode:NodePath, nodeName:str, texPath:str, posVec:Vec3, scaleVec:float):

        self.modelNode = loader.loadModel(modelPath)
        self.modelNode.reparentTo(parentNode)
        self.modelNode.setPos(posVec)
        self.modelNode.setScale(scaleVec)

        self.modelNode.setName(nodeName)
        tex = loader.loadTexture(texPath)
        self.modelNode.setTexture(tex,1)

class Drone(ShowBase):

    def __init__(self, loader:Loader, modelPath:str, parentNode:NodePath, nodeName:str, texPath:str, posVec:Vec3, scaleVec:float):

        self.modelNode = loader.loadModel(modelPath)
        self.modelNode.reparentTo(parentNode)
        self.modelNode.setPos(posVec)
        self.modelNode.setScale(scaleVec)

        self.modelNode.setName(nodeName)
        tex = loader.loadTexture(texPath)
        self.modelNode.setTexture(tex,1)

    droneCount = 0
