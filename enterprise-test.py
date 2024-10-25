import subprocess

# Loop through each block size and run FIO with the config file
output_file = f"enterprise-results/enterprise.json"  # Customize output file name per block size
print(f"Running test, saving to {output_file}")
subprocess.run([
    "fio",
    "my-fio-tests/enterprise-test.fio",  # Load parameters from your .fio file
    "--output-format=json",
    f"--output={output_file}" # Specify unique output file
])
print(f"Completed test")