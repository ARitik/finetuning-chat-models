
import torch
from transformers import GPT2LMHeadModel, GPT2Tokenizer
import gradio as gr

def main():
    # Load the fine-tuned GPT-2 model and tokenizer
    model_path = "output"  # Replace with the actual path to your "output" directory
    model = GPT2LMHeadModel.from_pretrained(model_path)
    tokenizer = GPT2Tokenizer.from_pretrained(model_path)

    # Define a function to generate responses
    def generate_response(input_text):
        input_ids = tokenizer.encode(input_text, return_tensors="pt", max_length=1028, truncation=True)
        response_ids = model.generate(input_ids, max_length=100, num_return_sequences=1, no_repeat_ngram_size=2, top_p=0.9, temperature=0.7)
        response_text = tokenizer.decode(response_ids[0], skip_special_tokens=True)
        return response_text

    # Set up the Gradio interface
    iface = gr.Interface(
        fn=generate_response,
        inputs="text",
        outputs="text",
        live=True,
        title="Chat with Fine-Tuned GPT-2 Model"
    )

    # Launch the Gradio interface
    iface.launch()

if __name__ == "__main__":
    main()
