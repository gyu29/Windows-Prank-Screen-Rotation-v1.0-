import time
import ctypes

def rotate_screen():
    try:
        user32 = ctypes.windll.user32
        user32.SetProcessDPIAware()
        width, height = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)
        
        for _ in range(4):
            user32.SetDisplayOrientation(0)  # Rotate to default
            time.sleep(0.5)  # Rotate every 0.5 seconds (adjust as needed)
            user32.SetDisplayOrientation(1)  # Rotate 90 degrees
            time.sleep(0.5)  # Rotate every 0.5 seconds (adjust as needed)
        
        user32.SetDisplayOrientation(0)  # Rotate back to default
    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    print("Windows Prank Screen Rotation - Press Enter to start the prank.")
    input()
    rotate_screen()
