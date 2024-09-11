import tkinter as tk
from tkinter import colorchooser

def choose_color():
    # 调用系统默认的颜色选择器，返回RGB元组和十六进制颜色码
    color_code = colorchooser.askcolor(title="选择颜色")
    if color_code:
        hex_color = color_code[1]
        label.config(text=f"选择的颜色代码: {hex_color}", bg=hex_color)
        copy_button.config(state=tk.NORMAL)
        root.clipboard_clear()  
        root.clipboard_append(hex_color)  


root = tk.Tk()
root.title("颜色选择器")



button = tk.Button(root, text="选择颜色", command=choose_color)
button.pack(pady=20)


label = tk.Label(root, text="选择的颜色代码:", font=('Arial', 12))
label.pack(pady=20)


copy_button = tk.Button(root, text="已复制到剪贴板", state=tk.DISABLED) #unusable as normal
copy_button.pack(pady=10)


root.geometry("300x200")
root.mainloop()
