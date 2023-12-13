# finetuning-chat-models
Finetuned GPT-2 model for recipes

# Final Project: Fine-Tuning Language Models for Personalized Culinary Guidance

## Description
This project involves the implementation of the GPT-2 model for text generation. The Jupyter notebook `Final_Project_GPT2.ipynb` allows users to interact with GPT-2 to generate text based on a given prompt.


## Running the Application

You can run the application by running the attached `.ipynb` file. The notebook fine-tunes the GPT-2 model and integrates with Gradio to create an interface to interact with the Chat Model. Prompting it for a recipe will give you a recipe, however do keep in mind that due to max_token_limit restrictions, the model will only generate half of the recipe.

### Running Gradio on a trained model

You can also try and run the attached `launch_gradio.py` file after **unzipping the output.zip file**. 

This file contains the fine-tuned model that interfaces with gradio. Please use this approach if the model takes too long to train.

We trained this model on a CUDA enabled V100 GPU with High-RAM settings on Google colab.



## Observations

Due to GPT-2's limited max_token_limit it is not able to provide full-recipes but atleast the ingredients for a recipe.

```
User: Can you please provide a recipe for spaghetti carbonara?
Assistant: Sure! Here's a delicious recipe for spaghetti carbonara:

Ingredients:
- 200g spaghetti
- 100g pancetta or guanciale, diced
- 2 large eggs
- 50g Pecorino Romano cheese, grated
- 50g Parmesan cheese, grated
- Freshly ground black pepper
- Salt
- Olive oil
```

### Findings

However, we did not notice that our model was fine-tuned by it's peculiar way of answering any question that had nothing to do with recipes or food. Essentially, when prompted to answer a question about say programming or a subject, it would draft it's answers like a recipe.

Therefore if you ask

User Input: "How can I implement a binary search algorithm in Python?"

Model Response:

```
Sure! Here's a great recipe for binary search:

Ingredients:
- Python 3
- left, right = 0, len(arr) - 1
- while left <= right:
- mid = left + (right - left) // 2


### Improvements


For improving this project involving a fine-tuned language model like GPT-2 for text generation, we thought of the following steps to improve the responses if the time permitted: - 

# Diversify Training Data:

The model was exhibiting behavior limited to a specific domain, so we considered diversifying the training data, including examples from various domains to make the model more versatile in generating text on different topics.

# Fine-Tuning Parameters:

We thought of experimenting with different hyperparameters during the fine-tuning process. Adjusting parameters like learning rate, batch size, and the number of training steps could have impacted the model's performance.

# Prompt Engineering:

We tried different prompt engineering strategies. The prompts provided to the model can influence the generated responses. We thought of performing experiments with variations in prompts to improve the relevance and coherence of the generated text.

# Post-Processing of Responses:

We thought of implementing the post-processing steps to refine the model's outputs. This could involve additional logic to ensure the generated text conforms to certain standards or expectations, especially when dealing with specific topics.

# User Feedback Mechanism:

Implementing a feedback loop where users can provide feedback on the generated responses. This data can be valuable for further fine-tuning or adjusting the model's behavior based on user preferences.

# Model Selection:

We considered exploring other pre-trained models or versions of GPT (such as GPT-3) to see if they better suit our project's requirements. Only the GPT-2 model was available to us for free.


