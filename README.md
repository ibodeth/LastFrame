# LastFrameDropper

A desktop utility that automatically extracts the final frame of any dropped video file losslessly.

## How it Works
The application uses CustomTkinter and TkinterDnD2 for drag-and-drop interaction. When a video file is dropped, the OpenCV backend automatically reads the video properties, extracts the final frame, and exports it as a PNG file in its original resolution and aspect ratio.

## Tech Stack
- **Languages/Frameworks:** Python, CustomTkinter
- **Services/Libraries:** OpenCV, TkinterDnD2
- **Infrastructure:** Windows, Linux, macOS

## Local Setup
1. Clone the repository:
   ```bash
   git clone https://github.com/ibodeth/LastFrame.git
   cd LastFrame
   ```
2. Install dependencies:
   ```bash
   pip install opencv-python customtkinter tkinterdnd2
   ```
3. Run the application:
   ```bash
   python main.py
   ```

## License
MIT
