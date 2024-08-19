# Unit Converter App

This repository contains two versions of a Unit Converter App that provides a simple interface for converting between various traditional measurement units. The first version (`app.py`) is a desktop application built using Tkinter, while the second version (`app-flux.py`) is a web application built using Flask.

## Special Notes

### Land Measurement Units in Bangladesh

This application is designed to handle traditional land measurement units used in Bangladesh. These units are specific to land area calculations and are commonly used in various contexts within the country. After an extensive search, it was challenging to find a reliable tool that could convert between these units.

To provide accurate conversions, this app utilizes conversion data sourced from the [Ministry of Land, Bangladesh](https://minland.gov.bd/site/page/4e44d7ef-2c36-4483-aa4e-77b294de729c/Land-Measurement-Unit). The data is used to ensure the app offers correct and reliable conversions between these traditional units.

## Features

- **Unit Conversion**: Convert values between traditional units using predefined conversion data.
- **Swap Units**: Easily swap the units and update the conversion.
- **Copy Result**: Select and copy the conversion result using the mouse (in the desktop version).

## Table of Contents

- [Installation](#installation)
  - [Desktop Version (Tkinter)](#desktop-version-tkinter)
  - [Web Version (Flask)](#web-version-flask)
- [Usage](#usage)
  - [Running the Desktop Version](#running-the-desktop-version)
  - [Running the Web Version](#running-the-web-version)
- [File Structure](#file-structure)
- [Customization](#customization)
- [Contributing](#contributing)
- [License](#license)

## Installation

### Desktop Version (Tkinter)

1. **Clone the Repository**:

   ```bash
   git clone https://github.com/NurAabideen/LandUnitConverter.git
   cd LandUnitConverter
   ```

2. **Run the Desktop App**:

   The Tkinter version does not require any additional dependencies. Simply run:

   ```bash
   python app.py
   ```

### Web Version (Flask)

1. **Ensure Python 3.x and `pip` are installed**.

2. **Install Flask**:

   ```bash
   pip install Flask
   ```

3. **Run the Web App**:

   ```bash
   python app-flux.py
   ```

## Usage

### Running the Desktop Version

- Run `app.py` using Python:

  ```bash
  python app.py
  ```

- Input a value, select the units to convert from and to, and see the conversion result. Use the swap button to switch units.

### Running the Web Version

- Run `app-flux.py` using Python:

  ```bash
  python app-flux.py
  ```

- Open your web browser and navigate to `http://127.0.0.1:5000/`.

- Input a value, select the units to convert from and to, and see the conversion result. Use the swap button to switch units.

## File Structure

- `app.py`: The Tkinter-based desktop application.
- `app-flux.py`: The Flask-based web application.
- `conversion_data.py`: The conversion data used by both versions.
- `templates/index.html`: The HTML template used by the Flask web application.
- `README.md`: Documentation file.

## Customization

You can modify the `conversion_data.py` file to add, remove, or update unit conversions for both versions of the app.

## Contributing

Feel free to fork this repository, create issues, and submit pull requests. Contributions are always welcome!

## License

This project is licensed under the MIT License. See the `LICENSE` file for more details.
```
