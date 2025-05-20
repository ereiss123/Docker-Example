`timescale 1ns/1ps

module example(
    input clk,
    input rst,
    output reg valid
);
    reg [9:0] counter;
    assign valid = counter[9];
    always @(posedge clk) begin
        if(!rst) begin
            counter <= 0;
        end else begin
            counter <= counter + 1;
        end
    end
endmodule;