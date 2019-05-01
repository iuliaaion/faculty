//
// Created by andreib on 27.04.2019.
//

#ifndef ASG6_MAPITERATOR_H
#define ASG6_MAPITERATOR_H

#include "Map.h"
#include "HashTable.h"


class Map;
typedef std::pair<int, int> TElem;

class MapIterator {

friend class Map;

private:
    explicit MapIterator(const Map&);

    const Map& map;
    int idx{};
public:
    void first();

    void next();

    bool valid() const;

    TElem getCurrent() const;
};


#endif //ASG6_MAPITERATOR_H
