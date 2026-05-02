# Name: Ariana Fafach
# Date: 5/1/2026
# Title: Program #4: Use PhoneBook database



import sqlite3
import tkinter
import tkinter.messagebox

class UsePhoneBookdbGUI:
    def __init__ (self):
        # Create and name the main window:
        self.main_window = tkinter.Tk()
        self.main_window.title("Use Phonebook")

        # Create and pack three frames:
        self.frame1 = tkinter.Frame(self.main_window)
        self.frame2 = tkinter.Frame(self.main_window)
        self.frame3 = tkinter.Frame(self.main_window)
        self.frame1.pack()
        self.frame2.pack()
        self.frame3.pack()

        # Creat and pack a label:
        self.label1 = tkinter.Label(self.frame1, text = "What would you like to do?")
        self.label1.pack()

        # Create and set a variable for the radiobuttons:
        self.radio_var = tkinter.IntVar()
        self.radio_var.set(1)

        # Create and pack three radiobuttons:
        self.readbutton = tkinter.Radiobutton(self.frame2, text = "Read Phone Book Database", variable = self.radio_var, value = 1)
        self.updatebutton = tkinter.Radiobutton(self.frame2, text = "Update Phone Book Database", variable = self.radio_var, value = 2)
        self.deletebutton = tkinter.Radiobutton(self.frame2, text = "Delete rows from Phone Book Database", variable = self.radio_var, value = 3)
        self.readbutton.pack()
        self.updatebutton.pack()
        self.deletebutton.pack()

        # Create and pack a 'go' and a quit button:
        self.go_button = tkinter.Button(self.frame3, text = "Go", command = self.do_stuff)
        self.quit_button = tkinter.Button(self.frame3, text = "Quit", command = self.main_window.destroy)

        self.go_button.pack(side = 'left')
        self.quit_button.pack(side = 'right')

        tkinter.mainloop()

    def do_stuff(self):
    
        if self.radio_var.get() == 1:
            # Create new window to display the information
            new_window = tkinter.Toplevel()
            # Name the new window:
            new_window.title('Phone Book Information')
            # Create a textbox and put it into the new window:
            text_box = tkinter.Text(new_window)

            # Connect to the phone book database:
            conn = sqlite3.connect('phone_book.db')

            # Create a cursor
            cur = conn.cursor()

            # Get all the data from the Entries table:
            cur.execute('SELECT * FROM Entries')
            information = cur.fetchall()

            # Display the information in the textbox:
            for row in information:
                text_box.insert(tkinter.END, str(row) + "\n")
            text_box.config(state = "disabled")

            text_box.pack()
            
            # Close the connection:
            conn.close()


        elif self.radio_var.get() == 2:
            # Create new window to update the information
            new_window = tkinter.Toplevel()
            # Name the new window:
            new_window.title('Update Phone Book Information')
            
            # Give the user instructions:
            label1 = tkinter.Label(new_window, text ="Which entry would you like to update?")
            # Pack the instructions:
            label1.pack()
            # Create a listbox and make it so the user can only select one option:
            listbox = tkinter.Listbox(new_window, selectmode = tkinter.SINGLE)

            # Connect to the database:
            conn = sqlite3.connect('phone_book.db')
            # Create a cursor:
            cur = conn.cursor()

            # Function to put the values into the listbox:
            def load_listbox():
                # Reset the listbox widget:
                listbox.delete(0, tkinter.END)
                # Get everything from the Entries table:
                cur.execute("SELECT * FROM Entries")
                information = cur.fetchall()
                # Enter each row into the listbox widget:
                for row in information:
                    listbox.insert(tkinter.END, (row[0], row[1], row[2]))
                # Pack the listbox:
                listbox.pack(ipadx = 50)
            load_listbox()

            # Function to populate the entry widget with the selected item:
            def on_select(event):
                selection = listbox.curselection()
                index = selection[0]
                # Find wich item the user selected:
                value = listbox.get(index)
                # Put the name into the top entry widget:
                name_entry.delete(0, tkinter.END)
                name_entry.insert(0, value[1])
                # Put the phone number into the bottom entry widget:
                phone_entry.delete(0, tkinter.END)
                phone_entry.insert(0, value[2])
               
            listbox.bind('<<ListboxSelect>>', on_select)

            # Create and pack the entry widgets:
            name_entry = tkinter.Entry(new_window)
            name_entry.pack(pady = 5, padx = 10, fill = tkinter.X)
            phone_entry = tkinter.Entry(new_window)
            phone_entry.pack(pady = 5, padx = 10, fill = tkinter.X)

            # Function gets what the user changed and calles the save_to_db function:
            def save_entered():
                # Get what the user changed:
                entered_name = name_entry.get()
                entered_phone = phone_entry.get()
                # Pass them to the function that will save them to the database:
                save_to_db(entered_name, entered_phone)
                # Reload the listbox:
                load_listbox()

            # Function saves the changes to the database:
            def save_to_db(name, phone_number):
                conn = sqlite3.connect('phone_book.db')
                cursor = conn.cursor()
                selection = listbox.curselection()
                index = selection[0]
                value = listbox.get(index)
                db_id = value[0]

                cursor.execute("UPDATE Entries SET name = ?, phone_number = ? WHERE id = ?", (name, phone_number, db_id))
                conn.commit()
                tkinter.messagebox.showinfo("Success!", f"Item {name}, {phone_number} saved to database.")
    
                conn.close()   

            # Create and pack the save and quit buttons:
            save_button = tkinter.Button(new_window, text="Save", command = save_entered)
            save_button.pack(pady=10)
            quit_button = tkinter.Button(new_window, text = "Quit", command = new_window.destroy)
            quit_button.pack()


        elif self.radio_var.get() == 3:
            # Create and name a new window:
            delete_window = tkinter.Toplevel()
            delete_window.title("Delete Information")

            # Create and pack three frames:
            frame1 = tkinter.Frame(delete_window)
            frame2 = tkinter.Frame(delete_window)
            frame3 = tkinter.Frame(delete_window)
            frame1.pack()
            frame2.pack()
            frame3.pack()

            # Create and pack the label:
            label = tkinter.Label(frame1, text = "Which entry would you like to delete?")
            label.pack()

            # Create and pack a listbox with padding:
            listbox = tkinter.Listbox(frame2, selectmode = tkinter.SINGLE)
            listbox.pack(padx = 5, pady = 5, ipady = 10)

            # Connect to the database:
            conn = sqlite3.connect('phone_book.db')
            # Create a cursor:
            cur = conn.cursor()

            def load_listbox():
                # Reset the listbox widget:
                listbox.delete(0, tkinter.END)
                # Get everything from the Entries table:
                cur.execute("SELECT * FROM Entries")
                information = cur.fetchall()
                # Enter each row into the listbox widget:
                for row in information:
                    listbox.insert(tkinter.END, (row[0], row[1], row[2]))
                # Pack the listbox:
                listbox.pack(ipadx = 50)
            load_listbox()

            def delete():
                selection = listbox.curselection()
                index = selection[0]
                selected_value = listbox.get(index)
                db_id = selected_value[0]

                cur.execute("DELETE FROM Entries WHERE id = ?", (db_id,))
                conn.commit()
                load_listbox()
            
            delete_button = tkinter.Button(frame3, text = 'Delete', command = delete)
            delete_button.pack()
            quit_button = tkinter.Button (frame3, text = "Quit", command = delete_window.destroy)
            quit_button.pack()
                

if __name__ == '__main__':
    mygui = UsePhoneBookdbGUI()
