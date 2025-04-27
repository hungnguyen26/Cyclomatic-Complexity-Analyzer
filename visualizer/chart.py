import matplotlib.pyplot as plt

def draw_bar_chart(results):
    names = [r["name"] for r in results]
    scores = [r["score"] for r in results]

    plt.bar(names, scores, color='skyblue')
    plt.axhline(10, color='red', linestyle='--', label='Ngưỡng phức tạp')
    plt.xlabel("Function")
    plt.ylabel("Cyclomatic Complexity")
    plt.title("Biểu đồ Độ phức tạp McCabe")
    plt.legend()
    plt.tight_layout()
    plt.show()
