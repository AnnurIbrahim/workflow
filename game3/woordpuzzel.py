# Grafische GUI puzzel met tkinter
import tkinter as tk


class WordPuzzleApp:
    def __init__(self, root):
        self.root = root

        # De correcte zin
        self.correct = [
            "Jan", "weet", "niet", "waarom",
            "met", "taxi", "mee", "moet"
        ]
        self.input = []

        # Achtergrondkleur
        bg_kleur = "#cce7ff"
        root.configure(bg=bg_kleur)

        # Titel
        tk.Label(
            root,
            text="Bouw de juiste zin",
            font=("Arial", 16, "bold"),
            bg=bg_kleur
        ).pack(pady=5)

        # Weergave van de zin
        self.output = tk.Label(
            root,
            text="",
            font=("Arial", 12),
            bg="white",
            width=30,
            height=2,
            relief="sunken"
        )
        self.output.pack(pady=5)

        # Beschikbare woorden (ook afleiders)
        woorden = [
            "Jan", "weet", "hij", "op", "moet",
            "thuis", "als", "heeft",
            "vergeet", "waarom",
            "mee", "de", "met", "niet", "taxi"
        ]

        knop_frame = tk.Frame(root, bg=bg_kleur)
        knop_frame.pack(pady=5)

        for index, woord in enumerate(woorden):
            btn = tk.Button(
                knop_frame,
                text=woord,
                font=("Arial", 10),
                width=8,
                height=1,
                bg="white",
                fg="black",
                activebackground="#b3d9ff",
                command=lambda w=woord: self.add_word(w)
            )
            rij = index // 4
            kolom = index % 4
            btn.grid(row=rij, column=kolom, padx=4, pady=4)

        # Besturingsknoppen
        controle_frame = tk.Frame(root, bg=bg_kleur)
        controle_frame.pack(pady=10)

        tk.Button(
            controle_frame,
            text="🔄 Opnieuw",
            font=("Arial", 10),
            width=12,
            command=self.reset
        ).grid(row=0, column=0, padx=5)

        tk.Button(
            controle_frame,
            text="⬅️ Laatste wissen",
            font=("Arial", 10),
            width=16,
            command=self.remove_last_word
        ).grid(row=0, column=1, padx=5)

    def add_word(self, woord):
        """Voeg woord toe en controleer de zin."""
        self.input.append(woord)
        self.update_display()

        if len(self.input) == len(self.correct):
            if self.input == self.correct:
                self.output.config(text="Zin klopt! Code: 0")
            else:
                self.output.config(text="Fout. Probeer opnieuw.")

    def remove_last_word(self):
        """Verwijder het laatste ingevoerde woord."""
        if self.input:
            self.input.pop()
            self.update_display()

    def reset(self):
        """Reset de invoer en het scherm."""
        self.input = []
        self.update_display()

    def update_display(self):
        """Update de tekst op het scherm."""
        self.output.config(text=" ".join(self.input))


# Start de app
root = tk.Tk()
root.attributes("-fullscreen", True)
app = WordPuzzleApp(root)
root.mainloop()
