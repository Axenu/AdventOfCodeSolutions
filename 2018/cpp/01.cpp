#include <fstream>
#include <iostream>
#include <sstream>
#include <string>

int main() {

  std::string line;
  std::ifstream input_file("./input/01.txt");
  if (!input_file.is_open()) {
    std::cout << "file not found" << std::endl;
    return 1;
  }

  // implementation
  int sum = 0;

  while (!input_file.eof()) {
    getline(input_file, line);
    // handle row
    if (!line.empty()) {
      std::istringstream ss(line);
      int i;
      ss >> i;
      sum += i;
    }
  }
  std::cout << sum << std::endl;

  input_file.close();

  return 0;
}
