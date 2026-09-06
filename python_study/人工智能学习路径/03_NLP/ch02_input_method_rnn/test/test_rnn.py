import torch
import torch.nn as nn

rnn=nn.RNN(input_size=3,hidden_size=4,batch_first=True,num_layers=2,bidirectional=True)

# input_shape:[batch_size,seq_len,input_size]
input=torch.randn(2,4,3)

# output_shape:[batch_size,seq_len,2*hidden_size]
# hidden_size:[num_layers × num_directions,batch_size,hidden_size]
output,hn=rnn(input)