#include <fstream>
// WARNING: No error checking is done here!
// This example is for illustrative purposes only.

#include <iostream>
#include <vector>
#include "lib/so_lpf.h"

static const std::string FILENAME{"output.csv"};

int main() {
  std::ofstream f(FILENAME, std::ios_base::out | std::ios::trunc);
  std::cout << "Computing step response into \"" << FILENAME << "\"...\n";

  // Input data: 10x of 0.0 and 500x of 1.0
  std::vector<float> in(10, 0.0);
  in.insert(in.end(), 500, 1.0);

  // Create the filter
  SO_LPF lpf;
  lpf.calculate_coeffs(2.0, 5.0, 375.0);

  // Process and output  data
  f << std::fixed;
  for (auto val : in) {
    f << lpf.process(val) << "\n";
  }

  std::cout << "Done!\n";
  return 0;
}