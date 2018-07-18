# -*- coding: utf-8 -*-
"""Sample program that uses BNode and BTree."""

# Written by Shuta Suzuki

from btree import BNode, BTree

def main():
    """Create a BTree and add a few BNodes."""
    tree = BTree(BNode("固定資産"))

    #tree.insert(BNode("無形固定資産", "固定資産"))
    #tree.insert(BNode("有形固定資産", "固定資産"))
    #tree.insert(BNode("土地", "有形固定資産"))
    #tree.insert(BNode("建物", "有形固定資産"))
    #tree.insert(BNode("構築物", "有形固定資産"))

    #tree.locate("建物")

if __name__ == "__main__":
    main()