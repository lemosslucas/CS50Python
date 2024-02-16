def main():
    # Storage the mass
    mass = int(input("m: "))
    # Call the function
    calculator_energy(mass)

def calculator_energy(mass):
    light_speed = 300000000
    # Calculates the Einsten's equation (The square of a number is he times it)
    energy = mass * (light_speed * light_speed)
    # Print the energy
    print(energy)

main()