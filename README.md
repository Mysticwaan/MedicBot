<div align="center">

# [Click here for MedicBot!](https://medicbot002.netlify.app/)
![ChatGPT Image May 13, 2025, 09_21_19 AM](https://github.com/user-attachments/assets/e5c49120-97be-4410-957a-945483bcc4a5)
![medicbot_banner](https://github.com/user-attachments/assets/ad0f387b-f6d6-43b2-a8dd-782bff8659fc)

# MedicBot - Open Source Medical Assistant Robot

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

  <p align="center">
  <img src="https://github.com/user-attachments/assets/2ac57d00-37ac-4e56-bc0d-133dbcd5ecfd" width="49%" height="800"/>
  <img src="https://github.com/user-attachments/assets/f2614c87-89a0-4ece-9ca0-e059609c59c4" width="49%" height="800"/>
</p>

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


![image](https://github.com/user-attachments/assets/69f98a7e-22a7-4d74-add5-6161b1f73f1e)   

## 💰 Materials & Pricing


| Component             | EU Price (Amazon) | US Price (Amazon) |
|-----------------------|-------------------|-------------------|
| Servo Motor           | [€10.00](https://www.amazon.de/dp/B07K8SQM6T) | [$12.00](https://www.amazon.com/dp/B07K8SQM6T) |
| Raspberry Pi 4 Model B (2GB) | [€45.00](https://www.amazon.de/dp/B09TTNPB4J) | [$49.99](https://www.amazon.com/dp/B09TTNPB4J) |
| LiDAR Sensor          | [€150.00](https://www.amazon.de/dp/B0CP6XDCWS) | [$160.00](https://www.amazon.com/dp/B0CP6XDCWS) |
| Infrared Thermometer  | [€15.00](https://www.amazon.de/dp/B089T5Y59H) | [$17.00](https://www.amazon.com/dp/B089T5Y59H) |
| Air Quality Sensor    | [€50.00](https://www.amazon.de/dp/B08X2V5K28) | [$50.00](https://www.amazon.com/dp/B08X2V5K28) |

*Note: Prices are approximate and may vary based on seller and availability.*

## 🖥️ Software Setup & Running MedicBot

### Prerequisites

- **Hardware:**
  - Raspberry Pi or compatible system
  - Sensors: Infrared thermometer, heart rate and SpO₂ monitor, blood pressure sensor, weight scale, air quality sensor, LiDAR module
- **Software:**
  - Python 3.x installed
  - Required Python libraries (install via `requirements.txt`)
  - Apple Health & Cloud API setup for additional features
 
  
![984a5501-518f-4113-9f2f-ac7cb209af1b](https://github.com/user-attachments/assets/0f49d96a-a1eb-40b5-89e5-ffdccee2bef9)


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
