# Definisikan grid
grid = [
    ['S', 1, 0, 0, 0],
    [0, 1, 1, 0, 0],
    [0, 0, 1, 1, 0],
    ['T', 1, 0, 1, 0],
    [0, 1, 1, 1, 0]
]

# Koordinat awal robot
robot_position = (0, 0)

# Fungsi untuk mencetak grid
def print_grid():
    for row in grid:
        print(" ".join(str(cell) for cell in row))
    print("\n")

# Fungsi untuk menggerakkan robot
def move_robot():
    global robot_position
    x, y = robot_position

    # Cek di sekitar (atas, bawah, kiri, kanan)
    moves = [(x-1, y), (x+1, y), (x, y-1), (x, y+1)]
    for new_x, new_y in moves:
        # Pastikan posisi baru ada dalam batas grid
        if 0 <= new_x < len(grid) and 0 <= new_y < len(grid[0]):
            # Jika ketemu '1', pindah ke posisi tersebut
            if grid[new_x][new_y] == 1:
                # Tandai posisi lama sebagai kosong dan perbarui posisi baru
                grid[x][y] = 0
                robot_position = (new_x, new_y)
                grid[new_x][new_y] = 'R'  # Tandai posisi robot di grid
                return True  # Langkah berhasil

            # Jika mencapai tujuan ('T'), robot berhenti
            elif grid[new_x][new_y] == 'T':
                grid[x][y] = 0
                grid[new_x][new_y] = 'R'  # Tandai posisi robot di tujuan
                print("Robot has reached the target!")
                return False  # Sinyal untuk berhenti
    return False  # Tidak ada langkah valid

# Main loop untuk pergerakan robot
print("Initial grid:")
print_grid()
running = True
while running:
    running = move_robot()  # Pindah ke posisi berikutnya
    print_grid()  # Cetak grid setelah setiap langkah
