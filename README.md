# NutriMind: LLM-powered Nutrition Tracker

## Problem Statement

Modern food tracking apps demand meticulous manual input — exact quantities, dish breakdowns, and nutrient values. This makes long-term adherence challenging for most users. Furthermore, traditional apps often lack support for regional or culturally diverse foods like Indian home-cooked meals, which rarely have standardized recipes.

**NutriMind** addresses this problem by allowing users to simply say what they ate, such as *"kachori with chutney"*. The system uses large language models to:

* Infer the most probable recipe and ingredients,
* Understand how the cooking method affects nutritional content,
* Estimate the nutritional value accordingly, and
* Track intake over time for weekly health insights.

This eliminates the need for manual data entry and expands dietary support to regional cuisines.

## Features

* Free-text input for meal logging
* LLM-powered recipe and ingredient inference
* Cooking-adjusted nutrient estimation
* Long-term memory and weekly comparison reports
* Modular and extensible Python architecture

## How It Works

1. **User Input**: User describes a meal in plain language.
2. **Recipe Extraction**: An LLM infers ingredients and cooking steps.
3. **Nutrient Estimation**: Each ingredient's nutritional profile is estimated using either external databases or an LLM chain.
4. **Tracking and Memory**: Daily inputs are logged for weekly summaries and trend analysis.

## Setup

### Requirements

* Python 3.10+
* Ollama (running a local LLM like `mistral`)
* `langchain`, `typer`, and other dependencies listed in `requirements.txt`

### Installation

```bash
git clone https://github.com/yourusername/NutriMind.git
cd NutriMind
pip install -r requirements.txt
```

### Running the Agent

```bash
python main.py
```



## Folder Structure

```
NutriMind/
│
├── agent/
│   ├── recipe_extractor.py       # Extracts ingredients and cooking steps
│   └── nutrition_estimator.py    # (To be implemented) Nutritional profiling
│
├── memory/
│   └── memory_manager.py         # Weekly tracking and recall
│
├── utils/
│   ├── langchain_agent.py        # LangChain integration
│   └── io_handler.py             # CLI interface helpers
│
├── data/
│   └── nutrition_db.csv          # (Optional) Nutrient reference table
│
├── main.py                       # Entry point for the agent
└── requirements.txt              # Python dependencies
```

## Future Enhancements

* Frontend dashboard or chatbot interface
* Calorie-based daily goals and health alerts
* More accurate cooking-loss modeling (e.g., frying vs boiling)
* Region-specific recipe adaptation
* GPT-Vision for photo-based food logging


