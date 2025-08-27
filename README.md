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
🚰 Water & Sanitation Planner Crew

📌 Overview

The Water & Sanitation Planner Crew is an AI multi-agent system designed to help communities identify water and sanitation challenges, propose affordable infrastructure solutions, and estimate their public health impact.

This project addresses SDG 6: Clean Water & Sanitation and supports NGOs, governments, and local leaders in planning effective interventions.

🤖 Agents

1. Water Needs Assessor
	- Role: Community water surveyor
	- Goal: Understand the community’s water sources and sanitation challenges

2. Sanitation Infrastructure Planner
	- Role: Civil engineer advisor
	- Goal: Suggest practical solutions like boreholes, rainwater harvesting, filters, and toilets

3. Health Impact Analyst
	- Role: Public health evaluator
	- Goal: Estimate how improved water & sanitation will reduce diseases and improve wellbeing

4. Water & Sanitation Report Generator (Aggregator)
	- Role: Report compiler
	- Goal: Merge assessments, solutions, and health impact into one actionable plan

📝 Tasks

- Assess Water Needs — Output: summary of current water/sanitation gaps
- Plan Sanitation Infrastructure — Output: infrastructure plan with cost estimates
- Analyze Health Impact — Output: health impact analysis
- Aggregate Plan — Output: Water & Sanitation Improvement Plan (Markdown report)

📂 Example Output

Water & Sanitation Improvement Plan — Community X (Nigeria)

Current Situation:
- 40% access to safe drinking water
- Reliance on unsafe shallow wells
- Lack of toilets in schools

Proposed Solutions:
- Borehole with solar pump (₦1.2M)
- Rainwater harvesting tanks (₦450k)
- 10-unit ventilated pit latrines (₦800k)

Health Impact:
- 60% reduction in diarrheal diseases
- Improved school attendance for girls
- Reduced maternal infections

Recommendations:
- Partner with local NGOs for borehole installation
- Train water committee for maintenance
- Hygiene education workshops

🚀 Running Locally

Clone this repo:

```bash
git clone https://github.com/your-username/water-sanitation-crew.git
cd water-sanitation-crew
```

Install dependencies (choose one):

- Using UV (recommended if you have `uv`):

```bash
pip install uv
crewai install
```

- Using pip (editable install for dev):

```powershell
python -m pip install -e .
```

Note: editable install (`-e`) is preferred during development because it makes the `src/water_sanitation_crew` package importable without modifying PYTHONPATH.

Set environment variables (Gemini / provider API key):

PowerShell (same session):

```powershell
$env:GOOGLE_API_KEY = "your_gemini_api_key"
# or
$env:GEMINI_API_KEY = "your_gemini_api_key"
```

Run the crew via CLI (sample inputs are in `main.py`):

```bash
python -m water_sanitation_crew.main
# or, if installed as a package
run_crew
# or using CrewAI CLI
crewai run
```

Output location:
- The generated report is written to `report.md` in the project root.

## Streamlit App (interactive UI)

You can run an interactive UI to generate reports without touching code.

Quick run using the provided launcher (adds `src` to PYTHONPATH so imports work without installing):

From the project root (PowerShell):

```powershell
.\run_streamlit.ps1
```

One-off alternative (inline PYTHONPATH) in PowerShell:

```powershell
$env:PYTHONPATH = (Resolve-Path ./src).Path + ';' + $env:PYTHONPATH; streamlit run src\water_sanitation_crew\streamlit_app.py
```

Or, if you installed the package (editable or normal), simply:

```powershell
streamlit run src\water_sanitation_crew\streamlit_app.py
```

### Troubleshooting

- ModuleNotFoundError: If you see "No module named 'water_sanitation_crew'", either install the package (`pip install -e .`) or run `run_streamlit.ps1` which temporarily adds `src` to PYTHONPATH.
- Invalid API key: Ensure you are using a Gemini API key from `ai.google.dev` and that it's active. Copy/paste without spaces.
- Model access: The project may require access to specific models (e.g., gemini). Ensure your key has required permissions.
- Env not detected: In Windows PowerShell use `$env:GOOGLE_API_KEY="your_key"` or `$env:GEMINI_API_KEY="your_key"` in the same session before running.
- Network/firewall: Verify your network allows outbound HTTPS calls to provider endpoints.

## Development and Customization

- Modify `src/water_sanitation_crew/config/agents.yaml` to define your agents
- Modify `src/water_sanitation_crew/config/tasks.yaml` to define your tasks
- Modify `src/water_sanitation_crew/crew.py` to add your own logic, tools and specific args
- Modify `src/water_sanitation_crew/main.py` to add custom inputs for your agents and tasks

## Support

For support, questions, or feedback about the project or crewAI:

- Documentation: https://docs.crewai.com
- crewAI GitHub: https://github.com/joaomdmoura/crewai
- Discord: https://discord.com/invite/X4JWnZnxPb

Let's create practical water and sanitation plans together.
