import numpy as np
import scipy as sp
import matplotlib.pyplot as plt


INTREST = 0.18 / 12
MONTHLY_PAYMENT = 20


def equation(x: float, y: float) -> float:
	return INTREST * y + MONTHLY_PAYMENT


def solution(y_0: float, x: float) -> float:
    return (y_0 - MONTHLY_PAYMENT / INTREST) * np.exp(INTREST * x) + MONTHLY_PAYMENT / INTREST


def effective_cost(x: float) -> float:
    func = lambda z: (np.log(MONTHLY_PAYMENT) - np.log(MONTHLY_PAYMENT - INTREST * z)) / INTREST
    return (func(1000 + x) - func(1000)) * MONTHLY_PAYMENT


def main():
    INITIAL_AMOUNT = 1016.0
    sol = (np.log(MONTHLY_PAYMENT) - np.log(MONTHLY_PAYMENT - INTREST * INITIAL_AMOUNT)) / INTREST
    xs = np.linspace(0, sol, 1000)
    ys = solution(INITIAL_AMOUNT, xs)
    
    total_cost = np.ceil(sol) * MONTHLY_PAYMENT
    
    print(sol)
    print(total_cost)
    
    plt.plot(xs, ys)
    plt.show()


if __name__ == '__main__':
    main()
