import os
from crewai import Agent, Crew, Process, Task, LLM
from crewai.project import CrewBase, agent, crew, task
from crewai.agents.agent_builder.base_agent import BaseAgent
from typing import List

# Defining a Crew using the CrewAI framework
@CrewBase
class WaterSanitationCrew():
    """WaterSanitationCrew crew"""

    agents: List[BaseAgent]
    tasks: List[Task]

    # Defining agents using the @agent decorator
    def _default_llm(self) -> LLM:
        """Always use Gemini via LiteLLM. Requires GOOGLE_API_KEY or GEMINI_API_KEY to be set."""
        # Gemini via LiteLLM uses the `gemini/` prefix
        return LLM(model="gemini/gemini-1.5-flash")
    @agent
    def water_needs_assessor(self) -> Agent:
        return Agent(
            config=self.agents_config['water_needs_assessor'], # type: ignore[index]
            verbose=True,
            llm=self._default_llm()
        )

    @agent
    def sanitation_infra_planner(self) -> Agent:
        return Agent(
            config=self.agents_config['sanitation_infra_planner'], # type: ignore[index]
            verbose=True,
            llm=self._default_llm()
        )
    
    @agent
    def health_impact_analyst(self) -> Agent:
        return Agent(
            config=self.agents_config['health_impact_analyst'], # type: ignore[index]
            verbose=True,
            llm=self._default_llm()
        )
    
    @agent
    def water_sanitation_aggregator(self) -> Agent:
        return Agent(
            config=self.agents_config['water_sanitation_aggregator'], # type: ignore[index]
            verbose=True,
            llm=self._default_llm()
        )

    # Defining tasks using the @task decorator
    @task
    def assess_water_needs_task(self) -> Task:
        return Task(
            config=self.tasks_config['assess_water_needs_task'], # type: ignore[index]
        )
    
    @task
    def plan_sanitation_infra_task(self) -> Task:
        return Task(
            config=self.tasks_config['plan_sanitation_infra_task'], # type: ignore[index]
        )
    
    @task
    def analyze_health_impact_task(self) -> Task:
        return Task(
            config=self.tasks_config['analyze_health_impact_task'], # type: ignore[index]
        )

    @task
    def aggregate_task(self) -> Task:
        return Task(
            config=self.tasks_config['aggregate_task'], # type: ignore[index]
            output_file='report.md'
        )

    @crew
    def crew(self) -> Crew:
        """Creates the WaterSanitationCrew crew"""
 
        return Crew(
            agents=self.agents, # Automatically created by the @agent decorator
            tasks=self.tasks, # Automatically created by the @task decorator
            process=Process.sequential,
            verbose=True,
        )
