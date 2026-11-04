import tkinter as tk
import cv2
from PIL import Image, ImageTk

root=tk.Tk()
root.title("Face Detection Program")

label=tk.Label(root)
label.pack()

count_label = tk.Label(root, text="Faces detected: 0", font=("Arial", 12))
count_label.pack()

video=cv2.VideoCapture(0)
face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

def update_frame():
    ret, frame = video.read()

    if ret:
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(
            gray,
            scaleFactor=1.1,
            minNeighbors=5,
            minSize=(30, 30),
        )

        count_label.config(text=f"Faces detected: {len(faces)}")
        
        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        img = Image.fromarray(rgb)
        imgtk = ImageTk.PhotoImage(image=img)

        label.imgtk = imgtk
        label.config(image=imgtk)

    label.after(10, update_frame)

update_frame()
root.mainloop()
