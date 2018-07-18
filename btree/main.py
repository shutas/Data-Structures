# -*- coding: utf-8 -*-
"""Sample program that uses BNode and BTree."""

# Written by Shuta Suzuki

from btree import BNode, BTree

def main():
    """Create a BTree and add a few BNodes."""
    # Create BNodes
    kotei = BNode("固定資産")

    mukei = BNode("無形固定資産", kotei)
    yukei = BNode("有形固定資産", kotei)

    tochi = BNode("土地", yukei)
    tatemono = BNode("建物", yukei)
    kouchiku = BNode("構築物", yukei)

    # Create BTree with kotei BNode as root node
    tree = BTree(kotei)

    # Construct BTree
    tree.insert(mukei)
    tree.insert(yukei)
    tree.insert(tochi)
    tree.insert(tatemono)
    tree.insert(kouchiku)


    #tree.locate("建物")

if __name__ == "__main__":
    main()