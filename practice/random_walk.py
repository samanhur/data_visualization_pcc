from random import choice


class RandomWalk:
    """A class to generate random walks."""

    def __init__(self, num_points=5_000):
        """Initialize attributes of a walk."""
        self.num_points = num_points

        # All walks start at (0, 0).
        self.x_coordinate = [0]
        self.y_coordinate = [0]

    def fill_walk(self):
        """Calculate all the points in the walk."""

        # Keep taking steps until the walks reaches the desired length.
        while len(self.x_coordinate) < self.num_points:

            # Decide which direction to go, and how far to go.
            x_step = self.get_step()
            y_step = self.get_step()

            # Reject moves that go nowhere.
            if x_step == 0 and y_step == 0:
                continue

            # Calculate the new position.
            x = self.x_coordinate[-1] + x_step
            y = self.y_coordinate[-1] + y_step

            self.x_coordinate.append(x)
            self.y_coordinate.append(y)
            
    def get_step(self):
        direction = choice([-1, 1])
        distance = choice(list(range(8)))
        step = direction * distance
        
        return step
