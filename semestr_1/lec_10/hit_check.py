def norm_2d(v):
    return (v[0] ** 2 + v[1] ** 2) ** 0.5


def sc_mul(a, b):
    return sum([aa * bb for aa, bb in zip(a, b)])


def get_point_line_distance(point, r0, n):
    """Return distance between the point and the line.

    The distance is positive if the point is on the
    outer half-plane and negative if the point
    is on the inner half-plane. The outer half-plane is 
    the half-plane to which vector `n` is directed.

    Args:
        point (`tuple` or `list` of 2 numbers): The point
            coordinates.
        r0 (`tuple` or `list` of 2 numbers): Coordinates
            of any point on the line.
        n (`tuple` or `list` of 2 numbers): The normal vector.
    Returns:
        float: the distance between the point and the line.
    """
    dr = (point[0] - r0[0], point[1] - r0[1])
    return sc_mul(dr, n) / norm_2d(n)


def project(v, a):
    """Return the projection of vector `v` onto vector `a`

    Args:
        v (`tuple` or `list` of 2 numbers): Any 2D vector.
        a (`tuple` or `list` of 2 numbers): Any 2D vector.
    Returns:
        `tuple` of 2 numbers: the projection vector.
    """
    a_sqr = a[0] ** 2 + a[1] ** 2
    return a[0] * sc_mul(v, a) / a_sqr, a[1] * sc_mul(v, a) / a_sqr


def is_hit(ball, r_ball, v, target, r_target):
    """Check if the ball hits the target.

    The ball radius-vector changes by the vector `v` and
    the function returns `True` if the target is on the way of
    the ball.

    Args:
        ball (`tuple` or `list` of 2 numbers): The ball
            coordinates before the ball movement.
        r_ball (number): The ball radius.
        v (`tuple` or `list` of 2 numbers): The ball velocity.
        target (`tuple` or `list` of 2 numbers): The target
            coordinates.
        r_target (number): The target radius.
    Returns:
        bool
    """
    v_norm = norm_2d(v)
    dr = (target[0] - ball[0], target[1] - ball[1])
    dr_norm = norm_2d(dr)

    p = project(dr, v)
    p_norm = norm_2d(p)

    if p_norm > v_norm:
        c = (v_norm ** 2 + dr_norm ** 2 - 2 * sc_mul(v, dr)) ** 0.5
        return c <= r_ball + r_target

    h = get_point_line_distance(target, ball, (-v[1], v[0]))
    return abs(h) <= r_ball + r_target

