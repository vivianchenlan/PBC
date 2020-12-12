import tkinter as tk

#  建立主視窗


class window_1(tk.Frame):
    def _init_(self, parent):
        tk.Frame._inti_(self, parent)
        self.parent = parent
        

#  文字        
root = tk.Tk()
root.title("pick your drink!!!")
root.geometry("700x500+250+100")
root.configure(bg="#FFF8DC")

label_1 = tk.Label(root, text="\n 你今天想喝什麼樣的飲料呢?",
                   bg = "#FFF8DC",
                    font = ("微軟正黑體", "15")).grid(row=0,column=1, columnspan=6, sticky=tk.NSEW)
label_2 = tk.Label(root, text="選個地區吧!(可複選)",
                   bg = "#FFF8DC",
                   font = ("微軟正黑體", "12")).grid(row=1, column=1, columnspan=6, sticky=tk.NSEW)
#  def 全選
def select_clear_states():
    global checkboxes, all_states
    states = all_states.get()
        
    if states == 0:
        
        for i in range(5):
            checkboxes[i].set(0)
        
    if states == 1:
        for i in range(5):
            checkboxes[i].set(1)

    
    #  def 回傳資料
def select_area():
    global select
    select = []
    for j in checkboxes:
        if checkboxes[j].get()==True:
            select.append(area[j])
    return select
    

def print_area():
    print(select)

    #  地區資料
area = {0:"第一區", 1:"第二區", 2:"第三區", 3:"第四區", 4:"第五區"}
    #  各選項的布林值
checkboxes = {}

# selected_area = []
    
    #  按鈕:第一區到第五區
for i in range(len(area)):
    checkboxes[i] = tk.BooleanVar()
    checkbox = tk.Checkbutton(root, text=area[i], variable=checkboxes[i], bg="#FFF8DC").grid(row=3, column=i+1, padx=25, pady=10)
    #  按鈕:全選
all_states = tk.IntVar()
select_all = tk.Checkbutton(root, text="全選", variable=all_states, command=select_clear_states, bg="#FFF8DC")
select_all.grid(row=3, column=6, padx=25, pady=10)
    #  按鈕:OK
tk.Button(root, text="ok", command = lambda:[select_area(), print_area()]).grid(row=5, column=1, columnspan=6, pady=300)




root.mainloop()