from jira_api.jiraInteractions import getJiraIssues, commentAndLabel 
from ollama_interaction.ollamaQuery import askOllama
from config.set_context import setContext

# Setting config from config.json
context = setContext('config/config.json')

# Status to query on (also queries on a specific label set in config)
issues = getJiraIssues(context)

# Evaluates each issue, comments on it and labels it
print("Starting evaluation")
for issue in issues:
    if not issue.fields.description:
        print("Issue", issue.key, "has no description, skipping")
        continue
    else:
        ollama_response = askOllama(issue.fields.description)
        commentAndLabel(issue.key, ollama_response['message']['content'], context)
        print ("Comment left on Issue", issue.key)

print("Ollama evaluation complete")