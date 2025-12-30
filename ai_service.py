from openai import OpenAI

client = OpenAI()

# def generate_text(prompt: str):
  #  return client.responses.create(
    #    model="gpt-4.1-mini",
     #   input=prompt
   # )
def generate_text(prompt: str) -> str:
    return f"[MOCKED RESPONSE] Você enviou: {prompt}"

  #  return response.output_text


