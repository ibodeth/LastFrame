# 🎞️ LastFrameDropper

![Python](https://img.shields.io/badge/Python-3.9+-3776AB?style=for-the-badge\&logo=python\&logoColor=white)
![OpenCV](https://img.shields.io/badge/OpenCV-5C3EE8?style=for-the-badge\&logo=opencv\&logoColor=white)
![CustomTkinter](https://img.shields.io/badge/CustomTkinter-darkgreen?style=for-the-badge)
![Desktop App](https://img.shields.io/badge/Desktop-App-2c3e50?style=for-the-badge)
![AI Workflow](https://img.shields.io/badge/AI-Video_Workflow-8E44AD?style=for-the-badge)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)

**LastFrameDropper** is a minimalist desktop tool that extracts the **last frame of a video losslessly**.

> **Note:** This is a lightweight desktop utility designed to drop video files and extract their final frame.

Built for **AI video generation workflows** where frame continuity is critical.

---

## 📸 Preview

> Drag a video → last frame is saved automatically in original resolution.

---

## 🚀 What It Does

* Drag & drop a video file
* Extracts the **exact final frame**
* Saves as PNG with **no re-encoding**
* Keeps original resolution and aspect ratio

```text
video_name_last_frame.png
```

---

## 🧠 AI Video Use Cases

Designed for:

* **Video continuation** (Runway, Pika, Luma, SVD)
* **Frame-to-frame consistency**
* **Image-to-video / video-to-video** pipelines

Typical flow:

1. Generate a video
2. Extract last frame with LastFrameDropper
3. Feed that frame back into the AI model as input

This reduces visual jumps and keeps camera, lighting, and composition consistent.

---

## ✨ Features

* Drag & drop interface
* Lossless last-frame extraction
* Original resolution preserved
* Fast (OpenCV backend)
* Borderless, dark-themed UI

---

## 🛠 Tech Stack

* Python 3
* OpenCV
* CustomTkinter
* TkinterDnD2

---

## 📦 Installation

```bash
pip install opencv-python customtkinter tkinterdnd2
```

---

## ▶️ Run

```bash
python main.py
```

Drop a video file into the window. The last frame is saved automatically.

---

## 🧑‍💻 Developer

**İbrahim Nuryağınlı**

[![YouTube](https://img.shields.io/badge/YouTube-FF0000?style=for-the-badge\&logo=youtube\&logoColor=white)](https://www.youtube.com/@ibrahim.python)
[![GitHub](https://img.shields.io/badge/GitHub-100000?style=for-the-badge\&logo=github\&logoColor=white)](https://github.com/ibodeth)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge\&logo=linkedin\&logoColor=white)](https://www.linkedin.com/in/ibrahimnuryaginli/)
[![Website](https://img.shields.io/badge/Website-2196F3?style=for-the-badge\&logo=google-chrome\&logoColor=white)](https://ibodeth.github.io/)

---

## 📄 License

MIT License
