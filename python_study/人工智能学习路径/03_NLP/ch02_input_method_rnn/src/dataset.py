# 1.定义Dataset
import torch
import pandas as pd
import config
from torch.utils.data import Dataset,DataLoader


class InputMethodDataset(Dataset):
    def __init__(self,path):
        self.data=pd.read_json(path,orient='records',lines=True).to_dict('records')

    def __len__(self):
        return len(self.data)

    def __getitem__(self, idx):
        input_tensor = torch.tensor(self.data[idx]['input'],dtype=torch.long)
        target_tensor = torch.tensor(self.data[idx]['target'],dtype=torch.long)
        return input_tensor, target_tensor


# 2.定义一个获取dataloader的方法
def get_dataloader(train=True):
    path=config.PROCESSED_DATA_DIR/("train.jsonl" if train else "test.jsonl")
    dataset=InputMethodDataset(path)
    return DataLoader(dataset,batch_size=config.BATCH_SIZE,shuffle=train)


if __name__=="__main__":
    train_dataloader=get_dataloader()
    test_dataloader = get_dataloader(train=False)
    print(len(train_dataloader))
    print(len(test_dataloader))

    for input_tensor, target_tensor in train_dataloader:
        print(input_tensor.shape)
        print(target_tensor.shape)
        break