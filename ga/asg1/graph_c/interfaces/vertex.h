#ifndef VERTEX_H
#define VERTEX_H

#include <vector>
#include "iterator.h"


class Vertex {
private:
  std::vector<int> inbound;
  std::vector<int> outbound;
public:
  int label;

  Vertex(int);

  int get_degree_in(void) const;

  int get_degree_out(void) const;

  bool add_inbound(int);

  bool add_outbound(int);

  Iterator<int> get_inbound_edges_iterator() const;

  Iterator<int> get_outbound_edges_iterator() const;

  void remove_inbound(int);

  void remove_outbound(int);
};

#endif
