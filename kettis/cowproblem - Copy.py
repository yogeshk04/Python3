def x_start_generator(a, b):
    """Generate start x-coordinate of the n'th diagonal"""

    above_b = False    # Indicates if an earlier x_start=0 has y > b
    beyond_a = False   # Indicates if an earlier x_start > a
    two_pow_n = 1      # Iterates 2**n, instead of calculating it

    while True:

        if beyond_a:
            yield a+1
            continue

        # Verify if x_start is on left edge (that is 'not above_b')
        if not above_b:
            above_b =  (two_pow_n - 1) > b


        # If on left edge, return start_x = 0 ...
        if not above_b:
            yield 0
        else:

            # ... else find x_start on line at height b
            x_start = two_pow_n - 1 - b

            # Check if x_start is beyond the value of a, and store this
            beyond_a = x_start > a

            # If not beyond return x_start matching the top edge
            if not beyond_a:
                yield x_start

        # Prepare for next n
        two_pow_n *= 2


def x_end_generator(a, b):
    """Generate end x-coordinate of the n'th diagonal"""

    beyond_a = False  # Indicates if an earlier x_end > b
    two_pow_n = 1

    while True:
        # If x_end has once been larger than a, limit it to a
        if beyond_a:
            yield a
            continue

        # Find end coordinate when diagonal crosses y=0
        x_end = two_pow_n - 1

        # Check if we've passed a, and store this
        beyond_a = x_end > a

        # If not passed, return x coordinate
        if not beyond_a:
            yield x_end

        # Prepare for next iteration
        two_pow_n *= 2


def find_legal_places(a, b, print_xtras=False):
    """Return number of legal places within (0, 0) -> (a, b)

    Using the x_start_generator() and x_end_generator() find the start
    and end coordinators of the n'th diagonal. If it's a valid diagonal
    add the legal places from this diagonal to the total. When not any
    more valid coordinates are found, return the total.

    If wanted, print_xtras=True, you can get print outs of the coordinates
    as we tag along, and a nice total.
    """
    x_start_range = x_start_generator(a, b)
    x_end_range = x_end_generator(a, b)

    legal_places = 0
    n = 0

    while True:
        x_start = next(x_start_range)
        x_end = next(x_end_range)

        if x_start < a and x_start <= x_end:
            legal_places += x_end - x_start + 1
            if print_xtras:
                print('n: {: 4d}, x_start: {: 12d}, x_end: {: 12d}, legal places: {: 12d}'.format(
                      n, x_start, x_end, legal_places))
        else:
            break

        n += 1
    if print_xtras:
        print('    For A={} and B={} there are {} legal places\n'.format(a, b, legal_places))

    return legal_places

def main():
    print ('Sample Output 1')
    for (a, b) in [(2, 3), (7, 7)]:
       print(find_legal_places(a, b))

    print

    find_legal_places(7, 7, True)

    print('a=10**1000, b=10**1000, legal_places={}'.format(find_legal_places(7**1000, 7**1000)))


if __name__ == '__main__':
    main()