import clueai
import streamlit as st
def introduction():
    st.markdown('''
    # 全中文任务支持零样本学习模型

[PromptCLUE](https://github.com/clue-ai/PromptCLUE)：支持最多中文任务的开源预训练模型

这个模型是基于1000亿token中文语料上预训练，并且在数百种任务上进行Prompt任务式训练。针对理解类任务，如分类、情感分析、抽取等，可以自定义标签体系；针对多种生成任务，可以进行采样自由生成。

## 模型描述

支持几十个不同类型的任务，具有较好的零样本学习能力和少样本学习能力。针对理解类任务，如分类、情感分析、抽取等，可以自定义标签体系；针对生成任务，可以进行采样自由生成。千亿中文token上大规模预训练，累计学习1.5万亿中文token，亿级中文任务数据上完成训练，训练任务超过150+。比base版平均任务提升7个点+；具有更好的理解、生成和抽取能力，并且支持文本改写、纠错、知识图谱问答。 实现了中文上的三大统一：统一模型框架，统一任务形式，统一应用方式。

- 统一模型框架：采用Text-to-Text的生成式预训练模型进行统一建模。
- 统一任务形式：Prompt统一不同的NLP任务间的差异，转化为统一的text-to-text数据形式。
- 统一应用方式：对目标任务形成拿来即用的模型，下游应用时都可转化为统一的prompt自适应方式，进行zero-shot/few-shot测试。

### 模型局限性及可能的偏差

我们的模型基于大规模NLP数据集（如[pCLUE](https://github.com/CLUEbenchmark/pCLUE)），各领域综合表现素质较高，但在某些垂直领域可能表现稍弱；

## 训练数据介绍

pCLUE：基于提示的大规模预训练数据集，用于多任务学习和零样本学习

### 目前已经有包含9个数据集：

```
1.单分类tnews 
2.单分类iflytek 
3.自然语言推理ocnli 
4.语义匹配afqmc 
5.指代消解-cluewsc2020 
6.关键词识别-csl 
7.阅读理解-自由式c3 
8.阅读理解-抽取式cmrc2018 
9.阅读理解-成语填空chid 
```

### 字段说明及评价标准：

```
input:模型的输入
target:模型的输出
type:任务类型，阅读理解(mrc),分类(classify)，生成(generate)，自然语言推理(nli)
评价标准：阅读理解(em),分类(acc)，生成(em)，自然语言推理(acc)
answer_choices:选项（只有分类、推理类任务有）
```

## 数据评估及结果

效果对比--16类中文任务

|            任务类型            | PromptCLUE-base | PromptCLUE-large |
| :----------------------------: | :-------------: | :--------------: |
|         **分数** Score         |      63.47      |   70.55(+7.08)   |
|        参数 Parameters         |      220M       |       770M       |
|   **理解任务**（acc，10类）    |                 |                  |
|         分类 classify          |      89.56      |      92.89       |
|   情感分析 emotion_analysis    |      80.55      |      85.64       |
|       相似度计算 similar       |      70.94      |      78.47       |
|        自然语言推理 nli        |      78.00      |      86.67       |
|  指代消解 anaphora_resolution  |      30.00      |      64.00       |
| 阅读理解 reading_comprehension |      71.69      |      84.78       |
| 关键词提取 keywords_extraction |      41.44      |      47.78       |
|          信息抽取 ner          |      63.02      |      70.09       |
|  知识图谱问答 knowledge_graph  |        -        |      53.11       |
| 中心词提取 Keyword_extraction  |      66.50      |      71.50       |
|   **生成任务**（rouge，6类）   |                 |                  |
|     翻译（英中、中英） nmt     |      55.92      |      59.67       |
|          摘要 summary          |      31.71      |      34.48       |
|            问答 qa             |      21.18      |      27.05       |
|     生成（文章、问题生成）     |      35.86      |      39.87       |
|        改写 paraphrase         |        -        |      57.68       |
|          纠错 correct          |        -        |      93.35       |
    
    
    ''')
if __name__ == '__main__':
    cl = clueai.Client('wTzinq_UcR-eYoS0iZuEc101001011')
    st.markdown("# Hi! 🖐️🖐️🖐️\n"
                "# 这是一个文本摘要在线生成工具\n"
                "不知道如何使用\n？"
                "很简单：只需要将文本复制到**文本框**中，再点击**生成**就可以了"
                ""
                "")
    phrase = '对于美方提出两国元首在巴厘岛举行会晤等涉华言论，在今天（10日）举行的中国外交部例行记者会上，发言人赵立坚表示，中美两国元首通过多种方式保持经常性联系。中方重视美方提出两国元首在巴厘岛举行会晤的建议，目前双方正就此保持沟通。中方对美政策立场是一贯和明确的，我们致力于同美方实现相互尊重、和平共处、合作共赢，同时坚定捍卫自身主权安全发展利益。'
    st.markdown(f" **示例文本：**\n  >{phrase} ")
    st.markdown(f" **示例输出：**\n  >外交部：中方重视美方提议两国元首巴厘岛会晤 ")
    st.markdown("😊😊 \n **已经了解了?接下来开始文本你的文本摘要之旅吧！**")
    text = st.text_area("在此输入",height=50)
    # generate a prediction for a prompt
    butt = st.button("生成")
    if butt and text != "":
        prompt = f'''
                  概括文章中心思想：{text}
                  摘要：?
                  '''
        # print the predicted text
        prediction = cl.generate(
            model_name='clueai-large',
            prompt=prompt)
        st.markdown(f"**生成摘要：**\n > {prediction.generations[0].text}")
        st.balloons()
    st.write("\n")
    st.write("\n")
    st.write("\n")
    st.write("\n")
    click=1
    c=st.button("模型介绍")
    if c:
        introduction()


