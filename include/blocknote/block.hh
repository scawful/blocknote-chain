#ifndef BLOCKNOTE_BLOCK_H
#define BLOCKNOTE_BLOCK_H

#include <string>

namespace blocknote {
namespace block {

class Block {
 public:
  void create_block();
  int get_index();
  std::string get_hash();

 private:
  int index_;
  std::string previous_hash_;
  std::string current_hash_;
  std::string nonce_;
};

}  // namespace block
}  // namespace blocknote

#endif