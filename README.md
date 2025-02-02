# AI-Enhanced Customer Support Ticket Resolution and Proactive Issue Prevention System

## Project Overview
This project aims to develop an advanced AI-powered customer support system that leverages historical ticket data analysis to predict recurring issues and proactively address potential concerns. By integrating **LLMs like OpenAI GPT and Meta LLaMA** for natural language processing and sentiment analysis with **Google Sheets, Slack, and Email**, the system automates responses to common issues, escalates high-priority tickets based on sentiment and urgency, and provides preemptive solutions. This solution enhances customer support efficiency, reduces response times, and improves overall customer satisfaction by addressing issues before they escalate.

## Key Features
- **Predictive Issue Detection**: Analyzes past support tickets to identify patterns and generate automated solutions for recurring problems.
- **Real-Time Sentiment Analysis**: Flags high-priority tickets based on urgency and customer sentiment for immediate escalation.
- **Automated Response System**: Uses AI-generated content to resolve repetitive issues efficiently.
- **Proactive Issue Prevention Dashboard**: Provides insights on potential future issues and suggests preemptive measures.
- **Seamless Communication Integration**: Syncs with Google Sheets, Slack, and Email for streamlined issue resolution.

## Installation and Setup
### Prerequisites
Ensure you have the following installed:
- **Python 3.8+**
- **pip** (Python package manager)
- **Node.js & npm** (for backend integrations)
- **Virtual Environment (venv)** (optional but recommended)

### Installation Steps
1. Clone the repository:
   ```sh
   git clone https://github.com/your-repo/AI-Customer-Support.git
   cd AI-Customer-Support
   ```
2. Set up a virtual environment (optional but recommended):
   ```sh
   python -m venv venv
   source venv/bin/activate   # On Windows: venv\Scripts\activate
   ```
3. Install required Python dependencies:
   ```sh
   pip install -r requirements.txt
   ```
4. Configure environment variables (create a `.env` file):
   ```env
   OPENAI_API_KEY=your_openai_api_key
   META_LLAMA_API_KEY=your_meta_llama_api_key
   SLACK_API_TOKEN=your_slack_api_token
   EMAIL_SMTP_SERVER=smtp.example.com
   EMAIL_USERNAME=your_email@example.com
   EMAIL_PASSWORD=your_email_password
   ```
5. Run the application:
   ```sh
   python main.py
   ```

## Usage
- Upload historical support tickets to **Google Sheets** for analysis.
- AI models will detect recurring issues and suggest preemptive solutions.
- New tickets are analyzed in real-time for **sentiment and urgency**.
- **Automated responses** are generated for common queries and sent via Slack/Email.
- A **dashboard** provides insights into potential future issues and suggests preventive actions.


## Technologies Used
- **Python** (Backend Development)
- **FastAPI** (API Development)
- **OpenAI GPT & Meta LLaMA** (Natural Language Processing)
- **Google Sheets API** (Data Management)
- **Slack API & Email SMTP** (Communication Integration)
- **Matplotlib & Seaborn** (Data Visualization)

## Contributing
Contributions are welcome! Follow these steps:
1. Fork the repository.
2. Create a new branch 
3. Commit your changes.
4. Push to your branch and submit a pull request.

## License
This project is licensed under the MIT License. 

## Contact
For any queries or support, reach out to:
- **Keerthi Gorla** (Project Lead) - [gorlakeerthi2205@gmail.com]

