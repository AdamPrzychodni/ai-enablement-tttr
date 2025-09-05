# 🌍 AI Enablement for Nonprofits (Tech To The Rescue)

Welcome\! 👋
This repository brings together a set of AI-powered tools designed to support nonprofits and social impact organizations on their technology journey.

It includes:

  * 🤖 **AI Architect API** — turns organizational needs into clear, actionable tech recommendations.
  * 📊 **AI Readiness Assessment Tool** — helps organizations understand how prepared they are for AI adoption.

This project was created for **Tech To The Rescue** with the aim of empowering the broader nonprofit tech community. 💙

-----

## 🔧 Overall Setup & Installation

Before running either of the projects, please set up the environment.

1.  **Navigate to the project directory:**

    ```bash
    cd ai-enablement-tttr
    ```

2.  **Create and activate a virtual environment:**

    ```bash
    # Create the virtual environment
    python -m venv venv

    # Activate on macOS and Linux
    source venv/bin/activate

    # Activate on Windows
    .\\venv\\Scripts\\activate
    ```

3.  **Install all required dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

-----

## 🏛️ Task 1: AI Architect for Nonprofit Solutions

The **AI Architect API** helps nonprofits by taking a free-form problem statement, identifying the core issue, and suggesting a technical solution with tools, frameworks, and first steps.

### ▶️ Running the Server

1.  **Configure your environment file:**

    ```bash
    cp task_1_solution_architect/.env.example task_1_solution_architect/.env
    ```

    Then, add your **OpenAI API key** inside the new `.env` file.

2.  **Start the server:**
    From the **root** directory, run:

    ```bash
    uvicorn task_1_solution_architect.src.main:app --reload
    ```

    The API will be live at 👉 `http://127.0.0.1:8000`

### ✅ Testing

Run automated tests with:

```bash
pytest task_1_solution_architect/tests
```

-----

## 📊 Task 2: AI Readiness Assessment Tool

The **AI Readiness Survey** helps nonprofits explore their preparedness for AI transformation by guiding them through questions and generating a personalized report with scores and actionable insights.

### ▶️ Running the App

1.  **Configure your environment file (optional):**
    This step is only needed if you want to use the LLM-based report generation feature.

    ```bash
    cp task_2_readiness_survey/.env.example task_2_readiness_survey/.env
    ```

    Then, add your **OpenAI API key** inside the new `.env` file.

2.  **Run the application:**
    From the **root** directory, run:

    ```bash
    streamlit run task_2_readiness_survey/src/main.py
    ```

    Your app will open in the browser at 👉 `http://localhost:8501`

### ✅ Testing

Run automated tests with:

```bash
pytest task_2_readiness_survey/tests
```

-----

### Note on the Language Model (LLM)

For **testing and development** purposes, both projects have been implemented using the **`gpt-3.5-turbo-0125`** model. This choice was primarily driven by **cost-effectiveness** 💰. The architecture of both tools was designed with flexibility in mind, and the model can easily be **replaced** with a more powerful one like **`gpt-4-turbo`** or **`gpt-4o`** in the configuration file without any code changes.

-----

## 📜 License

This project is licensed under the **MIT License**. See the [LICENSE](https://www.google.com/search?q=./LICENSE) file for details.