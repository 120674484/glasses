import tkinter as tk
import random
mask_options = ['戴','不戴']
def show_random_option():
    label.config(text=random.choice(mask_options))
root = tk.Tk()
root.title("眼镜")
root.state('zoomed')
label = tk.Label(root,font=("Arial", 48))
label.pack(pady=100)
button = tk.Button(root, text="随机选择", font=("Arial", 36), command=show_random_option)
button.pack(pady=50)
root.mainloop()