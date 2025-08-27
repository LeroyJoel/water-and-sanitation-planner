🚰 Water & Sanitation Planner Crew
📌 Overview

The Water & Sanitation Planner Crew is an AI multi-agent system designed to help communities in Nigeria identify water and sanitation challenges, propose affordable infrastructure solutions, and estimate their public health impact.

This project addresses SDG 6: Clean Water & Sanitation and supports NGOs, governments, and local leaders in planning effective interventions.

🤖 Agents
1. Water Needs Assessor

Role: Community water surveyor

Goal: Understand the community’s water sources and sanitation challenges

Backstory: A development officer who interacts with local communities to collect insights.

2. Sanitation Infrastructure Planner

Role: Civil engineer advisor

Goal: Suggest practical solutions like boreholes, rainwater harvesting, filters, and toilets

Backstory: Infrastructure planner with focus on rural development and cost-effectiveness.

3. Health Impact Analyst

Role: Public health evaluator

Goal: Estimate how improved water & sanitation will reduce diseases and improve wellbeing

Backstory: Health advisor tracking links between clean water and community health.

4. Water & Sanitation Report Generator (Aggregator)

Role: Report compiler

Goal: Merge assessments, solutions, and health impact into one actionable plan

Backstory: Final agent that structures outputs for NGOs, local government, or donors.

📝 Tasks

Assess Water Needs

Collect information about the community’s water sources, sanitation, and challenges.

Output: Summary of current water/sanitation gaps.

Plan Sanitation Infrastructure

Recommend low-cost, practical water & sanitation improvements.

Output: Infrastructure plan with cost estimates.

Analyze Health Impact

Assess how improvements will reduce disease and improve community wellbeing.

Output: Health impact analysis.

Aggregate Plan

Combine findings into one structured document.

Output: Water & Sanitation Improvement Plan (Markdown report).

📂 Example Output

Water & Sanitation Improvement Plan — Community X (Nigeria)

Current Situation:

40% access to safe drinking water

Reliance on unsafe shallow wells

Lack of toilets in schools

Proposed Solutions:

Borehole with solar pump (₦1.2M)

Rainwater harvesting tanks (₦450k)

10-unit ventilated pit latrines (₦800k)

Health Impact:

60% reduction in diarrheal diseases

Improved school attendance for girls

Reduced maternal infections

Recommendations:

Partner with local NGOs for borehole installation

Train water committee for maintenance

Hygiene education workshops

🚀 Running Locally

Clone this repo:

git clone https://github.com/your-username/water-sanitation-crew.git
cd water-sanitation-crew


Install dependencies (choose one):

- Using UV (recommended if you have `uv`):

```bash
pip install uv
crewai install
```

- Using pip:

```bash
pip install .
```


Set environment variables (Gemini only):

```bash
# One of these must be set
set GOOGLE_API_KEY=your_gemini_api_key   # Windows PowerShell: $env:GOOGLE_API_KEY="..."
set GEMINI_API_KEY=your_gemini_api_key   # Windows PowerShell: $env:GEMINI_API_KEY="..."
```


Run the crew via CLI (sample inputs are hardcoded in `main.py`):

```bash
python -m water_sanitation_crew.main
# or if installed as a package
run_crew
# or using CrewAI CLI
crewai run
```


Output location:

- The generated report is written to `report.md` in the project root.

🎯 Impact

By combining infrastructure planning + health analysis, this AI solution provides practical, low-cost, data-driven plans that help governments, NGOs, and donors improve water and sanitation in Nigerian communities.

## Installation

Ensure you have Python >=3.10 <3.14 installed on your system. This project uses [UV](https://docs.astral.sh/uv/) for dependency management and package handling, offering a seamless setup and execution experience.

First, if you haven't already, install uv:

```bash
pip install uv
```

Next, navigate to your project directory and install the dependencies:

(Optional) Lock the dependencies and install them by using the CLI command:
```bash
crewai install
```
### Customizing

Set your Gemini key in your environment as `GOOGLE_API_KEY` or `GEMINI_API_KEY`.

- Modify `src/water_sanitation_crew/config/agents.yaml` to define your agents
- Modify `src/water_sanitation_crew/config/tasks.yaml` to define your tasks
- Modify `src/water_sanitation_crew/crew.py` to add your own logic, tools and specific args
- Modify `src/water_sanitation_crew/main.py` to add custom inputs for your agents and tasks

## Running the Project

To kickstart your crew of AI agents and begin task execution, run this from the root folder of your project:

```bash
$ crewai run
```

This command initializes the water_sanitation_crew Crew, assembling the agents and assigning them tasks as defined in your configuration.

This example, unmodified, will create a `report.md` file with the output plan in the project root.

## Understanding Your Crew

The water_sanitation_crew Crew is composed of multiple AI agents, each with unique roles, goals, and tools. These agents collaborate on a series of tasks, defined in `config/tasks.yaml`, leveraging their collective skills to achieve complex objectives. The `config/agents.yaml` file outlines the capabilities and configurations of each agent in your crew.

## Support

For support, questions, or feedback regarding the WaterSanitationCrew Crew or crewAI.
- Visit our [documentation](https://docs.crewai.com)
- Reach out to us through our [GitHub repository](https://github.com/joaomdmoura/crewai)
- [Join our Discord](https://discord.com/invite/X4JWnZnxPb)
- [Chat with our docs](https://chat.g.pt/DWjSBZn)

Let's create wonders together with the power and simplicity of crewAI.

## Streamlit App

You can run an interactive UI to generate reports without touching code.

### Install dependencies

If you are using UV:

```bash
crewai install
```

Or with pip:

```bash
pip install .
```

### Set environment

Set your Gemini environment variable: `GOOGLE_API_KEY` or `GEMINI_API_KEY`.

### Run the app

From the project root:

```bash
streamlit run src/water_sanitation_crew/streamlit_app.py
```

Then open the URL shown in the terminal (usually `http://localhost:8501`). Enter your community details (name, population, % without toilets, water source) and click "Generate Report". The app will run the agents and display a downloadable `report.md`.

### Troubleshooting

- Invalid API key: Ensure you are using a Gemini API key from `ai.google.dev` and that it's active. Copy/paste without spaces.
- Model access: The project uses `gemini/gemini-1.5-flash`. Ensure your key has access to this model.
- Env not detected: In Windows PowerShell use `$env:GOOGLE_API_KEY="your_key"` or `$env:GEMINI_API_KEY="your_key"` in the same session before running.
- Network/firewall: Verify your network allows outbound HTTPS calls to Google AI endpoints.
