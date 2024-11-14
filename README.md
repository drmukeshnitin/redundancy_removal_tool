Here's a README file for your FASTA Redundancy Checker tool:

---

# Redundancy Removal Tool

## Overview

The FASTA Redundancy Removal Tool is a GUI-based Python application that allows users to remove redundant sequences from a FASTA file, keeping only the longest sequence for each unique ID. This tool is built with `Tkinter` for the graphical interface and `Biopython` for sequence processing. It provides a polished interface with a colorful background, easy file selection, and a downloadable output file.

## Features

- **Remove Redundant Sequences**: Retains only the longest sequence for each unique ID in the provided FASTA file.
- **Simple GUI**: Uses `Tkinter` for a user-friendly, interactive experience.
- **Downloadable Output**: Generates a filtered FASTA file with a "Download Output" option for saving results.
- **Aesthetic Design**: Features a colorful and high-end GUI with intuitive buttons and messaging.

## Installation

### Requirements

1. Python 3.x
2. [Biopython](https://biopython.org/)
3. Tkinter (included with most Python installations)

### Installation Steps

1. Clone this repository or download the Python script.
2. Install the required libraries using pip:
   ```bash
   pip install biopython
   ```

## Usage

1. **Run the Script**: Start the application by running the Python script.
   ```bash
   python fasta_redundancy_checker.py
   ```

2. **Select FASTA File**: Click on "Select FASTA File" to open a file dialog and choose the input FASTA file.

3. **Remove Redundancy**: The tool will process the selected file, removing redundant sequences and keeping the longest sequence for each unique ID.

4. **Download Output**: Once the redundancy check is complete, the "Download Output" button will be enabled. Click this button to save the output file to your chosen location.

## Example

1. Launch the application.
2. Select an input FASTA file.
3. The tool will notify you when the redundancy check is complete.
4. Click "Download Output" to save the processed file.

## Code Overview

The application consists of the following main functions:

- `remove_redundancy(input_fasta, output_fasta="redundancy_check.fasta")`: Processes the FASTA file to remove redundant sequences, keeping only the longest sequence for each unique ID.
- `select_file()`: Opens a file dialog for selecting the input FASTA file.
- `download_output()`: Allows the user to save the processed output file to a specified location.

## Troubleshooting

- Ensure you have `Biopython` installed. If not, install it using:
  ```bash
  pip install biopython
  ```
- If Tkinter is not working, verify that your Python installation includes Tkinter (usually pre-installed with Python).

## Dependencies

- [Biopython](https://biopython.org/): For sequence processing.
- Tkinter: For the GUI interface (comes with most Python distributions).

## License

This project is licensed under the MIT License.
Copyright (c) 2019-2024 Othneil Drew

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

## Contact

For any questions or suggestions, please feel free to contact email-drmukeshnitin@gmail.com

---

Enjoy using the FASTA Redundancy Removal Tool!
