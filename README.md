<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=gradient&customColorList=12,20,24&height=200&section=header&text=Aaryan%20Bairagi&fontSize=60&fontColor=ffffff&animation=fadeIn&fontAlignY=38&desc=Software%20Engineer%20%7C%20Full-Stack%20%7C%20Backend%20%7C%20AI%2FML%20Systems&descAlignY=58&descColor=a78bfa" width="100%"/>

[![Typing SVG](https://readme-typing-svg.demolab.com?font=JetBrains+Mono&weight=600&size=22&pause=1000&color=7C3AED&center=true&vCenter=true&width=800&lines=Building+Systems+That+Work+in+Production;Full-Stack+%7C+Backend+%7C+AI%2FML+%7C+IoT+Engineering;Event-Driven+Architecture+%7C+Scalable+APIs;Digital+Twins+%7C+Blockchain+%7C+Real-Time+Systems;Not+Just+on+Localhost.)](https://git.io/typing-svg)

<br/>

![Location](https://img.shields.io/badge/Pune%2C%20Maharashtra%2C%20India-0f172a?style=flat-square&logo=googlemaps&logoColor=a78bfa)

<br/>

![Profile Views](https://komarev.com/ghpvc/?username=AaryanBairagi&color=7c3aed&style=flat-square&label=Profile+Views)
![GitHub Followers](https://img.shields.io/github/followers/AaryanBairagi?style=flat-square&color=6d28d9&label=Followers)
![GitHub Stars](https://img.shields.io/github/stars/AaryanBairagi?style=flat-square&color=4c1d95&label=Stars)

</div>

---

## About

I build systems — full-stack applications, backend infrastructure, and ML-integrated products that work in production, not just on localhost. Taking an idea from scratch and turning it into something people can actually use is what drives most of what I do.

My work spans three areas: backend and full-stack engineering using Node.js, Next.js, TypeScript, PostgreSQL, and MongoDB; applied ML/AI including TensorFlow, Keras, neural networks, async AI pipelines, and LLM integration; and IoT/edge systems using Computer Vision, MQTT, Raspberry Pi, and real-time data ingestion. Most of what I build sits at the intersection of at least two of these.

I approach engineering with an architectural mindset — designing for scalability, failure tolerance, and maintainability from the start, not as an afterthought. I take distributed systems, event-driven architecture, and system design seriously, and that thinking shows up in how I structure projects, not just on paper.

**Open To:** Backend Engineering · Full-Stack Engineering · ML/AI Engineering · SWE Internships · Full-Time Roles

---

## Tech Stack

<div align="center">

**Languages**

[![My Skills](https://skillicons.dev/icons?i=ts,js,python,java,c&theme=dark)](https://skillicons.dev)

**Frontend**

[![My Skills](https://skillicons.dev/icons?i=nextjs,react,tailwind,html,css&theme=dark)](https://skillicons.dev)

**Backend & Databases**

[![My Skills](https://skillicons.dev/icons?i=nodejs,express,postgresql,mongodb,redis,prisma,mysql&theme=dark)](https://skillicons.dev)

**Cloud, DevOps & Tooling**

[![My Skills](https://skillicons.dev/icons?i=aws,gcp,docker,vercel,git,github,vscode&theme=dark)](https://skillicons.dev)

</div>

---

## AI / ML Expertise

<div align="center">

| Domain | Proficiency | Details |
|:---|:---:|:---|
| Deep Learning | Advanced | Neural Networks, CNNs, ANNs, Transformer Models |
| ML Frameworks | Advanced | TensorFlow, Keras, Scikit-learn |
| AI Pipelines | Advanced | Async multi-stage orchestration, fault-tolerant execution |
| LLM Integration | Intermediate | API integration, prompt engineering, context management |
| Computer Vision | Intermediate | Real-time inference, edge deployment on Raspberry Pi |
| Predictive Modeling | Intermediate | Feature engineering, model training, evaluation |
| Data Engineering | Intermediate | Pandas, Matplotlib, InfluxDB, time-series analytics |
| IoT / Edge AI | Intermediate | MQTT, Mosquitto broker, sensor data ingestion |

</div>

---

## Featured Projects

<details>
<summary><b>DSHIELD — Digital Twin-based Stampede Hazard Identification, Estimation & Live Detection</b></summary>

<br/>

A hybrid AI + IoT crowd monitoring system for real-time stampede risk detection and emergency response coordination. DSHIELD combines ML inference models with physics-based crowd behavior analysis in a single hybrid backend, deployed on edge hardware and connected to cloud infrastructure for real-time alerting.

<div align="center">

| Attribute | Details |
|:---|:---|
| **Stack** | Python · Node.js · MQTT (Mosquitto) · Raspberry Pi · InfluxDB · Amazon RDS · JavaScript |
| **Architecture** | Digital twin with hybrid edge-cloud data pipeline |
| **Performance** | Low-latency MQTT edge ingestion via publisher-subscriber model |
| **Security** | Human-in-the-loop validation layer before alert escalation |
| **Storage** | InfluxDB for time-series crowd analytics · Amazon RDS for structured user data |
| **Impact** | Real-world stampede detection with automated evacuation coordination |
| **Status** | Final Year Project · Research Paper in Progress |
| **Repository** | [github.com/AaryanBairagi/dshield](https://github.com/AaryanBairagi) |

</div>

Built a closed-loop alert system that triggers automatic notifications to event organizers and dispatches mobile-connected volunteers for coordinated crowd evacuation upon risk threshold breach. The system implements a human-in-the-loop decision layer that inserts manual validation checkpoints before alert escalation, ensuring operational feasibility and reducing false-positive evacuations in real-world deployments.

</details>

---

<details>
<summary><b>AutoMata — AI Workflow Automation SaaS Platform</b></summary>

<br/>

A full-stack SaaS platform for building trigger-based workflow automations across 7 external platforms — Google Drive, Gmail, Gemini, Slack, Discord, Notion, and Google Calendar — without relying on Zapier or similar no-code middleware. Built with an event-driven runtime, asynchronous execution, and Stripe billing.

<div align="center">

| Attribute | Details |
|:---|:---|
| **Stack** | Next.js · PostgreSQL · Prisma ORM · TypeScript · OAuth 2.0 · React Flow · Clerk · Stripe |
| **Architecture** | Event-driven workflow runtime with dependency-aware node orchestration |
| **Scale** | 7 third-party platform integrations with native OAuth 2.0 |
| **Performance** | Asynchronous task execution with webhook triggers |
| **Security** | Custom OAuth 2.0 integrations · token refresh · scope validation · revocation |
| **Billing** | Stripe subscription + usage-based credit billing |
| **Impact** | No third-party middleware — built the entire execution layer from scratch |
| **Repository** | [github.com/AaryanBairagi/AutoMata](https://github.com/AaryanBairagi/AutoMata) |

</div>

Designed event-driven workflow runtime with asynchronous task execution, webhook triggers, and dependency-aware node orchestration. Implemented custom OAuth 2.0 integrations and secure token lifecycle management for all 7 third-party services — handling token refresh, scope validation, and revocation natively. Integrated Stripe subscription and usage-based credit billing, allowing teams to cap workflow execution spend and automatically pause execution when credit thresholds are hit.

</details>

---

<details>
<summary><b>Social — Directed Graph-based Students & Alumni Networking Platform</b></summary>

<br/>

A production-grade full-stack social networking platform with graph-based relationship modeling, end-to-end encrypted messaging, and a second-degree recommendation engine. Built for students and alumni to connect, share content, and collaborate through a modern social ecosystem.

<div align="center">

| Attribute | Details |
|:---|:---|
| **Stack** | Next.js · MongoDB · TypeScript · WebSockets · Redis · Clerk · Cloudinary · Tailwind CSS |
| **Architecture** | Directed-edge graph data model for O(1) follower lookups and scalable traversal |
| **Scale** | Graph traversal supporting first and second-degree connection analysis |
| **Performance** | Redis-compatible caching + route-level rate limiting under high load |
| **Security** | AES-256-GCM encryption before database persistence — unreadable at rest |
| **Real-Time** | WebSocket messaging, likes, comments, and live notification delivery |
| **Impact** | Second-degree recommendation engine with explainable reasoning |
| **Repository** | [github.com/AaryanBairagi/social](https://github.com/AaryanBairagi/social) |

</div>

Designed a directed-edge graph data model in MongoDB for user relationships, enabling O(1) follower lookups and efficient follow-request state management at scale. Built a graph-based recommendation engine using second-degree connection traversal and mutual-connection scoring. Secured all chat data with AES-256-GCM encryption before database persistence — ensuring messages are unreadable even in the event of a direct database breach. Improved backend throughput by layering Redis-compatible caching and route-level rate limiting to prevent abuse during traffic spikes.

</details>

---

<details>
<summary><b>Cerebrum — Decentralized Exam Integrity Platform</b></summary>

<br/>

A decentralized exam integrity platform using blockchain technology and cryptographic security to prevent paper leaks and tampering at the infrastructure level. Built in direct response to institutional failures like the NEET paper leak — where centralized systems created single points of compromise.

<div align="center">

| Attribute | Details |
|:---|:---|
| **Stack** | Solidity · RSA Signature · AES-256 · Blockchain · Node.js · TypeScript |
| **Architecture** | Decentralized tamper-detection via smart contracts |
| **Security** | RSA + AES-256 encryption · Solidity smart contracts · blockchain audit trail |
| **Impact** | Paper leak prevention at infrastructure level — tamper attribution via chain |
| **Status** | Currently Building |
| **Repository** | [github.com/AaryanBairagi/cerebrum](https://github.com/AaryanBairagi) |

</div>

Built so that paper leaks like NEET cannot happen — and if tampering is attempted, the blockchain identifies exactly where and by whom. Implements Solidity smart contracts for tamper detection, RSA signature verification for identity, and AES-256 encryption for content security.

</details>

---

## Experience

**Software Engineering Intern**
IBN Technologies Limited · Remote, Pune
*January 2025 – February 2025*

Designed and shipped a multi-stage AI video pipeline (QuickVid AI) transforming JSON prompts into fully rendered videos — handling script generation, scene-wise asset creation, caption generation, and final video composition using Remotion.

- Integrated 4+ external AI services (AssemblyAI, Google Cloud TTS, HuggingFace) with custom async orchestration and fault-tolerant failure handling to ensure pipeline reliability under partial service failures
- Built a Stripe subscription and credit billing system with webhook-driven event handling for real-time user access control, automating plan upgrades, downgrades, and credit top-ups
- Delivered a production-ready AI pipeline capable of handling concurrent video generation requests with graceful degradation on service failures

![Next.js](https://img.shields.io/badge/Next.js-000000?style=flat-square&logo=nextdotjs&logoColor=white)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-4169E1?style=flat-square&logo=postgresql&logoColor=white)
![TypeScript](https://img.shields.io/badge/TypeScript-3178C6?style=flat-square&logo=typescript&logoColor=white)
![Stripe](https://img.shields.io/badge/Stripe-008CDD?style=flat-square&logo=stripe&logoColor=white)
![Google Cloud](https://img.shields.io/badge/Google%20Cloud-4285F4?style=flat-square&logo=googlecloud&logoColor=white)
![HuggingFace](https://img.shields.io/badge/HuggingFace-FFD21E?style=flat-square&logo=huggingface&logoColor=black)

---

## Academic Performances

<div align="center">

| Recognition | Details |
|:---:|:---|
| BE [SPPU] Performance | B.E. IT with Honours in Data Science · CGPA 8.8/10 |
| HSC Performance | 86% · Ranked 4th in college for outstanding academic performance |
| ICSE Performance | 95.6% · Ranked 9th in school for outstanding academic performance |

</div>

---

## Certifications

<div align="center">

**DeepLearning.AI**

![Deep Learning Specialization](https://img.shields.io/badge/Deep%20Learning%20Specialization-Andrew%20Ng-0056D2?style=for-the-badge&logo=coursera&logoColor=white)

**Amazon Web Services**

![AWS](https://img.shields.io/badge/AWS%20Solutions%20Architect-Associate-FF9900?style=for-the-badge&logo=amazonaws&logoColor=white)

**MongoDB**

![MongoDB](https://img.shields.io/badge/MongoDB%20Associate%20Developer-Node.js%20Track-47A248?style=for-the-badge&logo=mongodb&logoColor=white)

**Google**

![Google Cloud](https://img.shields.io/badge/Google%20Cloud%20Skill%20Boost-Intermediate%20Badges-4285F4?style=for-the-badge&logo=googlecloud&logoColor=white)
![Kaggle](https://img.shields.io/badge/Kaggle-Intermediate%20ML%20%7C%20Deep%20Learning-20BEFF?style=for-the-badge&logo=kaggle&logoColor=white)

**GitHub**

![GitHub Foundations](https://img.shields.io/badge/GitHub%20Foundations-Certified-171515?style=for-the-badge&logo=github&logoColor=white)
![GitHub Actions](https://img.shields.io/badge/GitHub%20Actions-CI%2FCD-2088FF?style=for-the-badge&logo=githubactions&logoColor=white)

**Postman**

![Postman](https://img.shields.io/badge/Postman%20Student%20Expert-API%20Fundamentals-FF6C37?style=for-the-badge&logo=postman&logoColor=white)

**Meta**

![Meta](https://img.shields.io/badge/Meta%20Back--End%20Developer-Professional%20Certificate-0866FF?style=for-the-badge&logo=meta&logoColor=white)

</div>

---

## Coding Profiles

<div align="center">

[![LeetCode](https://img.shields.io/badge/LeetCode-aaryanb4real-FFA116?style=for-the-badge&logo=leetcode&logoColor=black)](https://leetcode.com/u/aaryanb4real/)
[![GeeksforGeeks](https://img.shields.io/badge/GeeksforGeeks-aaryanbairagi1108-2F8D46?style=for-the-badge&logo=geeksforgeeks&logoColor=white)](https://www.geeksforgeeks.org/profile/aaryanbairagi1108)
[![GitHub](https://img.shields.io/badge/GitHub-AaryanBairagi-171515?style=for-the-badge&logo=github&logoColor=white)](https://github.com/AaryanBairagi)

</div>

---

## GitHub Analytics

<div align="center">

<img height="180em" src="https://github-readme-stats.vercel.app/api?username=AaryanBairagi&show_icons=true&theme=midnight-purple&include_all_commits=true&count_private=true&hide_border=true&bg_color=0d0d1a&title_color=7c3aed&icon_color=a78bfa&text_color=e2e8f0"/>
<img height="180em" src="https://github-readme-stats.vercel.app/api/top-langs/?username=AaryanBairagi&layout=compact&langs_count=8&theme=midnight-purple&hide_border=true&bg_color=0d0d1a&title_color=7c3aed&text_color=e2e8f0"/>

</div>

<div align="center">

<img src="https://github-readme-streak-stats.herokuapp.com/?user=AaryanBairagi&theme=midnight-purple&hide_border=true&background=0d0d1a&stroke=7c3aed&ring=6d28d9&fire=a78bfa&currStreakLabel=7c3aed&sideLabels=e2e8f0&currStreakNum=e2e8f0&sideNums=e2e8f0&dates=94a3b8"/>

</div>

---


## Core Competencies

<div align="center">

| Area | Focus |
|---|---|
| Backend | APIs, auth, databases, scaling |
| Frontend | Next.js, React, responsive UI |
| AI/ML | pipelines, integration, deployment |
| Systems | event-driven architecture, reliability |
| Security | encryption, access control, tamper detection |

</div>
---

## Contribution Activity

<div align="center">

[![Aaryan's github activity graph](https://github-readme-activity-graph.vercel.app/graph?username=AaryanBairagi&bg_color=0d0d1a&color=a78bfa&line=7c3aed&point=6d28d9&area=true&hide_border=true&area_color=4c1d95)](https://github.com/ashutosh00710/github-readme-activity-graph)

</div>

---

## Contribution Snake

<div align="center">

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/AaryanBairagi/AaryanBairagi/output/github-contribution-grid-snake-dark.svg">
  <source media="(prefers-color-scheme: light)" srcset="https://raw.githubusercontent.com/AaryanBairagi/AaryanBairagi/output/github-contribution-grid-snake.svg">
  <img alt="github contribution grid snake animation" src="https://raw.githubusercontent.com/AaryanBairagi/AaryanBairagi/output/github-contribution-grid-snake.svg">
</picture>

</div>

---

## Current Focus

```yaml
current_focus:
  learning:
    - AWS Solutions Architect Associate (SAA-C03)
    - DeepLearning.AI Deep Learning Specialization
    - Advanced System Design and Distributed Systems
    - Blockchain development with Solidity

  building:
    - Cerebrum: Decentralized Exam Integrity Platform
    - DSHIELD: Research paper and system refinement
    - Backend infrastructure for production-scale systems

  exploring:
    - Zero-knowledge proofs for exam security
    - Real-time ML inference optimization on edge hardware
    - LLM integration patterns for production applications
    - CI/CD pipelines with GitHub Actions

  open_to:
    - Backend Engineering roles
    - Full-Stack Engineering roles
    - ML / AI Engineering roles
    - SWE Internships and Full-Time positions
    - Research collaborations in AI / IoT / Security
```

---

## Connect

<div align="center">

[![Gmail](https://img.shields.io/badge/Gmail-aaryanbairagi1108@gmail.com-EA4335?style=for-the-badge&logo=gmail&logoColor=white)](mailto:aaryanbairagi1108@gmail.com)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Aaryan%20Bairagi-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/aaryan-bairagi-183249249/)
[![GitHub](https://img.shields.io/badge/GitHub-AaryanBairagi-171515?style=for-the-badge&logo=github&logoColor=white)](https://github.com/AaryanBairagi)
[![Twitter](https://img.shields.io/badge/Twitter-@aaryanb4real-000000?style=for-the-badge&logo=x&logoColor=white)](https://x.com/aaryanb4real)
[![Instagram](https://img.shields.io/badge/Instagram-@aaryanb4real-E4405F?style=for-the-badge&logo=instagram&logoColor=white)](https://www.instagram.com/aaryanb4real/)

</div>

---

<div align="center">

*"The best systems are not the ones that never fail — they are the ones that fail gracefully and recover automatically."*

<img src="https://capsule-render.vercel.app/api?type=waving&color=gradient&customColorList=12,20,24&height=120&section=footer&animation=fadeIn" width="100%"/>

</div> 
