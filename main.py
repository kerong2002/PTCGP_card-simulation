# 此模擬情形，只基於ex寶可夢為主機率進行分布
import numpy as np
import matplotlib.pyplot as plt

# 抽到稀有卡包機率是 0.05%
rare_pack_prob = 0.0005  # 抽到稀有卡包機率 0.05%

# 一般卡包中第 4 張卡的機率:
# 0.04% * 2(金卡) + 0.222%(時鏡卡) + 0.041% * 9(全圖+彩邊ex) + 0.333% * 5(普通ex)
slot_4_prob = (0.0004 * 2) + 0.00222 + (0.00041 * 9) + (0.00333 * 5)

# 一般卡包中第 5 張卡的機率:
# 0.08% * 2(金卡) + 0.888%(時鏡卡) + 0.166% * 9(全圖+彩邊ex) + 1.332% * 5(普通ex)
slot_5_prob = (0.0008 * 2) + 0.00888 + (0.00166 * 9) + (0.01332 * 5)

# 稀有卡包中每張卡的機率:
# 3.846%(金卡) + 3.846%(時鏡卡) + 3.846% * 9(全圖+彩邊ex) + 0%(沒有普通ex)
rare_card_prob = (0.03846 + 0.03846 + (0.03846 * 9)) / 100

def simulate_pulls(num_tests, num_packs):
    results_rare_cards = []  # 用來存儲每次測試中抽到的稀有卡數量
    results_rare_packs = []  # 用來存儲每次測試中抽到的稀有卡包數量

    for _ in range(num_tests):
        total_rare_cards = 0
        total_rare_packs = 0
        for _ in range(num_packs):
            if np.random.rand() < rare_pack_prob:
                # 抽到稀有卡包, 每張卡片都有機率是稀有卡
                total_rare_cards += np.random.binomial(5, rare_card_prob)
                total_rare_packs += 1  # 記錄這次抽到的稀有卡包
            else:
                # 抽到一般卡包, 只有第4張和第5張有機率是稀有卡
                total_rare_cards += np.random.binomial(1, slot_4_prob) + np.random.binomial(1, slot_5_prob)
        results_rare_cards.append(total_rare_cards)
        results_rare_packs.append(total_rare_packs)

    return results_rare_cards, results_rare_packs


def plot_distribution(results, num_packs, title):
    plt.hist(results, bins=range(0, max(results) + 2), density=True, alpha=0.7, color='blue', edgecolor='black', label='Simulation')

    # 計算正態分布的參數
    mean = np.mean(results)
    std = np.std(results)
    if std > 0:
        # 生成正態分布曲線
        x = np.linspace(0, max(results), 100)
        y = (1 / (std * np.sqrt(2 * np.pi))) * np.exp(-0.5 * ((x - mean) / std) ** 2)
        plt.plot(x, y, 'r-', label='Normal Distribution')

    plt.xlabel("Number of Rare Cards" if title == "Rare Cards" else "Number of Rare Packs")
    plt.ylabel("Probability Density")
    plt.title(f"{title} in {num_packs} Packs")
    plt.legend()


if __name__ == "__main__":
    num_tests = 100_0000  # 測試次數
    num_packs = 60
    results_rare_cards, results_rare_packs = simulate_pulls(num_tests, num_packs)

    # 創建兩個子圖來同時顯示兩張圖
    plt.figure(figsize=(12, 6))

    # Subplot 1: 稀有卡數量分布
    plt.subplot(1, 2, 1)
    plot_distribution(results_rare_cards, num_packs, "Rare Cards")

    # Subplot 2: 稀有卡包數量分布
    plt.subplot(1, 2, 2)
    plot_distribution(results_rare_packs, num_packs, "Rare Packs")

    plt.tight_layout()
    plt.show()
