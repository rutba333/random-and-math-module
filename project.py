import math

# Take input from the user
angle_degrees = float(input("Enter the angle in degrees: "))

# Convert degrees to radians because math functions in Python use radians
angle_radians = math.radians(angle_degrees)

# Calculate sine, cosine, and tangent
sin_value = math.sin(angle_radians)
cos_value = math.cos(angle_radians)
tan_value = math.tan(angle_radians)

# Display the results
print(f"Sine of {angle_degrees} degrees: {sin_value}")
print(f"Cosine of {angle_degrees} degrees: {cos_value}")
print(f"Tangent of {angle_degrees} degrees: {tan_value}")
