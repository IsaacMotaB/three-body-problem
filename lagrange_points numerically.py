# Code to find the positions of Lagrange points L1, L2 and L3 of a binary-star (star-planet) system numerically
# L4 and L5 can be easily find geometrically

# We assume the center of mass of the stars is at the origin and the stars themselves at the x-axis

# Set the net acceleration on L (currently calculating for L3 position, change the expression accordingly)
def function1(L):
    return m1/(L-r1)**2 + m2/(L+r2)**2


# Set the centripetal acceleration on L (angular speed ω can be derived from the stars positions and masses)
def function2(L):
    return m2 * L / (R**2 * r1)


def find_intersection(interval_min, interval_max):
    step_len = 1
    current_min = interval_min
    current_max = interval_max
    while True:
        print(f"{current_min} - {current_max} || {step_len}")
        print("")
        num_steps = int((current_max - current_min) / step_len)
        for i in range(num_steps + 1):
            func_input = current_min + step_len * i
            value1 = function1(func_input)
            value2 = function2(func_input)
            dif = abs(value1 - value2)
            print(f"{func_input}: {value1} = {value2} || dif of {dif}")
            if i == 0:
                lower_dif = dif
                intersection = func_input
            elif dif <= lower_dif:
                lower_dif = dif
                intersection = func_input
        current_min = intersection - step_len
        current_max = intersection + step_len
        step_len /= 10
        print(f"intersection: {intersection}")
        print(f"min_dif: {lower_dif}")
        print("--------------------------------------------------------------")

        if lower_dif < 10**(-10):
            break

    return intersection


# System data
m1 = 125
m2 = 1
r1 = 0.1984126984
r2 = 24.8015873016
R = 25

L_intersection = find_intersection(15, 30)
print(L_intersection)

# With these positions, you can easily find their velocities using the known value of the angular speed ω
