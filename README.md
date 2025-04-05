# Python-Verilator-ALU

> [!NOTE]
> it's a simple example as a kick-start

This repository provides a **Verilator-based** testbench for an **ALU (Arithmetic Logic Unit)**, using **VPW (Verilator Python Wrapper)**. It includes a Python testbench that verifies various ALU operations.

## 📌 Features
- Implements an **8-bit ALU** supporting:
  - `AND`, `OR`, `XOR`
  - `ADD`, `SUB`, `MULT`
  - `BYPASS_A` (high priority), `BYPASS_B` (low priority)
  - `SHIFT` (left/right based on `dir`)
  - `ROTATE` (left/right based on `dir`)
- **VPW-based testbench** to automate verification.
- **Bash script (`setup.sh`)** to install dependencies and run tests automatically.
- Uses **Verilator** for simulation and **GTKWave** for waveform viewing.

---

## 🚀 Setup & Installation

### 1️⃣ Prerequisites
Ensure your system has **Ubuntu** (or a compatible Linux distribution) and that you have `git` installed.

```sh
sudo apt update
sudo apt install git -y
```

### 2️⃣ Clone the Repository

```sh
git clone https://github.com/Abdelrahman1810/Python-Verilator-ALU.git
cd Python-Verilator-ALU
```
### 3️⃣ Run the Setup Script
This will install dependencies, extract the virtual environment, and run the testbench.

```sh
chmod +x setup.sh
source setup.sh
```

## 📜 File Structure
```
📂 ALU-Testbench/
│── 📂 example/             
│── ├── ALU.py              
│── ├── 📂 hdl/
│── ├── │── ALU.SV          
│── ├── 📂 vpw/
│── ├── │── __init__.py
│── ├── │── testbench.hh
│── setup.sh    
│── README.md           
│── Verilator.pdf       
```

## 🛠 Running the Testbench

Once the setup is complete, you can manually re-run the testbench:

```sh
source ~/venv/bin/activate   # Activate the Python virtual environment
cd example
make run                     # Compile and Run the ALU testbench
```
## To analyze simulation waveforms, use:

```sh
make sim                     # simulation waveform on GTKWave without script
make sim_script              # simulation waveform on GTKWave with script
```

> [!IMPORTANT]
> - If you modify the ALU design (ALU.v), you need to recompile it with Verilator.
> - The Bash script (setup.sh) automates everything, so you don’t have to install dependencies manually.
> - to deactivate the vertiual environment you can run command

## 🤝 Contributing

Feel free to fork this repository and submit pull requests! Any enhancements to the testbench or ALU design are welcome.


## ⚖️ License
This project is open-source under the MIT License.

## 🙌 Acknowledgments
Special thanks to **[Mr.Martini](https://www.linkedin.com/in/berin-martini/)** for their valuable help and contributions to this project!

---
