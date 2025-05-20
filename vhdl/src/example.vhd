library ieee;
context ieee.IEEE_STD_CONTEXT;

entity example is
    port (
        clk   : in std_logic;
        rst : in std_logic;
        valid : out std_logic
    );
end entity example;

architecture rtl of example is
    signal counter : unsigned(9 downto 0) := (others => '0') ;
begin
    cnt_proc : process(clk) begin
        if rising_edge(clk) then
            if rst = '0' then
                counter <= (others => '0') ;
            else
                counter <= counter + 1;
            end if;
        end if;
    end process;
    valid <= counter(9);
end architecture;
