import tkinter as tk
import tkinter.ttk as ttk
import sqlite3


def fetch_data():
    try:
        conn = sqlite3.connect("student_database.db")
        cursor = conn.cursor()

        cursor.execute('''CREATE TABLE IF NOT EXISTS Students (
                            email TEXT,
                            name TEXT,
                            surname TEXT,
                            project REAL,
                            l_1 REAL,
                            l_2 REAL,
                            l_3 REAL,
                            h_1 REAL,
                            h_2 REAL,
                            h_3 REAL,
                            h_4 REAL,
                            h_5 REAL,
                            h_6 REAL,
                            h_7 REAL,
                            h_8 REAL,
                            h_9 REAL,
                            h_10 REAL,
                            grade REAL,
                            status TEXT)
                            ''')

        conn.commit()
        cursor.execute("SELECT * FROM Students")
        res = cursor.fetchall()
        return res
    except sqlite3.Error as e:
        print(f"Error: {e}")
    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()


def show_data():
    data = fetch_data()
    treeview.delete(*treeview.get_children())

    for row in data:
        d = list()
        for i in range(len(row)):
            d.append(row[i])
        treeview.insert("", "end", values=tuple(d))


def open_new_student_window():
    new_window = tk.Toplevel(root, padx=20, pady=20)
    new_window.title("Add new student")

    email_label = ttk.Label(new_window, text="Email:")
    email_label.pack()
    email_entry = ttk.Entry(new_window)
    email_entry.pack()

    name_label = ttk.Label(new_window, text="Name:")
    name_label.pack()
    name_entry = ttk.Entry(new_window)
    name_entry.pack()

    surname_label = ttk.Label(new_window, text="Surname:")
    surname_label.pack()
    surname_entry = ttk.Entry(new_window)
    surname_entry.pack()

    project_label = ttk.Label(new_window, text="Project:")
    project_label.pack()
    project_entry = ttk.Entry(new_window)
    project_entry.pack()

    l1_label = ttk.Label(new_window, text="List 1:")
    l1_label.pack()
    l1_entry = ttk.Entry(new_window)
    l1_entry.pack()

    l2_label = ttk.Label(new_window, text="List 2:")
    l2_label.pack()
    l2_entry = ttk.Entry(new_window)
    l2_entry.pack()

    l3_label = ttk.Label(new_window, text="List 3:")
    l3_label.pack()
    l3_entry = ttk.Entry(new_window)
    l3_entry.pack()

    h1_label = ttk.Label(new_window, text="Homework 1:")
    h1_label.pack()
    h1_entry = ttk.Entry(new_window)
    h1_entry.pack()

    h2_label = ttk.Label(new_window, text="Homework 2:")
    h2_label.pack()
    h2_entry = ttk.Entry(new_window)
    h2_entry.pack()

    h3_label = ttk.Label(new_window, text="Homework 3:")
    h3_label.pack()
    h3_entry = ttk.Entry(new_window)
    h3_entry.pack()

    h4_label = ttk.Label(new_window, text="Homework 4:")
    h4_label.pack()
    h4_entry = ttk.Entry(new_window)
    h4_entry.pack()

    h5_label = ttk.Label(new_window, text="Homework 5:")
    h5_label.pack()
    h5_entry = ttk.Entry(new_window)
    h5_entry.pack()

    h6_label = ttk.Label(new_window, text="Homework 6:")
    h6_label.pack()
    h6_entry = ttk.Entry(new_window)
    h6_entry.pack()

    h7_label = ttk.Label(new_window, text="Homework 7:")
    h7_label.pack()
    h7_entry = ttk.Entry(new_window)
    h7_entry.pack()

    h8_label = ttk.Label(new_window, text="Homework 8:")
    h8_label.pack()
    h8_entry = ttk.Entry(new_window)
    h8_entry.pack()

    h9_label = ttk.Label(new_window, text="Homework 9:")
    h9_label.pack()
    h9_entry = ttk.Entry(new_window)
    h9_entry.pack()

    h10_label = ttk.Label(new_window, text="Homework 10:")
    h10_label.pack()
    h10_entry = ttk.Entry(new_window)
    h10_entry.pack()

    grade_label = ttk.Label(new_window, text="Grade:")
    grade_label.pack()
    grade_entry = ttk.Entry(new_window)
    grade_entry.pack()

    status_label = ttk.Label(new_window, text="Status:")
    status_label.pack()
    status_entry = ttk.Entry(new_window)
    status_entry.pack()

    def add_student():
        try:
            connection = sqlite3.connect("student_database.db")
            cursor = connection.cursor()

            data = list()
            data.append(email_entry.get())
            data.append(name_entry.get())
            data.append(surname_entry.get())
            append_data(data, project_entry.get())
            append_data(data, l1_entry.get())
            append_data(data, l2_entry.get())
            append_data(data, l3_entry.get())
            append_data(data, h1_entry.get())
            append_data(data, h2_entry.get())
            append_data(data, h3_entry.get())
            append_data(data, h4_entry.get())
            append_data(data, h5_entry.get())
            append_data(data, h6_entry.get())
            append_data(data, h7_entry.get())
            append_data(data, h8_entry.get())
            append_data(data, h9_entry.get())
            append_data(data, h10_entry.get())
            append_data(data, grade_entry.get())
            data.append(status_entry.get())

            params = tuple(data)
            sql = "INSERT INTO Students (email, name, surname, project, l_1, l_2, l_3, " \
                  "h_1, h_2, h_3, h_4, h_5, h_6, h_7, h_8, h_9, h_10, grade, status) VALUES " \
                  "(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"

            cursor.execute(sql, params)
            connection.commit()
            show_data()
            new_window.destroy()
        except sqlite3.Error as e:
            print(f"Error: {e}")
        finally:
            if cursor:
                cursor.close()
            if connection:
                connection.close()

    add_button = tk.Button(new_window, text="Add", command=add_student)
    add_button.pack()


def open_details_window(event):
    selected_item = treeview.focus()

    if selected_item:
        item_data = treeview.item(selected_item)
        item_values = item_data["values"]

        details_window = tk.Toplevel(root, padx=10, pady=10)
        details_window.title("Details")

        email_label = ttk.Label(details_window, text="Email:")
        email_label.pack()
        email_entry = ttk.Entry(details_window)
        email_entry.insert(0, item_values[0])
        email_entry.config(state="disabled")
        email_entry.pack()

        name_label = ttk.Label(details_window, text="Name:")
        name_label.pack()
        name_entry = ttk.Entry(details_window)
        name_entry.insert(0, item_values[1])
        name_entry.pack()

        surname_label = ttk.Label(details_window, text="Surname:")
        surname_label.pack()
        surname_entry = ttk.Entry(details_window)
        surname_entry.insert(0, item_values[2])
        surname_entry.pack()

        project_label = ttk.Label(details_window, text="Project:")
        project_label.pack()
        project_entry = ttk.Entry(details_window)
        project_entry.insert(0, item_values[3])
        project_entry.pack()

        l1_label = ttk.Label(details_window, text="List 1:")
        l1_label.pack()
        l1_entry = ttk.Entry(details_window)
        l1_entry.insert(0, item_values[4])
        l1_entry.pack()

        l2_label = ttk.Label(details_window, text="List 2:")
        l2_label.pack()
        l2_entry = ttk.Entry(details_window)
        l2_entry.insert(0, item_values[5])
        l2_entry.pack()

        l3_label = ttk.Label(details_window, text="List 3:")
        l3_label.pack()
        l3_entry = ttk.Entry(details_window)
        l3_entry.insert(0, item_values[6])
        l3_entry.pack()

        h1_label = ttk.Label(details_window, text="Homework 1:")
        h1_label.pack()
        h1_entry = ttk.Entry(details_window)
        h1_entry.insert(0, item_values[7])
        h1_entry.pack()

        h2_label = ttk.Label(details_window, text="Homework 2:")
        h2_label.pack()
        h2_entry = ttk.Entry(details_window)
        h2_entry.insert(0, item_values[8])
        h2_entry.pack()

        h3_label = ttk.Label(details_window, text="Homework 3:")
        h3_label.pack()
        h3_entry = ttk.Entry(details_window)
        h3_entry.insert(0, item_values[9])
        h3_entry.pack()

        h4_label = ttk.Label(details_window, text="Homework 4:")
        h4_label.pack()
        h4_entry = ttk.Entry(details_window)
        h4_entry.insert(0, item_values[10])
        h4_entry.pack()

        h5_label = ttk.Label(details_window, text="Homework 5:")
        h5_label.pack()
        h5_entry = ttk.Entry(details_window)
        h5_entry.insert(0, item_values[11])
        h5_entry.pack()

        h6_label = ttk.Label(details_window, text="Homework 6:")
        h6_label.pack()
        h6_entry = ttk.Entry(details_window)
        h6_entry.insert(0, item_values[12])
        h6_entry.pack()

        h7_label = ttk.Label(details_window, text="Homework 7:")
        h7_label.pack()
        h7_entry = ttk.Entry(details_window)
        h7_entry.insert(0, item_values[13])
        h7_entry.pack()

        h8_label = ttk.Label(details_window, text="Homework 8:")
        h8_label.pack()
        h8_entry = ttk.Entry(details_window)
        h8_entry.insert(0, item_values[14])
        h8_entry.pack()

        h9_label = ttk.Label(details_window, text="Homework 9:")
        h9_label.pack()
        h9_entry = ttk.Entry(details_window)
        h9_entry.insert(0, item_values[15])
        h9_entry.pack()

        h10_label = ttk.Label(details_window, text="Homework 10:")
        h10_label.pack()
        h10_entry = ttk.Entry(details_window)
        h10_entry.insert(0, item_values[16])
        h10_entry.pack()

        grade_label = ttk.Label(details_window, text="Grade:")
        grade_label.pack()
        grade_entry = ttk.Entry(details_window)
        grade_entry.insert(0, item_values[17])
        grade_entry.pack()

        status_label = ttk.Label(details_window, text="Status:")
        status_label.pack()
        status_entry = ttk.Entry(details_window)
        status_entry.insert(0, item_values[18])
        status_entry.pack()

        def delete_student():
            try:
                connection = sqlite3.connect("student_database.db")
                mycursor = connection.cursor()
                params = (email_entry.get(),)
                sql = "DELETE FROM Students WHERE email = ?"
                mycursor.execute(sql, params)
                connection.commit()
                show_data()
                details_window.destroy()
            except sqlite3.Error as e:
                print(f"Error: {e}")
            finally:
                if mycursor:
                    mycursor.close()
                if connection:
                    connection.close()

        def edit_student():
            try:
                connection = sqlite3.connect("student_database.db")
                mycursor = connection.cursor()

                data = list()
                data.append(name_entry.get())
                data.append(surname_entry.get())
                append_data(data, project_entry.get())
                append_data(data, l1_entry.get())
                append_data(data, l2_entry.get())
                append_data(data, l3_entry.get())
                append_data(data, h1_entry.get())
                append_data(data, h2_entry.get())
                append_data(data, h3_entry.get())
                append_data(data, h4_entry.get())
                append_data(data, h5_entry.get())
                append_data(data, h6_entry.get())
                append_data(data, h7_entry.get())
                append_data(data, h8_entry.get())
                append_data(data, h9_entry.get())
                append_data(data, h10_entry.get())
                append_data(data, grade_entry.get())
                data.append(status_entry.get())
                data.append(email_entry.get())

                params = tuple(data)
                sql = "UPDATE Students SET name = ?, surname = ?, project = ?, l_1 = ?, l_2 = ?, l_3 = ?, " \
                  "h_1 = ?, h_2 = ?, h_3 = ?, h_4 = ?, h_5 = ?, h_6 = ?, h_7 = ?, h_8 = ?, h_9 = ?, h_10 = ?, grade = ?, status = ?" \
                  "WHERE email = ?"
                mycursor.execute(sql, params)
                connection.commit()
                show_data()
                details_window.destroy()
            except sqlite3.Error as e:
                print(f"Error: {e}")
            finally:
                if mycursor:
                    mycursor.close()
                if connection:
                    connection.close()

        edit_button = tk.Button(details_window, text="Edit", command=edit_student)
        delete_button = tk.Button(details_window, text="Delete", command=delete_student)
        edit_button.pack()
        delete_button.pack()


def append_data(data, entry):
    if entry == "":
        data.append(-1)
    else:
        data.append(entry)


print(fetch_data())
root = tk.Tk()
root.title("Student database")

treeview = ttk.Treeview(root)
treeview["columns"] = ("email", "name", "surname", "project", "l_1", "l_2", "l_3", "h_1", "h_2", "h_3",
                       "h_4", "h_5", "h_6", "h_7", "h_8", "h_9", "h_10", "grade", "status")
treeview.column("#0", width=0)
treeview.heading("email", text="Email")
treeview.heading("name", text="Name")
treeview.heading("surname", text="Surname")
treeview.heading("project", text="Project")
treeview.heading("l_1", text="List 1")
treeview.heading("l_2", text="List 2")
treeview.heading("l_3", text="List 3")
treeview.heading("h_1", text="Hw 1")
treeview.heading("h_2", text="Hw 2")
treeview.heading("h_3", text="Hw 3")
treeview.heading("h_4", text="Hw 4")
treeview.heading("h_5", text="Hw 5")
treeview.heading("h_6", text="Hw 6")
treeview.heading("h_7", text="Hw 7")
treeview.heading("h_8", text="Hw 8")
treeview.heading("h_9", text="Hw 9")
treeview.heading("h_10", text="Hw 10")
treeview.heading("grade", text="Grade")
treeview.heading("status", text="Status")

for col in treeview["columns"]:
    treeview.column(col, width=80)

treeview.bind("<Double-1>", open_details_window)
treeview.pack()

add_new_student_button = tk.Button(root, text="Add new student", command=open_new_student_window)
add_new_student_button.pack(side="left")

show_data()
root.mainloop()
