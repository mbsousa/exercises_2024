
# Faça uma função que recebe por parâmetro o raio de uma esfera e calcula o
# seu volume (v = 4/3 * PI * R**3).

# Write a function that takes as a parameter the radius of a sphere and calculates the
# its volume (v = 4/3 * PI * R**3).

import math
def Operation(r):
    v = (4/3) * math.pi * (r**3)
    return v

assert abs(Operation(5)) > 500
assert abs(Operation(10)) > 233
assert abs(Operation(20)) > 200

print("Successf operation.")