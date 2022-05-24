import tkinter as tk

rootWindow = tk.Tk()    # 创建窗口
rootWindow.title('123')     # 窗口名
rootWindow.geometry('450x300')  # 长 x 宽
rootWindow.iconbitmap('favicon.ico')     # 窗口图标
rootWindow['background'] = 'white'   # 窗口背景颜色
text = tk.Label(rootWindow,text="这是lable", bg="yellow",fg="black",font=('Times', 20, 'bold italic'))
text.pack()         # 将文本内容放置在主窗口内
button = tk.Button(rootWindow, text="关闭", command=rootWindow.quit)
button.pack(side="bottom")
rootWindow.mainloop()   # 让页面保持