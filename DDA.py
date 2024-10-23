import matplotlib.pyplot as plt

def dda(x1, y1, x2, y2):
    # Hitung delta perubahan
    dx = x2 - x1
    dy = y2 - y1
    
    # Tentukan jumlah langkah yang lebih besar, apakah perubahan di x atau di y
    steps = abs(dx) if abs(dx) > abs(dy) else abs(dy)
    
    # Kemudian hitung increment pada tiap langkah
    x_inc = dx / steps
    y_inc = dy / steps
    
    # Lalu buat list untuk menyimpan titik-titik garis
    x_values = [x1]
    y_values = [y1]
    
    # Inisialisasi titik awal
    x = x1
    y = y1
    
    # Iterasi untuk membuat titik-titik garis
    for _ in range(int(steps)):
        x += x_inc
        y += y_inc
        x_values.append(round(x))
        y_values.append(round(y))
    
    return x_values, y_values

# Titik awal dan akhir garis
x1, y1 = 6, 4
x2, y2 = 9, 7

# Hitung gradien (m)
if x2 - x1 != 0:
    m = (y2 - y1) / (x2 - x1)
else:
    m = None  # Mengatasi pembagian dengan nol jika x1 == x2 (garis vertikal)

# Selanjutnya dapatkan titik-titik garis menggunakan algoritma DDA
x_vals, y_vals = dda(x1, y1, x2, y2)

# Plot hasil garis
plt.plot(x_vals, y_vals, marker='o')
plt.title(f"Garis antara ({x1}, {y1}) dan ({x2}, {y2}) menggunakan DDA")
plt.xlabel("X")
plt.ylabel("Y")
plt.grid(True)

# Tampilkan gradien di plot
if m is not None:
    plt.text(min(x_vals), min(y_vals), f'Gradien = {m:.2f}', fontsize=10, color='red')
else:
    plt.text(min(x_vals), min(y_vals), 'Gradien = Tak Terdefinisi', fontsize=12, color='red')

plt.show()



