from typing import List, Tuple


def sum_3_integers(triplet: List[int]) -> int:
    x1,y1,z1 = triplet
    sum3 = x1+y1+z1
    return sum3


def compute_volume(box_dimensions: Tuple[int, int, int]) -> int:
    x2,y2,z2 = box_dimensions
    vol = x2*y2*z2
    return vol
  

# do not modify below this line
print(sum_3_integers([1, 2, 3]))
print(sum_3_integers([4, 6, 2]))

print(compute_volume((1, 2, 3)))
print(compute_volume((3, 2, 1)))
print(compute_volume((3, 9, 7)))
