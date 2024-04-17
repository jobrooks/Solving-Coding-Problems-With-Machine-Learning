import math

class Droplet:
    def __init__(self, x, y, v_x, v_y, r):
        self.x = x
        self.y = y
        self.v_x = v_x
        self.v_y = v_y
        self.r = r

    def update(self, dt):
        self.x += self.v_x * dt
        self.y += self.v_y * dt

    def distance(self, other):
        dx = self.x - other.x
        dy = self.y - other.y
        return math.sqrt(dx * dx + dy * dy)

    def overlaps(self, other):
        return self.distance(other) < self.r + other.r

    def collide(self, other):
        # Calculate the new position of the combined droplet
        new_x = (self.x * self.r + other.x * other.r) / (self.r + other.r)
        new_y = (self.y * self.r + other.y * other.r) / (self.r + other.r)

        # Calculate the new velocity of the combined droplet
        new_v_x = (self.v_x * self.r + other.v_x * other.r) / (self.r + other.r)
        new_v_y = (self.v_y * self.r + other.v_y * other.r) / (self.r + other.r)

        # Create the new droplet
        new_droplet = Droplet(new_x, new_y, new_v_x, new_v_y, self.r + other.r)
        return new_droplet


def simulate(droplets, dt):
    """
    Simulates the motion of a list of droplets until they collide.

    Args:
        droplets (list): The list of droplets to simulate.
        dt (float): The time step to use in the simulation.

    Returns:
        A tuple containing the final list of droplets and the time at which the last collision occurred.
    """

    # Update the positions of all the droplets
    for droplet in droplets:
        droplet.update(dt)

    # Check for collisions between all pairs of droplets
    for i in range(len(droplets)):
        for j in range(i + 1, len(droplets)):
            if droplets[i].overlaps(droplets[j]):
                # A collision has occurred, so create a new droplet and remove the two colliding droplets
                new_droplet = droplets[i].collide(droplets[j])
                droplets.pop(i)
                droplets.pop(j)
                droplets.append(new_droplet)
                return droplets, new_droplet.time

    # No collisions occurred, so return the current list of droplets
    return droplets, 0.0


def main():
    # Read the input
    n = int(input())
    droplets = []
    for i in range(n):
        x, y, v_x, v_y, r = map(int, input().split())
        droplets.append(Droplet(x, y, v_x, v_y, r))

    # Simulate the motion of the droplets
    dt = 0.001
    t = 0.0
    while True:
        droplets, collision_time = simulate(droplets, dt)
        if collision_time == 0.0:
            break
        t += collision_time

    # Print the output
    print("{} {}".format(len(droplets), t))


if __name__ == "__main__":
    main()