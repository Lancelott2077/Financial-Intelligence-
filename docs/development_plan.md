# Development Plan — Financial Intelligence Platform

> **Status:** Placeholder — fill in sprint plan before implementation begins.

## Sprint 0 — Scaffold ✅

- [x] Generate complete project skeleton
- [x] Configure backend (FastAPI, Pydantic, SQLAlchemy)
- [x] Configure frontend (Next.js, TypeScript, Tailwind, shadcn)
- [x] Create placeholder pages, components, hooks, services
- [x] Create placeholder ORM models and Pydantic schemas
- [x] Create engineering documentation stubs

## Sprint 1 — Data Processing Pipeline

- [ ] Implement CSVParser (multi-format column detection)
- [ ] Implement Normaliser (date parsing, amount sign normalisation)
- [ ] Implement Categoriser (keyword rules + Gemini batch fallback)
- [ ] Implement ProcessingPipeline.run()
- [ ] Implement /upload endpoint end-to-end
- [ ] Implement Transaction ORM persistence
- [ ] Write unit tests for processing modules

## Sprint 2 — Feature Extraction & Behaviour Detection

- [ ] Implement TemporalFeatureExtractor
- [ ] Implement SpendingFeatureExtractor
- [ ] Implement MerchantFeatureExtractor
- [ ] Implement CategoryFeatureExtractor
- [ ] Implement FeatureMatrix.build()
- [ ] Implement PresentBiasDetector
- [ ] Implement LossAversionDetector
- [ ] Implement AnchoringDetector
- [ ] Implement MentalAccountingDetector
- [ ] Implement StatusQuoBiasDetector
- [ ] Implement DetectorRegistry.run_all()
- [ ] Implement EvidenceCollector.persist()
- [ ] Write unit tests for detectors

## Sprint 3 — Decision Engine & Simulation

- [ ] Define Rule definitions in rules.py
- [ ] Implement RuleEngine.evaluate()
- [ ] Implement DecisionBuilder.build_plan()
- [ ] Implement SimulationEngine.run()
- [ ] Implement Projector.project()
- [ ] Implement /simulation endpoint
- [ ] Write unit tests

## Sprint 4 — AI Integration

- [ ] Implement GeminiClient.generate() / generate_json()
- [ ] Implement PromptBuilder templates
- [ ] Implement ResponseParser
- [ ] Implement CoachService.chat()
- [ ] Implement /coach/chat endpoint
- [ ] Write prompt templates in prompts/ directory

## Sprint 5 — Frontend Implementation

- [ ] Implement Upload page with UploadDropzone
- [ ] Implement Financial Snapshot page with charts
- [ ] Implement Behaviour Report page with BiasCard
- [ ] Implement Savings Opportunities page
- [ ] Implement Counterfactual Replay page with ScenarioBuilder
- [ ] Implement AI Coach page with ChatWindow
- [ ] Implement Action Plan page with PlanItem components
- [ ] Connect all hooks to backend API

## Sprint 6 — Polish & Demo Prep

- [ ] Add loading states and error boundaries
- [ ] Add responsive layouts
- [ ] Add seed data / demo mode
- [ ] End-to-end testing
- [ ] Performance optimisation
