#ifndef BLOCKNOTE_NETWORK_H
#define BLOCKNOTE_NETWORK_H

#include <iostream>
#include <string>

namespace blocknote {

void ws_send(std::string&& msg);

class network {
 public:
  network() noexcept = default;
  network(const network&) noexcept = default;
  network(network&&) noexcept = default;
  network& operator=(network&&) noexcept = default;
  network& operator=(const network&) noexcept = default;

  void print() { std::cout << "class network" << std::endl; }
  void test();

 private:
};

}  // namespace blocknote

#endif