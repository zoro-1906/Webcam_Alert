import smtplib
import mimetypes
from email.message import EmailMessage

PASSWORD = "x y z"
# Generate an app password using ur gmail account and paste it in the "PASSWORD" variable.
SENDER = "apptestpy19@gmail.com"
RECEIVER = "apptestpy19@gmail.com"

def send_email(image_path):
    print("send_email function started")
    email_message = EmailMessage()
    email_message["Subject"] = "New object entered the frame!"
    email_message["From"] = SENDER
    email_message["To"] = RECEIVER
    email_message.set_content("Hey, a person appeared in the camera, you may want to check it.")

    # Open the image file and read its content
    with open(image_path, "rb") as file:
        content = file.read()

    # Get the MIME type and subtype
    mime_type, _ = mimetypes.guess_type(image_path)
    if mime_type is None:
        raise ValueError("Could not determine the image type")

    maintype, subtype = mime_type.split("/")

    # Attach the image to the email
    email_message.add_attachment(content, maintype=maintype, subtype=subtype)

    # Connect to the Gmail server
    with smtplib.SMTP("smtp.gmail.com", 587) as gmail:
        gmail.ehlo()  # Identify yourself to the server
        gmail.starttls()  # Secure the connection
        gmail.login(SENDER, PASSWORD)
        gmail.send_message(email_message)  # Send the email

    print("clean_folder function ended")

# if __name__ == "__main__":
#     send_email(image_path="images/9.png")
