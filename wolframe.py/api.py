from wolframalpha import Client

def get_global_temp():
  client = Client('ekram zafar')  # Replace with your Wolfram Alpha App ID
  # Define the Wolfram Alpha query
  query = "average global temperature"

  try:
    # Send the query to Wolfram Alpha
    res = client.query(query)
    # Extract the desired data from the response (replace with appropriate logic)
    answer = res['pod'][0]['subpod'][0]['plaintext']  # Example extraction (modify based on response structure)
    return answer
  except Exception as e:
    # Handle potential errors during query or data extraction
    return f"Error retrieving data: {e}"

