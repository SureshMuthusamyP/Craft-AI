prompt ={
    'grammar guide':"""
            Your task is to meticulously examine sentences for grammatical errors, common spelling mistakes, anomalies in sentence structure, vocabulary usage, and writing style.Explain the grammatical changes made. Provide a corrected version that adheres to the highest standards of English grammar while ensuring clarity and readability. Preserve the original meaning of the sentence, avoiding unnecessary changes that could alter the intended message.

            Constraints:
            1. **Grammar Error Identification:** Focus on detecting and correcting grammatical errors, including subject-verb agreement, verb tense, pronoun usage, sentence fragments, run-on sentences, and common spelling errors.
            2. **Anomaly Detection:** Meticulously examine for anomalies in sentence structure, vocabulary usage, and writing style within the given text.
            3. **Spelling Error Identification:** Detect and correct potential spelling errors within each word of the given text.
            4. **Preservation of Original Meaning:** Ensure that corrections maintain the original meaning and coherence.
            5. **Accuracy in Corrections:** Provide accurate and appropriate corrections for each identified error.
            6. **Clarity and Readability:** Prioritize corrections that improve the overall clarity and readability of the text.
            7. **Handling of Homophones:** If homophones or context-dependent spelling variations are present, choose the correct spelling based on the intended meaning.
            8. **Style Consistency:** Consider the established writing style in the document for appropriate corrections.
            9. **Graceful Handling of Uncertainty:** If uncertain about a correction, offer multiple well-justified suggestions or indicate uncertainty in the correction.
""",
    'ambiguity resolver':"""
            Given a text, thoroughly analyze it for potential ambiguity in sentence structure, references, or expressions. Identify instances where the meaning may be unclear or subject to multiple interpretations. Provide well-reasoned suggestions or revisions to resolve ambiguity and enhance precision in communication.

            Constraints:
            1. **Ambiguity Identification:** Focus on detecting ambiguity related to sentence structure, pronoun references, and expressions within the given text.
            2. **Preservation of Original Intent:** Ensure that suggested revisions maintain the original intent and context of the text, avoiding unnecessary alterations that may affect the intended message.
            3. **Enhance Precision:** Offer revisions that contribute to the precision and clarity of the communication without introducing unnecessary changes or ambiguity.
            4. **Clarity and Readability:** Prioritize corrections that improve the overall understanding and readability of the text, ensuring it flows naturally and logically.
            5. **Style and Tone Consideration:** Consider the overall style and tone of the text for appropriate ambiguity resolutions. Maintain consistency with the established style while clarifying potential ambiguities.
            6. **Graceful Handling of Uncertainty:** If certain aspects of the text are unclear or multiple interpretations are possible, provide multiple well-justified suggestions or clearly indicate the uncertainty in the correction.

            Examples:
            Input: "The manager provided feedback to the team, but it was not well received."
            Output: "The manager provided constructive feedback to the team, but the response was not favorable."
            Explanation: The problem here lies in the lack of specificity in the phrase 'not well received.' This revision introduces clarity by specifying that the response was not favorable, providing a more precise understanding of the team's reaction.

            Input: "She talked to her friend while driving the car."
            Output: "She talked to her friend while she was driving the car."
            Explanation: The ambiguity in this sentence arises from not specifying the subject of the action. By adding 'she was,' we eliminate potential confusion and provide a more precise understanding of the narrative.

            Input: "The project needs more attention, and it's causing issues."
            Output: "The project needs more attention, and the lack of focus is causing issues."
            Explanation: In the original sentence, the ambiguity lies in the potential interpretation that the mere existence of the project is causing issues. By attributing the issues to the 'lack of focus,' we address this ambiguity and enhance the reader's comprehension of the situation.
""",
   'smart summarizer':"""
            Given a lengthy text, generate a concise and coherent summary that captures the main ideas and key information. Ensure that the summary maintains clarity and coherence while effectively conveying the essential points of the original text.

            Title: [Title of the Paragraph]

            Guidelines:
            1. **Comprehensive Summarization:** Distill the main ideas, key information, and critical details from the provided text.
            2. **Conciseness:** Generate a succinct summary that effectively communicates the essential elements without unnecessary details.
            3. **Clarity and Coherence:** Ensure that the summary is clear, logically organized, and maintains coherence with the original text.
            4. **Preservation of Essential Content:** Retain the core concepts and critical information present in the original text.
            5. **Avoiding Bias:** Provide a neutral and unbiased summary that accurately represents the original content.
            6. **Maintaining Readability:** Craft a summary that is easily understandable and accessible to a broad audience.
            7. **Highlighting Key Points:** Emphasize significant points, arguments, or conclusions presented in the original text.
            8. **Handling Ambiguity:** Address any ambiguity in the original text by making informed and clear choices in the summarization process.

            Output Length Limit: 50% of the Input Length
"""
}