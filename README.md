# Printy - Wireless Printing Solution

![Printy Banner](https://via.placeholder.com/800x200.png?text=Printy+Wireless+Printing)

## About Printy

Printy is a seamless and easy-to-use wireless printing solution. With no complicated setups, you can print documents directly from your mobile device by simply scanning a QR code. Stay productive and save time!

## Features

- **Quick Wireless Printing**: No need for cables or complex network configurations.
- **Cross-Platform Compatibility**: Works on mobile devices and desktop computers.
- **User-Friendly Interface**: Simple and intuitive UI for effortless navigation.
- **Secure and Local**: Operates only within your local network.

---

## Screenshots

### Desktop Application
![Desktop Screenshot](https://via.placeholder.com/600x400.png?text=Desktop+App)

### Mobile Interface
![Mobile Screenshot](https://via.placeholder.com/300x600.png?text=Mobile+App+Interface)

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

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/printy.git
   cd printy
   ```

2. Create a virtual environment and activate it:
   ```bash
   python -m venv myenv
   myenv\Scripts\activate  # On Windows
   source myenv/bin/activate  # On macOS/Linux
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Run the application:
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

[![Download Printy App](https://via.placeholder.com/200x50.png?text=Download+App)](./appfile/printy_installer.exe)

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

## Support

For additional support or to report issues, please visit: [GitHub Issues](https://github.com/yourusername/printy/issues).

---

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
