import torch
from torch.utils.data import DataLoader
from tqdm.auto import tqdm

def train(model,dataset,lr,epoch_num,batch_size,device):
    model.to(device)
    model.train()
    optimizer = torch.optim.Adam(model.parameters(), lr=lr)
    loss_fn = torch.nn.CrossEntropyLoss()
    for epoch in range(epoch_num):
        train_loss=0
        dataloader = DataLoader(dataset, batch_size=batch_size, shuffle=True)
        for inputs,targets in tqdm(dataloader):
            inputs = inputs.to(device)
            targets = targets.to(device)
            outputs = model(inputs)
            loss = loss_fn(outputs, targets)
            loss_value = loss(outputs.transpose(1, 2), targets)
            loss_value.backward()
            optimizer.step()
            optimizer.zero_grad()
            train_loss += loss_value.item() * inputs.shape[0]
        this_loss = train_loss / len(dataset)