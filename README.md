<div align="center">

# 🎯 Face Detection GUI

**Real-time face detection from your webcam, in a simple desktop app.**

![Python](https://img.shields.io/badge/Python-3.9%2B-3776AB?logo=python&logoColor=white)
![OpenCV](https://img.shields.io/badge/OpenCV-5.0-5C3EE8?logo=opencv&logoColor=white)
![Tkinter](https://img.shields.io/badge/GUI-Tkinter-orange)

![Demo](assets/screenshot.png)

</div>

---

## ✨ Features

- 📹 Live webcam feed inside a Tkinter window
- 🟩 Green rectangles around every detected face
- 🔢 Live face counter
- ▶️ Start / Stop button

## 🛠️ Built With

Python · OpenCV (Haar Cascade) · Tkinter · Pillow

## 🚀 Getting Started

```bash
git clone https://github.com/Ujesh-Borthakur/Face-Detection-GUI.git
cd Face-Detection-GUI
pip install -r requirements.txt
python face_gui.py
```

Click **Start** to begin detection and **Stop** to pause.

## 🧠 How It Works

Each frame is converted to grayscale and passed to a Haar Cascade
classifier, which returns an `(x, y, w, h)` box for every face. The boxes
are drawn on the frame, which is converted from BGR to RGB and shown in a
Tkinter label. Tkinter's `after()` schedules the next frame so the GUI
never freezes.

## 🔧 Troubleshooting

- **`cv2` has no attribute `CascadeClassifier`**: OpenCV 5.0 moved it to
  the contrib modules. Use `opencv-contrib-python`, and don't install it
  alongside plain `opencv-python`.
- **Can't open the `.xml` file**: the OpenCV 5.0 pip package doesn't
  bundle the cascade files, so one is included in this repo. Run the
  program from the project folder.
- **Webcam won't open**: close other apps using the camera and check your
  OS privacy settings.
