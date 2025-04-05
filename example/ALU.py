#!/usr/bin/env python3
"""
ALU Testbench using VPW
"""

import vpw

if __name__ == '__main__':
    # Create the DUT instance
    dut = vpw.create(package='ALU',  # Adjust to match your VPW package
                     module='ALU',
                     clock='clk',
                     parameter={'DATA_WIDTH': 8})

    dut.init(trace=True)

    # Reset sequence
    for _ in range(5):
        dut.tick()

    # Define ALU operations
    ALU_OPS = {
        'AND': 0b000,
        'OR': 0b001,
        'XOR': 0b010,
        'ADD': 0b011,
        'SUB': 0b100,
        'MULT': 0b101,
        'SHIFT': 0b110,  # Uses 'dir' for left/right shift
        'ROTATE': 0b111  # Uses 'dir' for left/right rotate
    }

    # Test vectors
    test_cases = [
        {'op': 'AND', 'a': 0b1010, 'b': 0b1100, 'dir': 0, 'bypass_a': 0, 'bypass_b': 0, 'expected': 0b00001000},
        {'op': 'OR', 'a': 0b1010, 'b': 0b1100, 'dir': 0, 'bypass_a': 0, 'bypass_b': 0, 'expected': 0b00001110},
        {'op': 'XOR', 'a': 0b1010, 'b': 0b1100, 'dir': 0, 'bypass_a': 0, 'bypass_b': 0, 'expected': 0b00000110},
        {'op': 'ADD', 'a': 8, 'b': 15, 'dir': 0, 'bypass_a': 0, 'bypass_b': 0, 'expected': 23},
        {'op': 'SUB', 'a': 10, 'b': 2, 'dir': 0, 'bypass_a': 0, 'bypass_b': 0, 'expected': 8},
        {'op': 'MULT', 'a': 5, 'b': 3, 'dir': 0, 'bypass_a': 0, 'bypass_b': 0, 'expected': 15},
        {'op': 'SHIFT', 'a': 0b0111, 'b': 0, 'dir': 1, 'bypass_a': 0, 'bypass_b': 0, 'expected': 0b00001110},  # Left shift
        {'op': 'SHIFT', 'a': 0b0111, 'b': 0, 'dir': 0, 'bypass_a': 0, 'bypass_b': 0, 'expected': 0b00000011},  # Right shift
        {'op': 'ROTATE', 'a': 0b1001, 'b': 0, 'dir': 1, 'bypass_a': 0, 'bypass_b': 0, 'expected': 0b00010010},  # Left rotate
        {'op': 'ROTATE', 'a': 0b1001, 'b': 0, 'dir': 0, 'bypass_a': 0, 'bypass_b': 0, 'expected': 0b10000100},  # Right rotate

        {'op': 'ROTATE', 'a': 0b1001, 'b': 0b1100, 'dir': 0, 'bypass_a': 1, 'bypass_b': 0, 'expected': 0b00001001},  # bypass a
        {'op': 'ROTATE', 'a': 0b1001, 'b': 0b1100, 'dir': 0, 'bypass_a': 0, 'bypass_b': 1, 'expected': 0b00001100},  # bypass b
    ]

    # Run test cases
    print("\nRunning ALU tests...\n")
    for test in test_cases:
        dut.prep("op", [ALU_OPS[test['op']]])
        dut.prep("a", [test['a']])
        dut.prep("b", [test['b']])
        dut.prep("dir", [test['dir']])
        io = dut.tick()
        
        # Read the output
        result = io["result"]
        result_reg = io["result_reg"]
        print(f"Test: {test['op']:6} | A: {test['a']:08b} | B: {test['b']:08b} | bypass_a: {test['bypass_a']} | bypass_B: {test['bypass_b']} | "
              f"Dir: {test['dir']} | Expected: {test['expected']:08b} | Got: {result:08b} "
              f"{'✅' if result == test['expected'] else '❌'}")
        print(f"result_reg: {result_reg:08b}")
        print("")

    # Cleanup
    dut.finish()
