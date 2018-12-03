#include <fstream>
#include <iostream>
#include <map>
#include <sstream>
#include <string>
#include <vector>

int main() {

  std::string line;
  std::ifstream input_file("./input/01.txt");
  if (!input_file.is_open()) {
    std::cout << "file not found" << std::endl;
    return 1;
  }

  std::vector<std::string> rows;
  while (!input_file.eof()) {
    getline(input_file, line);
    if (!line.empty()) {
      rows.push_back(line);
    }
  }
  input_file.close();

  // implementation
  int sum = 0;
  bool done = false;
  std::map<int, bool> visited;

  while (!done) {
    for (int i = 0; i < rows.size(); i++) {
      std::istringstream ss(rows[i]);
      int j;
      ss >> j;
      sum += j;
      if (visited.find(sum) != visited.end()) {
        std::cout << sum << std::endl;
        done = true;
        break;
      }
      visited[sum] = true;
    }
  }

  return 0;
}
