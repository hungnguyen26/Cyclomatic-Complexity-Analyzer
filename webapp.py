import streamlit as st
import ast
from analyzer.python_analyzer import ComplexityAnalyzer
from suggestions.refactor import refactor_suggestion
import matplotlib.pyplot as plt

def analyze_code_from_string(code_str):
    results = []
    try:
        tree = ast.parse(code_str)
        for node in tree.body:
            if isinstance(node, ast.FunctionDef):
                analyzer = ComplexityAnalyzer()
                analyzer.visit(node)
                results.append({
                    "name": node.name,
                    "score": analyzer.complexity,
                    "suggestion": refactor_suggestion(analyzer.complexity)
                })
    except Exception as e:
        st.error(f"❌ Lỗi khi phân tích: {e}")
    return results

def draw_chart(results):
    if not results:
        st.warning("Không có hàm nào để hiển thị.")
        return

    fig, ax = plt.subplots()
    names = [r["name"] for r in results]
    scores = [r["score"] for r in results]
    
    ax.bar(names, scores, color='lightblue')
    ax.axhline(10, color='red', linestyle='--', label='Ngưỡng phức tạp')
    ax.set_xlabel("Function Name")
    ax.set_ylabel("Cyclomatic Complexity")
    ax.set_title("Biểu đồ Độ phức tạp McCabe")
    ax.legend()
    st.pyplot(fig)

# Streamlit UI
st.set_page_config(page_title="Cyclomatic Analyzer", layout="centered")
st.title("🧠 Phân tích độ phức tạp mã nguồn (McCabe’s Cyclomatic Complexity)")
st.write("Nhập hoặc tải mã Python để tính toán độ phức tạp McCabe.")

input_type = st.radio("Chọn cách nhập code:", ["Nhập thủ công", "Tải file"])

code_input = ""
if input_type == "Nhập thủ công":
    code_input = st.text_area("Nhập mã Python tại đây:", height=300)
else:
    uploaded_file = st.file_uploader("Tải file .py", type=["py"])
    if uploaded_file:
        code_input = uploaded_file.read().decode("utf-8")
        st.code(code_input, language='python')

if st.button("🔍 Phân tích"):
    if code_input.strip() == "":
        st.warning("Vui lòng nhập mã nguồn hoặc tải file.")
    else:
        results = analyze_code_from_string(code_input)
        if results:
            for r in results:
                st.markdown(f"### 🔹 `{r['name']}` – Complexity: `{r['score']}`")
                st.markdown(f"> 💡 **Gợi ý:** {r['suggestion']}")
            draw_chart(results)
