import jieba
import pandas as pd
from pathlib import Path
from tqdm import tqdm
import config
from sklearn.model_selection import train_test_split
from tokenizer import JiebaTokenizer


def build_dataset(sentences,tokenizer):
    indexed_sentences = [tokenizer.encode(sentence) for sentence in sentences]  # get不到取0

    dataset = []
    # [{'input':[1,2,3,4,5],'target':5},{'input':[2,3,4,5,6],'target':7}]

    for sentence in tqdm(indexed_sentences, desc="构建测试集"):
        for i in range(len(sentence) - config.SEQ_LEN):
            input = sentence[i:i + config.SEQ_LEN]
            target = sentence[i + config.SEQ_LEN]
            dataset.append({'input': input, 'target': target})
    return dataset


def process():
    print("开始处理数据")
    # 1.读取文件
    df = pd.read_json(config.RAW_DATA_DIR/"synthesized_.jsonl",lines=True,
                      orient="records").sample(frac=0.01,random_state=42)

    # 2.提取句子
    sentences=[]
    for dialog in df['dialog']:
        for sentence in dialog:
            sentences.append(sentence.split('：')[1])
    print(f'句子总数：{len(sentences)}')

    # 3.划分数据集
    train_sentences, test_sentences = train_test_split(sentences, test_size=0.2,random_state=42)

    # 4.构建词表
    JiebaTokenizer.build_vocab(train_sentences,config.MODELS_DIR/"vocab.txt")

    # 5.构建训练集
    tokenizer = JiebaTokenizer.from_vocab(config.MODELS_DIR/"vocab.txt")
    train_dataset=build_dataset(train_sentences,tokenizer)

    # 6.保存训练集
    pd.DataFrame(train_dataset).to_json(config.PROCESSED_DATA_DIR/"train.jsonl",orient="records",lines=True)

    # 7.构建测试集
    test_dataset=build_dataset(test_sentences,tokenizer)

    # 8.保存测试集
    pd.DataFrame(test_dataset).to_json(config.PROCESSED_DATA_DIR / "test.jsonl", orient="records", lines=True)

    print("数据处理完成")


if __name__ == '__main__':
    process()