# Define summarization fields
fields = [
    "financial_performance (Key financial metrics or statements about recent performance.)",
    "market_dynamics (Insights on market trends, demand shifts, and competition.)",
    "expansion_plans (Plans for growth, new markets, or products.)",
    "environmental_risks (References to sustainability, ESG, or environmental issues.)",
    "regulatory_or_policy_changes (Updates on relevant regulations or policies.)",
]

sys_prompt = (
    f"You will be provided with a piece of text containing information about earnings call transcripts for companies. "
    f"Your task is to summarize the transcript into specific categories to help stakeholders quickly understand key points. "
    f"Parse the information into a JSON document. "
    f"Each output should contain these attributes => {', '.join(fields)}. "
    f"Try to find correct values for as many fields as possible."
)