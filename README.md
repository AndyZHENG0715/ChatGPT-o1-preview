# OpenAI o1-preview with Python by Azure AI Inference

## Purpose
This repository implements a web-based chatbot interface using OpenAI's models through Azure AI Inference. The application allows users to interact with different AI models including o1-preview, o1-mini, gpt-4o, and gpt-4o-mini.

## Getting Started

### Prerequisites
- Python 3.7 or higher
- GitHub Personal Access Token
- Azure AI Inference subscription

### Setup
1. **Clone the repository:**
   ```bash
   git clone https://github.com/AndyZHENG0715/ChatGPT-o1-preview.git
   cd ChatGPT-o1-preview
   

2. **Create a virtual environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install dependencies:**
   ```bash
   pip install azure-ai-ml openai
   ```

4. **Configure Azure and OpenAI:**
   - Set up your Azure credentials and OpenAI API key in your environment variables.

### Usage
Create a Python script, e.g., `main.py`, and implement your inference logic. Below is a basic example:

```python
from azure.ai.ml import MLClient
from azure.identity import DefaultAzureCredential
import openai

# Authenticate with Azure
ml_client = MLClient(
    DefaultAzureCredential(),
    subscription_id="your-subscription-id",
    resource_group_name="your-resource-group",
    workspace_name="your-workspace"
)

# Set up OpenAI
openai.api_key = "your-openai-api-key"

# Make an inference
response = openai.Completion.create(
    model="o1-preview",
    prompt="Translate the following English text to French: 'Hello, how are you?'"
)

print(response.choices[0].text)
```

### Project Progress Checklist
- [ ] Create and set up the repository
- [ ] Configure Python environment and dependencies
- [ ] Implement basic OpenAI and Azure AI Inference integration
- [ ] Test the integration with sample inputs
- [ ] Document the setup and usage instructions
- [ ] Extend functionality as needed

## Contributing
Contributions are welcome! Please open an issue or submit a pull request.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
