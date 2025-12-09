from mindmap_leaf import MindMapLeaf
from mindmap_composite import MindMapComposite

# Step 6: Create MindMapComposite and MindMapLeaf objects to test
root = MindMapComposite("Root", "circle")
leaf1 = MindMapLeaf("Child 1", "square")
leaf2 = MindMapLeaf("Child 2", "cloud")
root.add(leaf1)
root.add(leaf2)

#print(str(root)) # Should display "((Root))"
root.display()    # Should display root and its children

print("MindMapComposite tests completed!")