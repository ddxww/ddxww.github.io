from datasets import Dataset
import torch
import torch.nn as nn

class PoetryDataset(Dataset):
    def __init__(self, id_seqs, seqs_len):
        self.seqs_len = seqs_len
        self.data = []
        for id_seq in id_seqs:
            for i in range(0, len(id_seq) - self.seqs_len):
                self.data.append((id_seq[i:i + self.seqs_len], id_seq[i + 1:i + 1 + self.seqs_len]))

    def __len__(self):
        return len(self.data)

    def __getitem__(self, idx):
        x = self.data[idx][0]
        y = self.data[idx][1]
        return torch.tensor(x), torch.tensor(y)

class PoetryRNN(nn.Module):
    def __init__(self,vocab_size,embedding_dim,hidden_size,num_layers=1):
        super(self).__init__()
        self.embedding = nn.Embedding(vocab_size,embedding_dim)
        self.rnn=nn.RNN(embedding_dim,hidden_size,num_layers,batch_first=True)
        self.linear=nn.Linear(hidden_size,vocab_size)

    def forward(self,input):
        x = self.embedding(input)
        output, hidden = self.rnn(x)
        output = self.linear(output)
        return output