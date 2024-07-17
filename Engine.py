import random
import time

NUM_PARTICLES = 1

class Vector2():
    def __init__(self, x, y):
        self.x = x 
        self.y = y
        
class Particle():
    def __init__(self, position, velocity, mass):
        self.position = position
        self.velocity = velocity
        self.mass = mass
        
particles = [None] * NUM_PARTICLES

def PrintParticles():
    for i in range(NUM_PARTICLES):
        particle = particles[i]
        print(f"particle[{i}] ({particle.position.x:.2f}, {particle.position.y:.2f})")
        
def initializeParticles():
    for i in range(NUM_PARTICLES):
        particles[i] = Particle(Vector2(random.uniform(0, 50), random.uniform(0, 50)), Vector2(0,0), 1)
        
def ComputeForce(particle):
    return Vector2(0, particle.mass * -9.81)

def run_simulation():
    totalSimulationTime = 10
    currentTime = 0
    dt = 1
    
    initializeParticles()
    PrintParticles()
    
    while currentTime < totalSimulationTime:
        time.sleep(dt)
        
        
        for i in range(NUM_PARTICLES):
            particle = particles[i]
            force = ComputeForce(particle)
            acceleration = Vector2(force.x / particle.mass, force.y/particle.mass)
            particle.velocity.x += acceleration.x * dt
            particle.velocity.y += acceleration.y * dt
            particle.position.x += particle.velocity.x * dt
            particle.position.y += particle.velocity.y * dt
            
        PrintParticles()
        currentTime += dt

if __name__ == "__main__":
    run_simulation()
            
            
    
        
