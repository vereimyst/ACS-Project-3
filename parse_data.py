import json
import csv
import glob
import os

# Specify the folder containing JSON files, CSV output filename, and CSV headers
# -------------------- data access --------------------
# folder_path = "data-access-results"
# csv_filename = os.path.join(folder_path, "data_access_results.csv")
# csv_headers = ["Block Size", "Read Speed (MBPS)", "Write Speed (MBPS)", 
#                 "Read Latency (ns)", "Write Latency (ns)"]

# -------------------- rw intensity --------------------
# folder_path = "rw-intensity-results"
# csv_filename = os.path.join(folder_path, "rw_intensity_results.csv")
# csv_headers = ["Block Size", "Read Percentage", "Read Speed (MBPS)", 
#                 "Write Speed (MBPS)", "Read Latency (ns)", "Write Latency (ns)"]

# -------------------- queue depth --------------------
# folder_path = "queue-depth-results"
# csv_filename = os.path.join(folder_path, "queue_depth_results.csv")
# csv_headers = ["Block Size", "I/O Depth", "Read Speed (MBPS)", 
#                 "Write Speed (MBPS)", "Read Latency (ns)", "Write Latency (ns)"]

# -------------------- enterprise --------------------
folder_path = "enterprise-results"
csv_filename = os.path.join(folder_path, "enterprise_results.csv")
csv_headers = ["Seq Read (MBPS)", "Seq Write (MBPS)", "Random Read (IOPS)", 
                "Random Write (IOPS)"]


# Open the specified CSV file for writing
with open(csv_filename, mode="w", newline="") as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow(csv_headers)
    
    # Iterate over JSON files in the specified folder
    for file in glob.glob(os.path.join(folder_path, "*.json")):
        try:
            with open(file, "r") as json_file:
                data = json.load(json_file)
                
                # Extract metrics from JSON & Write row to CSV

                # -------------------- data access --------------------
                # block_size = data["global options"]["bs"]
                # r_speed = data["jobs"][0]["read"]["bw_mean"] / 1024  # To MB/s
                # r_latency = data["jobs"][0]["read"]["lat_ns"]["mean"]
                # w_speed = data["jobs"][1]["write"]["bw_mean"] / 1024  # To MB/s
                # w_latency = data["jobs"][1]["write"]["lat_ns"]["mean"]
                # writer.writerow([block_size, r_speed, w_speed, r_latency, w_latency])

                # -------------------- rw intensity --------------------
                # block_size = data["global options"]["bs"]
                # for i in range(0, 11):
                #     if "rwmixread" in data["jobs"][i]["job options"]:
                #         r_percentage = data["jobs"][i]["job options"]["rwmixread"]
                #     elif data["jobs"][i]["job options"]["rw"] == "read":
                #         r_percentage = 100
                #     else:
                #         r_percentage = 0
                #     r_speed = data["jobs"][i]["read"]["bw_mean"] / 1024  # To MB/s
                #     w_speed = data["jobs"][i]["write"]["bw_mean"] / 1024  # To MB/s
                #     r_latency = data["jobs"][i]["read"]["lat_ns"]["mean"]
                #     w_latency = data["jobs"][i]["write"]["lat_ns"]["mean"]
                #     writer.writerow([block_size, r_percentage, r_speed, w_speed, 
                #                     r_latency, w_latency])

                # -------------------- queue depth --------------------
                # block_size = data["global options"]["bs"]
                # for i in range(0, 11):
                #     iodepth = data["jobs"][i]["job options"]["iodepth"]
                #     r_speed = data["jobs"][i]["read"]["bw_mean"] / 1024  # To MB/s
                #     r_latency = data["jobs"][i]["read"]["lat_ns"]["mean"]
                #     w_speed = data["jobs"][i+11]["write"]["bw_mean"] / 1024  # To MB/s
                #     w_latency = data["jobs"][i+11]["write"]["lat_ns"]["mean"]
                #     writer.writerow([block_size, iodepth, r_speed, w_speed, 
                #                     r_latency, w_latency])

                # -------------------- enterprise --------------------
                seqr_speed = data["jobs"][0]["read"]["bw_mean"] / 1024  # To MB/s
                seqw_speed = data["jobs"][1]["write"]["bw_mean"] / 1024  # To MB/s
                randr_speed = data["jobs"][2]["read"]["bw_mean"]
                randw_speed = data["jobs"][3]["write"]["bw_mean"]
                writer.writerow([seqr_speed, seqw_speed, randr_speed, randw_speed])
                

        except (json.JSONDecodeError, KeyError) as e:
            print(f"Skipping {file} due to error: {e}")

print(f"Data has been extracted to {csv_filename}")
