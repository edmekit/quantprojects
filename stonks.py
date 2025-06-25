import math, random

St = int(input("Enter the price of the stock: "))
mew = float(input("Enter the expected return: ")) 
sigma = float(input("Enter the volatility: "))   
days = int(input("Enter the number of days: "))
dt = 1 / 252   
story = 1000

def tommorow(S, mu, igma, tri):
    Z = random.gauss(0, 1)
    return S * math.exp((mu - 0.5 * igma ** 2) * tri + igma * math.sqrt(tri) * Z)

def stories(S, mu, igma, days):
    today = S
    for i in range(days):
        today = tommorow(today, mu, igma, dt)
    return today

prices = [stories(St, mew, sigma, days) for i in range(story)]

avg = sum(prices) / len(prices)
prob_up = sum(1 for price in prices if price > St) / len(prices)


print(f"The average price of the stock after {days} days is {avg:.2f}")
print(f"The probability of the stock going up is {prob_up * 100:.2f}%")