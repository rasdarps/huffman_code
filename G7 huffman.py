import heapq
from collections import defaultdict

class Node:
    def __init__(self, char=None, freq=0, left=None, right=None):
        self.char = char
        self.freq = freq
        self.left = left
        self.right = right

    def __lt__(self, other):
        return self.freq < other.freq

    def __eq__(self, other):
        if other is None:
            return False
        if not isinstance(other, Node):
            return False
        return self.char == other.char and self.freq == other.freq

def build_huffman_tree(text):
    # Count the frequency of each character in the text using a defaultdict
    freq = defaultdict(int)
    for char in text:
        freq[char] += 1

    # Build a priority queue of nodes, where the priority is based on the frequency of each character
    pq = []
    
    print("\nFrequency table:")
    print("Character | Frequency")
    print("--------------------")
    for char, freq in freq.items():
        print(f"{char}         | {freq}")
        heapq.heappush(pq, Node(char=char, freq=freq))

    # Build the Huffman tree by repeatedly merging the two nodes with the smallest frequencies into a single parent node
    while len(pq) > 1:
        left = heapq.heappop(pq)
        right = heapq.heappop(pq)
        parent = Node(char=None, freq=left.freq+right.freq, left=left, right=right)
        heapq.heappush(pq, parent)

    # The final node in the priority queue is the root of the Huffman tree
    return pq[0]

def build_huffman_table(node, prefix="", table={}):
    # Recursively build the Huffman table by traversing the tree
    if node is None:
        return
    if node.char is not None:
        # Add the code for each character to the table when a leaf node is reached
        table[node.char] = prefix
    build_huffman_table(node.left, prefix+"0", table)
    build_huffman_table(node.right, prefix+"1", table)

def draw_huffman_tree(node, prefix="", is_left=True):
    # Recursively draw the Huffman tree using ASCII art
    if node is None:
        return

    draw_huffman_tree(node.right, prefix + ("│   " if is_left else "    "), False)
    print(prefix + ("└── " if is_left else "┌── ") + str(node.freq) + (f" ({node.char})" if node.char is not None else ""))
    draw_huffman_tree(node.left, prefix + ("    " if is_left else "│   "), True)

def huffman_encoding(text):
    if len(text) == 0:
        return "", None

    # Build the Huffman tree and table for the text
    root = build_huffman_tree(text)
    table = {}
    build_huffman_table(root, "", table)

    # Encode the text using the Huffman table
    encoded_text = "".join([table[char] for char in text])
    return encoded_text, root

def huffman_decoding(encoded_text, root):
    if root is None:
        return ""

    # Decode the text by traversing the Huffman tree
    decoded_text = []
    node = root
    for bit in encoded_text:
        if bit == "0":
            node = node.left
        else:
            node = node.right
        if node.char is not None:
            decoded_text.append(node.char)
            node = root
    return "".join(decoded_text)
print('====================================')
print(' ID      : Name')
print('====================================')
print('11005094 : Matthew Yankey')
print('11005180 : Elorm Vidza')
print('11005259 : Danny Ofori Saah')
print('11004990 : Joseph Goldman-Akrofi')
print('11361290 : Alex K. Ayensu Darpah')
print('11008296 : Evans Djangbah')
print('11010381 : Philip Baba')
print('11009273 : Nyankom Patrick Boafo')
print('11004756 : Mercy Tettey')
print('====================================')
# Accept user input
text = input("Enter a string: ")

# Encode the text
encoded_text, root = huffman_encoding(text)

# Print the Huffman codes for each character
table = {}
build_huffman_table(root, "", table)
print("\nHuffman codes:")
for char, code in table.items():
    print(f"{char}: {code}")

# Print the encoded text
print("\nEncoded text: ", encoded_text)

#new line
total_bits = len(encoded_text)
print("\nTotal encoded text bit length: ", total_bits)

# Decode the encoded text
decoded_text = huffman_decoding(encoded_text, root)
print("\nDecoded text:", decoded_text)

# Draw the Huffman tree
print("\nHuffman tree:")
draw_huffman_tree(root)
