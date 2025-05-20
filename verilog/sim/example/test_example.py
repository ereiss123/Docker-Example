import os
import cocotb
import logging
import cocotb_test.simulator
import cocotb.utils
from cocotb.regression import TestFactory
from cocotb.triggers import RisingEdge, FallingEdge, ClockCycles
from cocotb.clock import Clock

# Actual test functions cannot start with the word test
# and they must be async functions with the dut passed
async def counter_test(dut):
    # set up logging
    log = logging.getLogger("cocotb.tb")
    log.setLevel(logging.DEBUG)
    # Get handles to signals
    clk = dut.clk
    rst = dut.rst
    valid = dut.valid
    int_cnt = dut.counter # internal signal
    # Start 100 MHz clock
    clk_proc = cocotb.start_soon(Clock(clk, 10, "ns").start())
    # Assert reset for first test
    if cocotb.utils.get_sim_time("ns") == 0:
        rst.setimmediatevalue(0)
        await ClockCycles(clk, 10)
    # deassert reset
    rst.value = 1
    await RisingEdge(clk)
    assert valid.value.integer == 0
    # Counter is 10 bits and valid goes high on the when the tenth bit is high
    await ClockCycles(clk, int(2**9))
    assert valid.value.integer == 1
    # kill the clock process
    clk_proc.kill()

factory = TestFactory(counter_test)
factory.generate_tests() # make tests discoverable

# This function builds the test
def test_example():
    os.environ["SIM"] = "icarus"
    tests_dir = os.path.dirname(__file__) # get test directory
    cocotb_test.simulator.run(
        verilog_sources = [ # List vhdl sources
            os.path.join(tests_dir,"..","..","src","example.v")
        ],
        toplevel = "example", # VHDL entity name
        module = "test_example" # name of test function
    ) # To run, run "pytest example" from the sim directory