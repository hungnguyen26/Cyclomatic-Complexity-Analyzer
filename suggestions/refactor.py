def refactor_suggestion(score):
    if score <= 5:
        return "✅ Code đơn giản – Không cần chỉnh sửa."
    elif score <= 10:
        return "⚠️ Trung bình – Nên chia nhỏ hàm."
    else:
        return "🚨 Phức tạp – Cần refactor gấp!"
