from tkinter import * 
import backend

# Common style funcition
def apply_common_style(windows, widget_class, **style_options):
    for widget in windows.winfo_children():
        if isinstance(widget, widget_class):
            widget.configure(**style_options)

# Add items
def add_entry_command():
    if title_text.get() and author_text.get() and year_text.get() and isbn_text.get():
        # Check if the entry already exists in the database
        existing_items = backend.search_bookstore(title_text.get(), author_text.get(), year_text.get(), isbn_text.get())
        if existing_items:
            list_box.delete(0, END)
            list_box.insert(END, "Sorry this item is already exits. Please enter a new one!")
        else:
            backend.add_entry(title_text.get(), author_text.get(), year_text.get(), isbn_text.get()) #Add new items
            view_commend()
    else:
        list_box.delete(0, END)
        result = "Please fill in all fields before adding an entry."
        list_box.insert(END, result)

# Show item in list box
def view_commend():
    list_box.delete(0, END)
    for row in backend.fatch_bookstore():
        item_formating = f"  {row[0]}. Title: {row[1]}, Author: {row[2]}, Year: {row[3]}, ISBN: {row[4]} "
        list_box.insert(END, item_formating)

# Search Command
def search_command():
    list_box.delete(0, END)
    result = backend.search_bookstore(title_text.get(), author_text.get(), year_text.get(), isbn_text.get())
    if result:
        for row in result:
            item_formating = f"  {row[0]}. Title: {row[1]}, Author: {row[2]}, Year: {row[3]}, ISBN: {row[4]}"
            list_box.insert(END, item_formating)
    else:
        no_result = "Sorry, No Book found! Please try with Correct info."
        list_box.insert(END, no_result)
    

# Delet a Book
def delete_book():
    try:
        # Get the index of the selected item in the Listbox
        index = list_box.curselection()[0]

        # # Get the text of the selected item (e.g., "ID, Title: title. Author: author, Year: year, ISBN: isbn")
        # selected_text = list_box.get(index)
        # # Extract the ID from the selected item text
        # selected_str = (selected_text.split('.')[0].strip())
        # selected_id = int(selected_str)
        # # Delete the item from the database using the extracted ID
        # backend.delete_item(selected_id)

        # Remove the item from the Listbox
        list_box.delete(index)

    except IndexError:
        pass

# Create the Window interface
windows = Tk()
windows.title("Book Store") #Title

# Create the Labels
title = Label(windows, text="Title")
title.grid(row=1, column=0, padx=5, pady=5)

year = Label(windows, text="Year")
year.grid(row=2, column=0, padx=5, pady=5)

author = Label(windows, text="Author")
author.grid(row=1, column=2, padx=5, pady=5)

isbn = Label(windows, text="ISBN")
isbn.grid(row=2, column=2, padx=5, pady=5)

# Create the input boxes
title_text = StringVar()
title_entry = Entry(windows, textvariable=title_text)
title_entry.grid(row=1, column=1, padx=5, pady=5)

year_text = StringVar()
year_entry = Entry(windows, textvariable=year_text)
year_entry.grid(row=2, column=1, padx=5, pady=5)

author_text = StringVar()
author_entry = Entry(windows, textvariable=author_text)
author_entry.grid(row=1, column=3, padx=5, pady=5)

isbn_text = StringVar()
isbn_entry = Entry(windows, textvariable=isbn_text)
isbn_entry.grid(row=2, column=3, padx=5, pady=5)

# Create List Box
list_box = Listbox(windows, height=15, width=55, font=("Arial", 14), bd=5, relief="sunken", highlightthickness=0, bg="lightblue")
list_box.grid(row=3, column=0, rowspan=9, columnspan=4, padx=(10, 10), pady=(10, 10))

# Scrollbar
scroll_bar = Scrollbar(windows)
scroll_bar.grid(row=3, column=4,rowspan=7, padx=(0, 15), pady=(10, 0), sticky="ns")

scroll_bar_x = Scrollbar(windows, orient="horizontal")
scroll_bar_x.grid(row=12, column=0, columnspan=4,padx=10, pady=(0, 10), sticky="ew")

#Configure listbox with scroll bars
list_box.configure(yscrollcommand=scroll_bar.set, xscrollcommand=scroll_bar_x.set)
scroll_bar.configure(command=list_box.yview)
scroll_bar_x.configure(command=list_box.xview)

# Action buttons
view_all = Button(windows, text="View All", command=view_commend)
view_all.grid(row=3, column=5, padx=10, pady=(10, 2))

search_entry = Button(windows, text="Search Entry", command=search_command)
search_entry.grid(row=4, column=5, padx=10, pady=2)

add_entry = Button(windows, text="Add Entry", command=add_entry_command)
add_entry.grid(row=5, column=5, padx=10, pady=2)

update = Button(windows, text="Update Selected")
update.grid(row=6, column=5, padx=10, pady=2)

delete_entry = Button(windows, text="Delete Selected",command=delete_book)
delete_entry.grid(row=7, column=5, padx=10, pady=2)

close_window = Button(windows, text="Close", command=windows.destroy)
close_window.grid(row=8, column=5, padx=10, pady=(2, 15))

# Apply common style to the widgets
apply_common_style(windows, Entry, font=("Arial", 14), bd=5, relief="sunken", highlightthickness=0)
apply_common_style(windows, Label, font=("Arial", 12, "bold"), padx=5, pady=10)
apply_common_style(windows, Button, font=("Helvetica", 12, "bold"), bg="LightSteelBlue", padx=10, pady=10, width=15, bd=2, relief="groove", highlightthickness=0)



# Run the Tkinter windwo
windows.mainloop()