from openai import OpenAI
import os

os.environ["OPENAI_API_KEY"] = "sk-proj-"

client = OpenAI()

## 香港地址生成.
def genAddr():
    completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "你是一个测试工程师，擅长生成各类测试数据，用于应用上线之前的测试"},
        {"role": "user", "content": "生成一个香港真实地址，邮编，用于测试stripe收款账号注册流程.只需要回答地址和邮编，不要添加其他内容."}
    ]
    )

    print(completion.choices[0].message.content)
    return(completion.choices[0].message.content)

## 香港身份证生成.
def getCardId():
    completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "你是一个测试工程师，擅长生成各类测试数据，用于应用上线之前的测试"},
        {"role": "user", "content": "生成一个香港身份证号和对应姓名，用于测试stripe收款账号注册流程.只需要回答香港身份证号和姓名，不要添加其他内容."}
    ]
    )

    print(completion.choices[0].message.content)
    return(completion.choices[0].message.content)


getCardId()