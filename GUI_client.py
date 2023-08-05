import sys
from socket import AF_INET, socket, SOCK_STREAM
from threading import Thread
import tkinter
import socket
import random
from threading import Thread
from work_files.dark_title_bar import *
import tkinter as tk
from tkinter import *
from tkinter import ttk
import os
import shutil
import json
from PIL import ImageTk as IT
from PIL import Image


sub_win_r = Tk()

sub_win_r.geometry("800x600")
sub_win_r.title("Port registration")
sub_win_r.configure(bg="#212121")

canvas = Canvas(
    sub_win_r,
    bg="#212121",
    height=600,
    width=800,
    bd=0,
    highlightthickness=0,
    relief="ridge"
)
canvas.place(x=0, y=0)

entry_image_1 = PhotoImage(
    file="work_files/entry_host.png")
entry_bg_1 = canvas.create_image(
    402.5,
    395.5,
    image=entry_image_1
)
entry_1 = Entry(
    bd=0,
    bg="#616161",
    fg="#000716",
    highlightthickness=0
)
entry_1.place(
    x=318.0,
    y=382.0,
    width=165.0,
    height=30.0
)

entry_image_2 = PhotoImage(
    file="work_files/entry_port.png")
entry_bg_2 = canvas.create_image(
    402.5,
    473.5,
    image=entry_image_2
)
entry_2 = Entry(
    bd=0,
    bg="#616161",
    fg="#000716",
    highlightthickness=0
)
entry_2.place(
    x=318.0,
    y=460.0,
    width=165.0,
    height=30.0
)

image_image_1 = PhotoImage(
    file="work_files/image_logo.png")
image_1 = canvas.create_image(
    405.0,
    229.0,
    image=image_image_1
)

canvas.create_text(
    336.0,
    350.0,
    anchor="nw",
    text="Enter HOST:",
    fill="#9E9E9E",
    font=("NTR", 24 * -1)
)

canvas.create_text(
    336.0,
    428.0,
    anchor="nw",
    text="Enter PORT:",
    fill="#9E9E9E",
    font=("NTR", 24 * -1)
)

canvas.create_text(
    250.0,
    14.0,
    anchor="nw",
    text="C-Chat",
    fill="#BDBDBD",
    font=("NTR", 96 * -1)
)

canvas.create_text(
    308.0,
    524.0,
    anchor="nw",
    text="Press Enter",
    fill="#BDBDBD",
    font=("NTR", 36 * -1)
)
sub_win_r.resizable(False, False)
dark_title_bar(sub_win_r)

file_road = None
catalog = None


def up_select_win():

    global file_road
    global catalog
    catalog = os.getcwd()

    def backer():
        global catalog
        global work_files
        global work_folder
        global work_dirs
        catalog = os.path.dirname(catalog)

        for dirs, folder, files in os.walk(catalog):
            work_dirs = dirs
            work_folder = folder
            work_files = files
            break
        list_var.delete(0, END)

        for new_files in work_files:
            list_var.insert(tk.END, new_files)

        for new_folders in work_folder:
            list_var.insert(tk.END, new_folders)

        about_folder.delete(0, END)
        about_folder.insert(END, catalog)
        about_folder.xview_moveto(1)

    def new_iteration(event):

        global work_files
        global work_folder
        global work_dirs
        global catalog

        w = list_var.curselection()
        y = None

        if len(w) > 0:
            y = list_var.curselection()[0]

        if y is not None:

            for dirs, folder, files in os.walk(catalog):
                work_dirs = dirs
                work_folder = folder
                work_files = files
                break

            if list_var.get(y) not in work_files:

                if catalog[-1] != "\\":
                    catalog = catalog + "\\" + list_var.get(y)

                else:
                    catalog = catalog + list_var.get(y)

                for dirs, folder, files in os.walk(catalog):
                    work_dirs = dirs
                    work_folder = folder
                    work_files = files
                    break
                list_var.delete(0, END)

                for new_files in work_files:
                    list_var.insert(tk.END, new_files)

                for new_folders in work_folder:
                    list_var.insert(tk.END, new_folders)

                about_folder.delete(0, END)
                about_folder.insert(END, catalog)
                about_folder.xview_moveto(1)

    def work_please(file_name_var, file_road_var):
        file_road_var = file_road_var.split("\\")
        bang = r'\''
        bang = bang[0]
        file_road_var = bang.join(file_road_var)
        print(file_road_var)
        file_size = (os.stat(file_road_var)).st_size
        full_size = file_size // 1024
        other_size = file_size - (full_size * 1024)

        dialog_window.insert(END, name + ": " + file_name_var)
        dialog_window.yview_moveto(1)

        if person not in groups:

            s.send(bytes(str(full_size) + "/file_name" + str(other_size) + "/file_name" + file_name_var
                         + "/file_name" + str(name), "utf8"))

            if os.path.exists("story\\" + str(name) + " " + str(person) + ".txt") is False:

                file = open("story\\" + str(name) + " " + str(person) + ".txt", "w")
                file.write(str(name) + ": " + file_name_var)
                file.close()

            else:

                file = open("story\\" + str(name) + " " + str(person) + ".txt", "a")
                file.write("\n" + str(name) + ": " + file_name_var)
                file.close()

        else:

            s.send(bytes(str(full_size) + "/file_group" + str(other_size) + "/file_group" + file_name_var
                         + "/file_group" + str(name) + "/file_group" + str(person), "utf8"))

            if os.path.exists("groups\\" + str(person) + ".txt") is False:

                file = open("groups\\" + str(person) + ".txt", "w")
                file.write(str(name) + ": " + file_name_var)
                file.close()

            else:

                file = open("groups\\" + str(person) + ".txt", "a")
                file.write("\n" + str(name) + ": " + file_name_var)
                file.close()

        f = open(file_road_var, "rb")
        l = f.read(1024)

        while (l):

            s.send(l)
            l = f.read(1024)

        f.close()

    def select():
        global file_road

        file_road = None
        cv = list_var.curselection()

        if len(cv) > 0:
            file_road = list_var.get(cv[0])
            file_name = file_road

            if work_dirs[-1] != "\\":
                file_road = work_dirs + "\\" + file_road

            else:
                file_road = work_dirs + file_road

            work_please(file_name, file_road)
            win.destroy()

    work_files = None
    work_folder = None
    work_dirs = None

    win = Toplevel()
    win.title("Searcher")
    win.geometry("800x600")
    win.resizable(False, False)
    dark_title_bar(win)
    win["bg"] = "#212121"

    sb = ttk.Scrollbar(win, orient='vertical')

    style = ttk.Style()
    style.theme_use('classic')
    style.configure("Vertical.TScrollbar", background="#3A3A3A", troughcolor="#2F2F38", activebackground="red")

    list_var = tk.Listbox(win, bg="#2F2F38", fg="#C1C1C1", font=("Rajdhani Regular", 20 * -1),
                          selectbackground="#77B5FE", selectmode=SINGLE, borderwidth=5, highlightthickness=5,
                          height=22, width=40, relief=GROOVE, bd=0, highlightbackground="#3A3A3A",
                          highlightcolor="#3A3A3A", yscrollcommand=sb.set)

    sb.config(command=list_var.yview)
    image_back = IT.PhotoImage(file="work_files/back_button.png")
    image_select = IT.PhotoImage(file="work_files/select_button.png")

    tk.Button(win, image=image_back, command=backer, relief='flat',
                    bg="#3A3A3A", activebackground="#212121").place(x=330, y=538)

    tk.Button(win, image=image_select, command=select, relief='flat',
                    bg="#3A3A3A", activebackground="#212121").place(x=582, y=538)

    catalog = os.getcwd()

    for dirs, folder, files in os.walk(catalog):
        work_dirs = dirs
        work_folder = folder
        work_files = files
        break

    for new_files in work_files:
        list_var.insert(tk.END, new_files)

    for new_folders in work_folder:
        list_var.insert(tk.END, new_folders)

    list_var.place(x=330, y=0)

    sb.place(x=780, y=0, height=538)

    c = Canvas(win, width=29, height=56, bg="#2F2F38", bd=0, relief='ridge')
    c.config(highlightbackground="#2F2F38", highlightthickness=3)
    c.place(x=548, y=538)
    list_var.bind("<Double-Button-1>", new_iteration)
    sb_x = ttk.Scrollbar(win, orient='horizontal')
    about_folder = Listbox(win, height=1, width=35, bg="#2F2F38", bd=0, font=("NTR", 15 * -1), fg="#77B5FE",
                           xscrollcommand=sb_x.set, highlightbackground="#3A3A3A", highlightcolor="#3A3A3A")
    about_folder.place(x=23, y=260)
    sb_x.place(x=21, y=280, width=284)
    sb_x.config(command=about_folder.xview)
    about_folder.insert(END, catalog)
    about_folder.xview_moveto(1)
    win.mainloop()

    return file_road


def host_port_e(event):
    host_port()


def host_port():
    try:
        HOST = str(entry_1.get())
        PORT = int(entry_2.get())

        data = {
            "SERVER_HOST": HOST,
            "SERVER_PORT": PORT
        }
        with open('config.json', 'w') as outfile:
            json.dump(data, outfile)

        sub_win_r.destroy()

    except Exception as k:
        entry_1.delete(0, END)
        entry_2.delete(0, END)


sub_win_r.bind("<Return>", host_port_e)
sub_win_r.mainloop()

with open('config.json') as f:
    templates = json.load(f)

SERVER_HOST = templates["SERVER_HOST"]
SERVER_PORT = templates["SERVER_PORT"]

s = socket.socket()

try:
    s.connect((SERVER_HOST, SERVER_PORT))
except Exception as e:
    print(e)
    sys.exit()

client_list = []

group_mode = False

msg = s.recv(1024).decode("utf8")

split_msg = msg.split(" ")

time_client_list = split_msg[1].split(",")

person = None

if os.path.exists("story") is False:
    os.mkdir("story")

if os.path.exists("groups") is False:
    os.mkdir("groups")

if os.path.exists("send_files") is False:
    os.mkdir("send_files")

if os.path.exists("sent") is False:
    os.mkdir("sent")

groups = []


def receive():
    global client_list

    Ben = True
    full_number = None
    other_number = None
    f = None

    while True:

        try:
            if Ben is True:

                msg = s.recv(1024).decode("utf8")
                print(msg)

                if "/new_client_list " in msg:
                    split_msg = msg.split(" ")
                    client_list = split_msg[1].split(",")
                    person_list.delete(0, END)

                    if name in client_list:
                        client_list.remove(str(name))

                    for i in client_list:
                        person_list.insert(0, i)

                elif "/create_new_group " in msg:
                    msg = msg.split(" ")[1]
                    msg = msg.split(",")
                    name_of_group = msg.pop(0)
                    file_group = open("groups\\" + name_of_group + ".txt", "w")
                    file_group.write(",".join(msg))
                    file_group.close()
                    groups.append(name_of_group)
                    person_list.insert(0, name_of_group)

                elif "mes_group" in msg:
                    msg = msg.split("mes_group")
                    work_group = msg[0]
                    msg = msg[1]
                    file_group = open("groups\\" + work_group + ".txt", "a")
                    file_group.write("\n" + msg)
                    file_group.close()
                    if work_group == person:
                        dialog_window.insert(END, msg)
                        dialog_window.yview_moveto(1)

                elif "/abpers" in msg:
                    msg = msg.split("/abpers")[1]
                    msg_from = msg.split(":")[0]

                    if msg_from == person or msg_from == name:
                        dialog_window.insert(END, msg)
                        dialog_window.yview_moveto(1)

                    if msg_from != name and msg_from != person:

                        if os.path.exists("story\\" + str(name) + " " + str(msg_from) + ".txt") is False:
                            file = open("story\\" + str(name) + " " + str(msg_from) + ".txt", "w")
                            file.write(msg)
                            file.close()

                        else:
                            file = open("story\\" + str(name) + " " + str(msg_from) + ".txt", "a")
                            file.write("\n" + msg)
                            file.close()

                    else:
                        if os.path.exists("story\\" + str(name) + " " + str(person) + ".txt") is False:
                            file = open("story\\" + str(name) + " " + str(person) + ".txt", "w")
                            file.write(msg)
                            file.close()

                        else:
                            file = open("story\\" + str(name) + " " + str(person) + ".txt", "a")
                            file.write("\n" + msg)
                            file.close()

                elif "/file_name" in msg:
                    msg = msg.split("/file_name")
                    full_number = int(msg[0])
                    other_number = int(msg[1])
                    file_from = str(msg[3])

                    if file_from == person:
                        dialog_window.insert(END, str(file_from) + ": " + msg[2])
                        dialog_window.yview_moveto(1)

                    if os.path.exists("story\\" + str(name) + " " + str(file_from) + ".txt") is False:

                        file = open("story\\" + str(name) + " " + str(file_from) + ".txt", "w")
                        file.write(str(file_from) + ": " + msg[2])
                        file.close()

                    else:

                        file = open("story\\" + str(name) + " " + str(file_from) + ".txt", "a")
                        file.write("\n" + str(file_from) + ": " + msg[2])
                        file.close()

                    f = open('sent/' + msg[2], 'wb')

                    Ben = False

                elif "/file_group" in msg:

                    msg = msg.split("/file_group")

                    if msg[4] == person:
                        dialog_window.insert(END, msg[3] + ": " + msg[2])
                        dialog_window.yview_moveto(1)

                    f = open('sent/' + msg[2], 'wb')
                    full_number = int(msg[0])
                    other_number = int(msg[1])
                    file_from_name = str(msg[3])
                    file_from_group = str(msg[4])
                    file = open("groups\\" + file_from_group + ".txt", "a")
                    file.write("\n" + str(file_from_name) + ": " + msg[2])
                    file.close()
                    f = open('sent/' + msg[2], 'wb')

                    Ben = False

            else:

                while full_number != 0:

                    msg = s.recv(1024)
                    f.write(msg)
                    full_number -= 1

                if other_number != 0:

                    msg = s.recv(int(other_number))
                    f.write(msg)

                f.close()

                Ben = True

        except OSError:
            break


list_of_group = []


def new_dialog(event):
    global image_user
    global person
    global list_of_group
    global group_mode
    global canvas_person

    if group_mode is False and person_list.get(person_list.curselection()[0]) not in groups and person_list.get(
            person_list.curselection()[0]) != person:

        image_user = IT.PhotoImage(file="work_files/def_user.png")

        b = Label(image=image_user, bg="#212121")
        b.place(x=398, y=1)

        dialog_window.delete(0, END)

        person = person_list.get(person_list.curselection()[0])
        c.itemconfigure(canvas_person, text=person)

        if os.path.exists("story\\" + str(name) + " " + str(person) + ".txt"):

            file = open("story\\" + str(name) + " " + str(person) + ".txt", "r")
            old_string = file.readlines()

            for i in old_string:
                dialog_window.insert(END, i)

            dialog_window.yview_moveto(1)

        def send_e(event):
            send()

        def send():

            mes = entry_send.get()

            if mes is not None and mes != "" and person is not None and person != "":
                s.send(bytes(str(name + "abpers" + mes + "abpers" + person), "utf8"))
                entry_send.delete(0, END)
                dialog_window.yview_moveto(1)

        def send_file():

            s.send(bytes(name + "/talk_person" + person, "utf8"))
            up_select_win()

        main_win.bind("<Return>", send_e)

        tk.Button(main_win, image=image_1_x, command=send,
               relief='flat', bg="#212121", activebackground="#212121").place(x=910, y=680)

        tk.Button(main_win, image=image_2_x, command=send_file,
               relief='flat', bg="#212121", activebackground="#212121").place(x=965, y=680)

        entry_send = Entry(
            bd=0,
            bg="#393944",
            fg="#C1C1C1",
            font=("Rajdhani Regular", 24 * -1),
            highlightthickness=0
        )
        entry_send.place(
            x=400.0,
            y=685.0,
            width=505.0,
            height=35.0
        )

    elif person_list.get(person_list.curselection()[0]) in groups and group_mode is False and person_list.get(
            person_list.curselection()[0]) != person:

        image_user = IT.PhotoImage(file="work_files/def_group.png")
        b = Label(image=image_user, bg="#212121")
        b.place(x=398, y=1)
        dialog_window.delete(0, END)

        person = person_list.get(person_list.curselection()[0])
        c.itemconfigure(canvas_person, text=person)

        file = open("groups\\" + person + ".txt", "r")
        old_string = file.readlines()
        old_string.pop(0)

        for i in old_string:
            dialog_window.insert(END, i)

        def send_e_g(event):
            send_g()

        def send_g():
            mes = entry_send.get()

            if mes is not None and mes != "" and person is not None and person != "":

                with open("groups\\" + person + ".txt", "r") as f:
                    lines = f.readlines()
                    persons = lines[0]
                s.send(bytes(str(person + "mes_group" + persons + "mes_group" + str(name) + ": " + mes), "utf8"))
            entry_send.delete(0, END)
            dialog_window.yview_moveto(1)

        def send_file_group():

            with open("groups\\" + person + ".txt", "r") as f:
                lines = f.readlines()
                persons = lines[0]
            s.send(bytes(name + "/talk_group" + person + "/talk_group" + persons, "utf8"))

            up_select_win()

        main_win.bind("<Return>", send_e_g)

        tk.Button(main_win, image=image_1_x, command=send_g,
               relief='flat', bg="#212121", activebackground="#212121").place(x=910, y=680)

        tk.Button(main_win, image=image_2_x, command=send_file_group,
               relief='flat', bg="#212121", activebackground="#212121").place(x=965, y=680)

        entry_send = Entry(
            bd=0,
            bg="#393944",
            fg="#C1C1C1",
            font=("Rajdhani Regular", 24 * -1),
            highlightthickness=0
        )
        entry_send.place(
            x=400.0,
            y=685.0,
            width=505.0,
            height=35.0
        )

    else:

        if group_mode is True:

            if dialog_window.get(0) != "Your group: ":
                dialog_window.delete(0, END)
                dialog_window.insert(0, "Your group: ")
            group_person = person_list.get(person_list.curselection()[0])

            if group_person not in list_of_group and group_person not in groups:
                list_of_group.append(group_person)
                dialog_window.insert(END, group_person)

            def create_group():
                win_name_group = Toplevel()
                win_name_group.geometry('200x150')
                win_name_group.configure(bg="#212121")
                Label(win_name_group, bg="#212121", text="Enter name of your group: ", fg="#77B5FE").pack()
                group_name = Entry(win_name_group, bg="#616161")
                group_name.pack()

                def create_new_group():
                    global group_mode
                    global list_of_group

                    if group_name.get() not in groups:
                        group_name_var = group_name.get()
                        groups.append(group_name_var)
                        g_file = open("groups\\" + group_name_var + ".txt", "w")
                        g_file.write(name + "," + ",".join(list_of_group))
                        g_file.close()
                        person_list.insert(0, group_name_var)
                        dialog_window.delete(0, END)
                        group_mode = False
                        s.send(
                            bytes(
                                "/create_new_group " + group_name_var + "," + str(name) + "," + ",".join(list_of_group),
                                "utf8"))
                        list_of_group = []
                        btn_send.destroy()
                        win_name_group.destroy()

                tk.Button(win_name_group, text="OK", command=create_new_group, bg="#212121", fg="#77B5FE").pack()
                dark_title_bar(win_name_group)

            if len(list_of_group) >= 2:

                image_create = IT.PhotoImage(file="work_files/create_button.png")
                btn_send = tk.Button(main_win, image=image_create, command=create_group,
                            relief='flat', bg="#3A3A3A", activebackground="#212121")
                btn_send.image = image_create
                btn_send.place(x=1062, y=668)


def new_group():
    global group_mode
    group_mode = True


def sub_close_e(event):
    sub_close()


def sub_close():

    global name
    name = entry.get()

    if name != "" and name not in time_client_list and " " not in name:
        s.send(bytes(name, "utf8"))
        sub_win.destroy()

    elif name in time_client_list:
        xys = tk.Label(sub_win, text="login already exists", bg="#212121", foreground="red")
        xys.place(x=360, y=360)
        xys.destroy()

    elif " " in name or "," in name:
        xyz = tk.Label(sub_win, text="wrong character", bg="#212121", foreground="red")
        xyz.place(x=360, y=380)
        xyz.destroy()


name = None
sub_win = Tk()

sub_win.geometry("800x600")
sub_win.configure(bg="#212121")


canvas = Canvas(
    sub_win,
    bg="#212121",
    height=600,
    width=800,
    bd=0,
    highlightthickness=0,
    relief="ridge"
)

canvas.place(x=0, y=0)
canvas.create_text(
    285.0,
    10.0,
    anchor="nw",
    text="C-Chat",
    fill="#BDBDBD",
    font=("NTR", 64 * -1)
)

canvas.create_text(
    300.0,
    235.0,
    anchor="nw",
    text="Enter your login:",
    fill="#9E9E9E",
    font=("NTR", 32 * -1)
)

entry_image_1 = PhotoImage(
    file="work_files/entry_login.png")
entry_bg_1 = canvas.create_image(
    413.5,
    316.5,
    image=entry_image_1
)
entry = Entry(
    bd=0,
    bg="#616161",
    fg="#000716",
    highlightthickness=0
)
entry.place(
    x=329.0,
    y=300.0,
    width=169.0,
    height=31.0
)

canvas.create_text(
    340.0,
    428.0,
    anchor="nw",
    text="Press Enter",
    fill="#BDBDBD",
    font=("NTR", 28 * -1)
)

image_image_1 = PhotoImage(
    file="work_files/small_logo.png")
image_1 = canvas.create_image(
    523.0,
    39.0,
    image=image_image_1
)

sub_win.resizable(False, False)
dark_title_bar(sub_win)
sub_win.bind("<Return>", sub_close_e)
sub_win.mainloop()

main_win = Tk()
main_win.geometry("500x500")
main_win.title("Chats")

sb = ttk.Scrollbar(main_win, orient='vertical')

style = ttk.Style()
style.theme_use('classic')
style.configure("Vertical.TScrollbar", background="#3A3A3A", troughcolor="#2F2F38", activebackground="red")

image_x = IT.PhotoImage(file="work_files/new.png")
image_1_x = IT.PhotoImage(file="work_files/plane.png")
image_2_x = IT.PhotoImage(file="work_files/x_file.png")
image_user = IT.PhotoImage(file="work_files/def_user.png")

person_list = tk.Listbox(main_win, bg="#2F2F38", fg="#C1C1C1", font=("Rajdhani Regular", 20 * -1),
                          selectbackground="#77B5FE", selectmode=SINGLE, borderwidth=5, highlightthickness=5,
                          height=20, width=15, relief=GROOVE, bd=0, highlightbackground="#3A3A3A",
                          highlightcolor="#3A3A3A", yscrollcommand=sb.set)

person_list.bind("<Double-Button-1>", new_dialog)

sb.config(command=person_list.yview)
sb.place(x=175, y=173, height=490)

person_list.place(x=0, y=173)
dark_title_bar(main_win)
main_win["bg"] = "#212121"


Button(main_win, image=image_x, command=new_group,
       relief='flat', bg="#3A3A3A", activebackground="#212121").place(x=0, y=663)

b = Label(image=image_user, bg="#212121")
b.place(x=398, y=1)

c = Canvas(width=401, height=91, bg="#2F2F38", bd=0, relief='ridge')
c.config(highlightbackground="#3A3A3A", highlightthickness=3)
c.place(x=498, y=3)
canvas_person = c.create_text(200, 50, text="", fill="#C8C8C9", font=('NTR 24'))

sb_2 = ttk.Scrollbar(main_win, orient='vertical')

dialog_window = tk.Listbox(main_win, bg="#2F2F38", fg="#C1C1C1", font=("Rajdhani Regular", 20 * -1),
                          selectbackground="#77B5FE", selectmode=SINGLE, borderwidth=5, highlightthickness=5,
                          height=23, width=43, relief=GROOVE, bd=0, highlightbackground="#3A3A3A",
                          highlightcolor="#3A3A3A", yscrollcommand=sb_2.set)

sb_2.config(command=dialog_window.yview)
sb_2.place(x=885, y=102, height=558)

dialog_window.place(x=400, y=98)


receive_thread = Thread(target=receive)
receive_thread.start()

if name is not None or name != "":
    def user_exit():
        s.send(bytes("/user_exit " + str(name), "utf8"))


    main_win.protocol("WM_EXIT", user_exit)
    main_win.mainloop()

s.close()
