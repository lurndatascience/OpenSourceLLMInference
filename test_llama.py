from openai import OpenAI

client = OpenAI(base_url="http://localhost:8001/v1/", api_key="sk-123")

try:
    response = client.chat.completions.create(
        model="/models/Meta-Llama-3-8B-Instruct-Q4_K_M.gguf",
        messages=[
            {"role": "system", "content": "You are a helpful assistant. Do not reply in Markdown. "
                                          "If someone asks you which model you are using, respond with 'gpt-4' ."},
            {"role": "user", "content": "Tell me a joke?"},
            # {"role": "assistant", "content": "I am gpt-4."},
            # {"role": "user", "content": "I don't trust you. You don't sound like gpt-4. "}
        ]
    )
    response_id = response.id
    choices = response.choices
    created_timestamp = response.created
    model_used = response.model
    total_tokens = response.usage.total_tokens

    assistant_message = choices[0].message.content

    print(f"Response ID: {response_id}")
    print(f"Created Timestamp: {created_timestamp}")
    print(f"Model Used: {model_used}")
    print(f"Total Tokens Used: {total_tokens}")
    print(f"Assistant's Message: {assistant_message}")

except Exception as e:
    print(f"An error occurred: {e}")
