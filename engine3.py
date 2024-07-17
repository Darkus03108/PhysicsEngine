import Engine

class AABB:
    def __init__(self, min, max):
        self.min = min
        self.max = max
        
def testAABBOverlap(a, b):
    d1x = b.min.x - a.max.x
    d1y = b.min.y - a.max.y
    d2x = a.min.x - b.max.x
    d2y = a.min.y - b.max.y

    if d1x > 0.0 or d1y > 0.0:
        return False
    if d2x > 0.0 or d2y > 0.0:
        return False
    
    return True
        
        

        
