# Medical Expert System for Neurological Conditions
 
A rule-based expert system built in Python with [Experta](https://github.com/nilp0inter/experta) that asks about initial clinical signs and symptoms and suggests one of 12 possible neurological diagnoses.
 
**Team project, Tecnológico de Monterrey:** Emilio Estrada Pérez, Axel Yael Rodríguez Romero, Juan Diego Rodríguez Espinoza.

> **Disclaimer:** This is a simplified academic model developed by Data Science and Mathematics Engineering students. It is not a substitute for professional medical evaluation or for clinical tests (such as laboratory or imaging studies) needed for a definitive diagnosis. Anyone with neurological symptoms should see a healthcare specialist.
 
## How it works
 
The system asks a sequence of yes/no questions about symptoms. Each answer is stored as a fact, and Experta's inference engine fires the rules that match those facts, following the decision flow below until it reaches a diagnosis.
 
<img width="1920" height="1080" alt="Decision flow diagram" src="https://github.com/user-attachments/assets/3cbecf13-ac63-44c1-b8c1-8682e45961fc" />
**Possible diagnoses:** ischemic stroke, hemorrhagic stroke, bacterial meningitis, Alzheimer's disease, vascular dementia, Parkinson's disease, essential tremor, migraine, cluster headache, tension-type headache, epilepsy, and multiple sclerosis.
 
## Project structure
 
```
.
├── main.ipynb       # Expert system: facts, rules and inference engine
├── questions.txt    # Questions asked to the user
├── diagnoses.txt    # Diagnosis descriptions
└── env.yml          # Conda environment
```
 
## Getting started
 
```bash
conda env create -f env.yml
conda activate <env-name>   # name defined in env.yml
jupyter notebook main.ipynb
```
 
Run all cells and answer the questions in the notebook.
 
## Sources
 
| Diagnosis | Source |
|---|---|
| Ischemic stroke | American Stroke Association (2021). [Ischemic Stroke (Clots)](https://www.stroke.org/en/about-stroke/types-of-stroke/ischemic-stroke-clots) |
| Hemorrhagic stroke | Mayo Clinic (2022). [Hemorrhagic stroke: Symptoms and causes](https://www.mayoclinic.org/diseases-conditions/hemorrhagic-stroke/symptoms-causes/syc-20373220) |
| Bacterial meningitis | World Health Organization (2023). [Meningitis](https://www.who.int/news-room/fact-sheets/detail/meningitis) |
| Alzheimer's disease | Alzheimer's Association (2023). [Alzheimer's Disease Facts and Figures](https://www.alz.org/alzheimers-dementia/facts-figures) |
| Vascular dementia | National Institute on Aging (2021). [Vascular Dementia](https://www.nia.nih.gov/health/vascular-dementia) |
| Parkinson's disease | Parkinson's Foundation (2022). [What is Parkinson's?](https://www.parkinson.org/understanding-parkinsons/what-is-parkinsons) |
| Essential tremor | International Parkinson and Movement Disorder Society (2020). *Essential Tremor* |
| Migraine | International Headache Society (2018). [ICHD-3: Migraine](https://ichd-3.org/1-migraine/) |
| Cluster headache | International Headache Society (2018). [ICHD-3: Cluster Headache](https://ichd-3.org/3-trigeminal-autonomic-cephalalgias/3-1-cluster-headache/) |
| Tension-type headache | Cleveland Clinic (2023). *Tension-Type Headaches* |
| Epilepsy | International League Against Epilepsy (2017). [Operational classification of seizure types](https://www.ilae.org/guidelines/definition-and-classification) |
| Multiple sclerosis | National Multiple Sclerosis Society (2023). *Symptoms and Diagnosis* |
 
## License
 
MIT
 
