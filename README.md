# Economic Player Agent

> An autonomous AI agent living inside an economic simulation, making decisions, managing resources, developing capabilities, and optimizing long-term wealth.

---

## Overview

Most AI agents only generate responses.

**Economic Player Agent takes actions.**

This project builds an autonomous decision-making system where a local LLM controls a simulated economic player.

The agent's objective:

> **Maximize long-term net worth.**

The agent does not follow predefined financial rules.

Instead, it:

1. Observes the current economic state.
2. Reasons about possible strategies.
3. Selects an action.
4. Executes actions through tools.
5. Experiences consequences.
6. Stores previous decisions.
7. Improves future decisions.

The simulation environment is deterministic and reproducible, while the intelligence comes from a local LLM.

---

# Core Idea

Traditional economic simulations use fixed rules:

```python
if inflation_high:
    invest()

if cash_low:
    save()
```

This project replaces hard-coded behavior with an autonomous reasoning loop:

```
              Economic World

                    |
                    v

            State Observation

                    |
                    v

              LLM Reasoning

                    |
                    v

            Action Selection

                    |
                    v

             Tool Execution

                    |
                    v

            World Update

                    |
                    v

              Memory Storage

                    |
                    v

            Next Decision
```

The LLM does not directly modify the world.

It controls an agent that interacts with the world through controlled actions.

---

# Current Features

## Autonomous AI Agent

- Local LLM powered reasoning
- ReAct-style architecture
- Structured JSON outputs
- Goal-oriented decision making
- Tool-based action execution
- Decision time measurement
- Simulation history tracking

---

# Economic Simulation

The player model includes:

```
Player

├── Cash
├── Salary
├── Expenses
├── Investments
├── Debt
├── Capabilities
└── Memory
```

The economy contains:

```
Economy

├── Inflation
├── Stock Returns
├── Unemployment
└── Market Changes
```

Every simulation month changes the world and forces the agent to adapt.

---

# Action System

The agent can choose strategic actions.

Current actions:

## Allocate Capital

Invest available resources into assets.

Example:

```json
{
    "action": "allocate_capital",
    "parameters": {
        "amount": 5000,
        "asset": "stocks"
    }
}
```

---

## Develop Capability

Improve future earning potential.

Capabilities have:

- Cost
- Cooldown
- Long-term benefits
- Historical tracking

Example:

```json
{
    "action": "develop_capability",
    "parameters": {
        "capability": "machine_learning"
    }
}
```

The agent must decide whether investing in itself is better than immediate financial gains.

---

## Manage Expenses

Optimize spending behavior.

Example:

```json
{
    "action": "manage_expenses",
    "parameters": {
        "strategy": "reduce_costs"
    }
}
```

---

## Do Nothing

Sometimes waiting is the optimal decision.

The agent can choose not to act when opportunities are unfavorable.

---

# Memory System

The agent learns from previous decisions.

Instead of:

```
Observe
  |
Decide
  |
Forget
```

The goal is:

```
Observe
  |
Decide
  |
Execute
  |
Remember
  |
Improve
```

Example memory record:

```json
{
    "month": 5,
    "action": "develop_capability",
    "capability": "machine_learning",
    "result": "success"
}
```

Future decisions can use previous experiences.

---

# Example Decision

```json
{
    "thought": "The market return is positive, but increasing future capability may create higher long-term value.",
    "action": "develop_capability",
    "parameters": {
        "capability": "machine_learning"
    }
}
```

---

# Architecture

```
                     Environment

                          |
                          v

                  State Observation

                          |
                          v

                    ReAct Agent

                          |
                          v

                 Structured Decision

                          |
                          v

                    Tool System

              +-----------+-----------+
              |                       |
              v                       v

       Economic Actions        Capability Actions

              |                       |

              +-----------+-----------+

                          |
                          v

                 Updated Player State

                          |
                          v

                    Memory Update

                          |
                          v

                 Future Decisions
```

---

# Why This Project?

Most AI projects stop at:

```
User -> LLM -> Answer
```

This project explores:

```
Agent -> Environment -> Action -> Consequence -> Learning
```

The system separates:

- Intelligence
- Environment
- Actions
- Memory
- Simulation

This creates a foundation for:

- Autonomous agents
- Multi-agent environments
- Economic simulations
- Digital twins
- Strategy optimization systems

---

# Roadmap

## Version 1

[x] Economic world  
[x] Player model  
[x] Local LLM integration  
[x] ReAct agent  
[x] Tool execution  
[x] Monthly simulation loop  


## Version 2

[ ] Long-term memory improvement  
[ ] Better capability system  
[ ] More realistic economy  
[ ] Market events  
[ ] Risk evaluation  


## Version 3

[ ] Planning agent  
[ ] Strategy generation  
[ ] Multi-step objectives  
[ ] Self-evaluation  


## Version 4

[ ] Verification agent  
[ ] Self-correcting execution loop  
[ ] Monte Carlo strategy evaluation  
[ ] Multiple competing agents  
[ ] Full simulated economy  


---

# Tech Stack

- Python
- Ollama
- Local LLMs
- Qwen / Gemma models
- Dataclasses
- JSON structured outputs


---

# Design Philosophy

## Local First

No external API dependency.

The entire system can run locally.

## Transparent

Every decision has:

- Reasoning
- Action
- Result
- Historical record

## Modular

Components can be replaced independently:

- LLM model
- Economy
- Player logic
- Actions
- Memory


---

# Vision

The goal is not to build another chatbot.

The goal is to create an autonomous decision-making system capable of:

- Understanding environments
- Planning actions
- Executing strategies
- Learning from outcomes
- Improving decisions over time


Future possibilities:

- Autonomous digital twins
- Multi-agent economies
- AI researchers
- Self-improving simulation environments

---