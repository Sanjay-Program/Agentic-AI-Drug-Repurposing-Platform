# 🚀 Agentic AI Platform for Drug Repurposing  
### **Team SynergyX — EY Techathon 6.0 (Round 2 Submission)**  

**Team Members:**  
- 👩‍💼 **Gayathiri Botlagunta** — *Team Leader*  
- 👨‍💻 **Sanjay** — *Backend + Multi-Agent Architecture (GitHub: Sanjay-Program)*  
- 👨‍💻 **Tulasi Rama Krishna** — *Frontend + Data Visualization*

---

# 🎯 Problem Statement  
### **Pharmaceutical Innovation Through Agentic AI**

A leading multinational generic pharmaceutical company wants to move beyond the saturated, low-margin generics market and explore **high-value innovative opportunities**. They aim to repurpose **approved molecules** for new indications, patient populations, or dosage forms.

However, discovering such opportunities requires:

- Months of literature research  
- Patent & clinical trial analysis  
- Competitive & market study  
- Safety/regulatory evaluation  
- Internal insights alignment  

**Goal of EY Techathon Challenge:**  
✔ Build an *Agentic AI* solution that can:  
- Integrate external regulatory, clinical, scientific, and market data  
- Analyse opportunities rapidly  
- Summarize findings  
- Produce structured, decision-ready reports  
- Enable pharma teams to explore new molecule innovation cases  

---

# 🧠 Solution Overview  
### **Agentic AI–Driven Drug Repurposing Platform**

We built a complete, enterprise-grade **multi-agent AI platform** that automates end-to-end molecule evaluation, using an intelligent **Master Agent** orchestrating **12 specialized Worker Agents**.

Our solution performs:

- 🔬 Scientific evidence aggregation  
- 📚 Clinical trial discovery  
- 👩‍⚕️ Toxicity & safety analysis  
- 💰 Market & commercial modeling  
- 🧩 Knowledge-graph-driven indication prediction  
- 📊 ROI simulation  
- 🔍 Competitive & patent analysis  
- 📑 Automatic PDF storytelling  

This transforms a **3-month manual research cycle** into an **instant, explainable, AI-powered analysis**.

---

# 🏆 Key Innovations

### 🔹 **1. Full Multi-Agent Architecture (12 Domain Agents)**  
Each agent specializes in a pharmaceutical knowledge domain:

- IQVIA Market Insights Agent  
- EXIM Supply Chain Agent  
- Patent Landscape (USPTO) Agent  
- Clinical Trials Agent  
- Internal Documents Summarizer  
- Web Intelligence Agent (Guidelines & News)  
- Knowledge Graph Reasoner  
- Repurposing Opportunity Predictor  
- Toxicity & Safety Agent  
- Regulatory Feasibility Agent  
- Market Attractiveness Agent  
- Portfolio Optimizer Agent  

---

### 🔹 **2. Innovation Scoring Engine + Explainability**
Calculates:

- Clinical evidence score  
- Market attractiveness  
- Competition  
- Toxicity & safety  
- Patent and FTO  
- Regulatory feasibility  

Outputs:

- Overall Innovation Score  
- Recommendation → **GO / EXPLORE / NO-GO**  
- Contribution explanation (XAI)

---

### 🔹 **3. Scenario & ROI Simulator**
Financial tools include:

- NPV calculation  
- Payback estimation  
- Market-growth adjustments  
- Competitive risk modeling  

This aligns R&D decisions with business reality.

---

### 🔹 **4. Autonomous Research Mode**
System automatically:

- Selects molecules  
- Runs full evaluation  
- Ranks opportunities  
- Provides strategic recommendations  

---

### 🔹 **5. Signals & Intelligence Surveillance**
Real-time monitoring for:

- Patent expiry  
- New trials  
- Safety alerts  
- Guidelines updates  
- Scientific publications  

---

### 🔹 **6. Enterprise Memory**
All evaluations are stored in:

- **History archive**  
- **PDF library**  
- **Searchable evaluation database**  

---

### 🔹 **7. Professional React UI Dashboard**
Tabs:

1. Single Molecule Evaluation  
2. Portfolio / Batch Evaluation  
3. Auto Research  
4. Scenario & ROI Simulation  
5. History & Memory  
6. Signals & Watchlist  

---

# 🏗 System Architecture

(Insert generated architecture.png here)

```
docs/
 ├── architecture.png
 ├── agent-flow.png
 └── journey.png
```

Architecture Layers:

1. **Frontend Layer** — React dashboard  
2. **API Layer** — FastAPI  
3. **Master Agent**  
4. **Worker Agent Pool (12 agents)**  
5. **Analytical Engines**  
6. **Data Sources (Mock APIs)**  
7. **Storage: Memory + Reports**  

---

# 🧩 Agent Flow Diagram

(Insert generated agent-flow diagram here)

---

# 🧬 End-to-End Molecule Journey Diagram

(Insert generated journey diagram here)

---

# 📂 Folder Structure

```
Agentic-AI-Drug-Repurposing/
│
├── backend/
│   ├── app/
│   │   ├── agents/
│   │   ├── orchestrator/
│   │   ├── services/
│   │   ├── routers/
│   │   ├── mock_data.py
│   │   ├── schemas.py
│   │   └── main.py
│   └── requirements.txt
│
├── frontend/
│   ├── src/
│   │   ├── App.js
│   │   ├── api.js
│   │   └── App.css
│   └── package.json
│
├── docs/
│── README.md
```

---

# 🛠 Installation Guide

## **1. Clone Repository**

```bash
git clone https://github.com/Sanjay-Program/Agentic-AI-Drug-Repurposing-Platform.git
cd Agentic-AI-Drug-Repurposing-Platform
```

---

# 🌐 Backend Setup (FastAPI)

```bash
cd backend
pip install -r requirements.txt
uvicorn app.main:app --reload
```

API Documentation:  
➡ **http://localhost:8000/docs**

---

# 💻 Frontend Setup (React)

```bash
cd frontend
npm install
npm start
```

Dashboard:  
➡ **http://localhost:3000**

---

# 📘 Key API Endpoints

**Single Evaluation**
```
POST /api/evaluation/
```

**Batch Evaluation**
```
POST /api/evaluation/batch
```

**Auto Research**
```
GET /api/research/auto
```

**Signals**
```
GET /api/signals/?molecule=XYZ
```

**ROI Simulation**
```
POST /api/finance/simulate
```

**History**
```
GET /api/history
```

**PDF Download**
```
GET /api/reports/{id}
```

---

# 🎯 Why This Solution is Innovative

✔ Transforms pharma R&D decision-making  
✔ Automates multi-month research workflows  
✔ Uses Agentic AI instead of single-LMM reasoning  
✔ Adds explainability & financial modeling  
✔ Supports strategic-level portfolio decisions  
✔ Includes a complete surveillance system  
✔ Production-ready backend & frontend  

This solution aligns exactly with the **theme of EY Techathon 6.0: Agentic AI**.

---

# 🏅 Team SynergyX — Members

| Name | Role |
|------|------|
| **Gayathiri Botlagunta** | Team Leader, Strategic Design, Integration |
| **Sanjay (Sanjay-Program)** | Backend Lead, Multi-Agent Architecture, Data Engineering |
| **Tulasi Rama Krishna** | Frontend Lead, UX, Visualization |

---

# 📄 License  
MIT License — free to use with credit.

---

# 🤝 Acknowledgements  
This project was created for **EY Techathon 6.0** as a demonstration of practical **Agentic AI for pharmaceutical innovation**.

---

# ⭐ If you find this useful  
Star ⭐ the repo & follow **Sanjay-Program** on GitHub!

