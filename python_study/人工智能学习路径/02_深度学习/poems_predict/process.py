import re

def preprocess(file_path):
    print("开始处理数据")
    char_set=set()
    poems=[]
    with open(file_path,"r",encoding="utf-8") as f:
        for line in f:
            line = re.sub(r"[，。？！、：]", "", line)
            char_set.update(list(line))
            poems.append(line)
        index2word=['<unk>']+list(char_set)
        word2index={word:index for index,word in enumerate(index2word)}
        id_seqs=[]
        for poem in poems:
            id_seq=[word2index.get(word) for word in poem]
            id_seqs.append(id_seq)
        return id_seqs,index2word,word2index

if __name__ == "__main__":
    id_seqs, index2word, word2index = preprocess("../poems.txt")
    print(id_seqs, index2word, word2index)

