import tkinter as tk
from tkinter import filedialog, messagebox
from Bio import SeqIO
import os

def remove_redundancy(input_fasta, output_fasta="redundancy_check.fasta"):
    
    #Removes redundant sequences in a FASTA file, keeping the longest sequence for each unique ID.
    #Writes the filtered sequences to an output FASTA file.
    
    id_sequence_dict = {}

    for record in SeqIO.parse(input_fasta, "fasta"):
        seq_id = record.id
        seq_str = str(record.seq)
        
        # Check if the ID is already present in the dictionary
        if seq_id in id_sequence_dict:
            # If the sequence is different, keep the longer one
            if len(seq_str) > len(id_sequence_dict[seq_id]):
                id_sequence_dict[seq_id] = seq_str  # Keep the longer sequence
        else:
            # Add new ID and sequence to the dictionary
            id_sequence_dict[seq_id] = seq_str

    # Write the filtered records to the output file
    with open(output_fasta, "w") as output_handle:
        for seq_id, seq_str in id_sequence_dict.items():
            output_handle.write(f">{seq_id}\n{seq_str}\n")

    messagebox.showinfo("Success", f"Redundancy check completed!\nOutput saved as '{output_fasta}'.")
    download_button.config(state="normal")  # Enable download button after completion

def select_file():
    
    #Opens a file dialog to select the input FASTA file and runs the redundancy removal.
    
    input_fasta = filedialog.askopenfilename(
        title="Select FASTA File",
        filetypes=[("FASTA files", "*.fasta *.fa"), ("All files", "*.*")]
    )
    if input_fasta:
        remove_redundancy(input_fasta)

def download_output():
    
    #Allows user to save the output file to a selected location.
    
    output_fasta = "redundancy_check.fasta"
    if os.path.exists(output_fasta):
        destination = filedialog.asksaveasfilename(
            defaultextension=".fasta",
            filetypes=[("FASTA files", "*.fasta"), ("All files", "*.*")],
            title="Save Output As"
        )
        if destination:
            os.rename(output_fasta, destination)
            messagebox.showinfo("Download", "File downloaded successfully!")

# GUI Setup
root = tk.Tk()
root.title("FASTA Redundancy Checker")
root.geometry("500x400")
root.config(bg='#3d3d5c')

# Title Label
label = tk.Label(root, text="Redundancy Removal Tool", font=("Arial", 18, "bold"), fg="#ffffff", bg="#3d3d5c")
label.pack(pady=30)

# Select File Button
select_button = tk.Button(root, text="Select FASTA File", command=select_file, font=("Arial", 14, "bold"), fg="#ffffff", bg="#4d79ff", width=20)
select_button.pack(pady=20)

# Download Button
download_button = tk.Button(root, text="Download Output", command=download_output, font=("Arial", 14, "bold"), fg="#ffffff", bg="#4d79ff", width=20)
download_button.config(state="disabled")  # Initially disabled
download_button.pack(pady=20)

# Start GUI Loop
root.mainloop()
