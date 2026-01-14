import os
import cv2
import customtkinter as ctk
from tkinterdnd2 import TkinterDnD, DND_FILES

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")

class App(TkinterDnD.Tk):
    def __init__(self):
        super().__init__()

        self.overrideredirect(True)
        self.attributes("-topmost", True)
        
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        width = 720
        height = 420
        x = (screen_width / 2) - (width / 2)
        y = (screen_height / 2) - (height / 2)
        self.geometry(f"{width}x{height}+{int(x)}+{int(y)}")
        
        self.config(bg="#000000")
        self.attributes("-alpha", 0.0)
        self.fade_in()

        self.video_path = None

        self.main_frame = ctk.CTkFrame(self, corner_radius=30, fg_color="#1a1a1a")
        self.main_frame.pack(expand=True, fill="both", padx=0, pady=0)

        self.main_frame.bind("<ButtonPress-1>", self.start_move)
        self.main_frame.bind("<B1-Motion>", self.do_move)

        self.close_btn = ctk.CTkButton(
            self.main_frame, 
            text="✕", 
            width=40, 
            height=40,
            fg_color="transparent", 
            hover_color="#c0392b",
            text_color="white",
            font=("Arial", 16, "bold"),
            corner_radius=20,
            command=self.destroy
        )
        self.close_btn.place(relx=0.95, rely=0.05, anchor="center")

        self.title_label = ctk.CTkLabel(
            self.main_frame,
            text="",
            font=ctk.CTkFont(family="Segoe UI", size=26, weight="bold"),
            text_color="#ecf0f1"
        )
        self.title_label.pack(pady=(50, 5))
        self.animate_text("🎞️ Drag & Drop Video", 0)

        self.subtitle = ctk.CTkLabel(
            self.main_frame,
            text="Extract the last frame losslessly in exact resolution",
            font=ctk.CTkFont(family="Segoe UI", size=12),
            text_color="#95a5a6"
        )
        self.subtitle.pack(pady=(0, 30))

        self.drop_area = ctk.CTkFrame(
            self.main_frame,
            height=180,
            width=600,
            corner_radius=25,
            fg_color="#2c3e50",
            border_width=2,
            border_color="#34495e"
        )
        self.drop_area.pack(pady=10)
        self.drop_area.pack_propagate(False)

        self.drop_label = ctk.CTkLabel(
            self.drop_area,
            text="📥 Drop Video Here",
            font=ctk.CTkFont(family="Segoe UI", size=18),
            text_color="#bdc3c7"
        )
        self.drop_label.place(relx=0.5, rely=0.5, anchor="center")

        self.drop_area.drop_target_register(DND_FILES)
        self.drop_area.dnd_bind("<<Drop>>", self.on_drop)

        self.status = ctk.CTkLabel(
            self.main_frame, 
            text="", 
            font=ctk.CTkFont(size=13), 
            text_color="#2ecc71"
        )
        self.status.pack(pady=20)

    def fade_in(self):
        alpha = self.attributes("-alpha")
        if alpha < 1.0:
            alpha += 0.02
            self.attributes("-alpha", alpha)
            self.after(10, self.fade_in)

    def animate_text(self, text, index):
        if index < len(text):
            self.title_label.configure(text=self.title_label.cget("text") + text[index])
            self.after(16, self.animate_text, text, index + 1)

    def start_move(self, event):
        self.x = event.x
        self.y = event.y

    def do_move(self, event):
        deltax = event.x - self.x
        deltay = event.y - self.y
        x = self.winfo_x() + deltax
        y = self.winfo_y() + deltay
        self.geometry(f"+{x}+{y}")

    def on_drop(self, event):
        path = event.data.strip("{}")
        if not path.lower().endswith((".mp4", ".mov", ".avi", ".mkv")):
            self.status.configure(text="❌ Invalid video format", text_color="#e74c3c")
            self.drop_area.configure(border_color="#e74c3c")
            return

        self.video_path = path
        self.drop_area.configure(border_color="#2ecc71")
        self.extract_last_frame()

    def extract_last_frame(self):
        cap = cv2.VideoCapture(self.video_path)
        total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
        cap.set(cv2.CAP_PROP_POS_FRAMES, total_frames - 1)

        ret, frame = cap.read()
        cap.release()

        if not ret:
            self.status.configure(text="❌ Could not extract frame", text_color="#e74c3c")
            return

        output_path = os.path.splitext(self.video_path)[0] + "_last_frame.png"

        cv2.imwrite(output_path, frame)

        filename = os.path.basename(output_path)
        self.status.configure(
            text=f"✅ Saved: {filename}",
            text_color="#2ecc71"
        )
        self.drop_label.configure(text="✨ Success!")

if __name__ == "__main__":
    app = App()
    app.mainloop()