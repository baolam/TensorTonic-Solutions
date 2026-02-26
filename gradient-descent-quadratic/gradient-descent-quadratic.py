def gradient_descent_quadratic(a, b, c, x0, lr, steps):
    """
    Return final x after 'steps' iterations.
    """
    # Write code here
    def f_prime(x):
        return 2 * a * x + b

    x = x0
    for _ in range(steps):
        x = x - lr * f_prime(x)

    return x