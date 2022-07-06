#ifndef BLOCKNOTE_BLOCK_H
#define BLOCKNOTE_BLOCK_H

#include <string>
#include <vector>

#include "transaction.hh"

namespace blocknote {

class block {
 public:
  using tx_list_t = std::vector<tx>;

  struct blockheader {
    uint64_t nonce{0};
    uint64_t height{0};
    uint64_t timestamp{0};
    uint64_t tx_count{0};
    uint64_t difficulty{0};
    std::string current_hash;
    std::string hex_bloom_root_hash;
    std::string prev_hash;
  };

  block() = default;
  ~block() = default;
  explicit block(uint64_t h) { header_.height = h; }

  void print();
  tx_list_t tx_list() const;
  blockheader header() const;
  std::string hash() const;

  void setup(tx_list_t& txs);

 private:
  tx_list_t tx_list_;
  blockheader header_;
};

}  // namespace blocknote

#endif