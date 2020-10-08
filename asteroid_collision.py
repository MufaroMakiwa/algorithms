import random


def asteroidCollision(asteroids):

    prev_direction = 0
    to_left = []
    to_right = []
    index = 0

    while index < len(asteroids):

        direction = -1 if asteroids[index] < 0 else 1
        weight = asteroids[index]

        if prev_direction == 0 or prev_direction == -1:
            if direction < 0:
                to_left.append(weight)
            else:
                to_right.append(weight)
            prev_direction = direction

        else:
            # it is pointing to the right
            if direction > 0:
                to_right.append(weight)

            else:
                exploded = None
                while len(to_right) > 0:
                    if abs(weight) < to_right[-1]:
                        exploded = True
                        break

                    elif abs(weight) == to_right[-1]:
                        del to_right[-1]
                        exploded = True
                        break

                    else:
                        del to_right[-1]
                        exploded = False

                prev_direction = 1 if bool(to_right) else -1
                if not exploded and prev_direction < 0:
                    to_left.append(weight)

        index += 1

    return to_left + to_right


if __name__ == '__main__':

    arr = [-2, 1, -1, -2]
    print(arr)
    print(asteroidCollision(arr))


