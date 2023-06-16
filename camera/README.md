# balance - Camera module

## How to run

Assuming you have conda installed, run

```conda create --name <environment_name> --file requirements.txt```

To create a new env with the required dependencies, or

```conda install --file requirements.txt```

If you already have the dependencies installed.

Update the line

```self._cap = cv2.VideoCapture("http://192.168.0.101:4747/video")```

On camera.py to use your own ip address, or to '0' instead of an ip address to use a webcam.

---
## Notes

Prefer running on a 1080p screen for a better HUD layout.

