#ifndef BLOCKNOTE_NODE_H
#define BLOCKNOTE_NODE_H

#include <thread>

#include "blocknote/blockchain.hh"
#include "blocknote/consensus.hh"
#include "blocknote/logging.hh"
#include "blocknote/network.hh"

namespace blocknote {

class node {
 public:
  node() noexcept { log::info("node") << "node started"; }

  node(const node&) = default;
  node(node&&) = default;

  void test();
  bool check();

  void miner_run(std::string address);

  blockchain& chain() { return blockchain_; }

 private:
  blockchain blockchain_;
  miner miner_{blockchain_};
};

}  // namespace blocknote

#endif