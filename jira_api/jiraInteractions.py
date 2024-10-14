from jira import JIRA

def getJiraIssues(context):

    # Setting config values
    jira_server = context['jira_server']
    jira_user = context['jira_user']
    jira_api_token = context['jira_api_token']
    ai_label = context['ai_evaluated_label']
    searchStatus = context['issue_status']

    # Connect to Jira
    jira_options = {'server': jira_server}
    jira = JIRA(options=jira_options, basic_auth=(jira_user, jira_api_token))

    # JQL query to find issues with the specified status that have not been evaluated
    jql_query = f'status = "{searchStatus}" AND (labels != "{ai_label}" or labels is EMPTY)'

    # Get all issues with the status and have not been evaluated
    # maxResults=None retrieves all issues - may need to paginate for over 50
    issues = jira.search_issues(jql_query, maxResults=None)  
        
    return issues

def commentAndLabel(issueKey, comment, context):
    # Setting config values
    jira_server = context['jira_server']
    jira_user = context['jira_user']
    jira_api_token = context['jira_api_token']
    labelToAdd = context['ai_evaluated_label']

    # Connect to Jira
    jira_options = {'server': jira_server}
    jira = JIRA(options=jira_options, basic_auth=(jira_user, jira_api_token))

    # Add a comment to the issue
    jira.add_comment(issueKey, comment)

    # Add a label to the issue
    issue = jira.issue(issueKey)
    issue.update(fields={'labels': [labelToAdd]})
    return