# Author: Jason Lu

import random
from enum import Enum

TreeType = Enum('TreeType', 'apple_tree cherry_tree peach_tree')

class Tree(object):
    pool = dict()

    def __new__(cls, tree_type):
        obj = cls.pool.get(tree_type, None)

        if not obj:
            obj = object.__new__(cls)
            cls.pool[tree_type] = obj
            obj.tree_type = tree_type

        return obj

    def render(self, age, x, y):
        print('render a4 tree of type {} and age {} at ({}, {})'.format(
            self.tree_type,
            age,
            x,
            y
        ))


def main():
    rnd = random.Random()
    age_min, age_max = 1, 30
    min_point, max_point = 0, 100
    tree_count = 0

    for _ in range(10):
        t1 = Tree(TreeType.apple_tree)
        t1.render(rnd.randint(age_min, age_max),
                  rnd.randint(min_point, max_point),
                  rnd.randint(min_point, max_point))
        tree_count += 1

    for _ in range(3):
        t1 = Tree(TreeType.cherry_tree)
        t1.render(rnd.randint(age_min, age_max),
                  rnd.randint(min_point, max_point),
                  rnd.randint(min_point, max_point))
        tree_count += 1

    for _ in range(5):
        t1 = Tree(TreeType.peach_tree)
        t1.render(rnd.randint(age_min, age_max),
                  rnd.randint(min_point, max_point),
                  rnd.randint(min_point, max_point))
        tree_count += 1

    print('trees rendered: {}'.format(tree_count))
    print('trees actually created: {}'.format(len(Tree.pool)))


    t4 = Tree(TreeType.cherry_tree)
    t5 = Tree(TreeType.cherry_tree)
    t6 = Tree(TreeType.apple_tree)
    print('{} == {}?{}'.format(id(t4), id(t5), id(4) == id(5)))
    print('{} == {}?{}'.format(id(t5), id(t6), id(6) == id(5)))


if __name__ == '__main__':
    main()













