import matplotlib.pyplot as plt

# Hàm tính số lượng thành viên ở từng thế hệ bằng while loop
def calculate_generations_while(so_nam):
    generations = []  # Danh sách lưu số lượng thành viên mỗi thế hệ
    i = 0  # Khởi tạo thế hệ đầu tiên
    while i <= so_nam:  # Tiếp tục cho đến thế hệ cuối cùng
        generations.append(2**i)  # Tăng trưởng theo hàm mũ
        i += 1  # Tăng thế hệ
    return generations

# Hàm vẽ biểu đồ
def plot_generations(so_nam, generations):
    plt.figure(figsize=(10, 6))
    plt.plot(range(len(generations)), generations, marker='o', linestyle='-', color='b')
    plt.title('Số lượng thành viên theo từng thế hệ', fontsize=14)
    plt.xlabel('Thế hệ (g)', fontsize=12)
    plt.ylabel('Số lượng thành viên', fontsize=12)
    plt.xticks(range(len(generations)))
    plt.grid(True, linestyle='--', alpha=0.6)
    plt.show()

# Nhập số năm (thế hệ)
try:
    so_nam = int(input("Nhập số năm khảo sát (so_nam): "))
    if so_nam < 0:
        print("Vui lòng nhập số năm không âm!")
    else:
        # Tính toán số lượng thành viên mỗi thế hệ
        generations = calculate_generations_while(so_nam)

        # Hiển thị kết quả
        print("Số lượng thành viên theo từng thế hệ:")
        i = 0
        while i < len(generations):
            print(f"Thế hệ g_{i}: {generations[i]} thành viên")
            i += 1

        # Vẽ biểu đồ
        plot_generations(so_nam, generations)
except ValueError:
    print("Vui lòng nhập một số nguyên hợp lệ!")
