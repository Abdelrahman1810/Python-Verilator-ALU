`ifndef _ALU_
`define _ALU_

`default_nettype none

module ALU #(
    parameter DATA_WIDTH = 8
) (
    input wire clk,
    input  logic [2:0] op,       // Operation select
    input  logic [DATA_WIDTH-1:0] a, b,     // Input operands
    input  logic       dir,      // Direction signal for SHIFT/ROTATE
    input logic bypass_a, bypass_b,
    output logic [DATA_WIDTH-1:0] result, result_reg
);
// logic [DATA_WIDTH-1:0] out;    // ALU result
    always @(*) begin
        case (op)
            3'b000: result = a & b;                      // AND
            3'b001: result = a | b;                      // OR
            3'b010: result = a ^ b;                      // XOR
            3'b011: result = a + b;                      // ADD
            3'b100: result = a - b;                      // SUB
            3'b101: result = a * b;                      // MULT
            3'b110: result = dir ? (a << 1) : (a >> 1);  // SHIFT left/right
            3'b111: result = dir ? {result[DATA_WIDTH-2:0], result[DATA_WIDTH-1]} : {result[0], result[DATA_WIDTH-1:1]}; // ROTATE
        endcase

        // BYPASS conditions
        if (bypass_a) begin
            result = a;
        end else if (bypass_b) begin
            result = b;
        end
    end

    always @(posedge clk) begin
        result_reg = result;
    end
endmodule

`default_nettype wire

`endif //  `ifndef _example_