import gradio as gr
import re
from collections import Counter

def analyze_text(text):
    if not text.strip():
        return "Будь ласка, введіть текст для аналізу."
        
    sentences = [s.strip() for s in re.split(r'[.!?]+', text) if s.strip()]
    num_sentences = len(sentences) if sentences else 1 
    
    words = re.findall(r"[\w'’]+", text.lower())
    num_words = len(words)
    
    if num_words == 0:
        return "Текст не містить розпізнаваних слів."
        
    total_chars = sum(len(w) for w in words)
    avg_word_len = total_chars / num_words
    avg_sent_len = num_words / num_sentences

    word_counts = Counter(words)
    top_5 = word_counts.most_common(5)
    top_5_formatted = ", ".join([f"**{w}** ({count})" for w, count in top_5])
    
    unique_words = [w for w, count in word_counts.items() if count == 1]
    unique_words_formatted = ", ".join(unique_words) if unique_words else "Немає"

    result = f"""
### Базові метрики:
* **Кількість слів:** {num_words}
* **Кількість речень:** {num_sentences}
* **Середня довжина слова:** {avg_word_len:.1f} символів
* **Середня довжина речення:** {avg_sent_len:.1f} слів

### Лексичний аналіз:
* **Топ-5 найчастіших слів:** {top_5_formatted}
* **Унікальні слова:** {unique_words_formatted}
"""
    return result

interface = gr.Interface(
    fn=analyze_text,
    inputs=gr.Textbox(label="Введіть текст для аналізу", lines=6, placeholder="Вставте сюди текст..."),
    outputs=gr.Markdown(label="Результати"),
    title="Завдання 2: Аналіз тексту",
    description="Аналізує стилістичні характеристики введеного тексту."
)

if __name__ == "__main__":
    interface.launch()