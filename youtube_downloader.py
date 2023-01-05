import tkinter as tk
from tkinter import ttk
window = tk.Tk()
#methods
def download():
    from pytube import YouTube
    progress_bar["value"] = 100
    url = url_entry.get()
    yt = YouTube(url, on_progress_callback=progress_bar.update(), on_complete_callback=complete_label.grid(row=4, column=0, columnspan=2, pady=10))
    print(yt.title)
    print(yt.thumbnail_url)
    yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first().download()
    
#window
window.title("Youtube Downloader")
icon = tk.PhotoImage(file="youtube.png")
window.iconphoto(False, icon)
window.geometry("500x500")
window.resizable(False, False)
Title = tk.Label(window, text="Youtube Downloader", font=("Arial", 20))
Title.grid(row=0, column=0, columnspan=2, pady=10)
url = tk.Label(window, text="URL: ", font=("Arial", 15))
url.grid(row=1, column=0, pady=10)
url_entry = tk.Entry(window, width=50)
url_entry.grid(row=1, column=1, pady=10)
download_button = tk.Button(window, text="Download", font=("Arial", 15), command=download)
download_button.grid(row=2, column=0, columnspan=2, pady=10)
progress = tk.Label(window, text="Progress: ", font=("Arial", 15))
progress.grid(row=3, column=0, pady=10)
progress_bar = ttk.Progressbar(window, orient="horizontal", length=100, mode="determinate")
progress_bar.grid(row=3, column=1, pady=10)
complete_label = tk.Label(window, text="Download Complete", font=("Arial", 15))

window.mainloop()