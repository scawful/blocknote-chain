#ifndef BLOCKNOTE_COMMANDS_H
#define BLOCKNOTE_COMMANDS_H

#include <string>
#include <vector>

#include "blocknote/node.hh"

namespace blocknote {

class commands {
 public:
  typedef std::vector<std::string> vargv_t;
  commands(const vargv_t& vargv, node& node) : vargv_(vargv), node_(node) {}

  commands(const commands&) = default;
  commands(commands&&) = default;

  bool exec(std::string& out);

  static const vargv_t commands_list;

 private:
  const vargv_t& vargv_;
  node& node_;
};

}  // namespace blocknote

#endif