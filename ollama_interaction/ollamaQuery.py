import ollama
def askOllama(prompt):
    
  response = ollama.chat(model='llama3.1', messages=[
    {
      'role': 'system', 'content': "You are providing information to a developer on a project in the form on a comment on a Jira issue. Assume they have their environment set up correctly and provide suggestions for getting started on the issue, along with a code example or two.",
      'role': 'user',
      'content': prompt,
    },
  ])
  return response