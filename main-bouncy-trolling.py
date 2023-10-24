import tkinter as tk
import colorsys

# Die Abmessungen des Fensters
window_width = 300
window_height = 200

# Erstelle das tkinter-Fenster
root = tk.Tk()
root.geometry(f"{window_width}x{window_height}")
root.overrideredirect(1)
root.attributes('-topmost',True)
#root.wm_attributes('-fullscreen', 'True')

# Startposition des Fensters (oben links)
x = 0
y = 0
x_direction = 1  # Richtung für die X-Achse (1: nach rechts, -1: nach links)
y_direction = 1  # Richtung für die Y-Achse (1: nach unten, -1: nach oben)

# Farbparameter
hue = 0
hue_step = 0.001

# Funktion zur Aktualisierung der Fensterposition und Farbe
def update_position_and_color():
    global x, y, x_direction, y_direction, hue

    # Aktualisiere die Position
    x += 5 * x_direction
    y += 5 * y_direction

    # Überprüfe, ob das Fenster die Ecken erreicht hat
    if x <= 0 or x >= root.winfo_screenwidth() - window_width:
        x_direction *= -1
    if y <= 0 or y >= root.winfo_screenheight() - window_height:
        y_direction *= -1

    # Setze die neue Position
    root.geometry(f"+{x}+{y}")

    # Aktualisiere die Fensterfarbe im Regenbogenstil
    rgb_color = [int(c * 255) for c in colorsys.hsv_to_rgb(hue, 1, 1)]
    hex_color = f'#{rgb_color[0]:02X}{rgb_color[1]:02X}{rgb_color[2]:02X}'
    root.configure(bg=hex_color)

    # Aktualisiere den Farbhue-Wert
    hue = (hue + hue_step) % 1

    # Rufe die Funktion erneut nach einer Verzögerung auf
    root.after(1, update_position_and_color)

# Starte die Aktualisierungsfunktion
update_position_and_color()

# Starte die tkinter-Schleife
root.mainloop()
