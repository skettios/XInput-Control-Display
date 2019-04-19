import tkinter as tk
import xicd

def main():
    root = tk.Tk()
    app = xicd.App(root)
    app.loop()


if __name__ == "__main__":
    main()
