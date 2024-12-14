import os
import pandas as pd

def process_and_unify_datasets(directory_path, output_file, relevant_columns=None):
    """
    Process multiple CSV files by keeping all rows, selecting relevant columns,
    and adding labels derived from file names. Outputs a unified CSV file.

    Args:
        directory_path (str): Path to the directory containing the .csv files.
        output_file (str): Path to save the unified dataset.
        relevant_columns (list): List of column names to retain.
    """
    all_data = []

    for file_name in os.listdir(directory_path):
        if file_name.endswith(".csv"):
            try:
                
                label = file_name.split("-")[-1].split(".")[0]  # E.g., "DDos" from "Friday-WorkingHours-Afternoon-DDos.pcap_ISCX.csv"
                
                file_path = os.path.join(directory_path, file_name)
                print(f"Processing file: {file_path} with label: {label}")
   
                df = pd.read_csv(file_path)

                if relevant_columns:
                    missing_columns = [col for col in relevant_columns if col not in df.columns]
                    if missing_columns:
                        print(f"Warning: Missing columns {missing_columns} in file {file_name}. Skipping this file.")
                        continue
                    df = df[relevant_columns]

                df['Label'] = label
               
                all_data.append(df)
                print(f"File {file_name} processed successfully!")

            except Exception as e:
                print(f"Error processing file {file_name}: {e}")
   
    if not all_data:
        print("No valid data to concatenate. Exiting.")
        return

    
    unified_data = pd.concat(all_data, ignore_index=True)

    
    unified_data.to_csv(output_file, index=False)
    print(f"Unified dataset saved to: {output_file}")


directory_path = r"\datasets"  
output_file = r"combined_dataset.csv" 

# Define the relevant columns to keep
relevant_columns = [
    "Destination Port", "Flow Duration", "Total Fwd Packets", "Total Backward Packets",
    "Total Length of Fwd Packets", "Total Length of Bwd Packets", "Fwd Packet Length Max",
    "Fwd Packet Length Mean", "Fwd Packet Length Std", "Bwd Packet Length Max", 
    "Bwd Packet Length Mean", "Bwd Packet Length Std", "Flow Bytes/s", "Flow Packets/s",
    "Flow IAT Mean", "Flow IAT Std", "Flow IAT Max", "Flow IAT Min", "Fwd IAT Total",
    "Fwd IAT Mean", "Fwd IAT Std", "Fwd IAT Max", "Fwd IAT Min", "Bwd IAT Total",
    "Bwd IAT Mean", "Bwd IAT Std", "Bwd IAT Max", "Bwd IAT Min", "SYN Flag Count",
    "RST Flag Count", "ACK Flag Count", "Fwd Header Length", "Bwd Header Length",
    "Subflow Fwd Packets", "Subflow Fwd Bytes", "Subflow Bwd Packets", "Subflow Bwd Bytes",
    "Active Mean", "Idle Mean"
]

process_and_unify_datasets(directory_path, output_file, relevant_columns)
