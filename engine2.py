import math
import random
import time
import Engine


NUM_RIGID_BODIES = 1


class boxShape:
    def __init__(self, width, height, mass):
        self.width = width
        self.height = height
        self.mass = mass
        self.momentOfInertia  = self.computeMomentOfInertia()

    def computeMomentOfInertia(self):
        m = self.mass
        w = self.width
        h = self.height
        return (m * (w**2 + h**2)) / 12
        
class rigidBody():
    def __init__(self, position, linearVelocity, angularVelocity, angle, shape):
        self.position = position
        self.linearVelocity = linearVelocity
        self.angularVelocity = angularVelocity
        self.angle = angle
        self.force = Engine.Vector2(0, 0)
        self.torque = 0
        self.shape = shape
    
        
rigidBodies = [
    rigidBody(
        Engine.Vector2(random.uniform(0, 50), random.uniform(0, 50)),
        Engine.Vector2(0, 0),
        0, 
        random.uniform(0, 360) * (math.pi/180),
        boxShape(random.uniform(1, 3), random.uniform(1, 3), 10)       
    ) for _ in range(NUM_RIGID_BODIES)
] 

def printRigidBodies():
    for i, rigidBody in enumerate(rigidBodies):
        print(f"body[{i}] p = ({rigidBody.position.x:.2f}, {rigidBody.position.y:.2f}), a = {rigidBody.angle:.2f}")
        
def InitializeRigidBodies():
    for rigidBody in rigidBodies:
        rigidBody.position = Engine.Vector2(random.uniform(0, 50), random.uniform(0, 50))
        rigidBody.linearVelocity = Engine.Vector2(0, 0)
        rigidBody.angularVelocity = 0
        rigidBody.angle = random.uniform(0,360) * math.pi/180
        rigidBody.shape = boxShape(random.uniform(1, 3), random.uniform(1, 3), 10)
        
def computeForceAndTorque(rigidBody):
    f = Engine.Vector2(random.uniform(0, 100), random.uniform(0, 100))
    rigidBody.force = f
    r = Engine.Vector2(rigidBody.shape.height/2, rigidBody.shape.width /2)
    torque = r.x * f.y - r.y * f.x
    rigidBody.torque = torque

def runRigidBodySimulation():
    totalSimulationTime = 10
    currentTime = 0
    dt = 1
    
    InitializeRigidBodies()
    printRigidBodies()
    
    while(currentTime <= totalSimulationTime):
        time.sleep(dt)
        
        for rigidBody in rigidBodies:
            computeForceAndTorque(rigidBody)
            linearAcceleration = Engine.Vector2(rigidBody.force.x / rigidBody.shape.mass, rigidBody.force.y / rigidBody.shape.mass )
            rigidBody.linearVelocity.x += linearAcceleration.x * dt
            rigidBody.linearVelocity.y += linearAcceleration.y * dt
            rigidBody.position.x += rigidBody.linearVelocity.x * dt
            rigidBody.position.y += rigidBody.linearVelocity.y * dt       
            angularAcceleration = rigidBody.torque / rigidBody.shape.momentOfInertia
            rigidBody.angularVelocity = angularAcceleration * dt
            rigidBody.angle += rigidBody.angularVelocity * dt
            
        printRigidBodies()
        currentTime += dt

if __name__ == "__main__":
    print("Running Rigid Body Simulation")        
    runRigidBodySimulation()