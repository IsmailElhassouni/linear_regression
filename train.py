import csv

def estimate_price(theta0=0,theta1=0,mileage=0):
    return theta0 + (theta1 * mileage)

def normalize(x,min,max):
    return (x - min)/(max - min)

def load():
    try:
        with  open("data.csv","r") as f:
            reader = csv.reader(f)
            next(reader)
            prices =[]
            km = []
            for line in reader:
                    km.append(float(line[0]))
                    prices.append(float(line[1]))
            return prices,km
    except:
        exit(print("no data to train"))
def train(learning_rate=0.01,iterations=50000):
    prices,km = load()
    theta0 = 0
    theta1 = 0
    mi = min(km)
    ma = max(km)
    km = [normalize(x, mi, ma) for x in km]
    m = len(prices)#numbers of cars 
    for i in range(iterations):
        predictions = [estimate_price(theta0,theta1,x) for x in km]
        errors = [predictions[j] - prices[j] for j in range(m)]
        sum_errors = sum(errors)
        sum_errors_km = sum([e*m_val for e,m_val in zip(errors,km)])
        tmpO = theta0 - (learning_rate * (1/m) * sum_errors)
        tmp1 = theta1 - ( learning_rate * ( 1 / m) * sum_errors_km)
        theta0 = tmpO
        theta1 = tmp1
    with open('thetas','w') as f:
        f.write(f"{theta0}\n{theta1}\n{mi}\n{ma}")
if __name__ == "__main__":
    train()