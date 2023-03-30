import tkinter as tk


def put_num(num):
    n=o_win.get()
    xvc=len(n)
    o_win.insert(xvc+1,str(num))

def adder():
    payload1=o_win.get()
    global f_1
    f_1 = float(payload1)
    o_win.delete(first=0,last=len(o_win.get()))
    global has_been_called1, has_been_called2
    has_been_called1=True
    has_been_called2=False
    has_been_called3=False
    has_been_called4=False
    print(f_1)

def subber():
    payload2=o_win.get()
    global f_2
    f_2 = float(payload2)
    o_win.delete(first=0,last=len(o_win.get()))
    global has_been_called1, has_been_called2
    has_been_called1=False
    has_been_called2=True
    has_been_called3=False
    has_been_called4=False
    print(f_2)

def multy():
    payload1=o_win.get()
    global f_3
    f_3 = float(payload1)
    o_win.delete(first=0,last=len(o_win.get()))
    global has_been_called1, has_been_called2, has_been_called3
    has_been_called1=False
    has_been_called2=False
    has_been_called3=True
    has_been_called4=False
    print(f_3)

def dev():
    payload1=o_win.get()
    global f_4
    f_4 = float(payload1)
    o_win.delete(first=0,last=len(o_win.get()))
    global has_been_called1, has_been_called2, has_been_called3, has_been_called4
    has_been_called1=False
    has_been_called2=False
    has_been_called3=False
    has_been_called4=True
    print(f_4)

def b_clear():
    o_win.delete(first=0,last=len(o_win.get()))
    f_1=''
    f_2=''
    f_3=''
    f_4=''
    has_been_called1=False
    has_been_called2=False
    has_been_called3=False
    has_been_called4=False

def b_clear2():
    has_been_called1=False
    has_been_called2=False
    has_been_called3=False
    has_been_called4=False

def eval():
    if(has_been_called1):
        p=o_win.get()
        o_win.delete(first=0,last=len(o_win.get()))
        res1=float(f_1)+float(p)
        o_win.insert(0,float(res1))
        
    elif(has_been_called2): 
        p=o_win.get()
        o_win.delete(first=0,last=len(o_win.get()))
        res2=float(f_2)-float(p)
        o_win.insert(0,float(res2))

    elif(has_been_called3): 
        p=o_win.get()
        o_win.delete(first=0,last=len(o_win.get()))
        res3=float(f_3)*float(p)
        o_win.insert(0,float(res3))

    elif(has_been_called4): 
        p=o_win.get()
        o_win.delete(first=0,last=len(o_win.get()))
        res4=float(f_4)/float(p)
        o_win.insert(0,float(res4))
    
    else:
        p=o_win.get()
        o_win.insert(0,p)
    
gui=tk.Tk()
gui.title('calco')
gui.geometry("255x400")
gui.resizable(0,0)
o_win=tk.Entry(gui,font=('arial', '14'),width=100)
o_win.pack()


b0=tk.Button(gui,text='0',font=('arial 18'),width=11,height=1,command=lambda: put_num(0))
b0.place(x=5,y=350)

b1=tk.Button(gui,text='1',font=('arial 18'),width=3,height=2,command=lambda: put_num(1))
b1.place(x=5,y=270)

b2=tk.Button(gui,text='2',font=('arial 18'),width=3,height=2,command=lambda: put_num(2))
b2.place(x=60,y=270)

b3=tk.Button(gui,text='3',font=('arial 18'),width=3,height=2,command=lambda: put_num(3))
b3.place(x=117,y=270)

b4=tk.Button(gui,text='4',font=('arial 18'),width=3,height=2,command=lambda: put_num(4))
b4.place(x=5,y=193)

b5=tk.Button(gui,text='5',font=('arial 18'),width=3,height=2,command=lambda: put_num(5))
b5.place(x=60,y=193)

b6=tk.Button(gui,text='6',font=('arial 18'),width=3,height=2,command=lambda: put_num(6))
b6.place(x=117,y=193)

b7=tk.Button(gui,text='7',font=('arial 18'),width=3,height=2,command=lambda: put_num(7))
b7.place(x=5,y=116)

b8=tk.Button(gui,text='8',font=('arial 18'),width=3,height=2,command=lambda: put_num(8))
b8.place(x=60,y=116)

b9=tk.Button(gui,text='9',font=('arial 18'),width=3,height=2,command=lambda: put_num(9))
b9.place(x=117,y=116)


#---------------------------------------------------------------------------------------


beq=tk.Button(gui,text='=',font=('arial 18'),width=5,height=1,command=eval)
beq.place(x=172,y=350)

bp=tk.Button(gui,text='+',font=('arial 18'),width=5,height=2,command=adder)
bp.place(x=173,y=270)

bm=tk.Button(gui,text='-',font=('arial 18'),width=5,height=2,command=subber)
bm.place(x=173,y=193)

bx=tk.Button(gui,text='x',font=('arial 18'),width=5,height=2,command=multy)
bx.place(x=173,y=116)

bd=tk.Button(gui,text='/',font=('arial 18'),width=5,height=1,command=dev)
bd.place(x=172,y=67)

bc=tk.Button(gui,text='clear',font=('arial 18'),width=11,height=1,command=b_clear)
bc.place(x=5,y=67)


#---------------------------------------------------------------------------------------

gui.mainloop()