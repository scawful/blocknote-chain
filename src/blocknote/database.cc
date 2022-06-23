#include "blocknote/database.hh"

namespace blocknote {
void database::create_genesis_block() {
  block genesis_block;
  chain_database chain;
  chain.push(genesis_block);
}

void database::init() {}

void database::print() {}

void chain_database::push(const block& newblock) {}

block chain_database::get_last_block() {
  block cc;

  return cc;
}

uint64_t chain_database::height() { return 0; }

key_pair key_pair_database::get_new_key_pair() {
  key_pair key;

  return key;
}

}  // namespace blocknote