import tkinter as tkr
from tkinter import messagebox

player=1  # Player 1 
heaps=[5, 4, 3]  # Initial heap size

def player_change():
    global player
    player=3-player 

def update_box():
    for i in range(len(heaps)):
        buttons[i]["text"]=f"Heap{i+1}:{heaps[i]}"

def show_result(h_index, num_rmv):
    heaps[h_index]-=num_rmv
    if sum(heaps)==0:
        messagebox.showinfo( "Game over",f"Player {player} wins!")
        reset_game()
    else:
        player_change()
        if player==2:
            ai_move()
        update_box()

def max_val(heaps):
    if sum(heaps) == 0:
        return -1 
    max_num=float('-inf')
    for i in range(len(heaps)):
        for j in range(1, heaps[i] + 1):
            heaps_copy = heaps.copy()
            heaps_copy[i] -= j
            num = min_val(heaps_copy)
            max_num = max(max_num, num)
    return max_num

def min_val(heaps):
    if sum(heaps)==0:
        return 1  
    min_num=float('inf')
    for i in range(len(heaps)):
        for j in range(1, heaps[i] + 1):
            heaps_copy=heaps.copy()
            heaps_copy[i]-=j
            num=max_val(heaps_copy)
            min_num=min(min_num, num)
    return min_num

def best_move(heaps):
    max_num=float('-inf')
    new_heap=-1
    best_num_removed=-1

    for i in range(len(heaps)):
        for j in range(1, heaps[i] + 1):
            heaps_copy=heaps.copy()
            heaps_copy[i]-=j
            num=min_val(heaps_copy)
            if num>max_num:
                max_num=num
                new_heap=i
                best_num_removed=j

    return new_heap, best_num_removed

def ai_move():
    h_index, num_rmv=best_move(heaps)
    show_result(h_index, num_rmv)

def button_click(h_index):
    if heaps[h_index] > 0:
        no_input=in_put.get()
        if no_input.isdigit():
            num_rmv=int(no_input)
            if num_rmv>0 and num_rmv<=heaps[h_index]:
                show_result(h_index, num_rmv)
            else:
                messagebox.showinfo("Invalid Move", "Please enter a valid number.")
        else:
            messagebox.showinfo("Invalid Move", "Please enter a valid number.")
    else:
        messagebox.showinfo("Invalid Move", "Please select a non-empty heap.")

def reset_game():
    global heaps, player
    heaps=[5, 4, 3]
    player=1
    update_box()

window=tkr.Tk()
window.title("Nim Game")

c_size=tkr.Canvas(window, width=400, height=300)
c_size.pack() 

btn_width=40
btn_height=40
btn_padding=115
btn_colors=["red", "green", "blue"]
buttons=[]

for i in range(len(heaps)):
    x=btn_padding+i*(btn_width+btn_padding*2)
    y=btn_padding
    button=tkr.Button(
        window,
        text=f"Heap {i+1}: {heaps[i]}",
        width=btn_width,
        height=btn_height,
        bg=btn_colors[i],
        command=lambda heap_index=i: button_click(heap_index)
    )
    button.place(x=x, y=y)
    buttons.append(button)

txt = tkr.Label(window,text="Enter the number of stones to remove:")
txt.place(x=btn_padding,y=2*(btn_padding+btn_height))
in_put = tkr.Entry(window,width=btn_width)
in_put.place(x=btn_padding,y=2*(btn_padding+btn_height)+25)

update_box()

window.mainloop()