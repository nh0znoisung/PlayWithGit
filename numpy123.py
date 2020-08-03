import numpy as np
a = np.arange(12).reshape(3,4) +1
# Dùng chỉ số để lấy phần tử hàng 1, cột 2
print(a[1][2]) # 7
print(a[1, 2]) # 7
# Dùng slicing để lấy 2 hàng đầu tiên của 2 cột đầu tiên
print(a[:2][:2])
# [[1 2]
#   [5 6]]
# Kết hợp dùng slicing và indexing
# Chú ý: sẽ tạo ra mảng có rank thấp hơn mảng cũ
r1 = a[1, :] # Rank 1, hàng 1 của a 
print(r1, r1.shape) # [[5 6 7 8]] (4,))