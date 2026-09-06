import jieba
import torch
import config
from tokenizer import JiebaTokenizer
from model import ReviewAnalyzeModel

def predict_batch(model,inputs):
    """
    批量预测
    :param model:模型
    :param inputs:输入，shape:[batch_size,seq_length]
    :return: 预测结果，shape:[batch_size]
    """
    model.eval()
    with torch.no_grad():
        outputs = model(inputs)
        # outputs.shape:[batch_size]
        batch_result=torch.sigmoid(outputs)
    return batch_result.tolist()

def predict(text,model,tokenizer,device):
    # 1.处理输入
    indexes=tokenizer.encode(text,seq_len=config.SEQ_LEN)
    input_tensor=torch.tensor([indexes],dtype=torch.long).to(device)
    # input_tensor.shape:[batch_size,seq_len]

    # 2.预测模式
    batch_result=predict_batch(model,input_tensor)

    return batch_result[0]


def run_predict():

    # 准备资源
    # 1.确定设备
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

    # 2.词表
    tokenizer = JiebaTokenizer.from_vocab(config.MODELS_DIR/ "vocab.txt")
    print("此表加载成功")

    # 3.模型
    model = ReviewAnalyzeModel(tokenizer.vocab_size,tokenizer.pad_token_index).to(device)
    model.load_state_dict(torch.load(config.MODELS_DIR / "best.pt"))
    print("模型加载成功")

    print("欢迎使用情感分析模型（输入q或者quit推出）")

    while True:
        user_input = input("> ")
        if user_input in ['q', 'quit']:
            break
        if user_input.strip() == '':
            print("请输入内容")
            continue

        result = predict(user_input,model,tokenizer,device)
        if result>0.5:
            print(f"正向（置信度：{result:.4f}）")
        else:
            print(f"负向（置信度：{1-result:.4f}）")

if __name__=="__main__":
    run_predict()