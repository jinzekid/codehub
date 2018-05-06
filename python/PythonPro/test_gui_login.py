from tkinter import *
def reg():
    s1 = e1.get()
    s2 = e2.get()
    t1 = len(s1)
    t2 = len(s2)
    if s1 == '111' and s2 == '111':
        c['text'] = '登录成功'
    else:
        c['text'] = '用户名或密码错误'
        e1.delete(0, t1)
        e2.delete(0, t2)

root = Tk()

l = Label(root,text = "用户名:") #创建一个Label标签
l.grid(row = 0,column = 0,sticky = W) #布局

e1 = Entry(root) #创建一个输入框
e1.grid(row = 0, column = 1,sticky = E)

l2 = Label(root,text="密码:")
l2.grid(row = 1 , column = 0,sticky = W )

e2 = Entry(root)
e2['show'] = '*' #密码用 show = '*' 就可以隐藏了
e2.grid(row = 1, column = 1,sticky = E)

b = Button(root,text="登陆",command = reg ) #按钮 等于reg 方法
b.grid(row = 2,column = 1,sticky = E)

#显示登陆内容
c = Label(root,text='')
c.grid(row = 3)
root.mainloop()



