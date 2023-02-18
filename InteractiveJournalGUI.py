import tkinter as tk

class JournalApp:
    def __init__(self, master):
        self.prompts = [
            "What were the high points and low points of my week, and what caused them?",
            "What were the things that brought me joy and happiness this week?",
            "What challenges did I face this week, and how did I overcome them?",
            "What did I learn about myself this week?",
            "What goals did I accomplish this week, and what goals did I fall short of?"
        ]
        self.entries = []
        self.prompt_idx = 0

        self.prompt_label = tk.Label(master, text=self.prompts[0])
        self.prompt_label.pack()

        self.response_text = tk.Text(master, height=10, width=50)
        self.response_text.pack()

        self.submit_button = tk.Button(master, text="Submit", command=self.submit_response)
        self.submit_button.pack()

    def submit_response(self):
        response = self.response_text.get("1.0", "end-1c")
        self.entries.append((self.prompts[self.prompt_idx], response))
        self.prompt_idx += 1

        if self.prompt_idx < len(self.prompts):
            self.prompt_label.config(text=self.prompts[self.prompt_idx])
            self.response_text.delete("1.0", "end")
        else:
            self.prompt_label.config(text="Thank you for completing your journal entries!")
            self.response_text.pack_forget()
            self.submit_button.pack_forget()
            self.show_entries()

    def show_entries(self):
        entries_window = tk.Toplevel()
        entries_window.title("Journal Entries")

        for i, entry in enumerate(self.entries):
            prompt, response = entry
            entry_label = tk.Label(entries_window, text=f"Entry {i+1}: {prompt}\n{response}\n")
            entry_label.pack()

if __name__ == "__main__":
    root = tk.Tk()
    app = JournalApp(root)
    root.mainloop()
