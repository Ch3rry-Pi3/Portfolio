# 🦜🔗 **LangChain Chains for LLM Application Development**

## 📖 **Overview**
Chains are essential components in developing sophisticated applications using large language models (LLMs). They allow developers to combine prompts and memory modules into pipelines, enabling more advanced and versatile functionalities. LangChain provides various chain types to meet different use cases, ranging from simple prompt-response tasks to complex workflows involving multiple prompts and outputs.

The chains covered in this tutorial are:

1. **LLMChain**: Executes a single prompt-response task.
2. **SimpleSequentialChain**: Chains multiple tasks sequentially, where the output of one is the input to the next.
3. **SequentialChain**: Supports multiple inputs and outputs, enabling complex workflows.
4. **Router Chain**: Dynamically selects the appropriate chain based on input context, allowing versatile multi-domain handling.

These examples showcase how LangChain's chains can add increasing versatility to your applications.

## 📂 **Files**

1. `1_llm_chain.py`: Demonstrates the use of LLMChain for simple prompt-response tasks.
2. `2_simple_sequential_chain.py`: Highlights SimpleSequentialChain for basic sequential workflows.
3. `3_sequential_chain.py`: Explores SequentialChain for multi-input and multi-output workflows.
4. `4_router_chain.py`: Showcases Router Chain for dynamic chain selection based on input context.
5. `helper_functions.py`: Contains reusable utility functions for API setup and model selection.

## 🥇 **1. LLMChain**
### 🛠 **Description**
LLMChain is the simplest type of chain, designed for single-step prompt-response tasks. It’s ideal for straightforward scenarios where you want to process an input and obtain a response using a single prompt template.

### **Key Features**
- Executes a single prompt-response.
- Easy to set up and use.

### 🔑 **Code Snippet**
```python
prompt = ChatPromptTemplate.from_template(
    "What is the best name to describe a company that makes {product}?"
)

chain = LLMChain(llm=llm, prompt=prompt)
product = "Queen Size Sheet Set"
result = chain.run(product)
print(result)
```

### 📝 **Example Output**
```
Regal Linens
```

## 🥈 **2. SimpleSequentialChain**
### 🛠 **Description**
SimpleSequentialChain allows chaining multiple tasks together sequentially, where the output of one step becomes the input for the next. It’s useful for linear workflows.

### **Key Features**
- Chains multiple LLMChains sequentially.
- Supports verbosity to track the process.

### 🔑 **Code Snippet**
```python
chain_one = LLMChain(llm=llm, prompt=first_prompt)
chain_two = LLMChain(llm=llm, prompt=second_prompt)

simple_chain = SimpleSequentialChain(chains=[chain_one, chain_two], verbose=True)
product = "Queen Size Sheet Set"
result = simple_chain.run(product)
print(result)
```

### 📝 **Example Output**
```
> Entering new SimpleSequentialChain chain...
"Royal Slumber"
Royal Slumber creates luxurious and comfortable bedding products fit for royalty, ensuring a peaceful and restful night's sleep every time.

> Finished chain.
```

## 🥉 **3. SequentialChain**
### 🛠 **Description**
SequentialChain supports workflows with multiple inputs and outputs, enabling complex, multi-step processing. Each step in the chain can accept and produce multiple variables.

### **Key Features**
- Handles multi-input and multi-output workflows.
- Allows for more flexible and complex chains.

### 🔑 **Code Snippet**
```python
chain_one = LLMChain(llm=llm, prompt=first_prompt, output_key="English_Review")
chain_two = LLMChain(llm=llm, prompt=second_prompt, output_key="summary")

sequential_chain = SequentialChain(
    chains=[chain_one, chain_two],
    input_variables=["Review"],
    output_variables=["English_Review", "summary"],
    verbose=True
)
review = df.Review[5]
result = sequential_chain.run({"Review": review})
print(result["summary"])
```

### 📝 **Example Output**
```
> Entering new SequentialChain chain...
> Finished chain.
The reviewer is disappointed in the taste of the product and suspects it may be either an old batch or counterfeit.
```

## 🏅 **4. Router Chain**
### 🛠 **Description**
Router Chain dynamically selects the appropriate chain or prompt based on the input context. It’s highly versatile and well-suited for multi-domain applications.

### **Key Features**
- Dynamically selects the best-suited chain or prompt.
- Supports multi-domain and fallback options.

### 🔑 **Code Snippet**
```python
router_chain = LLMRouterChain.from_llm(llm, router_prompt)
chain = MultiPromptChain(
    router_chain=router_chain,
    destination_chains=destination_chains,
    verbose=True
)

result = chain.run("What is black body radiation?")
print(result)
```

### 📝 **Example Output**
```
> Entering new MultiPromptChain chain...
physics: {'input': 'What is black body radiation?'}
> Finished chain.
Black body radiation refers to the electromagnetic radiation emitted by a perfect black body...

> Entering new MultiPromptChain chain...
math: {'input': 'what is 2 + 2'}
> Finished chain.
The answer to 2 + 2 is 4.

> Entering new MultiPromptChain chain...
None: {'input': 'Why does every cell in our body contain DNA?'}
> Finished chain.
Every cell in our body contains DNA because it carries the genetic information...
```

## 🚀 **Conclusion**
LangChain’s chain modules empower developers to create intelligent, flexible, and scalable LLM applications. By leveraging these chains, you can:

1. **Simplify Workflows**: Automate multi-step processes with ease.
2. **Expand Versatility**: Handle diverse inputs and contexts dynamically.
3. **Enhance Efficiency**: Combine prompts and tasks into streamlined pipelines.

Explore these chain types and build advanced applications with LangChain. Happy coding! 🦜🔗

