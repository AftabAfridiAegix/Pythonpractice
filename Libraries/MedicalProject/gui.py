import tkinter as tk
from tkinter import ttk, messagebox
from Medical_Data import MedicalData


class MediPlusGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("MediPlus - Patient Records")
        self.root.geometry("950x600")
        self.root.minsize(800, 500)
        self.root.configure(bg="#EDF2F8")

        self.colors = {
            "navy": "#172554",
            "red": "#DC2626",
            "dark_red": "#B91C1C",
            "blue": "#2563EB",
            "green": "#15803D",
            "orange": "#F59E0B",
            "yellow": "#FDE047",
            "bg": "#EDF2F8",
            "white": "#FFFFFF",
            "text": "#1E293B",
            "muted": "#64748B",
            "border": "#D8E1EC"
        }

        self.data = MedicalData()

        self.setup_style()
        self.build_header()
        self.build_form()
        self.build_table()
        self.display_patients()

    def setup_style(self):
        style = ttk.Style()
        style.theme_use("clam")

        style.configure(
            "Treeview",
            background=self.colors["white"],
            fieldbackground=self.colors["white"],
            foreground=self.colors["text"],
            rowheight=32,
            font=("Segoe UI", 10),
            borderwidth=1
        )

        style.configure(
            "Treeview.Heading",
            background=self.colors["navy"],
            foreground=self.colors["white"],
            font=("Segoe UI", 10, "bold"),
            padding=9
        )

        style.map(
            "Treeview",
            background=[("selected", "#BFDBFE")],
            foreground=[("selected", self.colors["navy"])]
        )

        style.configure("TEntry", padding=7)

    def build_header(self):
        header = tk.Frame(
            self.root,
            bg=self.colors["navy"],
            height=95
        )
        header.pack(fill="x")
        header.pack_propagate(False)

        logo = tk.Frame(
            header,
            bg=self.colors["red"],
            width=55,
            height=55
        )
        logo.pack(side="left", padx=(22, 14), pady=20)
        logo.pack_propagate(False)

        tk.Label(
            logo,
            text="+",
            font=("Segoe UI", 29, "bold"),
            bg=self.colors["red"],
            fg=self.colors["white"]
        ).pack(expand=True)

        title = tk.Frame(header, bg=self.colors["navy"])
        title.pack(side="left", pady=17)

        tk.Label(
            title,
            text="MediPlus",
            font=("Segoe UI", 23, "bold"),
            bg=self.colors["navy"],
            fg=self.colors["white"]
        ).pack(anchor="w")

        tk.Label(
            title,
            text="PATIENT RECORDS MANAGEMENT",
            font=("Segoe UI", 9, "bold"),
            bg=self.colors["navy"],
            fg="#CBD5E1"
        ).pack(anchor="w")

    def build_form(self):
        section = tk.Frame(self.root, bg=self.colors["bg"])
        section.pack(fill="x", padx=24, pady=18)

        tk.Label(
            section,
            text="Add New Patient",
            font=("Segoe UI", 17, "bold"),
            bg=self.colors["bg"],
            fg=self.colors["navy"]
        ).pack(anchor="w")

        tk.Label(
            section,
            text="Enter patient information below",
            font=("Segoe UI", 10),
            bg=self.colors["bg"],
            fg=self.colors["muted"]
        ).pack(anchor="w", pady=(3, 12))

        form = tk.Frame(
            section,
            bg=self.colors["white"],
            highlightbackground=self.colors["border"],
            highlightthickness=1
        )
        form.pack(fill="x")

        fields = {
            "ID": "Patient ID",
            "Name": "Full name",
            "Age": "Patient age",
            "Disease": "Disease name"
        }

        self.entries = {}

        for col, (field, placeholder) in enumerate(fields.items()):
            cell = tk.Frame(form, bg=self.colors["white"])
            cell.grid(
                row=0,
                column=col,
                sticky="ew",
                padx=10,
                pady=12
            )
            form.columnconfigure(col, weight=1, uniform="fields")

            tk.Label(
                cell,
                text=field,
                font=("Segoe UI", 10, "bold"),
                bg=self.colors["white"],
                fg=self.colors["text"]
            ).pack(anchor="w", pady=(0, 6))

            entry = ttk.Entry(cell, font=("Segoe UI", 10))
            entry.pack(fill="x")
            entry.insert(0, placeholder)
            entry.configure(foreground=self.colors["muted"])

            entry.bind(
                "<FocusIn>",
                lambda event, e=entry, p=placeholder:
                self.clear_placeholder(e, p)
            )

            entry.bind(
                "<FocusOut>",
                lambda event, e=entry, p=placeholder:
                self.add_placeholder(e, p)
            )

            self.entries[field] = entry

        button_frame = tk.Frame(form, bg=self.colors["white"])
        button_frame.grid(
            row=1,
            column=0,
            columnspan=4,
            pady=(0, 14)
        )

        tk.Button(
            button_frame,
            text="+  Add Patient",
            command=self.add_patient,
            bg=self.colors["red"],
            fg=self.colors["white"],
            activebackground=self.colors["dark_red"],
            activeforeground=self.colors["white"],
            font=("Segoe UI", 10, "bold"),
            relief="flat",
            cursor="hand2",
            padx=18,
            pady=8,
            width=15
        ).pack()

    def clear_placeholder(self, entry, placeholder):
        if entry.get() == placeholder:
            entry.delete(0, tk.END)
            entry.configure(foreground=self.colors["text"])

    def add_placeholder(self, entry, placeholder):
        if not entry.get().strip():
            entry.delete(0, tk.END)
            entry.insert(0, placeholder)
            entry.configure(foreground=self.colors["muted"])

    def build_table(self):
        section = tk.Frame(self.root, bg=self.colors["bg"])
        section.pack(
            fill="both",
            expand=True,
            padx=24,
            pady=(0, 20)
        )

        heading = tk.Frame(section, bg=self.colors["bg"])
        heading.pack(fill="x", pady=(0, 10))

        tk.Label(
            heading,
            text="Patient Records",
            font=("Segoe UI", 17, "bold"),
            bg=self.colors["bg"],
            fg=self.colors["navy"]
        ).pack(side="left")

        tk.Label(
            heading,
            text="PANDAS DATAFRAME",
            font=("Segoe UI", 9, "bold"),
            bg=self.colors["bg"],
            fg=self.colors["blue"]
        ).pack(side="right")

        card = tk.Frame(
            section,
            bg=self.colors["white"],
            highlightbackground=self.colors["border"],
            highlightthickness=1
        )
        card.pack(fill="both", expand=True)

        columns = ("ID", "Name", "Age", "Disease")

        self.table = ttk.Treeview(
            card,
            columns=columns,
            show="headings"
        )

        widths = {
            "ID": 130,
            "Name": 250,
            "Age": 100,
            "Disease": 260
        }

        for column in columns:
            self.table.heading(column, text=column)
            self.table.column(
                column,
                width=widths[column],
                minwidth=70,
                anchor="center"
            )

        self.table.tag_configure(
            "odd",
            background="#FFFFFF"
        )
        self.table.tag_configure(
            "even",
            background="#EFF6FF"
        )

        scrollbar = ttk.Scrollbar(
            card,
            orient="vertical",
            command=self.table.yview
        )
        self.table.configure(yscrollcommand=scrollbar.set)

        self.table.pack(
            side="left",
            fill="both",
            expand=True,
            padx=7,
            pady=7
        )
        scrollbar.pack(side="right", fill="y", pady=7)

        tk.Label(
            section,
            text="♥  MediPlus | Patient Care Records",
            font=("Segoe UI", 9),
            bg=self.colors["bg"],
            fg=self.colors["muted"]
        ).pack(anchor="w", pady=(7, 0))

    def display_patients(self):
        self.table.delete(*self.table.get_children())

        for index, (_, patient) in enumerate(self.data.df.iterrows()):
            tag = "even" if index % 2 == 0 else "odd"

            self.table.insert(
                "",
                "end",
                values=(
                    patient["ID"],
                    patient["Name"],
                    patient["Age"],
                    patient["Disease"]
                ),
                tags=(tag,)
            )

    def add_patient(self):
        fields = ["ID", "Name", "Age", "Disease"]
        placeholders = {
            "ID": "Patient ID",
            "Name": "Full name",
            "Age": "Patient age",
            "Disease": "Disease name"
        }

        values = {
            field: self.entries[field].get().strip()
            for field in fields
        }

        for field in fields:
            if (
                not values[field]
                or values[field] == placeholders[field]
            ):
                messagebox.showwarning(
                    "Missing Information",
                    "Please complete all patient fields."
                )
                self.entries[field].focus_set()
                return

        try:
            self.data.add_patient(
                values["ID"],
                values["Name"],
                values["Age"],
                values["Disease"]
            )

        except ValueError as error:
            messagebox.showwarning(
                "Invalid Information",
                str(error)
            )
            return

        except Exception as error:
            messagebox.showerror(
                "Save Error",
                f"Could not save the patient:\n{error}"
            )
            return

        self.display_patients()

        for field in fields:
            entry = self.entries[field]
            entry.delete(0, tk.END)
            entry.insert(0, placeholders[field])
            entry.configure(foreground=self.colors["muted"])

        self.entries["ID"].focus_set()

        messagebox.showinfo(
            "Success",
            "Patient added and saved successfully!"
        )


if __name__ == "__main__":
    root = tk.Tk()
    app = MediPlusGUI(root)
    root.mainloop()