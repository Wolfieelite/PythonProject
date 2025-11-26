from mindmap_leaf import MindMapLeaf
from mindmap_composite import MindMapComposite

def main():
    if __name__ == "__main__":
        #ROOT of the mindmap
        root = MindMapComposite("Random Wolf Facts", "circle")

        species = MindMapComposite("Species", "oval")
        species.add(MindMapLeaf("Gray wolf", "plain"))
        species.add(MindMapLeaf("Mexican wolf", "plain"))
        species.add(MindMapLeaf("Arctic wolf", "plain"))
        species.add(MindMapLeaf("Red wolf", "plain"))
        root.add(species)

        biology = MindMapComposite("Biology", "oval")
        root.add(biology)

        locations = MindMapComposite("Locations", "oval")
        locations.add(MindMapLeaf("North America", "plain"))
        locations.add(MindMapLeaf("Canada", "plain"))
        locations.add(MindMapLeaf("Alaska", "plain"))
        root.add(locations)

        favorite_pray = MindMapComposite("Favorite Pray", "oval")
        root.add(favorite_pray)

        root.display()


if __name__ == "__main__":
    main()