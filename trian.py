def estimated(theta0,theta1,mileage):
    return theta0 + (theta1 * mileage)


def load():
    file = open("data.csv","r")
    prices =[]
    km = []
    for line in file:
        if line !="km,price\n":
            line =line.strip()
            line = line.split(",")
            prices.append(float(line[1]))
            km.append(float(line[0]))
    return prices,km

def train(fielname,learing_rate=0.000001,iterations=1000):
    prices,km = load()
    theta0 = 0
    theta1 = 0
    m = len(prices)
    for i in range(iterations):
        sum0 = 0
        sum1 = 0
        predictions = [estimated(theta0,theta1,x) for x in km]
        erros = [predictions[j] - prices[j] for j in range(m)]
        sum_erros = sum(erros)
        sum_errors_km = sum()