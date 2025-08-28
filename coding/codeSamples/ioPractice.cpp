#include <iostream>

int main(){
    std::cout << "Hello What is your name? \n";
    std::string name{};
    std::cin >> name;
    std::cout << "Hello " + name + "\n";
    return 0;
}
