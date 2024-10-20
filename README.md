What the project does:
This project captures video through a webcam, detects motion, and saves snapshots of detected objects. When a significant movement is identified, the system captures an image, sends an email with the image attached, and periodically cleans up old images from the folder. The project uses OpenCV for video processing and multithreading to handle email sending and folder cleanup in parallel.

Why the project is useful:
Motion Detection: Ideal for security applications, this system detects motion in real-time using a webcam feed and highlights moving objects.
Automated Alerts: When motion is detected, it captures the image and sends an email alert with the object’s snapshot, notifying you immediately.
Background Processing: By leveraging multithreading, the email notification and folder cleanup processes run without interrupting the motion detection flow.
Efficient Resource Management: Automatic folder cleanup ensures the system does not get clogged with too many image files, keeping disk usage under control.

How users can get started with the project:
1. Clone the repository:
git clone https://github.com/yourusername/motion-detection-email-notifier.git
cd motion-detection-email-notifier

3. Install the necessary dependencies:
You'll need Python, OpenCV, and a few other libraries. Run the following command to install them:
pip install opencv-python streamlit

3. Set up your email credentials:
The send_email function (in the emailing.py module) will require your email credentials to send the alerts. Update the function with your email settings. Ensure you use an app-specific password for Gmail (or similar services).

4. Prepare folder structure:
Create a folder named images to store the captured images:
mkdir images

5. Run the script

6. If you encounter any issues or have questions about the project, you can:
Open an issue: If you find a bug or need help with something specific, feel free to open an issue on the project's GitHub page.
