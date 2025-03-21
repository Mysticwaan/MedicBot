<div align="center">
  
# [MedicBot!](https://medicbot002.netlify.app/)


![medicbot_banner](https://github.com/user-attachments/assets/ad0f387b-f6d6-43b2-a8dd-782bff8659fc)



# MedicBot - Open Source Medical Assistant Robot

![Screenshot 2025-03-15 at 21-27-28 (JPEG Image 558 × 1024 pixels)](https://github.com/user-attachments/assets/2ac57d00-37ac-4e56-bc0d-133dbcd5ecfd)

## 🚀 Overview

MedicBot is an open-source medical assistant robot designed to revolutionize healthcare by combining robotics and autonomous systems for streamlined medical checks and patient care. This project provides **STL files** for 3D printing, a **materials price comparison table** for European and American Amazon, and **Python instructions** to run the robot efficiently.

## 📌 Features

- 🖨️ **3D Printable Parts:** All STL files included.
- 💰 **Materials Cost Comparison:** Price table for EU & US Amazon.
- 🖥️ **Python Control Software:** Step-by-step setup guide.
- 🔌 **Modular & Customizable:** Open-source and expandable.
- 🛠️ **Easy Assembly:** User-friendly design for quick setup.
- 🌡️ **Temperature Monitoring:** Non-contact infrared temperature measurement.
- ❤️ **Vital Signs Tracking:** Continuous monitoring of heart rate and SpO₂ levels.
- 🩺 **Blood Pressure Analysis:** Automated blood pressure measurement and tracking.
- ⚖️ **Weight & BMI Calculation:** Precise weight monitoring with instant BMI calculations.
- 🌬️ **Environmental Monitoring:** Real-time air quality assessment.
- 🗺️ **LiDAR Navigation:** Advanced mobility with precise spatial awareness.
- ⌚ **Apple Watch Integration:** Sync health data for real-time tracking.
- 🎙️ **Voice Commands:** Control MedicBot hands-free using voice recognition.
- ☁️ **Cloud-Based Health Tracking:** Store and analyze health data securely.

## 📂 Project Structure

```
MedicBot/
│── docs/                  # Documentation files
│── stl/                   # 3D printable STL files
│── scripts/               # Python control scripts
│── materials/             # Materials price table
│── images/                # Project images
│── README.md              # This file
│── LICENSE                # License file
```

## 🖨️ 3D Printing Instructions

1. **Download STL files:** Access the `stl/` directory to retrieve all necessary 3D models.
2. **Slice the models:** Use your preferred slicer software (e.g., Cura, PrusaSlicer) to prepare the models for printing.
3. **Select materials:** PLA filament is recommended for durability and ease of printing.
4. **Print the components:** Follow standard 3D printing procedures to produce each part.
5. **Assemble the robot:** Refer to the assembly guide in the `docs/` directory for step-by-step instructions.

## 💰 Materials & Pricing

| Component        | EU Price (Amazon) | US Price (Amazon) |
|------------------|-------------------|-------------------|
| Servo Motor      | €X.XX             | $X.XX             |
| Raspberry Pi     | €X.XX             | $X.XX             |
| LiDAR Sensor     | €X.XX             | $X.XX             |
| Infrared Thermometer | €X.XX         | $X.XX             |
| Air Quality Sensor | €X.XX           | $X.XX             |

*(For a full list, check `materials/pricing_table.csv`.)*

## 🖥️ Software Setup & Running MedicBot

### Prerequisites

- **Hardware:**
  - Raspberry Pi or compatible system
  - Sensors: Infrared thermometer, heart rate and SpO₂ monitor, blood pressure sensor, weight scale, air quality sensor, LiDAR module
- **Software:**
  - Python 3.x installed
  - Required Python libraries (install via `requirements.txt`)
  - Apple Health & Cloud API setup for additional features

### Installation Steps

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/MedicBot.git
   cd MedicBot/
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Configure the system:**
   - Update the configuration file in `scripts/config.py` with your hardware specifications and preferences.
   - Set up API keys for Apple Health and cloud-based tracking (optional).

4. **Run the main script:**
   ```bash
   python scripts/medicbot.py
   ```

## 📸 Project Images

![MedicBot Preview](https://medicbot002.netlify.app/assets/preview.png)

## 🤝 Contributing

We welcome contributions to enhance MedicBot's capabilities:

1. **Fork the repository:** Click the 'Fork' button on GitHub.
2. **Create a new branch:** Use `git checkout -b feature-name` to create a feature branch.
3. **Make your changes:** Implement your feature or bug fix.
4. **Submit a pull request:** Open a pull request with a detailed description of your changes.

## 📝 License

MedicBot is licensed under the **MIT License**. See the `LICENSE` file for more details.

## 📧 Contact

For questions or support, reach out at **your.email@example.com** or open an issue on GitHub.

---

**🔗 Website:** [MedicBot Official Page](https://medicbot002.netlify.app/)

