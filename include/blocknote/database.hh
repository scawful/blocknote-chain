#ifndef BLOCKNOTE_DATABASE_H
#define BLOCKNOTE_DATABASE_H

#include <algorithm>
#include <filesystem>

#include "blocknote/block.hh"

namespace blocknote {

class database {
 public:
  virtual void print();
  void init();
  void create_genesis_block();
};

class chain_database : public database {
 public:
  // inesert block into database
  void push(const block& newblock);

  uint64_t height();

  block get_last_block();

  bool get_block(const std::string block_hash, block& b) { return true; }

  bool get_tx(const std::string tx_hash, tx& t) { return true; }
};
struct key_pair {
  int key;
  void *value;
};
class key_pair_database : public database {
 public:
  uint64_t height();
  key_pair get_new_key_pair();
};

}  // namespace blocknote

#endif