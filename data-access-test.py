import subprocess

# Define block sizes
block_sizes = ["4K", "16K", "32K", "64K", "128K"]

# Loop through each block size and run FIO with the config file
for bs in block_sizes:
    output_file = f"data-access-results/data_access_{bs}.json"  # Customize output file name per block size
    print(f"Running test with block size {bs}, saving to {output_file}")
    subprocess.run([
        "fio",
        "my-fio-tests/data-access-test.fio",  # Load parameters from your .fio file
        f"--bs={bs}",            # Override block size
        "--output-format=json",
        f"--output={output_file}" # Specify unique output file
    ])
    print(f"Completed test with block size {bs}")