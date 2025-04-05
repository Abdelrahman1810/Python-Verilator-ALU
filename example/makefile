HDL= ALU.SV
TESTBENCH= ALU.py
WAVEFORM= gtkwave
VCD_FILE=ALU.vcd
SCRIPT=waveform.gtkw
all: run sim_script

run:
	./$(TESTBENCH)
sim_script:
	$(WAVEFORM) $(VCD_FILE) $(SCRIPT) &
sim:
	$(WAVEFORM) $(VCD_FILE) &
clean:
	rm -rf ALU.cpython-312-x86_64-linux-gnu.so ALU.vcd ALU
	rm -rf vpw/__pycache__
	clear
