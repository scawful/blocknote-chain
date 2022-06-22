#include "blocknote/block.hh"

#include <iostream>

namespace blocknote {

void block::print() { std::cout << "class block" << std::endl; }
block::tx_list_t block::tx_list() const { return tx_list_; }
block::blockheader block::header() const { return header_; }
std::string block::hash() const { return header_.current_hash; }
void block::setup(tx_list_t& txs) { tx_list_.swap(txs); }

}  // namespace blocknote
