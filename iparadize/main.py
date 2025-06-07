import tkinter as tk

WIDTH = 320
HEIGHT = 240

root = tk.Tk()
root.attributes('-fullscreen', True)
root.configure(bg='black')
root.geometry(f'{WIDTH}x{HEIGHT}+0+0')

canvas = tk.Canvas(
    root, width=WIDTH, height=HEIGHT, bg='black', highlightthickness=0
)
canvas.pack(expand=True)

text = 'iParadize'

for i in range(6):
    font_size = 12 + i * 4
    y = 5 + i * 38
    canvas.create_text(
        WIDTH // 2,
        y,
        text=text,
        fill='white',
        font=('Arial', font_size),
        anchor='n',
    )

# Pressione ESC para sair
root.bind('<Escape>', lambda e: root.destroy())

root.mainloop()
