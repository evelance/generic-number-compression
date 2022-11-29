CXX    := g++
CFLAGS := -Wall -Wextra

all: calc_table.py testfloat.dat testint.dat
	python $^

testfloat.dat: generate_float32_in_64b
	./$^

testint.dat: generate_int8_in_64b
	./$^

generate_float32_in_64b: generate_float32_in_64b.cpp
	$(CXX) $(CFLAGS) -o $@ $^

generate_int8_in_64b: generate_int8_in_64b.cpp
	$(CXX) $(CFLAGS) -o $@ $^

clean:
	rm -f generate_float32_in_64b generate_int8_in_64b *.dat*

.PHONY: all clean

