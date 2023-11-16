import tkinter as tk
from styles import APP_WIDTH, APP_HEIGHT, BACKGROUND_COLOR, TEXT_COLOR


class ToDo(tk.Tk):
    def __init__(self):
        super().__init__()

        # window settings
        self.title("To Do Tkinder")
        self.resizable(False, False)
        self.iconphoto(False, tk.PhotoImage(file="assets/todo_icon.png"))

        # window position (center of screen in this case)
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()

        x_position = (screen_width - 700) // 2
        y_position = (screen_height - 700) // 2

        self.geometry(
            "{}x{}+{}+{}".format(APP_WIDTH, APP_HEIGHT, x_position, y_position)
        )

        container = tk.Frame(self, bg=BACKGROUND_COLOR)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=0)
        container.grid_columnconfigure(0, weight=1)

        # title text on the app
        label_text = "To Do With Tkinder"
        label = tk.Label(container, text=label_text, fg=TEXT_COLOR, bg=BACKGROUND_COLOR)
        label.grid(row=0, column=0, pady=10)

        # text entry for the task
        self.todo_entry = tk.Entry(container)
        self.todo_entry.grid(row=1, column=0, pady=10)

        # buttons container frame
        buttons_container = tk.Frame(container, bg=BACKGROUND_COLOR)
        buttons_container.grid(row=2, column=0)

        # button for adding the task
        add_button = tk.Button(buttons_container, text="Add", command=self.add_task)
        add_button.pack(side="left", padx=5)

        # button for deleting a task
        delete_button = tk.Button(
            buttons_container, text="Delete", command=self.delete_task
        )
        delete_button.pack(side="left", padx=5)

        # button for completing a task
        complete_button = tk.Button(
            buttons_container, text="Complete", command=self.complete_task
        )
        complete_button.pack(side="left", padx=5)

        # todo list view
        self.todo_listbox = tk.Listbox(
            container, selectmode=tk.SINGLE, height=10, width=40
        )
        self.todo_listbox.grid(row=3, column=0, pady=10)

    def add_task(self):
        todo_text = self.todo_entry.get()

        if todo_text:
            self.todo_listbox.insert(tk.END, todo_text)
            self.todo_entry.delete(0, tk.END)

    def delete_task(self):
        selected_index = self.todo_listbox.curselection()

        if selected_index:
            self.todo_listbox.delete(selected_index)

    def complete_task(self):
        selected_index = self.todo_listbox.curselection()

        if selected_index:
            todo_text = self.todo_listbox.get(selected_index)

            self.todo_listbox.delete(selected_index)

            self.todo_listbox.insert(tk.END, "Completed: {}".format(todo_text))


if __name__ == "__main__":
    app = ToDo()
    app.mainloop()
