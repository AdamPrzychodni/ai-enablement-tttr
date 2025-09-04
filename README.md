# 🌍 AI Enablement for Nonprofits (Tech To The Rescue)

Welcome! 👋
This repository brings together a set of AI-powered tools designed to support nonprofits and social impact organizations on their technology journey.

It includes:

* 🤖 **AI Architect API** — turns organizational needs into clear, actionable tech recommendations.
* 📊 **AI Readiness Assessment Tool** — helps organizations understand how prepared they are for AI adoption.

This project was created for **Tech To The Rescue** with the aim of empowering the broader nonprofit tech community. 💙

---

## 📂 Project Structure

The repository is organized into two main parts:

1. **`task_1_solution_architect/`**
   A FastAPI server that acts as an "AI Architect," translating vague problem statements into structured, actionable AI solutions.

2. **`task_2_readiness_survey/`**
   A Streamlit web application that provides an AI Readiness Assessment survey, complete with scoring and tailored recommendations.

---

## 📐 👷🏻‍♀️ 🏛️ Task 1: AI Architect for Nonprofit Solutions

The **AI Architect API** helps nonprofits by:

* Taking a free-form problem statement ✍️
* Identifying the core issue 🔍
* Suggesting a technical solution with tools, frameworks, and first steps 🛠️

### 🔧 Setup & Installation

1. Navigate to the project directory:

   ```bash
   cd ai-enablement-tttr
   ```

2. Copy and configure your environment file:

   ```bash
   cp task_1_solution_architect/.env.example task_1_solution_architect/.env
   ```

   Add your **OpenAI API key** inside `.env`.

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

### ▶️ Running the Server

```bash
cd task_1_solution_architect
uvicorn src.main:app --reload
```

The API will be live at 👉 `http://127.0.0.1:8000`

### ✅ Testing

Run automated tests with:

```bash
pytest task_1_solution_architect/tests
```

---

## 🤖 📝 📊 Task 2: AI Readiness Assessment Tool

The **AI Readiness Survey** helps nonprofits explore their preparedness for AI transformation by guiding them through questions and generating a personalized report with scores and actionable insights.

### 🔧 Setup & Installation

1. Navigate to the project directory:

   ```bash
   cd ai-enablement-tttr
   ```

2. Copy and configure your environment file (optional, for LLM-based reports):

   ```bash
   cp task_2_readiness_survey/.env.example task_2_readiness_survey/.env
   ```

   Add your **OpenAI API key** inside `.env`.

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

### ▶️ Running the App

From the repository root, run:

```bash
streamlit run task_2_readiness_survey/src/main.py
```

Your app will open in the browser at 👉 `http://localhost:8501`

### ✅ Testing

```bash
pytest task_2_readiness_survey/tests
```

---

### Note on the Language Model (LLM)

For **testing and development** purposes, both projects have been implemented using the **`gpt-3.5-turbo-0125`** model.

***

#### Rationale
This choice was primarily driven by **cost-effectiveness** 💰. The `gpt-3.5-turbo-0125` model offers an excellent balance between performance and price, which allows for extensive testing without incurring significant costs.

***

#### Upgradability
The architecture of both tools was designed with flexibility in mind. In the configuration file (`.env`), the default model can easily be **replaced** with any newer, more powerful model from OpenAI, such as **`gpt-4-turbo`** or **`gpt-4o`**. A production deployment can therefore take full advantage of the advanced capabilities of these models without requiring any changes to the source code.

---

## 📜 License

This project is licensed under the **MIT License**. See the [LICENSE](./LICENSE) file for details.

---

✨ We hope this toolkit makes AI more accessible for nonprofits and helps drive positive impact in the world.
