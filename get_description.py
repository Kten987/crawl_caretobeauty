
def get_description_(description):
    keys = ["Characteristics", "Main Ingredients", "How to use"]
    parts = {}

    # Tìm vị trí của mỗi key trong description và lưu vào một list
    positions = [(key, description.find(key)) for key in keys if description.find(key) != -1]

    if positions == []:
        return {"Description": description}
    
    # Sắp xếp các vị trí dựa trên index
    positions.sort(key=lambda x: x[1])

    # Kiểm tra và thêm phần đầu vào "Description" nếu key đầu tiên không ở vị trí đầu tiên
    if positions and positions[0][1] > 0:
        parts["Description"] = description[:positions[0][1]].strip()

    # Tách description dựa vào các vị trí đã tìm
    for i, (key, pos) in enumerate(positions):
        # Nếu không phải key cuối cùng, tách từ vị trí hiện tại đến vị trí của key tiếp theo
        if i < len(positions) - 1:
            next_pos = positions[i + 1][1]
            parts[key] = description[pos:next_pos].strip()
        else:
            # Nếu là key cuối cùng, tách từ vị trí hiện tại đến cuối description
            parts[key] = description[pos:].strip()
    return parts

if __name__ == "__main__":
    get_description_("Description: This is a description. Characteristics: This is a characteristic. Main Ingredients: This is a main ingredient. How to use: This is how to use.")
