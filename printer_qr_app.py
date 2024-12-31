import os
import threading
import webbrowser
from tkinter import Tk, Label, Button, PhotoImage
from flask import Flask, request, jsonify
from flask_cors import CORS
import socket
from werkzeug.utils import secure_filename
import win32print
import win32api
import qrcode

# Flask app for handling mobile interactions
app = Flask(__name__)
CORS(app)  # Enable CORS to handle cross-origin requests

UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
PRINT_STATUS = {"status": "Idle"}

@app.route("/", methods=["GET"])
def index():
    return """
    <!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css" rel="stylesheet">
    <style>
        :root {
            --primary-color: #4361ee;
            --secondary-color: #3f37c9;
            --success-color: #4CAF50;
            --error-color: #f44336;
            --background-color: #f8f9fa;
            --card-background: #ffffff;
        }

        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background-color: var(--background-color);
            margin: 0;
            padding: 0;
            min-height: 100vh;
        }

        .navbar {
            background-color: var(--primary-color);
            padding: 1rem 2rem;
            color: white;
            box-shadow: 0 2px 10px rgba(0,0,0,0.1);
            position: fixed;
            width: 100%;
            top: 0;
            z-index: 1000;
            display: flex;
            justify-content: space-between;
            align-items: center;
        }

        .navbar-brand {
            display: flex;
            align-items: center;
            gap: 10px;
            font-size: 1.5rem;
            font-weight: bold;
        }

        .navbar-brand i {
            font-size: 1.8rem;
        }

        .main-content {
            min-height: 100vh;
            display: flex;
            justify-content: center;
            align-items: center;
            padding: 2rem;
            margin-top: 60px;
            background: linear-gradient(135deg, #f8f9fa 0%, #e9ecef 100%);
        }

        .container {
            text-align: center;
            background-color: var(--card-background);
            padding: 3rem;
            border-radius: 20px;
            box-shadow: 0 10px 30px rgba(0,0,0,0.1);
            width: 90%;
            max-width: 600px;
            transition: transform 0.3s ease;
        }

        .container:hover {
            transform: translateY(-5px);
        }

        h1 {
            color: #333;
            font-size: 28px;
            margin-bottom: 30px;
            position: relative;
        }

        h1::after {
            content: '';
            display: block;
            width: 50px;
            height: 3px;
            background-color: var(--primary-color);
            margin: 10px auto;
            border-radius: 2px;
        }

        .upload-area {
            border: 2px dashed #ccc;
            border-radius: 15px;
            padding: 2rem;
            margin: 20px 0;
            transition: all 0.3s ease;
            position: relative;
        }

        .upload-area:hover {
            border-color: var(--primary-color);
            background-color: rgba(67, 97, 238, 0.05);
        }

        .upload-icon {
            font-size: 3rem;
            color: var(--primary-color);
            margin-bottom: 1rem;
        }

        input[type="file"] {
            margin: 10px 0;
            padding: 10px;
            width: 100%;
            max-width: 300px;
            cursor: pointer;
            opacity: 0;
            position: absolute;
            top: 0;
            left: 0;
            height: 100%;
        }

        .upload-text {
            color: #666;
            margin: 10px 0;
        }

        button {
            background-color: var(--primary-color);
            color: white;
            border: none;
            padding: 15px 30px;
            font-size: 16px;
            cursor: pointer;
            border-radius: 30px;
            margin-top: 20px;
            transition: all 0.3s ease;
            display: inline-flex;
            align-items: center;
            gap: 10px;
        }

        button:hover {
            background-color: var(--secondary-color);
            transform: translateY(-2px);
            box-shadow: 0 5px 15px rgba(67, 97, 238, 0.3);
        }

        #status {
            margin-top: 25px;
            font-size: 18px;
            font-weight: 500;
            padding: 10px 20px;
            border-radius: 10px;
            display: inline-flex;
            align-items: center;
            gap: 10px;
        }

        .success {
            color: var(--success-color);
            background-color: rgba(76, 175, 80, 0.1);
        }

        .error {
            color: var(--error-color);
            background-color: rgba(244, 67, 54, 0.1);
        }

        /* Animation for status updates */
        @keyframes statusFade {
            0% { opacity: 0; transform: translateY(10px); }
            100% { opacity: 1; transform: translateY(0); }
        }

        #status.animate {
            animation: statusFade 0.3s ease-out forwards;
        }

        @media (max-width: 768px) {
            .container {
                padding: 2rem;
            }

            h1 {
                font-size: 24px;
            }

            .upload-area {
                padding: 1.5rem;
            }

            .upload-icon {
                font-size: 2.5rem;
            }

            button {
                padding: 12px 24px;
                font-size: 15px;
            }
        }

        @media (max-width: 480px) {
            .navbar {
                padding: 1rem;
            }

            .container {
                padding: 1.5rem;
            }

            h1 {
                font-size: 20px;
            }

            .upload-area {
                padding: 1rem;
            }

            .upload-icon {
                font-size: 2rem;
            }

            button {
                padding: 10px 20px;
                font-size: 14px;
                width: 100%;
                justify-content: center;
            }

            #status {
                font-size: 14px;
                padding: 8px 16px;
            }
        }
    </style>
</head>
<body>
    <nav class="navbar">
        <div class="navbar-brand">
            <i class="fas fa-print"></i>
            <span>Printy</span>
        </div>
    </nav>
    <div class="main-content">
        <div class="container">
            <h1>Upload File to Print</h1>
            <form action="/print" method="post" enctype="multipart/form-data">
                <div class="upload-area">
                    <i class="fas fa-cloud-upload-alt upload-icon"></i>
                    <input type="file" name="file" required id="fileInput">
                    <p class="upload-text">Drag and drop your file here or click to browse</p>
                    <p class="upload-text" id="fileName" style="display: none;"></p>
                </div>
                <button type="submit">
                    <i class="fas fa-print"></i>
                    Print File
                </button>
            </form>
            <p id="status" class="success">
                <i class="fas fa-circle-notch"></i>
                Status: Idle
            </p>
        </div>
    </div>
    <script>
        // File input handling
        const fileInput = document.getElementById('fileInput');
        const fileName = document.getElementById('fileName');
        const uploadText = document.querySelector('.upload-text');

        fileInput.addEventListener('change', (e) => {
            if (e.target.files.length > 0) {
                fileName.textContent = `Selected file: ${e.target.files[0].name}`;
                fileName.style.display = 'block';
                uploadText.style.display = 'none';
            }
        });

        // Status updates
        setInterval(async () => {
            try {
                const response = await fetch('/status');
                const data = await response.json();
                const statusElement = document.getElementById('status');
                const oldStatus = statusElement.textContent;
                const newStatus = 'Status: ' + data.status;
                
                if (oldStatus !== newStatus) {
                    statusElement.classList.remove('animate');
                    void statusElement.offsetWidth; // Trigger reflow
                    statusElement.classList.add('animate');
                }

                statusElement.innerHTML = `
                    ${data.status === "Printed successfully" 
                        ? '<i class="fas fa-check-circle"></i>' 
                        : data.status.startsWith("Error")
                            ? '<i class="fas fa-exclamation-circle"></i>'
                            : '<i class="fas fa-circle-notch fa-spin"></i>'}
                    Status: ${data.status}
                `;

                if (data.status === "Printed successfully") {
                    statusElement.classList.remove("error");
                    statusElement.classList.add("success");
                } else if (data.status.startsWith("Error")) {
                    statusElement.classList.remove("success");
                    statusElement.classList.add("error");
                }
            } catch (error) {
                console.error('Error fetching status:', error);
            }
        }, 1000);
    </script>
</body>
</html>
    """

@app.route("/print", methods=["POST"])
def print_file():
    global PRINT_STATUS
    file = request.files["file"]
    if file:
        filename = secure_filename(file.filename)
        filepath = os.path.join(UPLOAD_FOLDER, filename)
        file.save(filepath)
        
        PRINT_STATUS["status"] = "Printing"
        try:
            win32api.ShellExecute(0, "print", filepath, None, ".", 0)
            PRINT_STATUS["status"] = "Printed successfully"
        except Exception as e:
            PRINT_STATUS["status"] = f"Error: {e}"
        return jsonify({"message": "File sent to printer."})
    return jsonify({"error": "No file uploaded."})

@app.route("/status", methods=["GET"])
def status():
    return jsonify(PRINT_STATUS)

def start_server():
    app.run(host="0.0.0.0", port=5000)

# Tkinter GUI for the desktop app
def get_local_ip():
    hostname = socket.gethostname()
    return socket.gethostbyname(hostname)

def generate_qr_code(url):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(url)
    qr.make(fit=True)
    qr_img = qr.make_image(fill="black", back_color="white")
    qr_img_path = "qr_code.png"
    qr_img.save(qr_img_path)
    return qr_img_path

def start_gui():
    global PRINT_STATUS

    def open_browser():
        webbrowser.open(f"http://{get_local_ip()}:5000")

    root = Tk()
    root.title("Printer Server")
    root.geometry("400x400")

    link = f"http://{get_local_ip()}:5000"
    qr_img_path = generate_qr_code(link)
    
    qr_img = PhotoImage(file=qr_img_path)

    Label(root, text="Printer Server is running").pack(pady=10)
    Label(root, text="Scan the QR Code to upload and print:").pack(pady=5)
    qr_label = Label(root, image=qr_img)
    qr_label.image = qr_img
    qr_label.pack(pady=10)

    Button(root, text="Open in Browser", command=open_browser).pack(pady=10)

    status_label = Label(root, text="Status: Idle", fg="green")
    status_label.pack(pady=10)

    def update_status():
        while True:
            status_label.config(text=f"Status: {PRINT_STATUS['status']}")
            if PRINT_STATUS["status"] == "Printed successfully":
                status_label.config(fg="green")
            elif PRINT_STATUS["status"].startswith("Error"):
                status_label.config(fg="red")
            status_label.update()

    threading.Thread(target=update_status, daemon=True).start()
    root.mainloop()

if __name__ == "__main__":
    # Start the Flask server in a separate thread
    threading.Thread(target=start_server, daemon=True).start()
    # Start the GUI
    start_gui()
