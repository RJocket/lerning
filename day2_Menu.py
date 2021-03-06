from tkinter import *
'''
************** 添加顶层菜单 ************
1. 我们可以使用 Menu类来新建一个菜单， Menu和其他的组
件一样，第一个是 parent ，这里通常可以为窗口。
2. 然后我们可以用 add_commmand方法来为它添加菜单项，
如果该菜单是顶层菜单，则添加的菜单项依次向右添加。
如果该菜单时顶层菜单的一个菜单项，则它添加的是下拉	
菜单的菜单项。
3.add_command中的参数常用的有 label 属性，用来指定的
是菜单项的名称， command属性用来指定被点击的时候调用
的方法， acceletor 属性指定的是快捷键， underline 属性
是是否拥有下划线。
3. 最后可以用窗口的 menu属性指定我们使用哪一个作为它
的顶层菜单。
************ 有子菜单的情况 *************
1. 如果有子菜单，则情况稍微复杂点，这个时候，我们需
要使用 add_cascade ， cascade 可以理解为“级联”，即它
的作用只是为了引出后面的菜单。
2.add_cascade 的一个很重要的属性就是 menu属性，它指
明了要把那个菜单级联到该菜单项上，当然，还必不可少
的就是 label 属性，用于指定该菜单项的名称。
3. 我们先新建一个 Menu的实例，然后使用 add_command来
添加菜单项，这样等该菜单建立完毕，我们要把它作为另
一个菜单项的子菜单，就需要使用 add_cascade 方法。
'''	
from tkinter import *
root = Tk()

menubar =Menu(root)	

for item in['File','Edit','Selection','Find','View','Goto','Tools','Project','Preferences','Help']:
	menubar.add_command(label = item)

'''
二级菜单的创建，可先创建子菜单，再创建上级菜单
'''
fmenu = Menu(menubar)
for  item in ['新建文件','打开文件']:
	fmenu.add_command(label =item)

# 插入 分割线
fmenu.add_separator()

fmenu.add_command(label ='关闭文件')

vmenu = Menu(menubar)
for item in ['关于','注册']:
	vmenu.add_command(label = item)

# 绑定 二级菜单
menubar.add_cascade(label = '文件' ,menu = fmenu)
menubar.add_cascade(label = '帮助',menu = vmenu)

root['menu'] = menubar


if __name__ == '__main__':
	root.title("Sublime Text")
	root.geometry("800x600")
	root.mainloop()