import tkinter as tk



    rootWindow = tk.Tk()
    rootWindow.title("服务器")
    rootWindow.geometry('300x300')

    ip_label = tk.Label(rootWindow, text='服务器 ip 地址', width=1, height=1)
    ip_label.pack()
    ip_label.place(relx=0.1, rely=0.25, relwidth=0.8, relheight=0.1)
    ip_entry = tk.Entry(rootWindow)
    ip_entry.place(relx=0.1, rely=0.35, relwidth=0.8, relheight=0.1)


    port_label = tk.Label(rootWindow, text='端口号', width=1, height=1)
    port_label.pack()
    port_label.place(relx=0.1, rely=0.45, relwidth=0.8, relheight=0.1)
    port_entry = tk.Entry(rootWindow)
    port_entry.place(relx=0.1, rely=0.55, relwidth=0.8, relheight=0.1)
    

    connect_bt = tk.Button(rootWindow, text='Connect')
    connect_bt.place(relx=0.1, rely=0.7, relwidth=0.8, relheight=0.2)
    rootWindow.mainloop()