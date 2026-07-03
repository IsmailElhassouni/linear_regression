import matplotlib.pyplot as plt

from train import estimate_price, normalize, load


def load_thetas(path="thetas"):
    try:
        with open(path, "r") as f:
            theta0 = float(f.readline())
            theta1 = float(f.readline())
            mi = float(f.readline())
            ma = float(f.readline())
            return theta0, theta1, mi, ma
    except (FileNotFoundError, ValueError):
        print("No 'thetas' file found (or it's malformed) — run train.py first.")
        return 0.0, 0.0, 0.0, 1.0


def compute_precision(prices, predictions):
    m = len(prices)
    errors = [predictions[i] - prices[i] for i in range(m)]

    mae = sum(abs(e) for e in errors) / m
    mse = sum(e ** 2 for e in errors) / m
    rmse = mse ** 0.5

    mean_price = sum(prices) / m
    ss_tot = sum((p - mean_price) ** 2 for p in prices)
    ss_res = sum(e ** 2 for e in errors)
    r2 = 1 - (ss_res / ss_tot) if ss_tot != 0 else 0

    return mae, rmse, r2


def plot_data(km, prices, theta0, theta1, mi, ma):
    plt.figure(figsize=(9, 6))
    plt.scatter(km, prices, color="royalblue", label="Data points")

    x_line = [min(km), max(km)]
    y_line = [estimate_price(theta0, theta1, normalize(x, mi, ma)) for x in x_line]
    plt.plot(x_line, y_line, color="crimson", linewidth=2, label="Linear regression")

    plt.xlabel("Mileage (km)")
    plt.ylabel("Price")
    plt.title("Price vs Mileage")
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig("regression_plot.png", dpi=150)
    plt.show()


def main():
    prices, km = load()
    theta0, theta1, mi, ma = load_thetas()

    km_norm = [normalize(x, mi, ma) for x in km]
    predictions = [estimate_price(theta0, theta1, x) for x in km_norm]

    mae, rmse, r2 = compute_precision(prices, predictions)

    print(f"Model: price = {theta0:.4f} + {theta1:.4f} * normalize(mileage)")
    print(f"Number of samples : {len(prices)}")
    print(f"MAE  (Mean Abs Err): {mae:.2f}")
    print(f"RMSE (Root Mean Sq): {rmse:.2f}")
    print(f"R^2  (fit quality) : {r2:.4f}  (closer to 1 = better)")

    plot_data(km, prices, theta0, theta1, mi, ma)


if __name__ == "__main__":
    main()