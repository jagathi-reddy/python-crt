b = {
  "seq001": "ATGCGGAATT",
  "seq002": "CGTACGTAGC",
  "seq003": "TTATGCATTA",
  "seq004": "GGAATCCGTA",
  "seq005": "CATGCCGTAGC",
  "seq006": "GGGCGTGCAT",
  "seq007": "AATGCTAGCTA",
  "seq008": "CGCGATGCGC",
  "seq009": "TATATATATA",
  "seq010": "ATGCGGATGCA"
}

query = input("Enter a sequence to search for: ")

found = False
for seq_id, sequence in b.items():
    if query in sequence:
        print(f"Query found in {seq_id}: {sequence}")
        found = True

if not found:
    print("Query not found in any sequence.")