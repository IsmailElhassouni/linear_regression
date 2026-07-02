import csv
def estimated(theta0=0,theta1=0,mileage=0):
    return theta0 + (theta1 * mileage)


def load():
    with  open("data.csv","r") as f:
        reader = csv.reader(f)
        next(reader)
        prices =[]
        km = []
        for line in reader:
                km.append(float(line[0]))
                prices.append(float(line[1]))
        return prices,km

def train(learing_rate=0.0001,iterations=1000):
    prices,km = load()
    theta0 = 0
    theta1 = 0
    m = len(prices)#numbers of cars 
    for i in range(iterations):
        sum0 = 0
        sum1 = 0
        predictions = [estimated(theta0,theta1,x) for x in km]
        errors = [predictions[j] - prices[j] for j in range(m)]
        sum_errors = sum(errors)
        sum_errors_km = sum([e*m_val for e,m_val in zip(errors,km)])
        tmpO = theta0 - (learing_rate * (1/m) * sum_errors)
        tmp1 = theta1 - ( learing_rate * ( 1 / m) * sum_errors_km)
        theta0 = tmpO
        theta1 = tmp1
    with open('thetas','w') as f:
        f.write(f"{theta0}\n{theta1}")
train()