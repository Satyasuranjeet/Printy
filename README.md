# Printy - Wireless Printing Solution

 <img src="https://i.ibb.co/9pW1m13/Untitled-design.png" alt="Printy Banner" style="width: 100%; height: auto; display: block;">

---

## About Printy

**Printy** is a seamless and easy-to-use wireless printing solution. With no complicated setups, you can print documents directly from your mobile device by simply scanning a QR code. Stay productive and save time!

---

## Features

- **Quick Wireless Printing**: No need for cables or complex network configurations.
- **Cross-Platform Compatibility**: Works on both mobile devices and desktop computers.
- **User-Friendly Interface**: Simple and intuitive UI for effortless navigation.
- **Secure and Local**: Operates only within your local network for enhanced security.

---

## Screenshots

### Desktop Application
![Desktop Screenshot](https://raw.githubusercontent.com/Satyasuranjeet/Printy/refs/heads/master/Screenshot/4.jpg)

### Mobile Interface
![Mobile Screenshot](https://raw.githubusercontent.com/Satyasuranjeet/Printy/refs/heads/master/Screenshot/1.png)
![Mobile Screenshot](https://raw.githubusercontent.com/Satyasuranjeet/Printy/refs/heads/master/Screenshot/2.png)

---

## Tech Stack

- **Languages**: Python, HTML, JavaScript, CSS
- **Frameworks**: Flask, Flask-CORS
- **Libraries**: PyInstaller, QRCode, Pillow, PyWin32
- **Tools**: Virtualenv, PyInstaller

---

## Installation & Setup

### Prerequisites

Ensure you have the following installed:
- **Python 3.7+**
- **pip** (Python Package Manager)

### Steps

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/printy.git
   cd printy
   ```

2. **Create a virtual environment and activate it**:
   ```bash
   python -m venv myenv
   myenv\Scripts\activate  # On Windows
   source myenv/bin/activate  # On macOS/Linux
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the application**:
   ```bash
   python printer_qr_app.py
   ```

### Build the Application

To create a standalone executable:
```bash
pyinstaller --onefile --windowed --icon=resources/icon.ico printer_qr_app.py
```

The executable will be available in the `dist/` folder.

---

## Download the Application

[![Download Printy App](https://via.placeholder.com/200x50.png?text=Download+App)](appfile/printer_qr_app.exe)

---

## Folder Structure

```plaintext
printer_qr_app/
├── printer_qr_app.py         # Main Python script
├── uploads/                  # Folder to store uploaded files
├── myenv/                    # Virtual environment folder (auto-created)
├── resources/
│   ├── icon.ico              # Custom icon for the app
│   ├── qr_code.png           # Generated QR code (runtime-generated)
├── dist/                     # Generated .exe file (auto-created by PyInstaller)
├── build/                    # Build files (auto-created by PyInstaller)
└── __pycache__/              # Python cache files (auto-created)
```

---

## License

This project is licensed under the **MIT License**. See the [LICENSE](LICENSE) file for details.

