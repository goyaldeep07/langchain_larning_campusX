from langchain_core.prompts import PromptTemplate


template_text = """Please summarize the research paper titled "{paper_input}" with the following specifications:
                          Explanation Style: {style_input}  
                          Explanation Length: {length_input}  
                          1. Mathematical Details:  
                             - Include relevant mathematical equations if present in the paper.  
                             - Explain the mathematical concepts using simple, intuitive code snippets where applicable.  
                          2. Analogies:  
                             - Use relatable analogies to simplify complex ideas.  
                             If certain information is not available in the paper, respond with: "Insufficient information available" instead of guessing.  
                            Ensure the summary is clear, accurate, and aligned with the provided style and length."""
template = PromptTemplate(
    template=template_text, inputs=["paper_input", "style_input", "length_input"]
)

# Example usage
filled = template.format(
    paper_input="BERT: Pre-training of Deep Bidirectional Transformers",
    style_input="Technical",
    length_input="Medium (3-5 paragraphs)",
)
print(filled)

template.save("research_paper_summary_template.json")  # Save the template for later use
