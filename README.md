# ACS-Project-3

This project requires an installation of FIO version 3+. The python files can be run directly from the root directory. All results can be found in their respective folder. The outputs of the FIO tests are directly piped into `.json` files. In addition, a helper script file `parse_data.py` is provided to extract and convert key data points (JSON to CSV). I use Excel to access the CSV files and plot points on graphs. A simple python script can also easily be written to do it all (e.g., extract and plot points). My decision to do as such was simply a matter of aesthetics. Repository breakdown:
- Output Compilation Folders
    - `/data-access-results/`
    - `/rw-intensity-results/`
    - `/queue-depth-results/`
    - `/enterprise-results/`
- `/fio-tutorial/` - a folder containing some sample examples as well as the basic getting-started guide provided by FIO. [The man page](https://linux.die.net/man/1/fio) is also a great reference even if the system you are using is not Linux (like mine).
- `/fio-generated-io-logs/` - a folder containing all generated log files by FIO when starting and running a new job. The info is good for deeper performance analysis, but were unnecessary for the purposes of this project. (cleared prior to upload for sake of space)
- `/my-fio-tests/` - a folder containing the respective fio tests, each with parameters further specified by the matching, respective python script.
    - `data-access-test.fio`
    - `rw-intensity-test.fio`
    - `queue-depth-test.fio`
    - `enterprise-test.fio`
- Said python files
    - `data-access-test.py`
    - `rw-intensity-test.py`
    - `queue-depth-test.py`
    - `enterprise-test.py`
- D7-5600 Product Specifications.xls - self explanatory, found from [Solidigm's product page](https://www.solidigm.com/products/data-center/d7/p5600.html)