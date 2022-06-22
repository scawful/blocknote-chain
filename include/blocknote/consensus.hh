#ifndef BLOCKNOTE_CONSENSUS_H
#define BLOCKNOTE_CONSENSUS_H

#include <iostream>

#include "blocknote/block.hh"
#include "blocknote/blockchain.hh"
#include "blocknote/transaction.hh"

namespace blocknote {

class miner {
 public:
  miner(blockchain& chain) : chain_(chain){};
  miner(const miner&) = default;
  miner(miner&&) = default;

  void print() { std::cout << "class miner" << std::endl; }

  void start(std::string& addr);
  inline bool pow_once(block& new_block, std::string& addr);

  tx create_coinbase_tx(std::string& addr);
  tx create_binance_tx(std::string& addr);

 private:
  blockchain& chain_;
};

bool validate_tx(const tx& new_tx);

bool validate_block(const tx& new_block);

}  // namespace blocknote

#endif
