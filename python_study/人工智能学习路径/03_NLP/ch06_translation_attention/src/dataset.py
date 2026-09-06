# 1.定义Dataset
import pandas as pd
import torch
from torch.nn.utils.rnn import pad_sequence
import config
from torch.utils.data import Dataset, DataLoader


class TranslationDataset(Dataset):
    def __init__(self, path):
        self.data = pd.read_json(path, orient='records', lines=True).to_dict('records')

    def __len__(self):
        return len(self.data)

    def __getitem__(self, idx):
        input_tensor = torch.tensor(self.data[idx]['zh'], dtype=torch.long)
        target_tensor = torch.tensor(self.data[idx]['en'], dtype=torch.long)
        return input_tensor, target_tensor


# 2.定义一个获取dataloader的方法

def collate_fn(batch):
    # batch: 二元组列表:[(input_tensor,target_tensor)]
    input_tensor = [item[0] for item in batch]
    target_tensor = [item[1] for item in batch]

    input_tensor = pad_sequence(input_tensor, batch_first=True, padding_value=0)
    target_tensor = pad_sequence(target_tensor, batch_first=True, padding_value=0)

    return input_tensor, target_tensor

def get_dataloader(train=True):
    path = config.PROCESSED_DATA_DIR / ("train.jsonl" if train else "test.jsonl")
    dataset = TranslationDataset(path)
    return DataLoader(dataset, batch_size=config.BATCH_SIZE, shuffle=train, collate_fn=collate_fn)


if __name__ == "__main__":
    train_dataloader = get_dataloader()
    test_dataloader = get_dataloader(train=False)
    print(len(train_dataloader))
    print(len(test_dataloader))

    for input_tensor, target_tensor in train_dataloader:
        print(input_tensor.shape)
        print(target_tensor.shape)
        break
