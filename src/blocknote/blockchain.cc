#include "blocknote/blockchain.hh"

namespace blocknote {

block blockchain::get_last_block() { return chain_.get_last_block(); }

bool blockchain::get_block(std::string block_hash, block& b) {
  if (!chain_.get_block(block_hash, b)) {
    return false;
  }
  return true;
}

int blockchain::get_height() { return chain_.height(); }

bool blockchain::get_balance(std::string address, uint64_t balance) {
  return true;
}

bool blockchain::get_tx(std::string tx_hash, tx& t) {
  if (!chain_.get_tx(tx_hash, t)) {
    return false;
  }
  return true;
}

}  // namespace blocknote
