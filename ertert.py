import pickle  # 存放数据的模块
import tkinter as tk
import tkinter.messagebox

window = tk.Tk()
window.title("注册登陆页面")
window.geometry("500x400")

canvas = tk.Canvas(window, height=300, width=500)
#image_file = tk.PhotoImage(file="welcome.gif")
#image = canvas.create_image(0, 0, anchor='nw', image=image_file)
canvas.pack(side='top')

tk.Label(window, text='User name:').place(x=50, y=200)
tk.Label(window, text='Password:').place(x=50, y=250)

var_usr_name = tk.StringVar()
var_usr_name.set('请输入用户名')

var_usr_pwd = tk.StringVar()
#var_usr_pwd.set('请输入密码')

entry_usr_name = tk.Entry(window, textvariable=var_usr_name)
entry_usr_name.place(x=160, y=200)
entry_usr_pwd = tk.Entry(window, textvariable=var_usr_pwd, show='*')
entry_usr_pwd.place(x=160, y=250)


def usr_login():
    usr_name = var_usr_name.get()
    usr_pwd = var_usr_pwd.get()

    try:
        with open("usrs_info.pickle", "rb") as usr_file:  # 注意这个地方用到了pickle可以百度一下使用方法
            usrs_info = pickle.load(usr_file)
    except FileNotFoundError:
        with open("usrs_info.pickle", "wb") as usr_file:  # with open with语句可以自动关闭资源
            usrs_info = {"admin": "admin"}  # 以字典的形式保存账户和密码
            pickle.dump(usrs_info, usr_file)

    if usr_name in usrs_info:
        if usr_pwd == usrs_info[usr_name]:
            tk.messagebox.showinfo(
                title="Welcome", message="How are you! " + usr_name)
        else:
            tk.messagebox.showerror(
                message="Error,your password is wrong,try again")
    else:
        is_sign_up = tk.messagebox.askyesno(
            "Welcome", "You have not signed up yet.Sign up today?")
        if is_sign_up:
            usr_sign_up()


def usr_sign_up():
    def sign_to_Python():
        signpwd = sign_pwd.get()
        signpwdconfirm = sign_pwd_confirm.get()
        signname = sign_name.get()
        with open("usrs_info.pickle", "ab") as usr_file:
            exist_usr_info = pickle.load(usr_file)
        if signpwd != signpwdconfirm:
            tk.messagebox.showerror(
                "Error", "Password and confirm password must be the same!")
        elif signname in exist_usr_info:
            tk.messagebox.showerror(
                "Error", "The user has already signed up! ")
        else:
            exist_usr_info[signname] = signpwd
            with open("usrs_info.pickle", "ab") as usr_file:
                pickle.dump(exist_usr_info, usr_file)

            tk.messagebox.showinfo(
                "Welcome", "You have successfully signed up!")
            # close window
            window_sign_up.destroy()

    window_sign_up = tk.Toplevel(window)
    window_sign_up.geometry("350x200")
    window_sign_up.title("注册页面")

    sign_name = tk.StringVar()
    sign_name.set('请输入用户名')
    tk.Label(window_sign_up, text="User name:").place(x=10, y=10)
    entry_new_name = tk.Entry(window_sign_up, textvariable=sign_name)
    entry_new_name.place(x=150, y=10)

    sign_pwd = tk.StringVar()
    tk.Label(window_sign_up, text="Password:").place(x=10, y=50)
    entry_usr_pwd = tk.Entry(window_sign_up, textvariable=sign_pwd, show='*')
    entry_usr_pwd.place(x=150, y=50)

    sign_pwd_confirm = tk.StringVar()
    tk.Label(window_sign_up, text="Confirm password:").place(x=10, y=90)
    entry_usr_pwd_confirm = tk.Entry(
        window_sign_up, textvariable=sign_pwd_confirm, show='*')
    entry_usr_pwd_confirm.place(x=150, y=90)

    btn_confirm_sign_up = tk.Button(
        window_sign_up, text="Sign up", command=sign_to_Python)
    btn_confirm_sign_up.place(x=150, y=130)


# login and sign up
btn_login = tk.Button(window, text="Login", command=usr_login)
btn_login.place(x=155, y=300)

btn_sign_up = tk.Button(window, text="Sign up", command=usr_sign_up)
btn_sign_up.place(x=270, y=300)

window.mainloop()

