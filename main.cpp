#include <fstream>
#include <iostream>
#include <string>


std::string loadinput(std::string file) {
    std::string line;
    std::ifstream input("input/" + file);
    std::getline(input, line);
    input.close();

}

int main() {

}