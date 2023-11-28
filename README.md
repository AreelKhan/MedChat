# MedChat: Bridging AI and Medical Practice

## Inspiration
In the fast-evolving field of medical science, the gap between AI research and its practical application in healthcare is a significant challenge. With the continuous development of sophisticated medical diagnosis models, there's a pressing need for a unified platform. This platform should not only facilitate access to these AI tools but also integrate them seamlessly with peer-reviewed medical literature. Such a resource is invaluable for medical professionals striving to stay abreast of the latest advancements and apply them in their clinical practice.

## What MedChat Does
MedChat addresses this need by providing a user-friendly chat interface designed specifically for medical professionals. This innovative platform serves a dual purpose:

1. **Querying Medical Literature:** MedChat allows healthcare providers to effortlessly inquire about medical literature, aiding them in keeping up-to-date with the latest research findings, treatment protocols, and clinical guidelines.

2. **AI-Powered Diagnosis Assistance:** Beyond literature, MedChat integrates state-of-the-art, pre-trained medical models derived from cutting-edge research. These models assist in disease diagnosis, offering a second opinion and helping to validate medical decisions.

## How We Built MedChat
The construction of MedChat involved a multi-faceted technological approach:

- **Utilizing Cohere API:** The backbone of MedChat is the Cohere API. We leveraged various facets of this powerful tool, including Cohere Chat for natural language processing, Classify for categorizing queries, and Rerank for optimizing response relevance.

- **Frontend Development with Streamlit:** To make MedChat accessible and intuitive, we chose Streamlit for the frontend. This framework enabled us to create an interactive web interface that is both user-friendly and efficient.

- **Integrating Tensorflow for Running Medical Models:** The core functionality of disease diagnosis is powered by medical models run on Tensorflow. This integration allows MedChat to process complex medical data and provide accurate, AI-driven diagnostic suggestions.

## Challenges We Faced
A primary challenge in developing MedChat was:

- **Detecting User Intent Accurately:** To ensure that MedChat responds appropriately to the queries of medical professionals, a critical task was to accurately detect user intent. This involved discerning whether a query was seeking medical literature or a diagnosis, and then triggering the correct functions within the application. Achieving this required fine-tuning our natural language processing capabilities and optimizing the interface for clarity and precision in understanding user queries.

<img width="1791" alt="original" src="https://github.com/AreelKhan/MedChat/assets/20444505/b5a4bce0-c2ce-4429-bbba-59fe4d95cd29">

<img width="1791" alt="original (1)" src="https://github.com/AreelKhan/MedChat/assets/20444505/5d6377e6-5f09-4628-97a0-ffa95c8f1bdf">

<img width="3760" alt="original (2)" src="https://github.com/AreelKhan/MedChat/assets/20444505/06894c8c-6bb3-4a38-9abb-5663852f4741">
