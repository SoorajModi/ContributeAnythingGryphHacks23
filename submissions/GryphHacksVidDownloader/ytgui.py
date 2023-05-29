import tkinter as tk
from tkinter import ttk
from pytube import YouTube

class YouTubeDownloader(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("GryphHacks2023 YouTube Downloader")
        self.geometry("800x350")

        self.label1 = ttk.Label(self, text="Enter YouTube URL:")
        self.label1.pack(pady=10)

        self.url_entry = ttk.Entry(self)
        self.url_entry.pack()

        self.label2 = ttk.Label(self, text="Enter File Location:") # file name must have "/" or "\\" notation
        self.label2.pack(pady=10)

        self.file_entry = ttk.Entry(self)
        self.file_entry.pack()

        self.download_button = ttk.Button(self, text="Download", command=self.download)
        self.download_button.pack(pady=20)

        self.label3 = ttk.Label(self, text="Resource to download videos for you Hackathon Project")
        self.label3.pack(pady=20)

    def download(self):
        url = self.url_entry.get()
        file = self.file_entry.get()
        try:
            yt = YouTube(url)
            yd = yt.streams.get_highest_resolution() # Retrives the highest quality of video
            yd.download(file) # Downloads into file in bracket 
            ttk.Label(self, text="Download completed").pack()
        except:
            ttk.Label(self, text="Invalid URL or Error Occured").pack()

if __name__ == "__main__":
    app = YouTubeDownloader()
    app.mainloop()