import numpy as np
import matplotlib.pyplot as plt

plt.rcParams["font.family"] = ["SimSun", "Microsoft YaHei", "SimHei"]  # 支持中文
plt.rcParams["axes.unicode_minus"] = False  # 解决负号显示问题


class GM11:
    def __init__(self, data: list):
        self.x0 = np.array(data, dtype=np.float64)
        self.n = len(self.x0)
        if self.n < 2:
            raise ValueError("数据长度必须大于等于2")
        self.x1 = self.x0.cumsum()
        self.a, self.b = self._cal_params()
        self.fitted = self._fit_values()

    def _cal_params(self):
        B, Y = [], []
        for i in range(self.n - 1):
            z = -0.5 * (self.x1[i] + self.x1[i + 1])
            B.append([z, 1])
            Y.append(self.x0[i + 1])
        B = np.array(B)
        Y = np.array(Y).reshape(-1, 1)
        try:
            params = np.linalg.inv(B.T @ B) @ B.T @ Y
        except np.linalg.LinAlgError:
            params = np.linalg.lstsq(B, Y, rcond=None)[0]
        return params.flatten()

    def _fit_values(self):
        x1_pred = []
        for k in range(self.n):
            x1_k = (self.x0[0] - self.b / self.a) * np.exp(-self.a * k) + self.b / self.a
            x1_pred.append(x1_k)
        x1_pred = np.array(x1_pred)

        fitted = []
        for k in range(self.n):
            if k == 0:
                fitted.append(self.x0[0])
            else:
                fitted.append(x1_pred[k] - x1_pred[k - 1])
        return np.array(fitted)

    def get_fitting_error(self):
        residuals = self.x0 - self.fitted
        mse = np.mean(residuals ** 2)
        mape = np.mean(np.abs(residuals / self.x0)) * 100
        return {"MSE": mse, "MAPE": mape}

    def predict(self, steps: int):
        x1_pred = []
        for k in range(self.n + steps):
            x1_k = (self.x0[0] - self.b / self.a) * np.exp(-self.a * k) + self.b / self.a
            x1_pred.append(x1_k)
        x1_pred = np.array(x1_pred)

        x0_pred = [x1_pred[0]]
        for k in range(1, self.n + steps):
            x0_k = x1_pred[k] - x1_pred[k - 1]
            x0_pred.append(x0_k)
        return np.array(x0_pred)


if __name__ == "__main__":
    # 原始数据
    data = [100.59, 103.49, 117.38, 123.40, 129.43]
    years = [2019, 2020, 2021, 2022, 2023]
    model = GM11(data)

    # 模型评估
    errors = model.get_fitting_error()
    print("拟合误差指标：", errors)

    # 预测未来
    steps = 3
    all_pred = model.predict(steps=steps)
    future_years = [2024, 2025, 2026]

    # 可视化
    plt.figure(figsize=(9, 6))
    # 历史数据
    plt.plot(years, data, "o-", linewidth=2, label="历史数据")
    # 拟合曲线
    plt.plot(years, all_pred[:len(data)], "s--", linewidth=2, label="GM(1,1)拟合")
    # 未来预测
    plt.plot(future_years, all_pred[len(data):], "d-.", linewidth=2, color="orange", label="未来预测")

    # 标注误差
    plt.text(years[0], max(data) * 0.95,
             f"MAPE={errors['MAPE']:.2f}%\nMSE={errors['MSE']:.4f}",
             fontsize=11, bbox=dict(facecolor="white", alpha=0.6))

    plt.title("GM(1,1) 灰色预测模型拟合与预测", fontsize=14)
    plt.xlabel("年份", fontsize=12)
    plt.ylabel("数值", fontsize=12)
    plt.legend()
    plt.grid(True, linestyle="--", alpha=0.7)
    plt.tight_layout()
    plt.show()

