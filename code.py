def replaceWords(dict, sentence):
    trie = {}
    for root_word in dict:
        node = trie
        for c in root_word:
            if c not in node:
                node[c] = {}
            node = node[c]
        node['#'] = True
    
    words = sentence.split()
    result = []
    for word in words:
        current = trie
        prefix = []
        found = False
        for c in word:
            if c not in current:
                break
            current = current[c]
            prefi