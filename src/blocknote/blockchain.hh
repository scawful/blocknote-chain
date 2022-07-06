#ifndef BLOCKNOTE_CHAIN_H
#define BLOCKNOTE_CHAIN_H

#include <cstdint>
#include <cstdlib>

#include "blocknote/block.hh"
#include "blocknote/database.hh"

namespace blocknote {

class blockchain {
 public:
  blockchain() = default;

  void push_block(const block& new_block);
  int get_height();
  block get_last_block();
  bool get_block(std::string block_hash, block& out);
  bool get_tx(std::string tx_hash, tx& out);
  bool get_balance(std::string address, uint64_t balance);
  void reset_pool(size_t delta);

 private:
  uint16_t id_;
  block genesis_block_;
  chain_database chain_;
  key_pair_database key_pair_database_;
};

}  // namespace blocknote

#endif