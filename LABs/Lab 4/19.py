import sys
import math

def get_dist(p1, p2):
    return math.sqrt((p1[0]-p2[0])**2 + (p1[1]-p2[1])**2)

def solve():
    line1 = sys.stdin.readline()
    if not line1: return
    r = float(line1.strip())
    
    line2 = sys.stdin.readline()
    if not line2: return
    a = tuple(map(float, line2.split()))
    
    line3 = sys.stdin.readline()
    if not line3: return
    b = tuple(map(float, line3.split()))

    if a == b:
        print(f"{0.0:.10f}")
        return

    dx, dy = b[0] - a[0], b[1] - a[1]
    segment_len_sq = dx**2 + dy**2
    
   
   
    t = -(a[0]*dx + a[1]*dy) / segment_len_sq
    
    intersects = False
    if 0 < t < 1:
        nearest_x = a[0] + t * dx
        nearest_y = a[1] + t * dy
        dist_to_line = math.sqrt(nearest_x**2 + nearest_y**2)
        if dist_to_line < r - 1e-11:
            intersects = True
            
    if not intersects:
        print(f"{math.sqrt(segment_len_sq):.10f}")
    else:
        dist_oa = math.sqrt(a[0]**2 + a[1]**2)
        dist_ob = math.sqrt(b[0]**2 + b[1]**2)
        
        
        side_a = math.sqrt(max(0, dist_oa**2 - r**2))
        side_b = math.sqrt(max(0, dist_ob**2 - r**2))
        
    
        dot_product = (a[0]*b[0] + a[1]*b[1]) / (dist_oa * dist_ob)
        total_angle = math.acos(max(-1.0, min(1.0, dot_product)))
        
      
        angle_a = math.acos(max(-1.0, min(1.0, r / dist_oa)))
        angle_b = math.acos(max(-1.0, min(1.0, r / dist_ob)))
        
        arc_angle = total_angle - angle_a - angle_b
        arc_len = r * max(0, arc_angle)
        
        print(f"{side_a + side_b + arc_len:.10f}")

if __name__ == "__main__":
    solve()