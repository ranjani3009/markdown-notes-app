import tkinter as tk
from tkinter import filedialog, messagebox
import markdown
import webbrowser
import os

class MarkdownNotesApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Markdown Notes App")
        self.root.geometry("800x600")

        # Text area for markdown
        self.text = tk.Text(root, wrap='word', font=("Arial", 12))
        self.text.pack(side='left', fill='both', expand=True)

        # Menu bar
        menubar = tk.Menu(root)
        file_menu = tk.Menu(menubar, tearoff=0)
        file_menu.add_command(label="Open", command=self.open_file)
        file_menu.add_command(label="Save", command=self.save_file)
        file_menu.add_command(label="Preview", command=self.preview_markdown)
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=root.quit)
        menubar.add_cascade(label="File", menu=file_menu)
        root.config(menu=menubar)

    def open_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("Markdown Files", "*.md")])
        if file_path:
            with open(file_path, "r", encoding="utf-8") as file:
                content = file.read()
                self.text.delete("1.0", tk.END)
                self.text.insert(tk.END, content)

    def save_file(self):
        file_path = filedialog.asksaveasfilename(defaultextension=".md",
                                                 filetypes=[("Markdown Files", "*.md")])
        if file_path:
            with open(file_path, "w", encoding="utf-8") as file:
                file.write(self.text.get("1.0", tk.END))
            messagebox.showinfo("Saved", "File saved successfully!")

    def preview_markdown(self):
        md_content = self.text.get("1.0", tk.END)
        html_content = markdown.markdown(md_content)
        preview_path = os.path.abspath("preview.html")
        with open(preview_path, "w", encoding="utf-8") as file:
            file.write(html_content)
        webbrowser.open(f"file://{preview_path}")

# Run the app
if __name__ == "__main__":
    root = tk.Tk()
    app = MarkdownNotesApp(root)
    root.mainloop()